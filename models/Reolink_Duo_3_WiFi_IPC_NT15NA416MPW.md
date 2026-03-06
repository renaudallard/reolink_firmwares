# Reolink Duo 3 WiFi

[Back to overview](../README.md)

**Hardware**: IPC_NT15NA416MPW
**Firmware**: v3.0.0.4867_2505072126
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 9943 |
| fdt | 10115 |
| atf | 9982 |
| uboot | 10694 |
| kernel | 11626 |
| rootfs | 12580 |
| ai | 250507006500 |
| app | v3.0.0.4867_2505072126 |

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

## Developer Build Paths

- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/../common/mod_conta`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/snap/src`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/audio/sr`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/isp/src/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/../../modules/netse`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/service/`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/main_device.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../common/mod_containe`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/sys/src/`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

