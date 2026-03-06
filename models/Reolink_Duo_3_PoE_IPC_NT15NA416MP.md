# Reolink Duo 3 PoE

[Back to overview](../README.md)

**Hardware**: IPC_NT15NA416MP (also seen as IPC_NT13NA416MP)
**Firmware**: v3.0.0.4867_2505072124
**Platform**: Novatek NT98530 SoC, AArch64, Linux 5.10.168, glibc 2.35
**Device**: Reolink Duo 3 PoE (16MP dual-lens)
**Parent company**: Baichuan (hostname set to `BAICHUAN`)

---

## Firmware Structure

The `.pak` firmware file contains these partitions, mapped to flash MTD devices:

| Partition | Version | Description |
|-----------|---------|-------------|
| loader | 9943 | Boot loader |
| fdt | 10115 | Flattened Device Tree |
| atf | 9982 | ARM Trusted Firmware |
| uboot | 9982 | U-Boot bootloader |
| kernel | 11626 | Linux 5.10.168 kernel |
| rootfs | 12580 | Root filesystem (SquashFS, xz) |
| ai | 250507006500 | AI model data |
| app | v3.0.0.4867_2505072124 | Application partition (SquashFS, xz) |

The rootfs contains the base Linux system (busybox, init scripts, kernel modules). The app partition contains all Reolink application binaries, libraries, web interface, and configuration. A separate partition provides a writable parameters area mounted at `/mnt/para`.

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
- Email: `CERTIFICATE@CERTIFICATE.com`
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

### 4. Potential Command Injection in CGI

Multiple shell command constructions use unsanitized format strings:

- **Samba password setting**: `(echo %s; echo %s)| smbpasswd -s -c /var/run/samba/smb.conf -a root`
- **DNS resolver setting**: `echo "nameserver %s" > /etc/resolv.conf`
- **DDNS configuration**: `/mnt/tmp/ddns/ddns-config %s.swanndvr.net %s %s %s %d %s`
- **Network interface configuration**: `ifconfig %s`, `ifconfig %s hw ether %s`, `ifconfig %s %u.%u.%u.%u`
- **Route configuration**: `route add default dev %s gw %u.%u.%u.%u`

These are classic command injection vectors if user input is not properly sanitized before being passed to shell execution.

---

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | 3.3.2 (current, supported) |
| Mbed TLS | 2.28.9 (LTS, supported) |
| BusyBox | 1.36.0 (dangerous applets: httpd, wget, tftp) |
| live555 | 2025-03-21 |
| TLS certificate | RSA 2048 bit, self-signed, shared across all devices |
| TLS cert expiry | May 7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled (`support_supper_pwd="1"`) |
| Default password | *(empty)* |
| Amcrest/Dahua code | Not found in this firmware version |

---

## High and Medium Severity Issues

### High Severity

| Issue | Details |
|-------|---------|
| No privilege separation | Everything runs as root. No user accounts, no sandboxing, no capability dropping. A single exploit gives full device control. |
| `eval()` in web UI | `ControllerRemoteConfig.js` uses `eval(vars.js)` to execute server-provided JavaScript. If an attacker can inject content into the response, this enables XSS. |
| FTP/TFTP configured in inetd | `/etc/inetd.conf` configures FTP on port 21 (serving `/mnt/sd` as root) and TFTP on port 69 (serving `/home` as root). |

### Medium Severity

| Issue | Details |
|-------|---------|
| "Super password" mechanism | `support_supper_pwd="1"` enables a password recovery/bypass feature. Security depends on the algorithm's unpredictability. |
| AES key/IV logged in debug messages | Debug strings include: `encrypt str:%s, hex_buf_len:%d, aes_key=%s, iv:%s`. Encryption parameters disclosed if logs are accessible. |
| Debug/factory test modes | `MSG_RPCTOOL_DEBUG`, `MSG_PLAY_DEBUG`, `MSG_FTY_DEBUG_*`, `MSG_DIAG_TEST_MODE_SET` suggest debug and factory test modes may be triggerable at runtime. |
| Samba root mapping | Camera's admin user is mapped to system root: `root=admin` in `/var/run/samba/smbusers`. |
| Core dumps enabled | `/etc/profile` sets `ulimit -c unlimited` with core dumps saved to `/var/log/core-*`, potentially leaking sensitive memory contents. |
| DDNS over HTTP | DDNS update credentials for 3322.org, Swann DVR, and others are transmitted over plain HTTP. |

