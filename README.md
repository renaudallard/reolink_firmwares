# Reolink Firmware Security & Connectivity Analysis

Automated security analysis of **89 firmware images** across the entire Reolink product line,
covering cameras (IPC), NVRs, home hubs, doorbells, and fisheye devices.

## Summary

- **89 hardware versions** analyzed from latest available firmware
- **9 hardware versions** could not be extracted (cramfs/old formats)
- **4 unique root password hashes** found across all devices
- **Zero devices** use `/etc/shadow` properly (only 7 have shadow files)
- **Every device** runs everything as root with no privilege separation
- **No firmware** uses cryptographic signature verification (CRC32 + MD5 only)

## All Models Analyzed

| Model | HW Version | Firmware | Arch | BusyBox | OpenSSL | nginx | Root Hash |
|-------|------------|----------|------|---------|---------|-------|-----------|
| B1200 | IPC_52316M12MP | v3.1.0.5036_2506279222 | ARM | 1.24.1 | - | - | `5p6FGL0H1INXw` |
| B400 | IPC_5128M | v3.0.0.183_21012800 | MIPS | 1.24.1 | - | - | *(empty)* |
| B800 | IPC_5158MP8M | v3.0.0.183_21012800 | MIPS | 1.24.1 | - | - | *(empty)* |
| CX820 | IPC_NT16NA48MP | v3.2.0.5375_2509162386 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| ColorX Series P330X | IPC_NT2NA48MPB28 | v3.1.0.5129_2510222155 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| ColorX Series W320X | IPC_NT1NA44MP | v3.1.0.4366_2412021480 | ARM | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| D340P | DB_566128M5MP_P | v3.0.0.4662_2508131283 | ARM | 1.31.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| D340P-White | DB_566128M5MP_P_W | v3.0.0.4662_2508131302 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| D340W | DB_566128M5MP_W | v3.0.0.4662_2508131282 | ARM | 1.31.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| D340W-White | DB_566128M5MP_W_W | v3.0.0.4662_2508131301 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| D500 | IPC_5158M5M | v3.0.0.183_21012815 | MIPS | 1.24.1 | - | - | *(empty)* |
| D500 | IPC_515B8M5M_V2 | v3.1.0.2379_2412249791 | ARM | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| D800 | IPC_5158M8M_V2 | v3.1.0.4057_2409132132 | ARM | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| Duo Series P730 | IPC_529B17B8MP | v3.0.0.5586_2510291786 | ARM | 1.24.1 | - | - | `5p6FGL0H1INXw` |
| Duo Series P730 | IPC_NT18NA68MP | v3.2.0.5467_2510141198 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Duo Series P757 | IPC_NT17NA616MP | v3.2.0.5770_2512231311 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Duo Series W750 | IPC_NT17NA616MPW | v3.2.0.5770_2512231309 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| E Series E321 | IPC_MS4NO23MPW | v3.2.0.4858_2508273415 | ARM | 1.34.1 | - | - | `aRDwnwAt1ygAM` |
| E Series E330 | IPC_566SD54MP | v3.1.0.5112_2507081476 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E Series E331 | IPC_NT1NA45MPSD18V2 | v3.1.0.5714_2511271356 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E Series E340 | IPC_566SD664M5MP | v3.1.0.4417_2412122179 | ARM | 1.31.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| E Series E340 | IPC_NT14NA48MPSD6 | v3.2.0.4741_2503281993 | ARM | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| E Series E530X | IPC_MS1NA44MP | v3.0.0.3281_2403061749 | ARM | 1.31.1 | - | 1.22.0 | `x` |
| E Series E550 | IPC_NT2NA48MPSD8V3 | v3.1.0.5502_2510231295 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E Series E560 | IPC_560SD88MP | v3.1.0.4020_2409116797 | ARM | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| E1 | IPC_517SD5 | v3.0.0.2356 | MIPS | 1.24.1 | 1.0.2f | - | *(empty)* |
| E1 | IPC_566SD53MP | v3.1.0.3126_2401022459 | ARM | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| E1 | IPC_MS4NO24MPW | v3.2.0.4858_2508273531 | ARM | 1.34.1 | - | - | `aRDwnwAt1ygAM` |
| E1 Outdoor | IPC_523SD8 | v3.1.0.3514_2406039634 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| E1 Outdoor | IPC_566SD85MP | v3.1.0.5714_2511271358 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E1 Outdoor | IPC_NT1NA45MPSD8W | v3.1.0.5714_2511271352 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E1 Outdoor Pro | IPC_560SD88MPW | v3.1.0.5714_2511271366 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| E1 Pro | IPC_513SD5 | v3.0.0.2356_23062004 | MIPS | 1.24.1 | 1.0.2f | - | *(empty)* |
| E1 Pro | IPC_515SD5 | v3.0.0.2356_23062013 | MIPS | 1.24.1 | 1.0.2f | - | *(empty)* |
| E1 Zoom | IPC_515BSD6 | v3.0.0.2356_23062008 | MIPS | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| E1 Zoom | IPC_515SD6 | v3.0.0.2356 | MIPS | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| E1 Zoom | IPC_566SD65MP | v3.1.0.3382_2404177933 | ARM | 1.31.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| Elite Series W740 | IPC_NT15NA58MPW | v3.2.0.4558_2503142026 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Fisheye Series P520 | FE_529128M6MP_P | v3.0.0.5336_2509021916 | ARM | 1.24.1 | - | - | `aRDwnwAt1ygAM` |
| Fisheye Series W520 | FE_529128M6MP_W | v3.0.0.5336_2509021914 | ARM | 1.24.1 | - | - | `aRDwnwAt1ygAM` |
| Floodlight Series F751W | IPC_NT15NA68MPW | v3.2.0.5607_2511041997 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Lumus Series E450 | IPC_FH1NA48MPC7 | v3.2.0.4243_2507079897 | ? | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| NVC-D12M | IPC_NT5NO212MP | v3.1.0.3702_2501209008 | ARM | 1.24.1 | - | - | `XF4sg5T82tV4k` |
| NVS12W | NVR_NNT3NA58W_E | v3.5.1.368_24120611 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| NVS12W | NVR_NNT3NA58W_U | v3.5.1.368_24120610 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| NVS16 | N6MB01 | v3.6.3.422_25082953 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| NVS36 | N5MB01 | v3.6.3.437_25110428 | AArch64 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| NVS4 | NVR_NNT3NA54P | v3.6.3.437_25092006 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| NVS8 | N7MB01 | v3.6.3.422_25082949 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| P320 | IPC_NT1NA45MP | v3.1.0.5046_2506251383 | ARM | 1.31.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| P330M | IPC_560B218MP_P | v3.0.0.1783_23121201 | ARM | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| P430 | IPC_560B158MP | v3.1.0.4695_2504301441 | ARM | 1.31.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| RLC-1212A | IPC_523B18128M12MP | v3.1.0.5036_2509040629 | ARM | 1.24.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| RLC-1220A | IPC_523128M12MP | v3.1.0.861_24022105 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-1240A | IPC_NT18NA612MPD11 | v3.2.0.5758_2512031764 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| RLC-410 | IPC_51316M | v3.0.0.2356_23062000 | MIPS | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| RLC-410-5MP | IPC_51516M5M | v3.0.0.2356_23062000 | MIPS | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| RLC-410W | IPC_30K128M4MP | V3.1.0.739_22042505 | ARM | 1.20.2 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-410W-5MP | IPC_515B16M5M | v3.0.0.2356_23062002 | MIPS | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| RLC-511WA | IPC_523128M5MP | v3.1.0.4381_2411301864 | ARM | 1.24.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-542WA | IPC_523D95MP | v3.1.0.4381_2411301871 | ARM | 1.24.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-810A | IPC_523128M8MP | v3.1.0.956_24022103 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-810A | IPC_56064M8MP | v3.1.0.5764_2512171966 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| RLC-812A | IPC_523B188MP | v3.1.0.920_2402207844 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-823A 16X | IPC_523SD10 | v3.1.0.2898_23110119_v1.0.0.93 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-823S2 | IPC_NT2NA48MPSD12 | v3.1.0.5714_25112712_v1.0.0.159 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| RLC-824A | IPC_523D88MP | v3.1.0.920_2402207921 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-830A | IPC_560SD78MP | v3.1.0.2515_23082406 | ARM | 1.31.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLC-833A | IPC_NT2NA48MP | v3.1.0.4972_2510232468 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| RLC-842A | IPC_523D98MP | v3.1.0.1643_2402219328 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| RLN8-410 (NVR) | N3MB01 | v3.5.1.368_25010352 | ARM | 1.24.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| RP-PCT16MD | IPC_NT17NA616MPB | v3.2.0.5770_2512231313 | AArch64 | 1.36.0 | - | - | `5p6FGL0H1INXw` |
| RP-PCT8M | IPC_NT2NA48MPB | v3.1.0.5994_2601301346 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| RP-PCT8MD | IPC_NT17NA68MPB | v3.2.0.5770_2512231312 | AArch64 | 1.36.0 | - | - | `5p6FGL0H1INXw` |
| Reolink Duo 3 PoE | IPC_NT15NA416MP | v3.0.0.4867_2505072124 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Reolink Duo 3 WiFi | IPC_NT15NA416MPW | v3.0.0.4867_2505072126 | AArch64 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| Reolink Duo Floodlight WiFi v2 | IPC_NT7NA58MP | v3.0.0.4410_2506058704 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| Reolink Duo WiFi | IPC_528B174MP | v3.0.0.1388_24021901 | ARM | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| Reolink Home Hub | BASE_WENNT6NA5 | v3.3.0.456_25122258 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| Reolink Home Hub | BASE_WUNNT6NA5 | v3.3.0.456_25122248 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| Reolink Home Hub Pro | BASE_WENNT3NA5 | v3.3.0.369_25090459 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| Reolink Home Hub Pro | BASE_WUNNT3NA5 | v3.3.0.369_25090486 | ARM | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| Reolink Lumus | IPC_NT1NO24MP | v3.1.0.5047_2506271410 | ARM | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| Reolink TrackMix WiFi | IPC_529SD78MP | v3.0.0.5428_2509171974 | ARM | 1.24.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| V800W | IPC_NT2NO28MP | v3.1.0.3114_2407022284 | ARM | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| W320 | IPC_MS1NA45MP | v3.0.0.4348_2411261179 | ARM | 1.31.1 | - | 1.22.1 | `x` |
| W320C | IPC_MS1NO25MP | v3.0.0.3078_2405089137 | ARM | 1.31.1 | - | - | `x` |
| W330 | IPC_MS2NA48MP | v3.0.0.4348_2411261894 | ARM | 1.31.1 | - | 1.22.1 | `x` |
| W330C | IPC_MS2NO28MP | v3.0.0.5031_2506270556 | ARM | 1.31.1 | - | - | `x` |

