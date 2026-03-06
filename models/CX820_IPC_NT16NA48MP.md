# CX820 (Reolink CX Series 8MP PoE Camera)

[Back to overview](../README.md)

## Hardware Overview

| Property | Value |
|----------|-------|
| Hardware ID | IPC_NT16NA48MP |
| Display Type | CX820 |
| Item Number | P335X |
| SoC | Novatek NS02302 (AArch64) |
| Architecture | AArch64 (ARM 64-bit) |
| Kernel | Linux 5.10.168 |
| C Library | glibc 2.35 (Buildroot) |
| DRAM | 1 GB (0x40000000) |
| Storage | SPI NAND |
| Filesystems | SquashFS (rootfs), SquashFS (appfs) |
| Ethernet | EQOS (ntkimethmac) |
| WiFi | None |
| Hardware Version | D15_V2 |
| SDK | `/home/lmy/svn/sdk/ns02302_linux_sdk/` |
| SDK Config | `ns02302_ipc_a64_evb_defconfig_release` |
| Firmware | v3.2.0.5375_2509162386 |
| Build Date | 2025-09-16 |

## Firmware Partitions

| Partition | Version | OTA Update | Notes |
|-----------|---------|------------|-------|
| loader | 12087 | Forbidden | Bootloader |
| fdt | 11655 | Forbidden | Flattened Device Tree |
| atf | 10052 | Forbidden | ARM Trusted Firmware |
| uboot | 11522 | Forbidden | U-Boot |
| kernel | 11625 | Allowed | Linux 5.10.168 |
| ai | 250318006500 | Allowed | AI model data (policy: optional) |
| rootfs | 28358 | Allowed | Root filesystem |
| app | v3.2.0.5375_2509162386 | Allowed | Application filesystem |

The `forbid_ol_up` flag prevents over-the-air updates to bootloader components (loader, fdt, atf, uboot), while kernel, ai, rootfs, and app can be updated remotely. The `ai` partition uses `up_policy=1` (optional update), all others use `up_policy=0` (mandatory).

## Security Analysis

### Authentication

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt) |
| Shadow file | **No** (hash in `/etc/passwd`) |
| Password algorithm | DES (8-char max, weakest possible) |
| Default user password | *(empty)* |
| Super password | Enabled (`support_supper_pwd="1"`) |
| Max users | 12 total, 2 admin |
| Login lock | Enabled (`support_login_lock="1"`) |
| Signature login | Version 3 |
| ALPU encryption | Enabled |
| BC private key | Enabled |

The root password hash `aRDwnwAt1ygAM` is stored directly in `/etc/passwd` with no shadow file. DES crypt is limited to 8-character passwords and is trivially crackable. All processes run as root with no privilege separation.

### Cryptographic Libraries

| Library | Version | Status |
|---------|---------|--------|
| OpenSSL | **3.3.2** (2024-09-03) | Current, supported |
| Mbed TLS | 2.28.9 | LTS branch, supported |
| live555 | 2024.12.11 | Recent |
| libp2p.so | 2024.07.22 | Reolink proprietary P2P |
| libp2pc.so | - | Reolink proprietary P2P client |

**Notable improvement**: This is the first CX820 platform firmware to ship with OpenSSL 3.3.x instead of the EOL 1.0.x or 1.1.x branches found in older models. This is a significant security improvement.

### Web Server (nginx)

| Property | Value |
|----------|-------|
| Version | **Obfuscated** (`nginx/FakeVersion`) |
| Server tokens | Off |
| Worker processes | 1 |
| Worker connections | 1024 |
| TLS protocols | TLSv1.2 only |
| CGI backend | spawn-fcgi on 127.0.0.1:9527 |
| RTMP support | Built-in module |
| FLV live | Enabled |
| HTTP to HTTPS redirect | Conditional |

