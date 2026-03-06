# W320C

[Back to overview](../README.md)

**Hardware**: IPC_MS1NO25MP
**Firmware**: v3.0.0.3078_2405089137
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| uboot | 7535 |
| kernel | 7065 |
| rootfs | 7533 |
| app | v3.0.0.3078_2405089137 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |

