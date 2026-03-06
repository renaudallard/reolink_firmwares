# Reolink Firmware Security & Connectivity Analysis

## Models Analyzed

| Model | Firmware | Build Date | Platform | Architecture |
|-------|----------|------------|----------|--------------|
| [Reolink Duo 3 PoE](#reolink-duo-3-poe) | v3.0.0.5049_2506302188 | 2025-06-30 | Novatek NT98530 | AArch64 |
| [Reolink RLC-1224A](#reolink-rlc-1224a) | v3.1.0.2174_23050816 | 2023-05-08 | Novatek NT9852x | ARM 32-bit |

## Cross-Model Comparison

| Feature | RLC-1224A | Duo 3 PoE |
|---------|-----------|-----------|
| Build date | 2023-05-08 | 2025-06-30 |
| Codebase | V14 branch (2021) | V20.3 branch (2025) |
| SoC | Novatek NT9852x | Novatek NT98530 |
| Architecture | ARM 32-bit (armhf) | AArch64 (64-bit) |
| Kernel | Linux 4.19.91 | Linux 4.19.148 |
| glibc | 2.29 | 2.30 |
| BusyBox | 1.24.1 | 1.31.1 |
| Filesystem | UBIFS (SPI NAND) | SquashFS (xz) |
| OpenSSL | **1.0.2f (2016, EOL)** | 3.3.2 |
| Mbed TLS | 2.24.0 | 2.28.9 |
| nginx | 1.14.2 (2018) | 1.2.8 (2013) |
| live555 | 2019-09-02 | 2025-03-21 |
| TLS cert key size | RSA 4096-bit | RSA 2048-bit |
| TLS cert fingerprint | `0D:5D:11:C4:...` | `C3:61:12:65:...` |
| Root password hash | `XF4sg5T82tV4k` | `aRDwnwAt1ygAM` |
| telnetd in busybox | **Yes (compiled in)** | No (missing) |
| ftpd/tftpd in busybox | **Yes (compiled in)** | No (missing) |
| Cloud storage | Disabled | Enabled |
| P2P library | Built into netserver | Separate libp2p.so/libp2pc.so |
| AI inference library | None (broken CNNLib symlink) | libarm_compute.so |
| Parent company | Baichuan | Baichuan |

The RLC-1224A firmware is significantly older and uses more outdated components. The most critical difference is OpenSSL 1.0.2f (EOL since 2020) versus the Duo 3 PoE's OpenSSL 3.3.2. The presence of `telnetd` compiled into busybox also makes post-exploitation persistence easier on the RLC-1224A.

## Common Vulnerabilities Across All Models

These issues are present in every firmware analyzed:

| Vulnerability | Severity |
|---------------|----------|
| Hardcoded root password with weak DES hash in `/etc/passwd`, no `/etc/shadow` | Critical |
| Shared TLS private key baked into firmware (per product line) | Critical |
| No cryptographic firmware signature verification (CRC32 + MD5 only) | Critical |
| nginx running as root with no privilege separation | Critical |
| Potential command injection in CGI (smbpasswd, resolv.conf, ddns-config, ifconfig) | Critical |
| Everything runs as root, no privilege separation | High |
| `eval(vars.js)` in `ControllerRemoteConfig.js` web UI | High |
| "Super password" bypass mechanism (`support_supper_pwd="1"`) | Medium |
| Debug/factory test modes present in all binaries | Medium |
| Samba admin-to-root mapping | Medium |
| Core dumps enabled (`ulimit -c unlimited`) | Medium |
| DDNS credentials sent over plain HTTP (3322.org, Swann, PerfectEyes) | Medium |
| Amcrest/Dahua code sharing (`AmcrestToken` in binaries) | Medium |
| Outdated Linux 4.19 kernel | Medium |
| HSTS disabled, no TLS 1.3 | Low |
| Developer build paths leaked in binaries | Low |
| Empty default password (`default_pwd=""`) | Low |

---
---

# Reolink Duo 3 PoE

**Firmware**: v3.0.0.5049_2506302188 (built 2025-06-30)
**Platform**: Novatek NT98530 SoC, AArch64, Linux 4.19.148, glibc 2.30
**Device**: Reolink Duo 3 PoE (IPC_NT13NA416MP, 16MP)
**Parent company**: Baichuan (hostname set to `BAICHUAN`)

---

## Firmware Structure

The `.pak` firmware file contains these partitions, mapped to flash MTD devices:

| Partition | MTD Device | Description |
|-----------|------------|-------------|
| loader | /dev/mtd0 | Boot loader |
| fdt | /dev/mtd1 | Flattened Device Tree |
| atf | /dev/mtd2 | ARM Trusted Firmware |
| uboot | /dev/mtd3 | U-Boot bootloader |
| kernel | /dev/mtd4 | Linux 4.19.148 kernel |
| rootfs | /dev/mtd5 | Root filesystem (SquashFS, xz, 770 inodes) |
| app | /dev/mtd6 | Application partition (SquashFS, xz, 267 inodes) |
| para | /dev/mtd7 | Parameters partition (yaffs2, read-write) |
| sp | /dev/mtd8 | Spare partition |

The rootfs contains the base Linux system (busybox, init scripts, kernel modules). The app partition contains all Reolink application binaries, libraries, web interface, and configuration.

---

## Critical Vulnerabilities

### 1. Hardcoded Root Password with Weak DES Hash

`/etc/passwd` contains:
```
root:aRDwnwAt1ygAM:0:0:root:/root:/bin/sh
```

There is no `/etc/shadow` file. The hash uses the legacy DES crypt algorithm (only 8 significant password characters, 13-character hash with 2-character salt). This is brute-forcible in minutes on modern hardware. Only one user exists on the system (`root`, UID 0).

### 2. Shared TLS Private Key Across All Devices

The files `self.key` and `self.crt` are baked into the firmware image (and duplicated in `nginx_conf/`). Every Reolink Duo 3 PoE running this firmware version shares the **same RSA 2048-bit private key**.

Certificate details:
- Subject: `C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE`
- Validity: 2023-05-12 to 2043-05-07 (20 years)
- X.509 v1 (no extensions), Serial: 1
- SHA1 Fingerprint: `C3:61:12:65:DD:E2:FF:12:AE:C1:49:4B:16:88:2A:A1:06:24:03:8E`

Any attacker who downloads this firmware can extract the private key and perform man-in-the-middle attacks against HTTPS connections to any device running this firmware.

### 3. No Cryptographic Firmware Signature Verification

Firmware updates are verified only by:
- Magic number checks
- CRC32 checksums
- Board type validation

No RSA/ECDSA signature verification was found. The router binary uses MD5-based signature checking (`check different!md5SignedKey`), which is cryptographically broken. Combined with the shared TLS key (to MITM the update connection), an attacker could push malicious firmware to any device.

### 4. Nginx 1.2.8 Running as Root

The web server version dates from **2013** and has numerous known CVEs. It runs as `user root root` with no privilege separation. All CGI requests are proxied to `cgiserver.cgi` via FastCGI on localhost port 9527.

### 5. Potential Command Injection in CGI

Multiple shell command constructions use unsanitized format strings:

- **Samba password setting**: `(echo %s; echo %s)| smbpasswd -s -c /var/run/samba/smb.conf -a root`
- **DNS resolver setting**: `echo "nameserver %s" > /etc/resolv.conf`
- **DDNS configuration**: `/mnt/tmp/ddns/ddns-config %s.swanndvr.net %s %s %s %d %s`
- **Network interface configuration**: `ifconfig` commands with `%s` format strings

These are classic command injection vectors if user input is not properly sanitized before being passed to shell execution.

---

## High and Medium Severity Issues

### High Severity

| Issue | Details |
|-------|---------|
| No privilege separation | Everything runs as root. No user accounts, no sandboxing, no capability dropping. A single exploit gives full device control. |
| `eval()` in web UI | `ControllerRemoteConfig.js` (line 91) uses `eval(vars.js)` to execute server-provided JavaScript. If an attacker can inject content into the response, this enables XSS. |
| FTP/TFTP configured in inetd | `/etc/inetd.conf` configures FTP on port 21 (serving `/mnt/sd` as root) and TFTP on port 69 (serving `/home` as root). inetd startup is commented out and the `ftpd`/`tftpd` applets are not compiled into busybox, so this is not active. |

### Medium Severity

| Issue | Details |
|-------|---------|
| "Super password" mechanism | `support_supper_pwd="1"` enables a password recovery/bypass feature. Security depends on the algorithm's unpredictability. |
| AES key/IV logged in debug messages | Debug strings include: `encrypt str:%s, hex_buf_len:%d, aes_key=%s, iv:%s`. Encryption parameters disclosed if logs are accessible. |
| Debug/factory test modes | `MSG_RPCTOOL_DEBUG`, `MSG_PLAY_DEBUG`, `MSG_FTY_DEBUG_*`, `MSG_DIAG_TEST_MODE_SET` suggest debug and factory test modes may be triggerable at runtime. |
| Samba root mapping | Camera's admin user is mapped to system root: `root=admin` in `/var/run/samba/smbusers`. |
| Core dumps enabled | `/etc/profile` sets `ulimit -c unlimited` with core dumps saved to `/var/log/core-*`, potentially leaking sensitive memory contents. |
| DDNS over HTTP | DDNS update credentials for DynDNS, 3322.org, and others are transmitted over plain HTTP. |
| Outdated kernel | Linux 4.19.148 is significantly outdated and likely contains known CVEs. |
| Amcrest/Dahua code sharing | The string `AmcrestToken` appears in binaries, suggesting shared codebase with Amcrest/Dahua cameras. Vulnerabilities in those platforms may apply here. |

### Low Severity

| Issue | Details |
|-------|---------|
| HSTS disabled | `Strict-Transport-Security` header is commented out in nginx.conf. |
| No TLS 1.3 | Only TLS 1.2 is configured. TLS 1.0/1.1 and SSLv3 are correctly excluded. |
| Developer paths leaked | Build paths embedded in binaries: `/home/liqy/release/2025/release_20250630/ipc_20220409_V20.3/`, `/home/gt/ai/v20.3/sc/trunk/src/`. |
| SDK path in profile | `/etc/profile_prjcfg` exposes: `export MODEL=/home/zyc/530_sdk/na51102_linux_sdk/configs/...` |
| Empty default password | `dvr.xml` sets `default_pwd=""` (empty). While `enable_pwd="1"` requires a password, first-time setup starts with no password. |

---

## Connectivity Analysis

### Cloud Services (Outbound HTTPS)

| Service | Endpoint | Port | Purpose |
|---------|----------|------|---------|
| Cloud API | `devices-apis.reolink.com` | 443 | Cloud storage, device management |
| Firmware Updates | `devices-apis.reolink.com` | 443 | OTA update checks and downloads |
| Push Notifications | `pushx.reolink.com` | 9501 | Alert push delivery |

Firmware update URL patterns:
```
https://devices-apis.reolink.com:443/v1.0/devices/roms/latests/?uid=<uid>&build=<build>&board=<board>&mode=full&method=device
https://devices-apis.reolink.com:443/v1.0/devices/roms/latests/?uid=<uid>&build=<build>&board=<board>&mode=partial
```

Cloud storage uses Amazon S3 with presigned URLs and client-side encryption (`x-amz-server-side-encryption-customer-key`).

Cloud authentication uses an OAuth-like flow with `client_id`, `client_secret`, `boot_secret`, and Bearer tokens. A device public key is used for key exchange with `key_seed`, `shared_secret_b64`.

### P2P Infrastructure (Proprietary Protocol)

The camera uses Reolink's proprietary P2P system (not TUTK/IOTC) for remote access. It uses UDP for NAT traversal with TCP relay fallback.

| Domain | Purpose |
|--------|---------|
| `p2p%d.reolink.com` | Numbered P2P relay servers (international) |
| `p2p%d.reolink.com.cn` | Numbered P2P relay servers (China) |
| `p2pm-abr.reolink.com` | P2P management server (international) |
| `p2pm-ali.reolink.com` | P2P management server (Alibaba Cloud/China) |

- Device UID encodes the region for server selection
- Connection types: local discovery, NAT traversal (map), relay
- Both IPv4 and IPv6 supported
- XML-based command protocol (`TiXmlElement`)

### Local Network Services (Listening Ports)

| Service | Default Port | Protocol | Notes |
|---------|-------------|----------|-------|
| HTTP | 80 | TCP | nginx web interface |
| HTTPS | 443 | TCP | nginx, shared TLS key |
| RTMP | 1935 | TCP | nginx-rtmp module (apps: `live`, `vod`, `bcs`) |
| RTSP | configurable | TCP | live555 library (streams: `Preview_XX_main`, `Preview_XX_sub`) |
| ONVIF | configurable | TCP | Full Profile S/T implementation |
| Samba/SMB | standard | TCP | SD card share, NetBIOS name: `reolink`, workgroup: `WORKGROUP` |
| FLV Live | on HTTP/HTTPS | TCP | nginx `/flv` location |
| FastCGI | 9527 | TCP | localhost only (127.0.0.1) |

The camera automatically maps ports via UPnP IGD: HTTP, HTTPS, RTSP, ONVIF, RTMP.

### ONVIF Endpoints

- `http://<ip>:<port>/onvif/device_service`
- `http://<ip>:<port>/onvif/media_service`
- `http://<ip>:<port>/onvif/event_service`
- `http://<ip>:<port>/onvif/ptz_service`
- `http://<ip>:<port>/onvif/imaging_service`
- `http://<ip>:<port>/onvif/analytics_service`
- `http://<ip>:<port>/onvif/deviceIO_service`

WS-Discovery multicast addresses: `239.255.255.250` (SSDP), `239.0.1.0`

### DDNS Providers

| Provider | Server | Protocol |
|----------|--------|----------|
| DynDNS | `members.dyndns.org` | HTTPS |
| No-IP | `dynupdate.no-ip.com` | HTTPS |
| 3322.org | `members.3322.org` | HTTP |
| Swann DVR | `mydvr.swanndvr.com` | HTTP |
| PerfectEyes | `www.perfecteyes.com` | HTTP |
| Custom | User-configurable | User-configurable |

### Other Outbound Connections

| Purpose | Endpoint | Protocol |
|---------|----------|----------|
| NTP time sync | `pool.ntp.org` | NTP (UDP 123) |
| Connectivity check | `www.google.com` | ICMP ping |
| Connectivity check | `p2p.reolink.com` | ICMP ping |
| Cloud storage upload | Amazon S3 | HTTPS (presigned URLs) |
| Email alerts | User-configured SMTP | SMTP/SMTPS |
| FTP alerts | User-configured FTP server | FTP/FTPS |
| Webhooks | User-configured URLs | HTTPS |
| Fallback server | `54.235.60.142` | HTTPS (AWS us-east-1, hardcoded) |

### Smart Home Integration

`smarthome_proto="3"` is enabled. References to Amazon Alexa and Google integrations exist in the binaries.

### Protocols Not Found

No evidence of: MQTT, XMPP, WebSocket (wss/ws), SSH/Dropbear, Firebase Cloud Messaging, Apple Push Notification Service (APNs), or direct Chinese cloud provider integration beyond `.com.cn` P2P endpoints.

---

## Application Stack

The device starts these processes at boot (via `/etc/init.d/start_app`):

| Binary | Purpose |
|--------|---------|
| `router` | Network routing, DDNS, firewall |
| `device` | Core device management, hardware control |
| `recorder` | Video recording to SD card |
| `alarmcenter` | Motion/AI detection alerts |
| `netserver` | Network protocol server (P2P, proprietary) |
| `netclient` | Network client connections |
| `upgrade` | Firmware update manager |
| `cloud` | Cloud service client (S3 upload, API) |
| `push` | Push notification client |
| `factory` | Factory test/calibration |
| `rtsp` | RTSP streaming server |
| `ftp` | FTP alert upload client |
| `onvif` | ONVIF protocol server |
| `nginx` | Web server (HTTP/HTTPS/RTMP) |
| `spawn-fcgi` | FastCGI process manager |
| `cgiserver.cgi` | CGI API handler |
| `watchdog_monitor_start` | Hardware watchdog |

### Key Libraries

| Library | Purpose |
|---------|---------|
| `libcrypto.so` / `libssl.so` | OpenSSL 3.3.2 (crypto, TLS) |
| `libmbedtls.so` / `libmbedcrypto.so` / `libmbedx509.so` | Mbed TLS 2.28.9 (alternative TLS stack) |
| `libp2p.so` / `libp2pc.so` | Proprietary P2P connectivity |
| `liblive555.so` | RTSP streaming (live555, built 2025-03-21) |
| `libbase.so` | Base library (also symlinked as `libcrypt.so.1`) |
| `libnetpublic.so` | Network protocol utilities |
| `libStorageFileManager.so` | SD card / storage management |
| `libbchpc.so` | Baichuan HPC library |
| `libfsadpt.so` | Filesystem adapter |
| `libarm_compute.so` | ARM Compute Library (AI inference) |

### Web Interface API

The CGI API endpoint is `cgi-bin/api.cgi`. Authentication uses HTTP Digest. Notable API commands include:

Login, Logout, Reboot, Format, Snap, Search, AddUser, DelUser, GetUser, SetEmail, SetFtp, SetDdns, SetWifi, UpgradeOnline, ImportCertificate, SetWebHook, ExportCfg, and approximately 100 additional Get/Set commands for all device functions.

---

## Boot Sequence

1. **Kernel** boots, mounts rootfs
2. **`/init`** mounts sysfs, proc, tmpfs, devpts, debugfs. Populates `/dev`, runs `mdev -s`, installs busybox symlinks, execs `/sbin/init`
3. **`/etc/inittab`** runs `rcS` as sysinit (serial shell lines are commented out)
4. **`/etc/init.d/rcS`** sources `/etc/profile_prjcfg`, runs `mount -a`, executes init scripts in order:
   - `S00_PreReady`: Mounts app partition from `/dev/romblock6`, starts watchdog
   - `S07_SysInit`: Sets up mdev hotplug, loads MMC module
   - `S10_SysInit2`: Loads ~50 kernel modules (video, audio, ISP, AI, sensors IMX678/IMX415/OS08C10, cryptodev, DSP)
   - `S15_NvtAppInit`: Starts `crond`
   - `S25_Net`: Loads Ethernet driver, configures network. Attempts to start `telnetd` but the applet is not compiled into busybox, so it silently fails.
   - `S99_Sysctl`: Applies sysctl, runs `start_app`
5. **`start_app`**: Mounts parameters partition, enables WiFi GPIO, sets memory cgroup limits (20MB), checks serial console access, starts all application binaries

Serial console access is controlled by GPIO pin state or presence of `REOCYP` string in `/mnt/para/system.cfg` (checked in `serial_check.sh`).

---

## Busybox

Busybox v1.31.1 provides 310 applets. Notably, `telnetd`, `telnet`, `ftpd`, `tftpd`, and `httpd` are **not compiled in** despite symlinks existing for them. The init script `S25_Net` calls `telnetd` but it silently fails because the applet is missing.

Security-relevant applets that **are** compiled in:

- **Network**: `wget`, `ssl_client`, `udhcpc`, `ntpd`, `dnsd`, `nslookup`, `tcpsvd`, `udpsvd`, `zcip`
- **User management**: `login`, `getty`
- **Hardware access**: `devmem`, `i2cdetect`, `i2cdump`, `i2cget`, `i2cset`, `i2ctransfer`
- **Flash operations**: `flashcp`, `flash_eraseall`, `flash_lock`, `flash_unlock`, `nanddump`, `nandwrite`
- **UBI operations**: `ubiattach`, `ubidetach`, `ubimkvol`, `ubirename`, `ubirmvol`, `ubirsvol`, `ubiupdatevol`

---

## Attack Chain Summary

The most dangerous attack chain combines these findings:

1. **MITM capability**: The shared TLS private key allows intercepting HTTPS traffic to any device running this firmware
2. **Firmware injection**: No cryptographic signature verification means a MITM attacker can serve malicious firmware updates
3. **Web exploitation**: Nginx 1.2.8 (2013) running as root with potential command injection in CGI handlers provides a remote code execution path
4. **Full control**: Everything runs as root with no privilege separation. Any single exploit gives complete device control

Note: Telnet is **not active** despite the init script attempting to start it. The `telnetd` applet is not compiled into busybox, so port 23 is closed. However, the hardcoded root password hash in `/etc/passwd` remains a concern if any shell access is obtained through other means.

---

## Recommendations

1. Generate unique TLS keys per device during first boot
2. Implement cryptographic firmware signature verification (RSA/ECDSA)
3. Upgrade nginx to a current version and drop root privileges
4. Add `/etc/shadow` with proper permissions and use a strong hash algorithm (SHA-512)
5. Sanitize all user input before passing to shell commands
6. Implement privilege separation (run services as non-root users)
7. Disable core dumps in production builds
8. Remove debug message types from production firmware
9. Enable HSTS and add TLS 1.3 support
10. Use HTTPS for all DDNS update requests
11. Update the Linux kernel to a maintained LTS version
12. Remove dead telnetd symlinks and the `telnetd` call from `S25_Net` to avoid confusion and prevent accidental enablement in future busybox builds

---
---

# Reolink RLC-1224A

**Firmware**: v3.1.0.2174_23050816 (built 2023-05-08)
**Platform**: Novatek NT9852x SoC, ARM 32-bit (EABI5, armhf), Linux 4.19.91, glibc 2.29
**Device**: Reolink RLC-1224A (IPC_523D8128M12MP, 12MP, OS12D40 sensor)
**Parent company**: Baichuan (hostname set to `BAICHUAN`)

---

## Firmware Structure

The `.pak` firmware file contains these partitions, stored in UBI volumes on SPI NAND flash:

| Partition | Version | Description |
|-----------|---------|-------------|
| loader | 1801 | Boot loader |
| fdt | 2384 | Flattened Device Tree |
| uboot | 2357 | U-Boot bootloader |
| kernel | 4761 | Linux 4.19.91 kernel |
| rootfs | 5824 | Root filesystem (UBIFS, 32-bit ARM) |
| app | v3.1.0.2174_23050816 | Application partition (UBIFS) |

The rootfs contains the base Linux system (busybox, init scripts, kernel modules). The app partition contains all Reolink application binaries, libraries, web interface, and configuration. A separate UBI volume (MTD8) provides a writable parameters partition mounted at `/mnt/para`.

---

## Critical Vulnerabilities

### 1. Hardcoded Root Password with Weak DES Hash

`/etc/passwd` contains:
```
root:XF4sg5T82tV4k:0:0:root:/root:/bin/sh
```

There is no `/etc/shadow` file. The hash uses the legacy DES crypt algorithm (only 8 significant password characters, 13-character hash with 2-character salt). This is brute-forcible in minutes on modern hardware. Only one user exists on the system (`root`, UID 0). The hash differs from the Duo 3 PoE firmware (`aRDwnwAt1ygAM`), indicating a different root password per product line.

### 2. Shared TLS Private Key Across All Devices

The files `self.key` and `self.crt` are baked into the firmware image (and duplicated in `nginx_conf/`). Every RLC-1224A running this firmware version shares the **same RSA 4096-bit private key**.

Certificate details:
- Subject: `C=CN, ST=GD, L=SZ, O=certificate, OU=certificate, CN=certificate`
- Issuer: `C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE`
- Validity: 2022-06-06 to 2042-06-01 (20 years)
- X.509 v1 (no extensions), Serial: 1
- SHA1 Fingerprint: `0D:5D:11:C4:F3:AB:77:14:F7:5F:24:B4:3B:0D:C2:E4:5A:25:B9:08`

This is a **different key** from the Duo 3 PoE (fingerprint `C3:61:12:65:...`), meaning each product line has its own shared key. Any attacker who downloads this firmware can extract the private key and perform man-in-the-middle attacks against HTTPS connections to any RLC-1224A running this firmware.

### 3. Critically Outdated OpenSSL 1.0.2f (2016)

The firmware ships **OpenSSL 1.0.2f from January 28, 2016**. The OpenSSL 1.0.2 branch reached end-of-life on January 1, 2020. This version has numerous known CVEs including:
- Heartbleed mitigations were applied, but many post-2016 vulnerabilities remain unpatched
- No TLS 1.3 support
- Multiple memory corruption and denial-of-service vulnerabilities

This is dramatically worse than the Duo 3 PoE which ships OpenSSL 3.3.2.

### 4. No Cryptographic Firmware Signature Verification

Firmware updates are verified only by:
- Magic number checks
- CRC32 checksums (`crc failed:0x%x,0x%x`)
- Board type validation

The upgrade binary uses `Md5_encode_string` (MD5-based checking) and CRC verification only. No RSA/ECDSA signature verification was found. Combined with the shared TLS key (to MITM the update connection), an attacker could push malicious firmware to any device.

### 5. Nginx 1.14.2 Running as Root

The web server (nginx 1.14.2 from December 2018) runs as `user root root` with no privilege separation. While newer than the Duo 3 PoE's nginx 1.2.8, version 1.14.2 still has known CVEs and is no longer maintained. All CGI requests are proxied to `cgiserver.cgi` via FastCGI on localhost port 9527.

### 6. Potential Command Injection in CGI

Multiple shell command constructions use unsanitized format strings across `device`, `netserver`, `upgrade`, and `cgiserver.cgi`:

- **Samba password setting**: `(echo %s; echo %s)| %s -s -c /var/run/samba/smb.conf -a root`
- **DNS resolver setting**: `echo "nameserver %s" > /etc/resolv.conf`
- **DDNS configuration**: `/mnt/tmp/ddns/ddns-config %s %s %s %s %d %s`
- **DDNS Swann**: `/mnt/tmp/ddns/ddns-config %s.swanndvr.net %s %s %s %d %s`
- **Network interface configuration**: `ifconfig %s`, `ifconfig %s hw ether %s`, `ifconfig %s %u.%u.%u.%u`

These are classic command injection vectors if user input is not properly sanitized before being passed to shell execution.

---

## High and Medium Severity Issues

### High Severity

| Issue | Details |
|-------|---------|
| No privilege separation | Everything runs as root. No user accounts, no sandboxing, no capability dropping. A single exploit gives full device control. |
| `eval()` in web UI | `ControllerRemoteConfig.js` uses `eval(vars.js)` to execute server-provided JavaScript. If an attacker can inject content into the response, this enables XSS. |
| telnetd compiled into busybox | Unlike the Duo 3 PoE, the `telnetd` applet **is compiled** into BusyBox 1.24.1. While not started by init scripts, it could be enabled trivially if an attacker gains any code execution. Combined with the hardcoded root password, this provides persistent shell access. |
| ftpd/tftpd compiled into busybox | Both `ftpd` and `tftpd` are compiled in and available. inetd.conf has them commented out, and inetd itself is not started, but they're one configuration change away from activation. |
| inetd echo/daytime/time active | `inetd.conf` has echo (TCP/UDP), daytime (TCP/UDP), and time (TCP/UDP) services configured as active. While inetd itself is not started (`#inetd` in S15_NvtAppInit), if inetd were ever enabled, these services would be exposed. |
| Mbed TLS 2.24.0 | An outdated version of Mbed TLS with known vulnerabilities. The Duo 3 PoE ships 2.28.9. |

### Medium Severity

| Issue | Details |
|-------|---------|
| "Super password" mechanism | `support_supper_pwd="1"` enables a password recovery/bypass feature. Security depends on the algorithm's unpredictability. |
| Debug/factory test modes | `MSG_RPCTOOL_DEBUG`, `MSG_PLAY_DEBUG`, `MSG_FTY_DEBUG_*`, `MSG_FTY_TEST_*` messages present in all binaries suggest debug and factory test modes may be triggerable at runtime. |
| Samba root mapping | Camera's admin user is mapped to system root: `username map = /var/run/samba/smbusers`, `root=admin`. |
| Core dumps enabled | `/etc/profile` sets `ulimit -c unlimited` with core dumps saved to `/var/log/core-%e-%p-%t`, potentially leaking sensitive memory contents. |
| DDNS over HTTP | DDNS update credentials for 3322.org, Swann DVR, and PerfectEyes are transmitted over plain HTTP. |
| Outdated kernel | Linux 4.19.91 is significantly outdated and likely contains known CVEs. |
| Amcrest/Dahua code sharing | The string `AmcrestToken` appears in the `device` binary, suggesting shared codebase with Amcrest/Dahua cameras. Vulnerabilities in those platforms may apply here. |
| Outdated live555 | liblive555 version 2019-09-02 (much older than the Duo 3 PoE's 2025-03-21 build). |
| Broken CNNLib symlink | `CNNLib` is a broken symlink to `../src/CNNLib`, suggesting incomplete build or packaging. |

### Low Severity

| Issue | Details |
|-------|---------|
| HSTS disabled | `Strict-Transport-Security` header is commented out in nginx.conf. |
| No TLS 1.3 | Only TLS 1.2 is configured. TLS 1.0/1.1 and SSLv3 are correctly excluded. OpenSSL 1.0.2f cannot support TLS 1.3. |
| Developer paths leaked | Build paths embedded in binaries: `/home/lqy/freq/ipc_20210624_V14/`, `/home/pyc/2021_branch_V14_relese/ipc_20210624_V14/`, `/home/lqy/auto_nengliji/ipc_20210624_V14/` |
| SDK path in profile | `/etc/profile_prjcfg` exposes: `export MODEL=/home/zfj/520_project/sdk/v2.02/NT9852x_linux_sdk_v2.02.000/na51055_linux_sdk_bc/configs/...` |
| Empty default password | `dvr.xml` sets `default_pwd=""` (empty). While `enable_pwd="1"` requires a password, first-time setup starts with no password. |
| `libcrypt.so.1` symlinked to `libcrypto.so` | Non-standard library aliasing that could cause unexpected crypto behavior. |

---

## Connectivity Analysis

### Cloud Services (Outbound HTTPS)

| Service | Endpoint | Port | Purpose |
|---------|----------|------|---------|
| Cloud API | `devices-apis.reolink.com` | 443 | Device management, firmware updates |
| Push Notifications | `pushx.reolink.com` | 9501 | Alert push delivery |

Note: `support_cloud="0"` in dvr.xml means cloud storage is **disabled** on this model.

Firmware update URL patterns use the same `devices-apis.reolink.com:443` endpoint as the Duo 3 PoE.

Cloud authentication uses OAuth-like flow with `client_id`, `Bearer` tokens.

### P2P Infrastructure

The camera uses Reolink's P2P system for remote access.

| Domain | Purpose |
|--------|---------|
| `p2p.reolink.com` | P2P server (international) |
| `p2p.reolink.com.cn` | P2P server (China) |

Note: Unlike the Duo 3 PoE which has numbered `p2p%d.reolink.com` servers and `p2pm-abr`/`p2pm-ali` management servers, this older firmware uses simpler P2P infrastructure. No separate `libp2p.so` library exists. P2P functionality is built directly into `netserver`.

### Local Network Services (Listening Ports)

| Service | Default Port | Protocol | Notes |
|---------|-------------|----------|-------|
| HTTP | 80 | TCP | nginx web interface |
| HTTPS | 443 | TCP | nginx, shared TLS key |
| RTMP | 1935 | TCP | nginx-rtmp module (apps: `live`, `vod`, `bcs`) |
| RTSP | configurable | TCP | live555 library (streams: `h264Preview_XX_main`, `h264Preview_XX_sub`, `h265Preview_XX_main`) |
| ONVIF | configurable | TCP | Profile S/T implementation |
| Samba/SMB | standard | TCP | SD card share |
| FLV Live | on HTTP/HTTPS | TCP | nginx `/flv` location |
| FastCGI | 9527 | TCP | localhost only (127.0.0.1) |

The camera automatically maps ports via UPnP (`support_upnp="1"`): HTTP, HTTPS, RTSP, ONVIF, RTMP.

### ONVIF Endpoints

- `http://<ip>:<port>/onvif/device_service`
- `http://<ip>:<port>/onvif/media_service`
- `http://<ip>:<port>/onvif/event_service`
- `http://<ip>:<port>/onvif/ptz_service`
- `http://<ip>:<port>/onvif/imaging_service`
- `http://<ip>:<port>/onvif/deviceIO_service`

### DDNS Providers

| Provider | Server | Protocol |
|----------|--------|----------|
| DynDNS | `members.dyndns.org` | HTTPS |
| No-IP | `dynupdate.no-ip.com` | HTTPS |
| 3322.org | `members.3322.org` | HTTP |
| Swann DVR | via `ddns-config` | HTTP |
| PerfectEyes | via `ddns-config` | HTTP |

### Other Outbound Connections

| Purpose | Endpoint | Protocol |
|---------|----------|----------|
| NTP time sync | `pool.ntp.org` | NTP (UDP 123) |
| Connectivity check | `p2p.reolink.com` | ICMP ping |
| Email alerts | User-configured SMTP | SMTP/SMTPS |
| FTP alerts | User-configured FTP server | FTP/FTPS |
| Fallback server | `54.235.60.142` | HTTPS (AWS us-east-1, hardcoded) |

### Smart Home Integration

`smarthome_proto="3"` is enabled.

### Protocols Not Found

No evidence of: MQTT, XMPP, WebSocket (wss/ws), SSH/Dropbear, Firebase Cloud Messaging, Apple Push Notification Service (APNs), webhooks, or NAS support on this model.

---

## Application Stack

The device starts these processes at boot (via `/etc/init.d/start_app`):

| Binary | Purpose |
|--------|---------|
| `router` | Network routing, DDNS, firewall |
| `device` | Core device management, hardware control |
| `recorder` | Video recording to SD card |
| `alarmcenter` | Motion/AI detection alerts |
| `netserver` | Network protocol server (P2P, proprietary) |
| `netclient` | Network client connections |
| `upgrade` | Firmware update manager |
| `cloud` | Cloud service client |
| `push` | Push notification client |
| `factory` | Factory test/calibration |
| `rtsp` | RTSP streaming server |
| `ftp` | FTP alert upload client |
| `onvif` | ONVIF protocol server |
| `nginx` | Web server (HTTP/HTTPS/RTMP) |
| `spawn-fcgi` | FastCGI process manager |
| `cgiserver.cgi` | CGI API handler |
| `watchdog_monitor_start` | Hardware watchdog |
| `ftytest` | Factory test (only if present on filesystem) |

### Key Libraries

| Library | Purpose |
|---------|---------|
| `libcrypto.so` / `libssl.so` | OpenSSL 1.0.2f (crypto, TLS). **EOL since 2020.** |
| `libmbedtls.so` / `libmbedcrypto.so` / `libmbedx509.so` | Mbed TLS 2.24.0 (alternative TLS stack) |
| `libbase.so` | Base library (also symlinked as `libcrypt.so.1`) |
| `libnetpublic.so` | Network protocol utilities |
| `libStorageFileManager.so` | SD card / storage management |
| `libbchpc.so` | Baichuan HPC library |
| `libstreambuffer.so` | Stream buffer management |

### Web Interface API

The CGI API endpoint is `cgi-bin/api.cgi`. Authentication uses HTTP Digest. The web UI is Flash-based (uses `bcFlashPlayer`) with an HTML5 alternative (`BcH5Player.js`).

---

## Boot Sequence

1. **Kernel** boots, mounts rootfs
2. **`/init`** mounts sysfs, proc, tmpfs, devpts, debugfs. Populates `/dev`, runs `mdev -s`, installs busybox symlinks, execs `/linuxrc`
3. **`/etc/inittab`** runs `rcS` as sysinit, respawns `/bin/login` on console
4. **`/etc/init.d/rcS`** sources `/etc/profile_prjcfg`, runs `mount -a`, executes init scripts in order:
   - `S00_PreReady`: Attaches UBI volume 1 (MTD7), mounts app partition read-only at `/mnt/app`, starts watchdog, creates `/dev/pts`
   - `S07_SysInit`: Sets up mdev hotplug, loads MMC module
   - `S10_SysInit2`: Loads kernel modules (video, audio, ISP, AI/CNN, sensors IMX415/OS12D40/OS05A10, affine, motion detection)
   - `S15_NvtAppInit`: Starts `crond`. inetd is commented out (`#inetd`). Disables childless PLLs.
   - `S25_Net`: Loads Ethernet driver (`ntkimethmac`), configures network. No telnetd call (unlike Duo 3 PoE).
   - `S99_Sysctl`: Applies sysctl, detects sensor type, runs memory hotplug for OS12D40, then runs `start_app`
5. **`start_app`**: Mounts parameters UBI volume, enables WiFi GPIO, detects sensor, loads PTZ/AF drivers if supported, starts all application binaries. Spawns an additional `/bin/login` process.

Serial console access: `inittab` has `ttyS0` and `ttyUSB0` shell access commented out. The main console respawns `/bin/login`, requiring the root password.

---

## Busybox

Busybox v1.24.1 (2021-09-08) provides applets. Notably, unlike the Duo 3 PoE, **`telnetd`, `ftpd`, `tftpd`, and `httpd` ARE compiled in** and present as symlinks in `/usr/sbin/`.

Security-relevant applets that are compiled in:

- **Network**: `wget`, `ntpd`, `dnsd`, `arping`, `telnetd`, `ftpd`, `tftpd`, `httpd`, `inetd`
- **User management**: `login`, `getty`, `adduser`, `addgroup`, `chpasswd`
- **Hardware access**: `devmem`, `i2cdetect`, `i2cdump`, `i2cget`, `i2cset`
- **Flash operations**: `flashcp`, `flash_eraseall`, `flash_lock`, `flash_unlock`, `nanddump`, `nandwrite`
- **UBI operations**: `ubiattach`, `ubidetach`, `ubiformat`, `ubimkvol`, `ubirmvol`, `ubirsvol`, `ubiupdatevol`

---

## Attack Chain Summary

The most dangerous attack chain combines these findings:

1. **MITM capability**: The shared TLS private key allows intercepting HTTPS traffic to any RLC-1224A running this firmware
2. **Firmware injection**: No cryptographic signature verification means a MITM attacker can serve malicious firmware updates
3. **Web exploitation**: Nginx 1.14.2 running as root with potential command injection in CGI handlers provides a remote code execution path
4. **Full control**: Everything runs as root with no privilege separation. Any single exploit gives complete device control
5. **Persistent access**: Unlike the Duo 3 PoE, `telnetd` is compiled into busybox. An attacker with code execution can start telnetd and use the hardcoded root password for persistent access

The critically outdated OpenSSL 1.0.2f (2016, EOL 2020) significantly increases the attack surface compared to the Duo 3 PoE's OpenSSL 3.3.2.

---

## Recommendations

1. **Urgently upgrade OpenSSL** from 1.0.2f to a supported branch (3.x). This is the single most impactful fix.
2. Generate unique TLS keys per device during first boot
3. Implement cryptographic firmware signature verification (RSA/ECDSA)
4. Upgrade nginx to a current version and drop root privileges
5. Add `/etc/shadow` with proper permissions and use a strong hash algorithm (SHA-512)
6. Sanitize all user input before passing to shell commands
7. Implement privilege separation (run services as non-root users)
8. Disable core dumps in production builds
9. Remove debug message types from production firmware
10. Enable HSTS and add TLS 1.3 support (requires OpenSSL upgrade first)
11. Use HTTPS for all DDNS update requests
12. Update the Linux kernel to a maintained LTS version
13. Remove `telnetd`, `ftpd`, `tftpd` from busybox build or ensure they cannot be started
14. Remove inetd echo/daytime/time services from `inetd.conf`
15. Fix broken `CNNLib` symlink
16. Update Mbed TLS to a current release
17. Update live555 to a current version