**Security headers** configured in nginx:
- `X-Frame-Options: SAMEORIGIN` (clickjacking protection)
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`
- `server_tokens off` (version hidden)
- HSTS header present but commented out

**TLS cipher suite** is well-configured: strong ECDHE/DHE ciphers, explicit exclusion of aNULL, eNULL, EXPORT, DES, RC4, MD5, PSK, 3DES. Only TLSv1.2 enabled.

### TLS Certificate

| Property | Value |
|----------|-------|
| Type | Self-signed, X.509 v1 |
| Key | RSA 2048 bit |
| Signature | SHA-256 |
| Subject | C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE |
| Email | CERTIFICATE@CERTIFICATE.com |
| Valid from | May 12 09:36:46 2023 GMT |
| Expires | May 7 09:36:46 2043 GMT |
| SHA1 Fingerprint | C3:61:12:65:DD:E2:FF:12:AE:C1:49:4B:16:88:2A:A1:06:24:03:8E |

The private key is shipped in the firmware at `/mnt/app/self.key`. Same certificate and private key shared across all devices of this hardware revision. Any attacker with access to the firmware can decrypt TLS traffic or perform MITM attacks.

### BusyBox

| Property | Value |
|----------|-------|
| Version | 1.36.0 (2024-03-21) |
| Dangerous applets | httpd, wget, tftp |
| Not compiled | telnetd, ftpd, tftpd |

### Network Services

Services started at boot (from `start_app` and init scripts):

| Service | Type | Notes |
|---------|------|-------|
| nginx | HTTP/HTTPS/RTMP | Ports 80, 443, 1935 (from dvr.xml) |
| cgiserver.cgi | FastCGI | Via spawn-fcgi on 127.0.0.1:9527 |
| telnetd | Telnet | Started in `S25_Net` script unconditionally |
| crond | Cron | Started in `S15_NvtAppInit` |
| getty | Serial | On /dev/ttyS0 at 115200 baud (always started) |
| device | App daemon | Camera/ISP/audio control |
| netserver | App daemon | Network protocol handler |
| netclient | App daemon | Network client |
| router | App daemon | Configuration/routing |
| cloud | App daemon | Cloud connectivity |
| push | App daemon | Push notifications |
| rtsp | App daemon | RTSP streaming |
| onvif | App daemon | ONVIF protocol |
| recorder | App daemon | Video recording |
| alarmcenter | App daemon | Alarm management |
| ftp | App daemon | FTP uploads |
| upgrade | App daemon | Firmware upgrade |
| factory | App daemon | Factory test |
| ropclient | App daemon | Remote operations |
| watchdog_monitor_start | System | Started in S00_PreReady |

**Critical finding**: `telnetd` is started unconditionally in `/etc/init.d/S25_Net` (line: `telnetd`), providing remote root shell access with the DES-encrypted password. The serial console (`getty 115200 /dev/ttyS0`) is also always started in `start_app`, not gated by `/mnt/tmp/serial_open` (the check is commented out).

### inetd Services

Active services in `/etc/inetd.conf`:
- **echo** (TCP stream + UDP dgram) as root
- **daytime** (TCP stream + UDP dgram) as root
- **time** (TCP stream + UDP dgram) as root
- **FTP** on port 21 (`ftpd -w /mnt/sd`) as root, serving SD card contents
- **TFTP** on port 69 (`tftpd -l -c /home`) as root, serving `/home`

**Critical**: FTP and TFTP services are enabled in inetd.conf, providing unauthenticated file access to the SD card and `/home` directory.

### Cloud and P2P Connectivity

| Endpoint | Purpose |
|----------|---------|
| `devices-apis.reolink.com:443` | Update server and cloud API |
| `pushx.reolink.com:9501` | Push notification server |
| `p2p.reolink.com` | P2P connection broker |
| `p2p.reolink.com.cn` | P2P connection broker (China) |
| `p2p%d.reolink.com` | P2P numbered servers |
| `p2pm-abr.reolink.com` | P2P ABR server |
| `p2pm-ali.reolink.com` | P2P Alibaba server |
| `p2p1.reolink.review` | P2P review/staging server |
| `pool.ntp.org` | NTP time sync |
| `members.3322.org` | 3322 DDNS |
| `members.dyndns.org` | DynDNS |
| `dynupdate.no-ip.com` | No-IP DDNS |

P2P connectivity uses Reolink's proprietary `libp2p.so`/`libp2pc.so` libraries (not TUTK). Supports relay, local, and P2P connection modes. MQTT protocol is used for IoT communication with TLS (Mbed TLS).

Cloud features: `support_cloud="1"`, `support_cloud_encrypt="1"`, `cloud_mem_size="7340032"` (7 MB).

### Firmware Integrity

| Check | Result |
|-------|--------|
| Digital signature | **No** (CRC only) |
| Firmware verification | CRC32 checksums |
| Board type check | Yes |
| Online update | Enabled (policy: automatic) |
| SD card upgrade | Disabled |
| Reset upgrade | Disabled |

The `upgrade` binary validates firmware using CRC32 checksums and board type checks but performs no cryptographic signature verification (no RSA/ECDSA/HMAC). An attacker who can intercept the update channel or access the device network can push malicious firmware.

### Amcrest/Dahua Heritage

**None found**. Unlike older Reolink models (IPC_523128M8MP, etc.) that contain `AmcrestToken` strings, the CX820 platform shows no Amcrest/Dahua code references. This appears to be a clean break from the Dahua SDK heritage.

## Boot Sequence

1. **loader** (Novatek bootloader)
2. **ATF** (ARM Trusted Firmware)
3. **U-Boot** (boot configuration)
4. **Kernel** (Linux 5.10.168)
5. **rcS** runs init scripts S00 through S99:
   - `S00_PreReady`: Mounts appfs (SquashFS from `/dev/romblock7`), starts watchdog
   - `S07_SysInit`: MMC hotplug, mdev
   - `S10_SysInit2`: Loads all HDAL kernel modules (video capture, processing, encoding, AI, sensors, audio)
   - `S15_NvtAppInit`: Starts crond, disables unused PLLs
   - `S25_Net`: Loads Ethernet driver (`ntkimethmac`), configures network, **starts telnetd**
   - `S99_Sysctl`: Kernel tuning, calls `start_app`
6. **start_app**: Mounts parameter partition (yaffs2), sets memory cgroup limits (20 MB), detects sensor, loads PTZ/AF drivers if needed, configures clock frequencies, closes unused USB controllers, starts all 14 application daemons, spawns CGI server, starts getty

## Memory Management

A cgroup memory limit of 20 MB (`20971520` bytes) is applied via `/sys/fs/cgroup/mem_limit/memory.limit_in_bytes`. Core dumps are enabled globally (`ulimit -c unlimited` in `/etc/profile`) with pattern `/var/log/core-%e-%p-%t`.

## Image Sensors

Supported sensors (kernel modules loaded at boot):

| Sensor | Type | Notes |
|--------|------|-------|
| IMX678 | Sony 12MP Starvis 2 | Primary + slave |
| IMX415 | Sony 8MP Starvis | Primary + slave |
| OS08C10 | OmniVision 8MP | Primary + slave |
| OS12D40 | OmniVision 12MP | Primary |
| SC850SL | SmartSens 8MP | Primary |
| GC4653 | GalaxyCore 4MP | Primary |

Default encoding: H.265 at 3840x2160@25fps (8MP 4K), with H.264 sub/mobile streams at 640x360.

## Video Capabilities

| Stream | Codec | Resolution | Framerate | Bitrate |
|--------|-------|------------|-----------|---------|
| Main (H.265) | H.265 | 3840x2160 | 25 fps | 6144 kbps |
| Main (H.264) | H.264 | 2560x1440 | 25 fps | 6144 kbps |
| Main (H.264) | H.264 | 2304x1296 | 25 fps | 6144 kbps |
| Sub | H.264 | 640x360 | 10 fps | 256 kbps |
| Mobile | H.264 | 640x360 | 10 fps | 256 kbps |
| Extension | H.264 | 896x512 | 20 fps | 1228 kbps |

Protocols: RTSP, RTMP (port 1935), ONVIF, FLV live, Reolink proprietary (Baichuan).

## Command Injection Vectors

Format strings found in application binaries that pass user-controllable data to `system()`/`popen()`:

- `ifconfig %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `ifconfig %s 0.0.0.0`
- `ifconfig %s hw ether %s`
- `ifconfig %s %u.%u.%u.%u`
- `ifconfig %s netmask %u.%u.%u.%u`
- `ifconfig >> %s`
- `route >> %s`
- `route add default dev %s`
- `route del default dev %s`
- `route add default dev %s gw %u.%u.%u.%u`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `ip route > /mnt/tmp/iproute`
- `ping -w 5 p2p.reolink.com > %s`
- `ping -w 5 p2p.reolink.com >> %s`
- `cp /usr/sbin/ddns /mnt/tmp/ -rf`

