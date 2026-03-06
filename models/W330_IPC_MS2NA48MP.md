# W330

[Back to overview](../README.md)

**Hardware**: IPC_MS2NA48MP
**Firmware**: v3.0.0.4348_2411261894
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| cis | 6086 |
| uboot | 10535 |
| kernel | 10423 |
| rootfs | 11125 |
| app | v3.0.0.4348_2411261894 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| nginx | nginx/1.22.1 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
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

- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/s`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/../common/mod_`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/m`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/main_device.cp`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../../modul`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/../../modules/`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so
- libp2pc.so

