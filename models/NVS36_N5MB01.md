# NVS36

[Back to overview](../README.md)

**Hardware**: N5MB01
**Firmware**: v3.6.3.437_25110428
**Architecture**: AArch64
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

