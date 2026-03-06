# E1 Outdoor Pro

[Back to overview](../README.md)

**Hardware**: IPC_560SD88MPW
**Firmware**: v3.1.0.5714_2511271366
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |

