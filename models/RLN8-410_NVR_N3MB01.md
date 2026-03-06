# RLN8-410 (NVR)

[Back to overview](../README.md)

**Hardware**: N3MB01
**Firmware**: v3.5.1.368_25010352
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 1951 |
| fdt | 2617 |
| uboot | 2617 |
| kernel | 2618 |
| logo | 11523 |
| fs | 10437 |
| app | v3.5.1.368_25010352 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `ifconfig %s %u.%u.%u.%d`
- `ifconfig %s 192.168.10.%d`
- `route add default dev %s`
- `ifconfig %s up`
- `ifconfig %s down`
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

- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/sys/s`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/../../fsadpt/src`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/../../modules/co`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/main_netserver.c`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/push/`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/servi`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/netwo`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/main_device.cpp`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../common/mod_conta`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/commo`

## DDNS Providers

- dyndns
- members.dyndns.org
- members.3322.org

## P2P Libraries

- libp2p.so

