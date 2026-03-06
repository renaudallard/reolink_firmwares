# Floodlight Series F751W

[Back to overview](../README.md)

**Hardware**: IPC_NT15NA68MPW
**Firmware**: v3.2.0.5607_2511041997
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 12240 |
| fdt | 12245 |
| atf | 9982 |
| uboot | 14828 |
| kernel | 14827 |
| ai | 251104006500 |
| rootfs | 14616 |
| app | v3.2.0.5607_2511041997 |

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
- `Failed to execute child process "%s" (%s)`
- `Unknown error executing child process "%s"`
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

- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/netserver/../../session_interf`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src/s`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/netserver/../common/mod_contai`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src/e`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/cbb/lib/NT98539/advance/libnetpublic/inclu`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/network`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../common/mod_container`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/isp/src/i`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/service/s`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/snap/src/`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

## P2P Libraries

- libp2p.so
- libp2pc.so

