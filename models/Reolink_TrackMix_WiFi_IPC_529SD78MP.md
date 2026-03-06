# Reolink TrackMix WiFi

[Back to overview](../README.md)

**Hardware**: IPC_529SD78MP
**Firmware**: v3.0.0.5428_2509171974
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 3123 |
| fdt | 13751 |
| uboot | 13360 |
| kernel | 11185 |
| rootfs | 14208 |
| app | v3.0.0.5428_2509171974 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
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

- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/isp/src`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/service`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/netserver/main_netserver.cpp`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/network`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../common/mod_contain`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/main_device.cpp`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/snap/sr`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/audio/s`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/enc/src`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/netserver/../common/mod_cont`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

