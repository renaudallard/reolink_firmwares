# E Series E530X

[Back to overview](../README.md)

**Hardware**: IPC_MS1NA44MP
**Firmware**: v3.0.0.3281_2403061749
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| cis | 5892 |
| uboot | 8026 |
| kernel | 8030 |
| rootfs | 8343 |
| app | v3.0.0.3281_2403061749 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| nginx | nginx/1.22.0 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

- `Failed to execute child process "%s" (%s)`
- `Unknown error executing child process "%s"`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route add default dev %s`
- `route del default dev %s`
- `ifconfig %s 0.0.0.0`
- `ifconfig %s hw ether %s`
- `ifconfig %s %u.%u.%u.%u`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s netmask %u.%u.%u.%u`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `ifconfig %s netmask %s`

## Developer Build Paths

- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/aud`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/netserver/../../modules/`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/main_device.cpp`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../common/mod_con`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/enc`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/isp`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/sys`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/net`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/sna`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/netserver/../common/mod_`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

## P2P Libraries

- libp2p.so
- libp2pc.so

