#!/usr/bin/env python3
"""Automated Reolink firmware security analyzer.

Downloads, extracts, and analyzes firmware images, outputting
structured JSON results for each hardware version.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def run(cmd, timeout=120, **kwargs):
    """Run a command and return stdout."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, **kwargs)
        return r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return ""


def find_files(root, name):
    """Find files by name under root."""
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            if f == name:
                results.append(os.path.join(dirpath, f))
    return results


def find_files_glob(root, pattern):
    """Find files matching a glob pattern."""
    return list(Path(root).rglob(pattern))


def download_firmware(url, dest_dir):
    """Download firmware zip/pak file. Returns path to downloaded file."""
    os.makedirs(dest_dir, exist_ok=True)
    filename = url.split("/")[-1]
    if not filename.endswith((".zip", ".pak")):
        filename = "firmware.zip"
    dest = os.path.join(dest_dir, filename)
    if os.path.exists(dest):
        return dest
    r = subprocess.run(
        ["curl", "-sL", "-o", dest, url],
        timeout=300, capture_output=True
    )
    if r.returncode != 0 or not os.path.exists(dest):
        return None
    return dest


def extract_firmware(fw_path, extract_dir):
    """Extract firmware. Returns path to extraction root."""
    os.makedirs(extract_dir, exist_ok=True)

    # If zip, extract first
    if zipfile.is_zipfile(fw_path):
        with zipfile.ZipFile(fw_path) as zf:
            zf.extractall(extract_dir)
        # Find .pak or .paks file inside
        paks = list(Path(extract_dir).rglob("*.pak")) + list(Path(extract_dir).rglob("*.paks"))
        if paks:
            fw_path = str(paks[0])

    # Run binwalk on the pak
    run(f"cd {extract_dir} && binwalk -e -C {extract_dir} '{fw_path}'", timeout=300)
    return extract_dir


def extract_ubi_squashfs(extract_dir):
    """Extract SquashFS images found inside UBI volumes."""
    ubi_files = list(Path(extract_dir).rglob("*.ubi"))
    for ubi in ubi_files:
        img_dir = str(ubi) + "_images"
        if not os.path.exists(img_dir):
            run(f"ubireader_extract_images '{ubi}' -o '{img_dir}'", timeout=120)
        # Find extracted volume images and check if they're SquashFS
        for img_file in Path(img_dir).rglob("*"):
            if not img_file.is_file() or img_file.stat().st_size < 1000:
                continue
            file_type = run(f"file '{img_file}'")
            if "Squashfs" in file_type:
                sqsh_dir = str(img_file) + "_squashfs"
                if not os.path.exists(sqsh_dir):
                    run(f"unsquashfs -d '{sqsh_dir}' '{img_file}'", timeout=120)


def find_rootfs(extract_dir):
    """Find the root filesystem directory after extraction."""
    # Look for common rootfs indicators
    for indicator in ["etc/passwd", "bin/busybox", "etc/init.d"]:
        results = find_files(extract_dir, indicator.split("/")[-1])
        for r in results:
            if indicator in r:
                # Walk back to the rootfs root
                idx = r.find(indicator)
                candidate = r[:idx]
                if os.path.isdir(os.path.join(candidate, "etc")):
                    return candidate

    # Try ubifs extraction
    ubi_images = list(Path(extract_dir).rglob("*.ubi")) + list(Path(extract_dir).rglob("*.ubifs"))
    for ubi in ubi_images:
        ubi_dir = str(ubi) + "_extracted"
        if not os.path.exists(ubi_dir):
            run(f"ubireader_extract_files '{ubi}' -o '{ubi_dir}'", timeout=120)
        # Check inside
        results = find_files(ubi_dir, "passwd")
        for r in results:
            if "etc/passwd" in r:
                idx = r.find("etc/passwd")
                return r[:idx]

    # Try extracting SquashFS from UBI volumes (newer firmware stores
    # squashfs inside UBI despite naming files .ubifs)
    extract_ubi_squashfs(extract_dir)

    # Re-check for rootfs after squashfs extraction
    for indicator in ["etc/passwd", "bin/busybox"]:
        results = find_files(extract_dir, indicator.split("/")[-1])
        for r in results:
            if indicator in r:
                idx = r.find(indicator)
                candidate = r[:idx]
                if os.path.isdir(os.path.join(candidate, "etc")):
                    return candidate

    return None


