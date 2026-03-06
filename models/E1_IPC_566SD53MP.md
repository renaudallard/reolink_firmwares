# E1

[Back to overview](../README.md)

**Hardware**: IPC_566SD53MP
**Firmware**: v3.1.0.3126_2401022459
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 6509 |
| uboot | 7715 |
| kernel | 4316 |
| rootfs | 14345 |
| rootfs | v3.1.0.3126_2401022459 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

