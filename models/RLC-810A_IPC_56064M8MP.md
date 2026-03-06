# RLC-810A

[Back to overview](../README.md)

**Hardware**: IPC_56064M8MP
**Firmware**: v3.1.0.5764_2512171966
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

