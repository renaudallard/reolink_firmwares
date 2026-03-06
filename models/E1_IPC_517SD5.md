# E1

[Back to overview](../README.md)

**Hardware**: IPC_517SD5
**Firmware**: v3.0.0.2356
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

## Security Analysis

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
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

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/snap/snap.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/network/network.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/enc.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/sys/sys.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/main.cpp`

## DDNS Providers

- members.3322.org
- members.dyndns.org
- dyndns

## P2P Libraries

- libp2p.so

