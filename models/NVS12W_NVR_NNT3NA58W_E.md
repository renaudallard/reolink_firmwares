# NVS12W

[Back to overview](../README.md)

**Hardware**: NVR_NNT3NA58W_E
**Firmware**: v3.5.1.368_24120611
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

