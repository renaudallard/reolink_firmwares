# P320

[Back to overview](../README.md)

**Hardware**: IPC_NT1NA45MP
**Firmware**: v3.1.0.5046_2506251383
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 12968 |
| uboot | 10541 |
| kernel | 11531 |
| rootfs | 36734 |
| app | v3.1.0.5046_2506251383 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

## Command Injection Vectors

- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `route add default dev %s`
- `route del default dev %s`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s down`
- `ifconfig %s 0.0.0.0`
- `ifconfig %s up`
- `ifconfig %s %u.%u.%u.%u`
- `ifconfig %s hw ether %s`
- `ifconfig %s netmask %u.%u.%u.%u`

## Developer Build Paths

- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/audio/src/`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/netserver/../../modules/netserv`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../common/mod_container.`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/enc/src/en`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/isp/src/is`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/network/sr`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/sys/src/sy`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/netserver/../common/mod_contain`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

