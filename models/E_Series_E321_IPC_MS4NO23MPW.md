# E Series E321

[Back to overview](../README.md)

**Hardware**: IPC_MS4NO23MPW
**Firmware**: v3.2.0.4858_2508273415
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| uboot | 12734 |
| kernel | 13716 |
| rootfs | v3.2.0.4858_2508273415 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | Yes |
| BusyBox | 1.34.1 (dangerous applets: tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