## Critical Vulnerabilities (All Models)

These issues are present in **every firmware analyzed**:

| Vulnerability | Severity | Details |
|---------------|----------|---------|
| Hardcoded root password | Critical | DES hash in `/etc/passwd`, no `/etc/shadow`. Only 4 unique hashes across all 89 models |
| Shared TLS private key | Critical | Same certificate baked into firmware for entire product lines. 4 unique certs across 53 models |
| No firmware signature verification | Critical | Only CRC32 + MD5 integrity checks. Any modified firmware can be flashed |
| Everything runs as root | Critical | nginx, RTSP server, device manager. all run as UID 0, no privilege separation |
| Command injection vectors | Critical | `system()` calls with user input in smbpasswd, resolv.conf, ddns-config, ifconfig |
| Super password bypass | High | `support_supper_pwd="1"` in 58/89 models. factory backdoor password |
| Amcrest/Dahua code sharing | Medium | `AmcrestToken` found in 38/89 models. Shared OEM codebase |
| Core dumps enabled | Medium | `ulimit -c unlimited` in 4 models. Memory contents written to disk |
| Developer build paths | Low | Compiler paths like `/home/username/project/` leaked in binaries |

## Root Password Hashes

Only 4 unique DES hashes protect root access across 78 models (11 additional models have **no password at all**):

| Hash | Models Using It | Count |
|------|----------------|-------|
| `aRDwnwAt1ygAM` | CX820, D340P, D340P-White, D340W, D340W-White, ... (+25 more) | 30 |
| `XF4sg5T82tV4k` | ColorX Series W320X, D500, D800, E Series E340, E Series E560, ... (+18 more) | 23 |
| `5p6FGL0H1INXw` | B1200, ColorX Series P330X, Duo Series P730, E Series E330, E Series E331, ... (+15 more) | 20 |
| `x` | E Series E530X, W320, W320C, W330, W330C | 5 |
| *(empty)* | B400, B800, D500, E1, E1 Pro (x2), E1 Zoom (x2), RLC-410, RLC-410-5MP, RLC-410W-5MP | 11 |

All hashes are traditional DES crypt (13 characters), trivially crackable.
The hash `x` indicates the password field points to shadow, but the shadow files found are mostly empty or have the same weak hashes.
An **empty hash field** means passwordless root login. these 11 MIPS models allow root access without any password.

## OpenSSL Versions

| Version | Status | Models |
|---------|--------|--------|
| OpenSSL 1.0.2f | **EOL since 2020. CRITICAL** | 23 |
| not found | Uses Mbed TLS or statically linked | 66 |

