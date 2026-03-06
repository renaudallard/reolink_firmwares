# RLC-842A

[Back to overview](../README.md)

**Hardware**: IPC_523D98MP
**Firmware**: v3.1.0.1643_2402219328
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 1751 |
| rootfs | 3623 |
| app | v3.1.0.1643_2402219328 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 4096 bit, C=CN, ST=GD, L=SZ, O=test, OU=test, CN=test, emailAddress=test@test.com |
| TLS cert expiry | Dec  4 08:46:25 2041 GMT |
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

- `/home/wxh/wxh2022/12/23/523`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

