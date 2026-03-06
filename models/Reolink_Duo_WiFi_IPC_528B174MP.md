# Reolink Duo WiFi

[Back to overview](../README.md)

**Hardware**: IPC_528B174MP
**Firmware**: v3.0.0.1388_24021901
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 2738 |
| fdt | 2388 |
| uboot | 2868 |
| kernel | 2739 |
| rootfs | 4523 |
| app | v3.0.0.1388_24021901 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 4096 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | Jun  1 12:18:57 2042 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

## Command Injection Vectors

- `c_system_local::get_info MCU VERSION:%s`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
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

- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/main_device.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/network/src/networ`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/audio/src/bc_audio`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/service/src/servic`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/netserver/main_netserver.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../common/mod_container.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/netserver/../../modules/netserver/inclu`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/audio/src/a_policy`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so

