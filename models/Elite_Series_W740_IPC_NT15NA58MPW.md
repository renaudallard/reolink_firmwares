# Elite Series W740

[Back to overview](../README.md)

**Hardware**: IPC_NT15NA58MPW
**Firmware**: v3.2.0.4558_2503142026
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 10074 |
| fdt | 11352 |
| atf | 9982 |
| uboot | 11543 |
| kernel | 11626 |
| ai | 250109003805 |
| rootfs | 33900 |
| app | v3.2.0.4558_2503142026 |

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

## Developer Build Paths

- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/netserver/../../session_interface/src/sess`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/service/src/service.c`
- `/home/qinzj/working/repacket/ipc_20240626_V29/cbb/lib/NT98539/advance/libnetpublic/include/net_mempo`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/netserver/../common/mod_container.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/snap/src/snap.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/audio/src/a_policy.cp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/main_device.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/audio/src/a_policy.h`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

