# Reolink Duo 3 PoE Firmware Security & Connectivity Analysis

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
