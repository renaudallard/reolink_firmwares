# E Series E340

[Back to overview](../README.md)

**Hardware**: IPC_566SD664M5MP
**Firmware**: v3.1.0.4417_2412122179
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 10893 |
| uboot | 10894 |
| kernel | 6586 |
| rootfs | 17674 |
| app | v3.1.0.4417_2412122179 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

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

- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/main_device.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/netserver/main_netserver.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/netserver/../../modules/netserver/src/`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/service/src/servi`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/audio/src/a_polic`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/audio/src/bc_audi`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/network/src/netwo`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/enc/src/enc.cpp`

## DDNS Providers

- members.dyndns.org
- dyndns
- members.3322.org

