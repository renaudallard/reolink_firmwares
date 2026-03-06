# CX820

[Back to overview](../README.md)

**Hardware**: IPC_NT16NA48MP
**Firmware**: v3.2.0.5375_2509162386
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 12087 |
| fdt | 11655 |
| atf | 10052 |
| uboot | 11522 |
| kernel | 11625 |
| ai | 250318006500 |
| rootfs | 28358 |
| app | v3.2.0.5375_2509162386 |

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

- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/audio/src/a_policy.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../common/mod_container.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/netserver/../common/mod_container.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/network`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/service/src/service.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/audio/src/a_policy.h`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/snap/src/snap.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/netserver/../../session_interface/src/session_`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