### Low Severity

| Issue | Details |
|-------|---------|
| HSTS disabled | `Strict-Transport-Security` header is commented out in nginx.conf. |
| No TLS 1.3 | Only TLS 1.2 is configured. TLS 1.0/1.1 and SSLv3 are correctly excluded. |
| Developer paths leaked | Build paths embedded in binaries: `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/` |
| Empty default password | `dvr.xml` sets `default_pwd=""` (empty). While `enable_pwd="1"` requires a password, first-time setup starts with no password. |

---

## Connectivity Analysis

### Cloud Services (Outbound HTTPS)

| Service | Endpoint | Port | Purpose |
|---------|----------|------|---------|
| Cloud API | `devices-apis.reolink.com` | 443 | Cloud storage, device management |
| Firmware Updates | `devices-apis.reolink.com` | 443 | OTA update checks and downloads |
| Push Notifications | `pushx.reolink.com` | 9501 | Alert push delivery |

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
| `ropclient` | Remote operations client |
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

---

## Boot Sequence

1. **Kernel** boots, mounts rootfs
2. **`/init`** mounts sysfs, proc, tmpfs, devpts, debugfs. Populates `/dev`, runs `mdev -s`, installs busybox symlinks, execs `/sbin/init`
3. **`/etc/inittab`** runs `rcS` as sysinit (serial shell lines are commented out)
4. **`/etc/init.d/rcS`** sources `/etc/profile_prjcfg`, runs `mount -a`, executes init scripts in order:
   - `S00_PreReady`: Mounts app partition, starts watchdog
   - `S07_SysInit`: Sets up mdev hotplug, loads MMC module
   - `S10_SysInit2`: Loads ~50 kernel modules (video, audio, ISP, AI, sensors IMX678/IMX415/OS08C10, cryptodev, DSP)
   - `S15_NvtAppInit`: Starts `crond`
   - `S25_Net`: Loads Ethernet driver, configures network
   - `S99_Sysctl`: Applies sysctl, runs `start_app`
5. **`start_app`**: Mounts parameters partition, sets memory cgroup limits (20MB), checks serial console access, starts all application binaries

Serial console access is controlled by GPIO pin state or presence of `REOCYP` string in `/mnt/para/system.cfg` (checked in `serial_check.sh`).

---

## Developer Build Paths

- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/main_device.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/audio/src/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/isp/src/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/service/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/snap/src/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/sys/src/`

---

## Attack Chain Summary

The most dangerous attack chain combines these findings:

1. **MITM capability**: The shared TLS private key allows intercepting HTTPS traffic to any device running this firmware
2. **Firmware injection**: No cryptographic signature verification means a MITM attacker can serve malicious firmware updates
3. **Web exploitation**: Potential command injection in CGI handlers provides a remote code execution path
4. **Full control**: Everything runs as root with no privilege separation. Any single exploit gives complete device control

---

## Recommendations

1. Generate unique TLS keys per device during first boot
2. Implement cryptographic firmware signature verification (RSA/ECDSA)
3. Drop root privileges for nginx and application daemons
4. Add `/etc/shadow` with proper permissions and use a strong hash algorithm (SHA-512)
5. Sanitize all user input before passing to shell commands
6. Implement privilege separation (run services as non-root users)
7. Disable core dumps in production builds
8. Remove debug message types from production firmware
9. Enable HSTS and add TLS 1.3 support
10. Use HTTPS for all DDNS update requests
11. Remove the `eval()` call in the web UI