## nginx Versions

| Version | Status | Models |
|---------|--------|--------|
| nginx/1.14.2 | **2018, multiple CVEs** | 27 |
| nginx/1.22.0 | 2022, older but fewer CVEs | 1 |
| nginx/1.22.1 | 2022, older but fewer CVEs | 2 |
| not found | Uses app-integrated web server | 59 |

## BusyBox Versions & Dangerous Applets

| Version | Models | Notable Applets Compiled In |
|---------|--------|-----------------------------|
| 1.20.2 | 1 | tftp, wget |
| 1.24.1 | 30 | ftpd, httpd, nc, tftp, wget |
| 1.31.1 | 44 | tftp, wget |
| 1.34.1 | 2 | tftp |
| 1.36.0 | 12 | httpd, nc, tftp, tftpd, wget |

All versions include `tftp` and `wget`. Older versions (1.24.1 and below) additionally include
`telnetd`, `ftpd`, `tftpd`, and `httpd` which enable network service persistence after exploitation.

## TLS Certificate Analysis

Certificates are baked into firmware and shared across entire product lines.
The private key is extractable from any firmware image, making TLS effectively useless.

| Key Size | Models |
|----------|--------|
| 2048 bit | 47 |
| 4096 bit | 6 |
| N/A | 36 |

Only **4 unique TLS certificates** across 53 models that have certificates.
This means many different camera models share the exact same TLS private key.

## Mbed TLS Versions

| Version | Models |
|---------|--------|
| Mbed TLS 2.28.9 | 28 |
| mbed TLS 2.24.0 | 17 |
| not found | 44 |

## Cloud & Connectivity

- **Cloud enabled**: 35 models
- **Cloud disabled**: 24 models
- **Unknown/not in dvr.xml**: 30 models

All models with cloud support connect to `devices-apis.reolink.com:443` for firmware updates
and `p2p.reolink.com` for peer-to-peer connectivity. DDNS services include 3322.org, DynDNS, and NO-IP.

## Failed Extractions

These hardware versions could not be analyzed due to filesystem format limitations:

| Model | HW Version | Filesystem | Reason |
|-------|------------|------------|--------|
| RLN8-410 (NVR) | H3MB02 | cramfs, cramfs | cramfs not supported |
| RLN8-410 (NVR) | H3MB16 | cramfs, cramfs | cramfs not supported |
| RLN16-410 (NVR) | H3MB18 | cramfs, cramfs | cramfs not supported |
| RLC-422 | IPC-51516M | squashfs | extraction failed |
| RLC-410 | IPC-515B16M5M | squashfs | extraction failed |
| D500 | IPC_515B8M5M | squashfs | extraction failed |
| RLN8-410 (NVR) | N2MB02 or H3MB18 | cramfs, cramfs | cramfs not supported |
| RLN8-410 (NVR) | NVR_NNT3NA78P | ubifs, squashfs | extraction failed |
| NVS16-S | NVR_NNT4NA716P | ubifs, squashfs | extraction failed |

---

## Per-Model Security Details

Detailed security findings for each analyzed hardware version.

### B1200

**Hardware**: IPC_52316M12MP
**Firmware**: v3.1.0.5036_2506279222
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 2703 |
| fdt | 2702 |
| uboot | 2722 |
| kernel | 5569 |
| rootfs | 23712 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2025.06.23_523B18/KIT/ipc_20210624_V14/product/exe/device/main_de`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/KIT/ipc_20210624_V14/product/exe/device/../../m`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/KIT/ipc_20210624_V14/product/exe/netserver/../.`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/KIT/ipc_20210624_V14/product/exe/netserver/../c`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/KIT/ipc_20210624_V14/product/exe/netserver/main`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### B400

**Hardware**: IPC_5128M
**Firmware**: v3.0.0.183_21012800
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: nc, tftp) |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 4 more

**Developer build paths**:

- `/home/lgb/ipc_v1_ver/20210128/ipc_20200324_V1/product/netserver/src/nets_recoder.cpp`
- `/home/lgb/ipc_v1_ver/20210128/ipc_20200324_V1/product/device/src/isp/isp.cpp`
- `/home/lgb/ipc_v1_ver/20210128/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/lgb/ipc_v1_ver/20210128/ipc_20200324_V1/product/netserver/src/nets_md.cpp`
- `/home/lgb/ipc_v1_ver/20210128/ipc_20200324_V1/product/device/src/audio/bc_audio.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### B800

**Hardware**: IPC_5158MP8M
**Firmware**: v3.0.0.183_21012800
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, tftp) |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 4 more

**Developer build paths**:

- `/home/lgb/ipc_v1_ver/20210128_2/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/lgb/ipc_v1_ver/20210128_2/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/lgb/ipc_v1_ver/20210128_2/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/lgb/ipc_v1_ver/20210128_2/ipc_20200324_V1/product/device/src/enc/enc.cpp`
- `/home/lgb/ipc_v1_ver/20210128_2/ipc_20200324_V1/product/netserver/src/nets_md.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### CX820

**Hardware**: IPC_NT16NA48MP
**Firmware**: v3.2.0.5375_2509162386
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 12087 |
| fdt | 11655 |
| atf | 10052 |
| uboot | 11522 |
| kernel | 11625 |
| ai | 250318006500 |
| rootfs | 28358 |
| app | v3.2.0.5375_2509162386 |

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

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/audio/src/a_policy.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../common/mod_container.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/netserver/../common/mod_container.cpp`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/network`
- `/home/gt/version_v29_d15/ipc_20240626_V29/product/exe/device/../../modules/enc/src/enc.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### ColorX Series P330X

**Hardware**: IPC_NT2NA48MPB28
**Firmware**: v3.1.0.5129_2510222155
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### ColorX Series W320X

**Hardware**: IPC_NT1NA44MP
**Firmware**: v3.1.0.4366_2412021480
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### D340P

