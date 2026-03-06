# RLC-1240A

[Back to overview](../README.md)

**Hardware**: IPC_NT18NA612MPD11
**Firmware**: v3.2.0.5758_2512031764
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 14868 |
| fdt | 12824 |
| atf | 11694 |
| uboot | 14883 |
| kernel | 14849 |
| ai | 250722006500 |
| rootfs | 15503 |
| app | v3.2.0.5758_2512031764 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: httpd, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

## Command Injection Vectors

- `exec %s fail(%d)`
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
- `%s iot reroute failed`
- `%s iot reroute success`

## Developer Build Paths

- `/home/luojh/trunk/version`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

## P2P Libraries

- libp2p.so
- libp2pc.so

