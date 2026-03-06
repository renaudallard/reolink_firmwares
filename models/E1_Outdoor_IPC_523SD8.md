# E1 Outdoor

[Back to overview](../README.md)

**Hardware**: IPC_523SD8
**Firmware**: v3.1.0.3514_2406039634
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 1804 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 4754 |
| rootfs | 17329 |
| app | v3.1.0.3514_2406039634 |

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
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

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

- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/netserver/../../modules/netserve`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/network/src`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/snap/src/sn`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/netserver/../common/mod_containe`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/sys/src/sys`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/service/src`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/audio/src/b`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

