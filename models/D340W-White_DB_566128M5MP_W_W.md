# D340W-White

[Back to overview](../README.md)

**Hardware**: DB_566128M5MP_W_W
**Firmware**: v3.0.0.4662_2508131301
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Core dumps | **Enabled** (`ulimit -c unlimited`) |

