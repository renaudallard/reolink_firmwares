# NVC-D12M

[Back to overview](../README.md)

**Hardware**: IPC_NT5NO212MP
**Firmware**: v3.1.0.3702_2501209008
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 2703 |
| fdt | 2702 |
| uboot | 2722 |
| kernel | 5569 |
| rootfs | 18115 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
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

- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/main_device.`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/netserver/main_nets`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/../../module`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/../common/mo`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/netserver/../../mod`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/netserver/../common`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