If any of the `%s` parameters can be influenced by network input without proper sanitization, these represent command injection opportunities. The `echo nameserver` and `ifconfig` patterns are particularly concerning as they directly write to system files or configure network interfaces.

## Developer Build Paths

Multiple developer home directories found in binaries, revealing internal team structure:

| Developer | Role/Component | Path Prefix |
|-----------|---------------|-------------|
| `gt` | Main application (V29) | `/home/gt/version_v29_d15/ipc_20240626_V29/` |
| `lmy` | NS02302 SDK | `/home/lmy/svn/sdk/ns02302_linux_sdk/` |
| `liqy` | HAL library | `/home/liqy/new/V29/update/ipc_20240626_V29/` |
| `lqy` | JSON/XML libraries | `/home/lqy/new/539/V20.3_20240320_release/` |
| `luojh` | System config | `/home/luojh/trunk/ipc_20240626_V29/` |
| `xieyt` | Update/upgrade | `/home/xieyt/ipc/updatemisc/ipc_20240626_V29/` |
| `yzz` | live555 RTSP | `/home/yzz/live555_lib/rtsp/trunk/live555/` |

Key source tree structure:
- `product/exe/device/` . device daemon (camera, ISP, audio, encoder, network, PTZ)
- `product/exe/netserver/` . network server (sessions, preview, replay, cloud, push, IoT)
- `product/exe/router/` . configuration manager (all cfg_*.cpp modules)
- `media/host/nvt98530/` . Novatek media adapter (AI, ISP, encoding, OSD)
- `media/comm/` . common media (AEC, NALU parser, AI lib)
- `session_interface/` . session management (Mbed TLS connections)
- `fsadpt/` . filesystem adapter (recording, timelapse)
- `misc/libhal/` . hardware abstraction (params, net, LED PWM)
- `misc/libupdate/` . firmware update handling

