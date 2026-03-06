# Reolink Home Hub

[Back to overview](../README.md)

**Hardware**: BASE_WUNNT6NA5
**Firmware**: v3.3.0.456_25122248
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

