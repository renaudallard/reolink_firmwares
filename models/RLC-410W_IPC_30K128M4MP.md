# RLC-410W

[Back to overview](../README.md)

**Hardware**: IPC_30K128M4MP
**Firmware**: V3.1.0.739_22042505
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| BOOT | 2059 |
| KERNEL | 2403 |
| rootfs | 2622 |
| app | v3.1.0.739_22042505 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.20.2 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=REOLINK, OU=REOLINK, CN=REOLINK, emailAddress=service@reo-link.com |
| TLS cert expiry | Aug 23 07:40:49 2041 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

- `mi system version:%s`
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

- `/home/linj/v14/product/exe/netserver/../common/mod_container.cpp`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_replay_fs.cpp`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_md.cpp`
- `/home/linj/v14/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/linj/v14/product/exe/device/../common/mod_container.cpp`
- `/home/linj/v14/product/exe/device/../../modules/network/src/network.cpp`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_system.cpp`
- `/home/linj/v14/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/linj/v14/product/exe/device/../../modules/audio/src/a_policy.h`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_user.cpp`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so

