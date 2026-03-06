# RLC-824A

[Back to overview](../README.md)

**Hardware**: IPC_523D88MP
**Firmware**: v3.1.0.920_2402207921
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

## Firmware Partitions

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1820 |
| uboot | 2357 |
| kernel | 1819 |
| rootfs | 3057 |
| app | v3.1.0.920_2402207921 |

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 4096 bit, C=CN, ST=GD, L=SZ, O=test, OU=test, CN=test, emailAddress=test@test.com |
| TLS cert expiry | Dec  4 08:46:25 2041 GMT |
| Cloud support | Disabled |
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

- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/src/nets_replay_`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../common/mod_container.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/audio/src/a_policy.h`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/audio/src/bc_audio.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/main_netserver.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/src/nets_online_`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/include/nets_ser`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