**Hardware**: DB_566128M5MP_P
**Firmware**: v3.0.0.4662_2508131283
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 11863 |
| uboot | 11866 |
| kernel | 13835 |
| rootfs | 13833 |
| app | v3.0.0.4662_2508131283 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Core dumps | **Enabled** (`ulimit -c unlimited`) |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/netserver/../../modules`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../common/mod_co`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/da`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/ne`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/se`
- ... and 5 more

**DDNS providers**: dyndns, members.dyndns.org, members.3322.org

---

### D340P-White

**Hardware**: DB_566128M5MP_P_W
**Firmware**: v3.0.0.4662_2508131302
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Core dumps | **Enabled** (`ulimit -c unlimited`) |

---

### D340W

**Hardware**: DB_566128M5MP_W
**Firmware**: v3.0.0.4662_2508131282
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 11863 |
| uboot | 11866 |
| kernel | 13835 |
| rootfs | 13833 |
| app | v3.0.0.4662_2508131282 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Core dumps | **Enabled** (`ulimit -c unlimited`) |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/netserver/../../modules`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../common/mod_co`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/da`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/ne`
- `/home/xd/version_release/DB_V3/2025.08.07/black/ipc_20220214_V17/product/exe/device/../../modules/se`
- ... and 5 more

**DDNS providers**: dyndns, members.dyndns.org, members.3322.org

---

### D340W-White

**Hardware**: DB_566128M5MP_W_W
**Firmware**: v3.0.0.4662_2508131301
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Core dumps | **Enabled** (`ulimit -c unlimited`) |

---

### D500

**Hardware**: IPC_5158M5M
**Firmware**: v3.0.0.183_21012815
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 4 more

**Developer build paths**:

- `/home/lgb/ipc_v1_ver/20210128_3/ipc_20200324_V1/product/netserver/src/nets_recoder.cpp`
- `/home/lgb/ipc_v1_ver/20210128_3/ipc_20200324_V1/product/device/src/audio/a_policy.h`
- `/home/lgb/ipc_v1_ver/20210128_3/ipc_20200324_V1/product/device/src/isp/isp.cpp`
- `/home/lgb/ipc_v1_ver/20210128_3/ipc_20200324_V1/product/device/src/network/network.cpp`
- `/home/lgb/ipc_v1_ver/20210128_3/ipc_20200324_V1/product/device/src/snap/snap.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### D500

**Hardware**: IPC_515B8M5M_V2
**Firmware**: v3.1.0.2379_2412249791
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 10079 |
| fdt | 5769 |
| uboot | 3389 |
| kernel | 5769 |
| rootfs | 6418 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/lqy/release_20230627/ipc_20210624_V14/product/exe/device/../../modules/audio/src/bc_audio.cpp`
- `/home/lqy/release_20230627/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_u`
- `/home/lqy/release_20230627/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release_20230627/ipc_20210624_V14/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/lqy/release_20230627/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_I`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### D800

**Hardware**: IPC_5158M8M_V2
**Firmware**: v3.1.0.4057_2409132132
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 10079 |
| fdt | 5769 |
| uboot | 10541 |
| kernel | 5769 |
| rootfs | 20760 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `route add default dev %s`
- `route del default dev %s`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s down`
- ... and 10 more

**Developer build paths**:

- `/home/hjy/version/566/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_user.c`
- `/home/hjy/version/566/ipc_20210624_V14/product/exe/netserver/../common/mod_container.cpp`
- `/home/hjy/version/566/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_push.c`
- `/home/hjy/version/566/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/hjy/version/566/ipc_20210624_V14/product/exe/device/../../modules/snap/src/snap.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### Duo Series P730

**Hardware**: IPC_529B17B8MP
**Firmware**: v3.0.0.5586_2510291786
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |

---

### Duo Series P730

**Hardware**: IPC_NT18NA68MP
**Firmware**: v3.2.0.5467_2510141198
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 12681 |
| fdt | 13767 |
| atf | 11694 |
| uboot | 13235 |
| kernel | 12058 |
| ai | 250722006500 |
| rootfs | 14511 |
| app | v3.2.0.5467_2510141198 |

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

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/net`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/netserver/../../session_`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/main_device.cpp`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/device/../../modules/ser`
- `/home/liqy/release/2025/release_20250927_poe/ipc_20240626_V29.2/product/exe/netserver/../common/mod_`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### Duo Series P757

**Hardware**: IPC_NT17NA616MP
**Firmware**: v3.2.0.5770_2512231311
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 15147 |
| fdt | 13773 |
| atf | 12348 |
| uboot | 15147 |
| kernel | 12886 |
| ai | 250722006500 |
| rootfs | 15568 |
| app | v3.2.0.5770_2512231311 |

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

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/audio/s`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../../session_inte`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../common/mod_cont`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### Duo Series W750

**Hardware**: IPC_NT17NA616MPW
**Firmware**: v3.2.0.5770_2512231309
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 15147 |
| fdt | 13773 |
| atf | 12348 |
| uboot | 15147 |
| kernel | 12886 |
| ai | 250722006500 |
| rootfs | 15666 |
| app | v3.2.0.5770_2512231309 |

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

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/audio/s`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../../session_inte`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../common/mod_cont`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### E Series E321

**Hardware**: IPC_MS4NO23MPW
**Firmware**: v3.2.0.4858_2508273415
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| uboot | 12734 |
| kernel | 13716 |
| rootfs | v3.2.0.4858_2508273415 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | Yes |
| BusyBox | 1.34.1 (dangerous applets: tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### E Series E330

**Hardware**: IPC_566SD54MP
**Firmware**: v3.1.0.5112_2507081476
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 10330 |
| fdt | 6509 |
| uboot | 10541 |
| kernel | 4316 |
| rootfs | 19673 |
| rootfs | v3.1.0.5112_2507081476 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### E Series E331

**Hardware**: IPC_NT1NA45MPSD18V2
**Firmware**: v3.1.0.5714_2511271356
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### E Series E340

**Hardware**: IPC_566SD664M5MP
**Firmware**: v3.1.0.4417_2412122179
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 10893 |
| uboot | 10894 |
| kernel | 6586 |
| rootfs | 17674 |
| app | v3.1.0.4417_2412122179 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/main_device.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/netserver/main_netserver.cpp`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/netserver/../../modules/netserver/src/`
- `/home/hjy/version/v14.13/1212/ipc_20210624_V14.13/product/exe/device/../../modules/service/src/servi`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

---

### E Series E340

**Hardware**: IPC_NT14NA48MPSD6
**Firmware**: v3.2.0.4741_2503281993
**Architecture**: ARM
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: tftpd, httpd, nc, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |

---

### E Series E530X

**Hardware**: IPC_MS1NA44MP
**Firmware**: v3.0.0.3281_2403061749
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| cis | 5892 |
| uboot | 8026 |
| kernel | 8030 |
| rootfs | 8343 |
| app | v3.0.0.3281_2403061749 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/aud`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/netserver/../../modules/`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/main_device.cpp`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../common/mod_con`
- `/home/sxl/Versions/release_version/0306_377SD8/ipc_20230322_V26/product/exe/device/../../modules/enc`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### E Series E550

**Hardware**: IPC_NT2NA48MPSD8V3
**Firmware**: v3.1.0.5502_2510231295
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |

---

### E Series E560

**Hardware**: IPC_560SD88MP
**Firmware**: v3.1.0.4020_2409116797
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### E1

**Hardware**: IPC_517SD5
**Firmware**: v3.0.0.2356
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

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

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### E1

**Hardware**: IPC_566SD53MP
**Firmware**: v3.1.0.3126_2401022459
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 6509 |
| uboot | 7715 |
| kernel | 4316 |
| rootfs | 14345 |
| rootfs | v3.1.0.3126_2401022459 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### E1

**Hardware**: IPC_MS4NO24MPW
**Firmware**: v3.2.0.4858_2508273531
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| uboot | 12734 |
| kernel | 13716 |
| rootfs | v3.2.0.4858_2508273531 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | Yes |
| BusyBox | 1.34.1 (dangerous applets: tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### E1 Outdoor

**Hardware**: IPC_523SD8
**Firmware**: v3.1.0.3514_2406039634
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1804 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 4754 |
| rootfs | 17329 |
| app | v3.1.0.3514_2406039634 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/netserver/../../modules/netserve`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/network/src`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/device/../../modules/snap/src/sn`
- `/home/lqy/release/release_20240516_523/ipc_20210624_V14/product/exe/netserver/../common/mod_containe`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### E1 Outdoor

