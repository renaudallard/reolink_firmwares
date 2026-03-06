# RLC-511WA

[Back to overview](../README.md)

**Hardware**: IPC_523128M5MP
**Firmware**: v3.1.0.4381_2411301864
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 3800 |
| uboot | 2357 |
| kernel | 4761 |
| rootfs | 21371 |
| app | v3.1.0.4381_2411301864 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
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

- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.c`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../common/mod_container.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/audio/src/a_p`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/netserver/../common/mod_container.`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc.c`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/sys/src/sys.c`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/audio/src/bc_`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

