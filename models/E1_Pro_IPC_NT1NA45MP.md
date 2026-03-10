# E1 Pro

[Back to overview](../README.md)

**Hardware**: IPC_NT1NA45MP
**Firmware**: v3.1.0.4417_2412122130
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs
**SoC**: Novatek NA51089

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 3.3.2 |
| Mbed TLS | Mbed TLS 2.28.9 |
| BusyBox | 1.31.1 (dangerous applets: tftp, wget) |
| nginx | 1.14.2 |
| Cloud support | Enabled (`devices-apis.reolink.com`) |
| Super password | Enabled |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |
| TLS certificate | 2048-bit RSA, self-signed, expires 2043 |

## Web Interface

**The `www` directory is empty in this firmware.** Accessing the camera via HTTP returns **403 Forbidden** because nginx has no index files to serve. The web browser UI has been stripped from this hardware revision.

The HTTP API still works via `/api.cgi` (FastCGI to `cgiserver.cgi` on port 9527). This camera is designed to be used exclusively through the Reolink app or client software.

The `device` binary references `/mnt/app/www/index.html.org` but the file does not exist on this hardware version. On models that have the web UI (e.g. Duo 3 PoE), this file is copied to `/mnt/tmp/index.html` and patched with the media port at startup.

## Video Encoding

H.264 and H.265 hardware encoding and decoding supported via Novatek `kdrv_h26x.ko` and `kflow_videoenc.ko` kernel modules (`MP_H264Enc`, `MP_H265Enc`).

## Command Injection Vectors

- `ifconfig %s`
- `ifconfig >> %s`
- `route >> %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route add default dev %s`
- `route del default dev %s`
- `ifconfig %s 0.0.0.0`
- `ifconfig %s hw ether %s`
- `ifconfig %s %u.%u.%u.%u`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s netmask %u.%u.%u.%u`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `ifconfig %s netmask %s`

## Developer Build Paths

- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/main_device.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/network/src/network.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/snap/src/snap.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/audio/src/bc_audio.cpp`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns
- 3322
- no-ip