**Hardware**: IPC_566SD85MP
**Firmware**: v3.1.0.5714_2511271358
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### E1 Outdoor

**Hardware**: IPC_NT1NA45MPSD8W
**Firmware**: v3.1.0.5714_2511271352
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### E1 Outdoor Pro

**Hardware**: IPC_560SD88MPW
**Firmware**: v3.1.0.5714_2511271366
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |

---

### E1 Pro

**Hardware**: IPC_513SD5
**Firmware**: v3.0.0.2356_23062004
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### E1 Pro

**Hardware**: IPC_515SD5
**Firmware**: v3.0.0.2356_23062013
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### E1 Zoom

**Hardware**: IPC_515BSD6
**Firmware**: v3.0.0.2356_23062008
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### E1 Zoom

**Hardware**: IPC_515SD6
**Firmware**: v3.0.0.2356
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### E1 Zoom

**Hardware**: IPC_566SD65MP
**Firmware**: v3.1.0.3382_2404177933
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 5179 |
| uboot | 5180 |
| kernel | 4319 |
| rootfs | 14603 |
| app | v3.1.0.3382_2404177933 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/lqy/release/release_20240330_566_20240411/ipc_20210624_V14/product/exe/netserver/main_netserve`
- `/home/lqy/release/release_20240330_566_20240411_new/ipc_20210624_V14/product/exe/device/../common/mo`
- `/home/lqy/release/release_20240330_566_20240411/ipc_20210624_V14/product/exe/netserver/../../modules`
- `/home/lqy/release/release_20240330_566_20240411_new/ipc_20210624_V14/product/exe/device/../../module`
- `/home/lqy/release/release_20240330_566_20240411_new/ipc_20210624_V14/product/exe/device/main_device.`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### Elite Series W740

**Hardware**: IPC_NT15NA58MPW
**Firmware**: v3.2.0.4558_2503142026
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 10074 |
| fdt | 11352 |
| atf | 9982 |
| uboot | 11543 |
| kernel | 11626 |
| ai | 250109003805 |
| rootfs | 33900 |
| app | v3.2.0.4558_2503142026 |

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

**Command injection vectors**:

- `exec %s fail(%d)`
- `Failed to execute child process "%s" (%s)`
- `Unknown error executing child process "%s"`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route add default dev %s`
- ... and 8 more

**Developer build paths**:

- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/netserver/../../session_interface/src/sess`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/qinzj/working/repacket/ipc_20240626_V29/product/exe/device/../../modules/service/src/service.c`
- `/home/qinzj/working/repacket/ipc_20240626_V29/cbb/lib/NT98539/advance/libnetpublic/include/net_mempo`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### Fisheye Series P520

**Hardware**: FE_529128M6MP_P
**Firmware**: v3.0.0.5336_2509021916
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |

---

### Fisheye Series W520

**Hardware**: FE_529128M6MP_W
**Firmware**: v3.0.0.5336_2509021914
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |

---

### Floodlight Series F751W

**Hardware**: IPC_NT15NA68MPW
**Firmware**: v3.2.0.5607_2511041997
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 12240 |
| fdt | 12245 |
| atf | 9982 |
| uboot | 14828 |
| kernel | 14827 |
| ai | 251104006500 |
| rootfs | 14616 |
| app | v3.2.0.5607_2511041997 |

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

**Command injection vectors**:

- `exec %s fail(%d)`
- `Failed to execute child process "%s" (%s)`
- `Unknown error executing child process "%s"`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route add default dev %s`
- ... and 10 more

**Developer build paths**:

- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/netserver/../../session_interf`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src/s`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/netserver/../common/mod_contai`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src/e`
- `/home/lvyq/version_generation/20251104/ipc_20240626_V29.2/cbb/lib/NT98539/advance/libnetpublic/inclu`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### Lumus Series E450

**Hardware**: IPC_FH1NA48MPC7
**Firmware**: v3.2.0.4243_2507079897
**Architecture**: ?
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVC-D12M

**Hardware**: IPC_NT5NO212MP
**Firmware**: v3.1.0.3702_2501209008
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 2703 |
| fdt | 2702 |
| uboot | 2722 |
| kernel | 5569 |
| rootfs | 18115 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/main_device.`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/netserver/main_nets`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/../../module`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/device/../common/mo`
- `/home/sxl/Versions/release_version/2024.06.24_V1200/ipc_20210624_V14/product/exe/netserver/../../mod`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### NVS12W

**Hardware**: NVR_NNT3NA58W_E
**Firmware**: v3.5.1.368_24120611
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVS12W

**Hardware**: NVR_NNT3NA58W_U
**Firmware**: v3.5.1.368_24120610
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVS16

**Hardware**: N6MB01
**Firmware**: v3.6.3.422_25082953
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVS36

**Hardware**: N5MB01
**Firmware**: v3.6.3.437_25110428
**Architecture**: AArch64
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVS4

**Hardware**: NVR_NNT3NA54P
**Firmware**: v3.6.3.437_25092006
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### NVS8

**Hardware**: N7MB01
**Firmware**: v3.6.3.422_25082949
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### P320

**Hardware**: IPC_NT1NA45MP
**Firmware**: v3.1.0.5046_2506251383
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7874 |
| fdt | 12968 |
| uboot | 10541 |
| kernel | 11531 |
| rootfs | 36734 |
| app | v3.1.0.5046_2506251383 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

**Command injection vectors**:

- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `route add default dev %s`
- `route del default dev %s`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s down`
- ... and 5 more

**Developer build paths**:

- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../../modules/audio/src/`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/netserver/../../modules/netserv`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/lqy/release/2025/release_20250625/ipc_20210624_V14/product/exe/device/../common/mod_container.`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

---

### P330M

**Hardware**: IPC_560B218MP_P
**Firmware**: v3.0.0.1783_23121201
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### P430

**Hardware**: IPC_560B158MP
**Firmware**: v3.1.0.4695_2504301441
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 11619 |
| fdt | 11812 |
| uboot | 11811 |
| kernel | 11341 |
| rootfs | 34861 |
| app | v3.1.0.4695_2504301441 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

**Command injection vectors**:

- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `route add default dev %s`
- `route del default dev %s`
- `echo "nameserver %s" > /etc/resolv.conf`
- `echo "nameserver %s" >> /etc/resolv.conf`
- `route add default dev %s gw %u.%u.%u.%u`
- `ifconfig %s down`
- ... and 5 more

**Developer build paths**:

- `/home/lqy/release/2025/release_20250314_560V2_20250429/ipc_20210624_V14/product/exe/netserver/main_n`
- `/home/lqy/release/2025/release_20250314_560V2_20250429/ipc_20210624_V14/product/exe/device/main_devi`
- `/home/lqy/release/2025/release_20250314_560V2_20250429/ipc_20210624_V14/product/exe/netserver/../../`
- `/home/lqy/release/2025/release_20250314_560V2_20250429/ipc_20210624_V14/product/exe/device/../common`
- `/home/lqy/release/2025/release_20250314_560V2_20250429/ipc_20210624_V14/product/exe/netserver/../com`
- ... and 1 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

---

### RLC-1212A

**Hardware**: IPC_523B18128M12MP
**Firmware**: v3.1.0.5036_2509040629
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1801 |
| fdt | 2384 |
| uboot | 2357 |
| kernel | 4761 |
| rootfs | 36504 |
| app | v3.1.0.5036_2506276504 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2025.06.23_523B18/ipc_20210624_V14/product/exe/netserver/../commo`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/ipc_20210624_V14/product/exe/netserver/main_net`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/ipc_20210624_V14/product/exe/device/main_device`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/ipc_20210624_V14/product/exe/device/../common/m`
- `/home/sxl/Versions/release_version/2025.06.23_523B18/ipc_20210624_V14/product/exe/netserver/../../mo`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-1220A

**Hardware**: IPC_523128M12MP
**Firmware**: v3.1.0.861_24022105
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1821 |
| fdt | 1823 |
| uboot | 2357 |
| kernel | 1751 |
| rootfs | 3057 |
| app | v3.1.0.861_24022105 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/pyc/IPC_V14_gather/V14.3/ipc_20210624_V14.3/product/exe/netserver/main_netserver.cpp`
- `/home/pyc/IPC_V14_gather/V14.3/ipc_20210624_V14.3/product/exe/device/../../modules/service/src/servi`
- `/home/pyc/IPC_V14_gather/V14.3/ipc_20210624_V14.3/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/pyc/IPC_V14_gather/V14.3/ipc_20210624_V14.3/product/exe/device/../../modules/audio/src/bc_audi`
- `/home/pyc/IPC_V14_gather/V14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/incl`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-1240A

**Hardware**: IPC_NT18NA612MPD11
**Firmware**: v3.2.0.5758_2512031764
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

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

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/luojh/trunk/version`

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### RLC-410

**Hardware**: IPC_51316M
**Firmware**: v3.0.0.2356_23062000
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### RLC-410-5MP

**Hardware**: IPC_51516M5M
**Firmware**: v3.0.0.2356_23062000
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### RLC-410W

**Hardware**: IPC_30K128M4MP
**Firmware**: V3.1.0.739_22042505
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| BOOT | 2059 |
| KERNEL | 2403 |
| rootfs | 2622 |
| app | v3.1.0.739_22042505 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.20.2 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=REOLINK, OU=REOLINK, CN=REOLINK, emailAddress=service@reo-link.com |
| TLS cert expiry | Aug 23 07:40:49 2041 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

- `mi system version:%s`
- `ifconfig %s`
- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `route >> %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route add default dev %s`
- `route del default dev %s`
- `ifconfig %s 0.0.0.0`
- ... and 10 more

**Developer build paths**:

- `/home/linj/v14/product/exe/netserver/../common/mod_container.cpp`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_replay_fs.cpp`
- `/home/linj/v14/product/exe/netserver/../../modules/netserver/src/nets_md.cpp`
- `/home/linj/v14/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/linj/v14/product/exe/device/../common/mod_container.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### RLC-410W-5MP

**Hardware**: IPC_515B16M5M
**Firmware**: v3.0.0.2356_23062002
**Architecture**: MIPS
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

| Component | Details |
|-----------|---------|
| Root password | **No password (empty hash). Passwordless root login.** |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: ftpd, httpd, nc, wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_user.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/device/src/enc/utf2gbk.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_replay.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_system.cpp`
- `/home/ttc/ipcv1_version/20230620/ipc_20200324_V1/product/netserver/src/nets_cloud.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### RLC-511WA

**Hardware**: IPC_523128M5MP
**Firmware**: v3.1.0.4381_2411301864
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 3800 |
| uboot | 2357 |
| kernel | 4761 |
| rootfs | 21371 |
| app | v3.1.0.4381_2411301864 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.c`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../common/mod_container.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/audio/src/a_p`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-542WA

**Hardware**: IPC_523D95MP
**Firmware**: v3.1.0.4381_2411301871
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 4754 |
| rootfs | 21371 |
| app | v3.1.0.4381_2411301871 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/main_device.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.c`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../common/mod_container.cpp`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/device/../../modules/audio/src/a_p`
- `/home/xieyt/release/release_20241129/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-810A

**Hardware**: IPC_523128M8MP
**Firmware**: v3.1.0.956_24022103
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 1751 |
| rootfs | 3383 |
| app | v3.1.0.956_24022103 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/pyc/V14_release/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/pyc/V14_release/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_system`
- `/home/pyc/V14_release/ipc_20210624_V14/product/exe/netserver/../common/mod_container.cpp`
- `/home/pyc/V14_release/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/nets_push.c`
- `/home/pyc/V14_release/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/include/nets_se`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-810A

**Hardware**: IPC_56064M8MP
**Firmware**: v3.1.0.5764_2512171966
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### RLC-812A

**Hardware**: IPC_523B188MP
**Firmware**: v3.1.0.920_2402207844
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1820 |
| uboot | 2357 |
| kernel | 1819 |
| rootfs | 3057 |
| app | v3.1.0.920_2402207844 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/src/nets_replay_`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../common/mod_container.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/audio/src/a_policy.h`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-823A 16X

**Hardware**: IPC_523SD10
**Firmware**: v3.1.0.2898_23110119_v1.0.0.93
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 4402 |
| uboot | 3777 |
| kernel | 4761 |
| rootfs | 12362 |
| app | v3.1.0.2898_23110119 |
| ptzmcu | v1.0.0.93 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/lqy/release_202311101_SD10/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/incl`
- `/home/lqy/release_202311101_SD10/ipc_20210624_V14/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/lqy/release_202311101_SD10/ipc_20210624_V14/product/exe/device/../../modules/audio/src/bc_audi`
- `/home/lqy/release_202311101_SD10/ipc_20210624_V14/product/exe/netserver/../../modules/netserver/src/`
- `/home/lqy/release_202311101_SD10/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-823S2

**Hardware**: IPC_NT2NA48MPSD12
**Firmware**: v3.1.0.5714_25112712_v1.0.0.159
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### RLC-824A

**Hardware**: IPC_523D88MP
**Firmware**: v3.1.0.920_2402207921
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1820 |
| uboot | 2357 |
| kernel | 1819 |
| rootfs | 3057 |
| app | v3.1.0.920_2402207921 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../../modules/netserver/src/nets_replay_`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/netserver/../common/mod_container.cpp`
- `/home/pyc/V14/14.3/ipc_20210624_V14.3/product/exe/device/../../modules/audio/src/a_policy.h`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLC-830A

**Hardware**: IPC_560SD78MP
**Firmware**: v3.1.0.2515_23082406
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 6591 |
| fdt | 5217 |
| uboot | 6591 |
| kernel | 6590 |
| rootfs | 6224 |
| app | v3.1.0.2515_23082406 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/isp/src/isp.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/snap/src/snap.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/enc/src/enc.cpp`
- `/home/lqy/release_20230728_SD8/ipc_20210624_V14/product/exe/device/../../modules/service/src/service`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

---

### RLC-833A

**Hardware**: IPC_NT2NA48MP
**Firmware**: v3.1.0.4972_2510232468
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### RLC-842A

**Hardware**: IPC_523D98MP
**Firmware**: v3.1.0.1643_2402219328
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1666 |
| fdt | 1751 |
| uboot | 2357 |
| kernel | 1751 |
| rootfs | 3623 |
| app | v3.1.0.1643_2402219328 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/wxh/wxh2022/12/23/523`

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

---

### RLN8-410 (NVR)

**Hardware**: N3MB01
**Firmware**: v3.5.1.368_25010352
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 1951 |
| fdt | 2617 |
| uboot | 2617 |
| kernel | 2618 |
| logo | 11523 |
| fs | 10437 |
| app | v3.5.1.368_25010352 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

- `func:%s,line:%d,this is route ip:%s`
- `ifconfig >> %s`
- `ifconfig %s %u.%u.%u.%d`
- `ifconfig %s 192.168.10.%d`
- `route add default dev %s`
- `ifconfig %s up`
- `ifconfig %s down`
- `route del default dev %s`
- `ifconfig %s 0.0.0.0`
- `ifconfig %s hw ether %s`
- ... and 10 more

**Developer build paths**:

- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/sys/s`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/../../fsadpt/src`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/../../modules/co`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/netserver/main_netserver.c`
- `/home/gxs/v7/official/20250103_v7.5/NT98323/nvr_20220527_v7.5/product/exe/device/../../modules/push/`
- ... and 5 more

**DDNS providers**: dyndns, members.dyndns.org, members.3322.org

**P2P libraries**: libp2p.so

---

### RP-PCT16MD

**Hardware**: IPC_NT17NA616MPB
**Firmware**: v3.2.0.5770_2512231313
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 15147 |
| fdt | 13766 |
| atf | 12348 |
| uboot | 15147 |
| kernel | 12886 |
| ai | 250722006500 |
| rootfs | 15568 |
| app | v3.2.0.5770_2512231313 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: httpd, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/audio/s`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../../session_inte`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../common/mod_cont`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### RP-PCT8M

**Hardware**: IPC_NT2NA48MPB
**Firmware**: v3.1.0.5994_2601301346
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### RP-PCT8MD

**Hardware**: IPC_NT17NA68MPB
**Firmware**: v3.2.0.5770_2512231312
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 15147 |
| fdt | 13766 |
| atf | 12348 |
| uboot | 15147 |
| kernel | 12886 |
| ai | 250722006500 |
| rootfs | 15568 |
| app | v3.2.0.5770_2512231312 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.36.0 (dangerous applets: httpd, wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

**Command injection vectors**:

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
- ... and 8 more

**Developer build paths**:

- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/audio/s`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../../session_inte`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/sys/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/device/../../modules/enc/src`
- `/home/liqy/release/2025/release_20251205/ipc_20240626_V29.2/product/exe/netserver/../common/mod_cont`
- ... and 5 more

**DDNS providers**: members.dyndns.org, dyndns, members.3322.org

**P2P libraries**: libp2p.so, libp2pc.so

---

### Reolink Duo 3 PoE

**Hardware**: IPC_NT15NA416MP
**Firmware**: v3.0.0.4867_2505072124
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 9943 |
| fdt | 10115 |
| atf | 9982 |
| uboot | 9982 |
| kernel | 11626 |
| rootfs | 12580 |
| ai | 250507006500 |
| app | v3.0.0.4867_2505072124 |

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

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/../common/mod_conta`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/snap/src`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/audio/sr`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/isp/src/`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### Reolink Duo 3 WiFi

**Hardware**: IPC_NT15NA416MPW
**Firmware**: v3.0.0.4867_2505072126
**Architecture**: AArch64
**C Library**: glibc 2.35
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 9943 |
| fdt | 10115 |
| atf | 9982 |
| uboot | 10694 |
| kernel | 11626 |
| rootfs | 12580 |
| ai | 250507006500 |
| app | v3.0.0.4867_2505072126 |

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

**Command injection vectors**:

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
- ... and 6 more

**Developer build paths**:

- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/../common/mod_conta`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/netserver/main_netserver.cpp`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/snap/src`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/audio/sr`
- `/home/lqy/release/2025/release_20250507/ipc_20220409_V20.3/product/exe/device/../../modules/isp/src/`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### Reolink Duo Floodlight WiFi v2

**Hardware**: IPC_NT7NA58MP
**Firmware**: v3.0.0.4410_2506058704
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7906 |
| fdt | 5976 |
| uboot | 9701 |
| kernel | 8112 |
| rootfs | 11281 |
| app | v3.0.0.4410_2506058704 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | mbed TLS 2.24.0 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/i`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/netserver/../../module`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/e`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/../../modules/s`
- `/home/sxl/Versions/release_version/2024.12.05_F5/ipc_20220409_V20/product/exe/device/main_device.cpp`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### Reolink Duo WiFi

**Hardware**: IPC_528B174MP
**Firmware**: v3.0.0.1388_24021901
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 2738 |
| fdt | 2388 |
| uboot | 2868 |
| kernel | 2739 |
| rootfs | 4523 |
| app | v3.0.0.1388_24021901 |

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

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/main_device.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/network/src/networ`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/audio/src/bc_audio`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/sys/src/sys.cpp`
- `/home/ttc/ipcv5_version/20221006/ipc_20201208_V5/product/exe/device/../../modules/service/src/servic`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so

---

### Reolink Home Hub

**Hardware**: BASE_WENNT6NA5
**Firmware**: v3.3.0.456_25122258
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### Reolink Home Hub

**Hardware**: BASE_WUNNT6NA5
**Firmware**: v3.3.0.456_25122248
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### Reolink Home Hub Pro

**Hardware**: BASE_WENNT3NA5
**Firmware**: v3.3.0.369_25090459
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### Reolink Home Hub Pro

**Hardware**: BASE_WUNNT3NA5
**Firmware**: v3.3.0.369_25090486
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: ubifs, squashfs

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |

---

### Reolink Lumus

**Hardware**: IPC_NT1NO24MP
**Firmware**: v3.1.0.5047_2506271410
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 10330 |
| fdt | 13285 |
| uboot | 13286 |
| kernel | 6531 |
| rootfs | 20033 |
| rootfs | v3.1.0.5047_2506271410 |

| Component | Details |
|-----------|---------|
| Root password | `5p6FGL0H1INXw` (DES crypt, no shadow) |
| Shadow file | No |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### Reolink TrackMix WiFi

**Hardware**: IPC_529SD78MP
**Firmware**: v3.0.0.5428_2509171974
**Architecture**: ARM
**C Library**: glibc 2.29
**Filesystems**: ubifs, ubifs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 3123 |
| fdt | 13751 |
| uboot | 13360 |
| kernel | 11185 |
| rootfs | 14208 |
| app | v3.0.0.5428_2509171974 |

| Component | Details |
|-----------|---------|
| Root password | `aRDwnwAt1ygAM` (DES crypt, no shadow) |
| Shadow file | No |
| nginx | nginx/1.14.2 |
| BusyBox | 1.24.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/isp/src`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/service`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/netserver/main_netserver.cpp`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../../modules/network`
- `/home/xd/version_release/529SD7/2025.09.17/ipc_20220228_V18/product/exe/device/../common/mod_contain`
- ... and 5 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### V800W

**Hardware**: IPC_NT2NO28MP
**Firmware**: v3.1.0.3114_2407022284
**Architecture**: ARM
**C Library**: glibc 2.30
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| loader | 7218 |
| fdt | 7218 |
| uboot | 7633 |
| kernel | 7670 |
| rootfs | 15437 |

| Component | Details |
|-----------|---------|
| Root password | `XF4sg5T82tV4k` (DES crypt, no shadow) |
| Shadow file | No |
| OpenSSL | OpenSSL 1.0.2f **EOL since 2020** |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### W320

**Hardware**: IPC_MS1NA45MP
**Firmware**: v3.0.0.4348_2411261179
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| cis | 5892 |
| uboot | 10533 |
| kernel | 9535 |
| rootfs | 11123 |
| app | v3.0.0.4348_2411261179 |

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| nginx | nginx/1.22.1 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/s`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/../common/mod_`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/m`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/main_device.cp`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../../modul`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### W320C

**Hardware**: IPC_MS1NO25MP
**Firmware**: v3.0.0.3078_2405089137
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| uboot | 7535 |
| kernel | 7065 |
| rootfs | 7533 |
| app | v3.0.0.3078_2405089137 |

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

### W330

**Hardware**: IPC_MS2NA48MP
**Firmware**: v3.0.0.4348_2411261894
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs, squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| cis | 6086 |
| uboot | 10535 |
| kernel | 10423 |
| rootfs | 11125 |
| app | v3.0.0.4348_2411261894 |

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| nginx | nginx/1.22.1 |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| Mbed TLS | Mbed TLS 2.28.9 |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Enabled |
| Super password | Enabled |
| Default password | *(empty)* |
| Amcrest/Dahua code | `AmcrestToken` found in binaries |

**Command injection vectors**:

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
- ... and 10 more

**Developer build paths**:

- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/s`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/../common/mod_`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../common/m`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/device/main_device.cp`
- `/home/sxl/Versions/release_version/2024.11.26_V26/ipc_20230322_V26/product/exe/netserver/../../modul`
- ... and 1 more

**DDNS providers**: members.3322.org, members.dyndns.org, dyndns

**P2P libraries**: libp2p.so, libp2pc.so

---

### W330C

**Hardware**: IPC_MS2NO28MP
**Firmware**: v3.0.0.5031_2506270556
**Architecture**: ARM
**C Library**: glibc __glibc_strerror_r
**Filesystems**: squashfs

**Firmware Partitions**:

| Partition | Version |
|-----------|---------|
| uboot | 10422 |
| kernel | 10424 |
| rootfs | 13206 |
| app | v3.0.0.5031_2506270556 |

| Component | Details |
|-----------|---------|
| Root password | Hash in shadow file (`x`) |
| Shadow file | Yes |
| BusyBox | 1.31.1 (dangerous applets: wget, tftp) |
| TLS certificate | RSA 2048 bit, C=CN, ST=GD, L=SZ, O=CERTIFICATE, OU=CERTIFICATE, CN=CERTIFICATE, emailAddress=CERTIFICATE@CERTIFICATE.com |
| TLS cert expiry | May  7 09:36:46 2043 GMT |
| Cloud support | Disabled |
| Super password | Enabled |
| Default password | *(empty)* |

---

## Methodology

Each firmware was:
1. Downloaded from Reolink CDN (`home-cdn.reolink.us`)
2. Extracted using `binwalk`, `ubireader_extract_images`, and `unsquashfs`
3. Analyzed for: password hashes, TLS certificates, library versions (OpenSSL, nginx, Mbed TLS, live555, BusyBox), command injection vectors, privilege separation, cloud connectivity, developer artifacts

Firmware metadata sourced from [AT0myks/reolink-fw-archive](https://github.com/AT0myks/reolink-fw-archive).

## Key Findings

1. **Shared secrets at scale**: Only 4 root passwords and 4 TLS certificates protect 89 distinct hardware versions. Compromising one device gives credentials for dozens of models.
2. **No firmware signing**: Any attacker with network access can push malicious firmware. The OTA update mechanism uses only CRC32/MD5 integrity checks.
3. **Legacy libraries**: 23 models still ship OpenSSL 1.0.2f (EOL 2020), exposing them to years of known vulnerabilities.
4. **Universal root**: Every process runs as root. A single vulnerability in nginx, RTSP, or any network service gives full device control.
5. **OEM code sharing**: Amcrest/Dahua tokens in 38 models suggest shared IP camera firmware ancestry, meaning vulnerabilities may affect multiple brands.

