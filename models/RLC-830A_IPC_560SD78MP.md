# RLC-830A

[Back to overview](../README.md)

**Hardware**: IPC_560SD78MP
**Firmware**: v3.1.0.2515_23082406
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 6591 |
| fdt | 5217 |
| uboot | 6591 |
| kernel | 6590 |
| rootfs | 6224 |
| app | v3.1.0.2515_23082406 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
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

- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/snap/src/snap.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/service/src/service`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/includ`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/audio/src/a_policy.`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/network/src/network`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/audio/src/bc_audio.`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../common/mod_container.cpp`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