## DDNS Providers

| Provider | Server |
|----------|--------|
| DynDNS | members.dyndns.org |
| 3322 | members.3322.org |
| No-IP | dynupdate.no-ip.com |
| PerfectEyes | (symlink-based selection) |
| Swann | (symlink-based selection) |

## Application File Inventory

| Binary/Library | Size | Purpose |
|----------------|------|---------|
| device | 5.6 MB | Main camera daemon |
| libcrypto.so | 2.6 MB | OpenSSL 3.3.2 crypto |
| onvif | 2.0 MB | ONVIF protocol |
| nginx | 1.4 MB | Web server + RTMP |
| netserver | 1.2 MB | Network protocol server |
| router | 1.1 MB | Configuration manager |
| cgiserver.cgi | 1.1 MB | CGI API handler |
| liblive555.so | 779 KB | RTSP library |
| libzbar.so | 735 KB | QR code scanning |
| recorder | 653 KB | Video recording |
| cloud | 535 KB | Cloud connectivity |
| libssl.so | 519 KB | OpenSSL 3.3.2 TLS |
| libnetpublic.so | 506 KB | Network utilities |
| ropclient | 493 KB | Remote operations |
| upgrade | 462 KB | Firmware upgrade |
| libmbedcrypto.so | 457 KB | Mbed TLS 2.28.9 |
| push | 324 KB | Push notifications |
| ftp | 317 KB | FTP client |
| factory | 309 KB | Factory testing |
| libbase.so | 271 KB | Base library |
| netclient | 247 KB | Network client |
| cacert.pem | 233 KB | CA certificate bundle |
| alarmcenter | 233 KB | Alarm management |
| rtsp | 205 KB | RTSP service |
| libmbedtls.so | 192 KB | Mbed TLS |
| libp2pc.so | 176 KB | P2P client |
| libp2p.so | 152 KB | P2P library |
| libfsadpt.so | 142 KB | FS adapter |
| libmbedx509.so | 130 KB | Mbed TLS X.509 |
| do_before_app | 109 KB | Pre-app initialization |
| libbchpc.so | 76 KB | Baichuan HPC |
| rpctool | 56 KB | RPC utility |
| upnpc | 35 KB | UPnP client |
| wget_lite | 27 KB | Lightweight wget |
| ip_client | 14 KB | IP utility |
| watchdog_monitor_start | 10 KB | Watchdog |

## Web Interface

The web interface is served from `/mnt/app/www/` (~4 MB). `index.html` is symlinked to `/dev/null` (disabled), with the original saved as `index.html.org`. The interface uses:
- Gzipped JavaScript bundles (BcH5Player, CGI-API, etc.)
- WASM module for video decoding
- BCS format for live stream playback files
- Standard CSS/fonts/images

## Critical Findings Summary

1. **Telnetd always running**: Root shell accessible via telnet with weak DES password
2. **FTP/TFTP via inetd**: Unauthenticated file access to SD card and `/home`
3. **Shared TLS private key**: Same key across all devices enables MITM
4. **DES password hash**: 8-char max, trivially crackable, no shadow file
5. **No firmware signing**: CRC-only verification enables malicious firmware injection
6. **All processes as root**: No privilege separation, no sandboxing
7. **Core dumps enabled**: Crash dumps may leak sensitive data
8. **Hardcoded server endpoints**: Cloud/P2P servers cannot be changed by user
9. **Serial console always active**: Physical access gives immediate root shell

## Improvements Over Older Models

- **OpenSSL 3.3.2** (vs 1.0.2f EOL in older models). Major improvement
- **nginx version hidden** (`FakeVersion`) vs exposed in older models
- **No Amcrest/Dahua code** heritage
- **Modern kernel** (5.10.168 LTS vs older 4.x)
- **AArch64** architecture (vs 32-bit ARM)
- **TLSv1.2 only** (older models allowed TLS 1.0/1.1)
- **Good cipher suite** with proper exclusions
- **Security headers** on nginx (X-Frame-Options, X-XSS-Protection, X-Content-Type-Options)
- **Mbed TLS 2.28.9** LTS (supported)
- **AI partition** with separate update capability
- **Memory cgroup limits** (partial resource isolation)
