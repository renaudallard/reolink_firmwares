# Reolink Lumus

[Back to overview](../README.md)

**Hardware**: IPC_NT1NO24MP
**Firmware**: v3.1.0.5047_2506271410
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 10330 |
| fdt | 13285 |
| uboot | 13286 |
| kernel | 6531 |
| rootfs | 20033 |
| rootfs | v3.1.0.5047_2506271410 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

