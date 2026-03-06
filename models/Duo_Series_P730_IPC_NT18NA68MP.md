# Duo Series P730

[Back to overview](../README.md)

**Hardware**: IPC_NT18NA68MP
**Firmware**: v3.2.0.5467_2510141198
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 12681 |
| fdt | 13767 |
| atf | 11694 |
| uboot | 13235 |
| kernel | 12058 |
| ai | 250722006500 |
| rootfs | 14511 |
| app | v3.2.0.5467_2510141198 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: httpd, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

## Command Injection Vectors

- `exec %s fail(%d)`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
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
- `%s iot reroute failed`
- `%s iot reroute success`

## Developer Build Paths

- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/net`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/netserver/../../session_`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/main_device.cpp`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/ser`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/netserver/../common/mod_`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/cbb/lib/NT98538A/advance/libnetpubli`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/sys`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../common/mod_con`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/aud`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/sna`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

