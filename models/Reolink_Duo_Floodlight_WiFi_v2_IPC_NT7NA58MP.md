# Reolink Duo Floodlight WiFi v2

[Back to overview](../README.md)

**Hardware**: IPC_NT7NA58MP
**Firmware**: v3.0.0.4410_2506058704
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 7906 |
| fdt | 5976 |
| uboot | 9701 |
| kernel | 8112 |
| rootfs | 11281 |
| app | v3.0.0.4410_2506058704 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

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
- `ifconfig %s netmask %s`

## Developer Build Paths

- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/i`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/netserver/../../module`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/e`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/s`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/main_device.cpp`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../common/mod_c`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/netserver/../common/mo`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/n`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/netserver/main_netserv`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/a`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