def find_appfs(extract_dir):
    """Find the application filesystem directory."""
    # Look for dvr.xml or device binary as app partition indicators
    app_indicators = ["dvr.xml", "device", "nginx", "netserver"]
    candidates = []
    for indicator in app_indicators:
        results = find_files(extract_dir, indicator)
        for r in results:
            parent = os.path.dirname(r)
            # Verify it's an app dir (has multiple app files)
            try:
                siblings = os.listdir(parent)
            except OSError:
                continue
            score = sum(1 for s in app_indicators if s in siblings)
            if score >= 2:
                candidates.append((score, parent))
    if candidates:
        candidates.sort(reverse=True)
        return candidates[0][1]

    # Fallback: look for directories named "app" with content
    for dirpath, dirnames, filenames in os.walk(extract_dir):
        if os.path.basename(dirpath) == "app" and len(filenames) > 5:
            return dirpath
    return None


def analyze_passwd(rootfs):
    """Analyze password hashes."""
    passwd_file = os.path.join(rootfs, "etc/passwd")
    shadow_file = os.path.join(rootfs, "etc/shadow")
    result = {"has_shadow": os.path.exists(shadow_file), "entries": []}

    if os.path.exists(passwd_file):
        with open(passwd_file, "r", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(":")
                if len(parts) >= 7:
                    entry = {
                        "user": parts[0],
                        "hash": parts[1],
                        "uid": parts[2],
                        "gid": parts[3],
                        "shell": parts[6]
                    }
                    result["entries"].append(entry)

    if os.path.exists(shadow_file):
        with open(shadow_file, "r", errors="replace") as f:
            result["shadow_content"] = f.read().strip()

    return result


def analyze_tls_cert(appfs):
    """Analyze TLS certificates."""
    certs = []
    seen_fingerprints = set()
    for name in ["self.crt", "server.crt", "cert.pem", "server.pem"]:
        found = find_files(appfs, name) if appfs else []
        for cert_path in found:
            info = run(f"openssl x509 -in '{cert_path}' -noout -text -fingerprint -sha1 2>/dev/null")
            if info:
                cert_data = {"path": os.path.basename(cert_path), "details": ""}
                for line in info.split("\n"):
                    line = line.strip()
                    if "Public-Key:" in line:
                        cert_data["key_size"] = line
                    elif "Issuer:" in line:
                        cert_data["issuer"] = line
                    elif "Not After" in line:
                        cert_data["expiry"] = line
                    elif "Fingerprint" in line and ("SHA1" in line or "sha1" in line):
                        cert_data["sha1_fingerprint"] = line.split("=", 1)[1].strip() if "=" in line else line
                    elif "Signature Algorithm:" in line and "signature_algo" not in cert_data:
                        cert_data["signature_algo"] = line
                fp = cert_data.get("sha1_fingerprint", cert_path)
                if fp not in seen_fingerprints:
                    seen_fingerprints.add(fp)
                    certs.append(cert_data)
    return certs


def analyze_openssl(extract_dir):
    """Find OpenSSL version strings."""
    versions = set()
    for name in ["libssl.so", "libssl.so.1.0.0", "libssl.so.1.1", "libssl.so.3"]:
        found = find_files(extract_dir, name)
        for f in found:
            output = run(f"strings '{f}' | grep -i 'openssl' | head -5")
            for line in output.split("\n"):
                if "OpenSSL" in line and any(c.isdigit() for c in line):
                    versions.add(line.strip())
    return list(versions)


def analyze_nginx(extract_dir):
    """Find nginx version."""
    versions = set()
    found = find_files(extract_dir, "nginx")
    for f in found:
        if os.path.isfile(f) and os.access(f, os.R_OK):
            output = run(f"strings '{f}' | grep -E 'nginx/[0-9]' | head -5")
            for line in output.split("\n"):
                m = re.search(r'nginx/[\d.]+', line)
                if m:
                    versions.add(m.group())
    return list(versions)


def analyze_busybox(rootfs):
    """Analyze busybox version and compiled-in applets."""
    bb_path = os.path.join(rootfs, "bin/busybox")
    if not os.path.exists(bb_path):
        # Try sbin
        bb_path = os.path.join(rootfs, "sbin/busybox")
    if not os.path.exists(bb_path):
        return {"version": "not found", "dangerous_applets": []}

    output = run(f"strings '{bb_path}'")
    version = "unknown"
    for line in output.split("\n"):
        m = re.search(r'BusyBox v([\d.]+)', line)
        if m:
            version = m.group(1)
            break

    dangerous = ["telnetd", "ftpd", "tftpd", "httpd", "nc", "wget", "tftp"]
    found_dangerous = []
    for applet in dangerous:
        if re.search(rf'\b{applet}\b', output):
            found_dangerous.append(applet)

    return {"version": version, "dangerous_applets": found_dangerous}


def analyze_dvr_xml(extract_dir):
    """Parse dvr.xml for device configuration."""
    found = find_files(extract_dir, "dvr.xml")
    if not found:
        return {}

    with open(found[0], "r", errors="replace") as f:
        content = f.read()

    result = {}
    for attr in ["board_type", "board_name", "support_cloud", "support_supper_pwd",
                 "detail_machine_type", "default_pwd", "dev_type"]:
        m = re.search(rf'{attr}="([^"]*)"', content)
        if m:
            result[attr] = m.group(1)

    return result


def analyze_version_json(extract_dir):
    """Parse version.json."""
    found = find_files(extract_dir, "version.json")
    if not found:
        return {}
    try:
        with open(found[0]) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def analyze_connectivity(extract_dir):
    """Analyze network connectivity: P2P, cloud, DDNS, phone-home endpoints."""
    result = {
        "p2p_libs": [],
        "cloud_endpoints": set(),
        "ddns_providers": set(),
        "phone_home": set()
    }

    # Find key binaries
    for name in ["device", "netserver", "dvr"]:
        found = find_files(extract_dir, name)
        for f in found:
            if not os.path.isfile(f):
                continue
            size = os.path.getsize(f)
            if size < 1000 or size > 100_000_000:
                continue
            strings_out = run(f"strings '{f}'", timeout=60)

            # Cloud/API endpoints
            for line in strings_out.split("\n"):
                line = line.strip()
                if re.search(r'(reolink|baichuan|p2p|tutk|\.us/|\.com/|\.cn/).*api', line, re.I):
                    result["cloud_endpoints"].add(line[:200])
                if re.search(r'https?://[a-zA-Z0-9.-]+\.(com|us|cn|org|net)', line):
                    result["phone_home"].add(line[:200])
                if "3322.org" in line or "dyndns" in line.lower() or "noip" in line.lower():
                    result["ddns_providers"].add(line[:100])

    # P2P libraries
    for name in ["libp2p.so", "libp2pc.so", "libtutk.so"]:
        if find_files(extract_dir, name):
            result["p2p_libs"].append(name)

    result["cloud_endpoints"] = list(result["cloud_endpoints"])[:20]
    result["ddns_providers"] = list(result["ddns_providers"])[:10]
    result["phone_home"] = list(result["phone_home"])[:30]

    return result


def analyze_command_injection(extract_dir):
    """Look for potential command injection vectors."""
    vectors = []
    for name in ["device", "netserver", "dvr"]:
        found = find_files(extract_dir, name)
        for f in found:
            if not os.path.isfile(f):
                continue
            size = os.path.getsize(f)
            if size < 1000 or size > 100_000_000:
                continue
            strings_out = run(f"strings '{f}' | grep -E '(system|popen|exec).*(%s|\\$)' 2>/dev/null | head -20", timeout=30)
            for line in strings_out.split("\n"):
                line = line.strip()
                if line:
                    vectors.append(line[:200])

            # Also check for known dangerous patterns
            strings_out = run(f"strings '{f}' | grep -E '(smbpasswd|resolv\\.conf|ifconfig|route |iptables)' | head -20", timeout=30)
            for line in strings_out.split("\n"):
                line = line.strip()
                if line and ("%" in line or "$" in line or "`" in line):
                    vectors.append(line[:200])

    return vectors[:20]


def analyze_libc(rootfs):
    """Find libc version."""
    for name in ["libc.so.6", "libc.so", "libuClibc-*.so"]:
        found = find_files_glob(rootfs, name)
        for f in found:
            f = str(f)
            if os.path.islink(f):
                f = os.path.realpath(f)
            if not os.path.exists(f):
                continue
            output = run(f"strings '{f}' | grep -E '(glibc|GNU C Library|uClibc)' | head -5")
            for line in output.split("\n"):
                if "glibc" in line or "GNU C" in line or "uClibc" in line:
                    return line.strip()
    return "unknown"


def analyze_kernel(extract_dir):
    """Find kernel version from extracted images."""
    # Check for kernel strings in any large binary files
    for pattern in ["*uImage*", "*zImage*", "*Image*"]:
        found = find_files_glob(extract_dir, pattern)
        for f in found:
            f = str(f)
            if os.path.getsize(f) > 500000:
                output = run(f"strings '{f}' | grep 'Linux version' | head -1")
                if "Linux version" in output:
                    return output.strip()

    # Try /proc or profile files in rootfs
    for name in ["profile_prjcfg", "version"]:
        found = find_files(extract_dir, name)
        for f in found:
            with open(f, "r", errors="replace") as fh:
                content = fh.read()
                m = re.search(r'Linux version [\d.]+', content)
                if m:
                    return m.group()

    return "unknown"


def analyze_live555(extract_dir):
    """Find live555 streaming library version."""
    for name in ["libLiveMedia.so", "libliveMedia.so", "live555"]:
        found = find_files(extract_dir, name)
        for f in found:
            output = run(f"strings '{f}' | grep -E '20[12][0-9]\\.[01][0-9]\\.[0-3][0-9]' | head -3")
            for line in output.split("\n"):
                m = re.search(r'20\d{2}\.\d{2}\.\d{2}', line)
                if m:
                    return m.group()
    return None


def analyze_mbedtls(extract_dir):
    """Find Mbed TLS version."""
    for name in ["libmbedcrypto.so", "libmbedtls.so", "libmbedx509.so"]:
        found = find_files(extract_dir, name)
        for f in found:
            output = run(f"strings '{f}' | grep -i 'mbed.tls' | head -5")
            for line in output.split("\n"):
                m = re.search(r'Mbed TLS [\d.]+', line, re.I)
                if m:
                    return m.group()
    return None


def analyze_amcrest_dahua(extract_dir):
    """Check for Amcrest/Dahua code sharing indicators."""
    indicators = []
    for name in ["device", "netserver"]:
        found = find_files(extract_dir, name)
        for f in found:
            if not os.path.isfile(f):
                continue
            output = run(f"strings '{f}' | grep -iE '(amcrest|dahua)' | head -10")
            for line in output.split("\n"):
                line = line.strip()
                if line:
                    indicators.append(line[:100])
    return indicators[:10]


def analyze_dev_paths(extract_dir):
    """Find leaked developer build paths."""
    paths = set()
    for name in ["device", "netserver", "dvr"]:
        found = find_files(extract_dir, name)
        for f in found:
            if not os.path.isfile(f):
                continue
            output = run(f"strings '{f}' | grep -E '/home/[a-z]' | head -10")
            for line in output.split("\n"):
                m = re.search(r'/home/\w+[/\w.]+', line)
                if m:
                    paths.add(m.group()[:100])
    return list(paths)[:10]


def analyze_init_scripts(rootfs):
    """Analyze init scripts for security-relevant settings."""
    result = {"core_dumps": False, "ulimit_settings": [], "services": []}

    init_dirs = [
        os.path.join(rootfs, "etc/init.d"),
        os.path.join(rootfs, "etc/rcS.d"),
    ]

    for init_dir in init_dirs:
        if not os.path.isdir(init_dir):
            continue
        for f in os.listdir(init_dir):
            fp = os.path.join(init_dir, f)
            if not os.path.isfile(fp):
                continue
            try:
                with open(fp, "r", errors="replace") as fh:
                    content = fh.read()
                    if "ulimit -c unlimited" in content:
                        result["core_dumps"] = True
                    for m in re.finditer(r'ulimit\s+\S+', content):
                        result["ulimit_settings"].append(m.group())
            except IOError:
                pass

    # Check rcS or inittab
    for name in ["rcS", "inittab"]:
        found = find_files(rootfs, name)
        for f in found:
            try:
                with open(f, "r", errors="replace") as fh:
                    content = fh.read()
                    if "ulimit -c unlimited" in content:
                        result["core_dumps"] = True
            except IOError:
                pass

    return result


def full_analysis(fw_entry, work_dir):
    """Run full analysis on a firmware entry. Returns dict of findings."""
    model = fw_entry["model"]
    hw_ver = fw_entry["hw_ver"]
    version = fw_entry["version"]
    url = fw_entry["url"]
    arch = fw_entry["arch"]

    print(f"  Downloading {model} ({hw_ver})...")
    fw_file = download_firmware(url, work_dir)
    if not fw_file:
        return {"error": f"Download failed: {url}"}

    print(f"  Extracting...")
    extract_dir = os.path.join(work_dir, "extracted")
    extract_firmware(fw_file, extract_dir)

    # Try to find UBI volumes and extract them
    for ubi_file in find_files_glob(extract_dir, "*.ubi"):
        ubi_out = str(ubi_file) + "_ubifs"
        if not os.path.exists(ubi_out):
            run(f"ubireader_extract_files '{ubi_file}' -o '{ubi_out}'", timeout=120)
    for ubifs_file in find_files_glob(extract_dir, "*.ubifs"):
        ubifs_out = str(ubifs_file) + "_extracted"
        if not os.path.exists(ubifs_out):
            run(f"ubireader_extract_files '{ubifs_file}' -o '{ubifs_out}'", timeout=120)

    print(f"  Finding filesystems...")
    rootfs = find_rootfs(extract_dir)
    appfs = find_appfs(extract_dir)

    if not rootfs and not appfs:
        return {"error": "Could not find root or app filesystem", "extract_dir": extract_dir}

    print(f"  Analyzing security...")
    result = {
        "model": model,
        "hw_ver": hw_ver,
        "version": version,
        "arch": arch,
        "url": url,
        "rootfs_found": rootfs is not None,
        "appfs_found": appfs is not None,
    }

    if rootfs:
        result["passwd"] = analyze_passwd(rootfs)
        result["busybox"] = analyze_busybox(rootfs)
        result["libc"] = analyze_libc(rootfs)
        result["init"] = analyze_init_scripts(rootfs)

    search_dir = extract_dir
    result["tls_certs"] = analyze_tls_cert(appfs or extract_dir)
    result["openssl"] = analyze_openssl(search_dir)
    result["nginx"] = analyze_nginx(search_dir)
    result["dvr_xml"] = analyze_dvr_xml(search_dir)
    result["version_json"] = analyze_version_json(search_dir)
    result["live555"] = analyze_live555(search_dir)
    result["mbedtls"] = analyze_mbedtls(search_dir)
    result["amcrest_dahua"] = analyze_amcrest_dahua(search_dir)
    result["dev_paths"] = analyze_dev_paths(search_dir)
    result["cmd_injection"] = analyze_command_injection(search_dir)
    result["connectivity"] = analyze_connectivity(search_dir)
    result["kernel"] = analyze_kernel(search_dir)

    # Filesystem types
    result["filesystems"] = fw_entry.get("filesystems", [])

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_firmware.py <manifest_index> [work_dir]")
        print("       analyze_firmware.py all [work_dir]")
        sys.exit(1)

    # Use ordered list if available, otherwise manifest
    ordered_path = "/tmp/reolink_fw_ordered.json"
    manifest_path = "/tmp/reolink_fw_manifest.json"
    src = ordered_path if os.path.exists(ordered_path) else manifest_path
    with open(src) as f:
        remaining = json.load(f)

    index = sys.argv[1]
    work_base = sys.argv[2] if len(sys.argv) > 2 else "/tmp/reolink_fw_work"

    if index == "all":
        entries = remaining
    else:
        idx = int(index)
        if idx >= len(remaining):
            print(f"Index {idx} out of range (max {len(remaining)-1})")
            sys.exit(1)
        entries = [remaining[idx]]

    for entry in entries:
        hw = entry["hw_ver"]
        work_dir = os.path.join(work_base, hw)
        output_file = os.path.join(work_base, f"{hw}_analysis.json")

        if os.path.exists(output_file):
            print(f"Skipping {entry['model']} ({hw}) - already analyzed")
            continue

        print(f"\nAnalyzing: {entry['model']} ({hw})")
        try:
            result = full_analysis(entry, work_dir)
            with open(output_file, "w") as f:
                json.dump(result, f, indent=2)
            print(f"  Saved: {output_file}")
        except Exception as e:
            print(f"  ERROR: {e}")
            with open(output_file, "w") as f:
                json.dump({"error": str(e), "model": entry["model"], "hw_ver": hw}, f, indent=2)

        # Clean up extracted files to save disk space
        if os.path.exists(work_dir):
            shutil.rmtree(work_dir, ignore_errors=True)

        print(f"  Done: {entry['model']}")


if __name__ == "__main__":
    main()
