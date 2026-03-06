# V800W

[Back to overview](../README.md)

**Hardware**: IPC_NT2NO28MP
**Firmware**: v3.1.0.3114_2407022284
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 7218 |
| fdt | 7218 |
| uboot | 7633 |
| kernel | 7670 |
| rootfs | 15437 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |

