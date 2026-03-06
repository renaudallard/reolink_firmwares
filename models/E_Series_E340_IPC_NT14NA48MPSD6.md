# E Series E340

[Back to overview](../README.md)

**Hardware**: IPC_NT14NA48MPSD6
**Firmware**: v3.2.0.4741_2503281993
**Architecture**: ARM
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: tftpd, httpd, nc, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |

