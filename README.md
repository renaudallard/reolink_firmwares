# Reolink Firmware Security & Connectivity Analysis

Automated security analysis of **91 firmware images** across the entire Reolink product line,
covering cameras (IPC), NVRs, home hubs, doorbells, and fisheye devices.

## Summary

- **91 hardware versions** analyzed from latest available firmware
- **9 hardware versions** could not be extracted (cramfs/old formats)
- **4 unique root password hashes** found across all devices
- **Zero devices** use `/etc/shadow` properly (only 7 have shadow files)
- **Every device** runs everything as root with no privilege separation
- **No firmware** uses cryptographic signature verification (CRC32 + MD5 only)

## All Models Analyzed

| Model | HW Version | Firmware | Arch | Kernel | BusyBox | OpenSSL | nginx | Root Hash |
|-------|------------|----------|------|--------|---------|---------|-------|-----------|
| [B1200](models/B1200_IPC_52316M12MP.md) | IPC_52316M12MP | v3.1.0.5036_2506279222 | ARM | 4.19.91 | 1.24.1 | - | - | `5p6FGL0H1INXw` |
| [B400](models/B400_IPC_5128M.md) | IPC_5128M | v3.0.0.183_21012800 | MIPS | 4.1.0 | 1.24.1 | - | - | *(empty)* |
| [B800](models/B800_IPC_5158MP8M.md) | IPC_5158MP8M | v3.0.0.183_21012800 | MIPS | 4.1.0 | 1.24.1 | - | - | *(empty)* |
| [CX820](models/CX820_IPC_NT16NA48MP.md) | IPC_NT16NA48MP | v3.2.0.5375_2509162386 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [ColorX Series P330X](models/ColorX_Series_P330X_IPC_NT2NA48MPB28.md) | IPC_NT2NA48MPB28 | v3.1.0.5129_2510222155 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [ColorX Series W320X](models/ColorX_Series_W320X_IPC_NT1NA44MP.md) | IPC_NT1NA44MP | v3.1.0.4366_2412021480 | ARM | 4.19.91 | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| [D340P](models/D340P_DB_566128M5MP_P.md) | DB_566128M5MP_P | v3.0.0.4662_2508131283 | ARM | 4.19.91 | 1.31.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| [D340P-White](models/D340P-White_DB_566128M5MP_P_W.md) | DB_566128M5MP_P_W | v3.0.0.4662_2508131302 | ARM | 4.19.91 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [D340W](models/D340W_DB_566128M5MP_W.md) | DB_566128M5MP_W | v3.0.0.4662_2508131282 | ARM | 4.19.91 | 1.31.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| [D340W-White](models/D340W-White_DB_566128M5MP_W_W.md) | DB_566128M5MP_W_W | v3.0.0.4662_2508131301 | ARM | 4.19.91 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [D500](models/D500_IPC_5158M5M.md) | IPC_5158M5M | v3.0.0.183_21012815 | MIPS | 4.1.0 | 1.24.1 | - | - | *(empty)* |
| [D500](models/D500_IPC_515B8M5M_V2.md) | IPC_515B8M5M_V2 | v3.1.0.2379_2412249791 | ARM | 4.19.91 | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| [D800](models/D800_IPC_5158M8M_V2.md) | IPC_5158M8M_V2 | v3.1.0.4057_2409132132 | ARM | 4.19.91 | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| [Duo Series P730](models/Duo_Series_P730_IPC_529B17B8MP.md) | IPC_529B17B8MP | v3.0.0.5586_2510291786 | ARM | 4.19.91 | 1.24.1 | - | - | `5p6FGL0H1INXw` |
| [Duo Series P730](models/Duo_Series_P730_IPC_NT18NA68MP.md) | IPC_NT18NA68MP | v3.2.0.5467_2510141198 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Duo Series P757](models/Duo_Series_P757_IPC_NT17NA616MP.md) | IPC_NT17NA616MP | v3.2.0.5770_2512231311 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Duo Series W750](models/Duo_Series_W750_IPC_NT17NA616MPW.md) | IPC_NT17NA616MPW | v3.2.0.5770_2512231309 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [E Series E321](models/E_Series_E321_IPC_MS4NO23MPW.md) | IPC_MS4NO23MPW | v3.2.0.4858_2508273415 | ARM | 5.10.61 | 1.34.1 | - | - | `aRDwnwAt1ygAM` |
| [E Series E330](models/E_Series_E330_IPC_566SD54MP.md) | IPC_566SD54MP | v3.1.0.5112_2507081476 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E Series E331](models/E_Series_E331_IPC_NT1NA45MPSD18V2.md) | IPC_NT1NA45MPSD18V2 | v3.1.0.5714_2511271356 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E Series E340](models/E_Series_E340_IPC_566SD664M5MP.md) | IPC_566SD664M5MP | v3.1.0.4417_2412122179 | ARM | 4.19.91 | 1.31.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| [E Series E340](models/E_Series_E340_IPC_NT14NA48MPSD6.md) | IPC_NT14NA48MPSD6 | v3.2.0.4741_2503281993 | ARM | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [E Series E530X](models/E_Series_E530X_IPC_MS1NA44MP.md) | IPC_MS1NA44MP | v3.0.0.3281_2403061749 | ARM | 5.10.61 | 1.31.1 | - | 1.22.0 | `x` |
| [E Series E550](models/E_Series_E550_IPC_NT2NA48MPSD8V3.md) | IPC_NT2NA48MPSD8V3 | v3.1.0.5502_2510231295 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E Series E560](models/E_Series_E560_IPC_560SD88MP.md) | IPC_560SD88MP | v3.1.0.4020_2409116797 | ARM | 4.19.91 | 1.31.1 | - | - | `XF4sg5T82tV4k` |
| [E1](models/E1_IPC_517SD5.md) | IPC_517SD5 | v3.0.0.2356 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | - | *(empty)* |
| [E1](models/E1_IPC_566SD53MP.md) | IPC_566SD53MP | v3.1.0.3126_2401022459 | ARM | 4.19.91 | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| [E1](models/E1_IPC_MS4NO24MPW.md) | IPC_MS4NO24MPW | v3.2.0.4858_2508273531 | ARM | 5.10.61 | 1.34.1 | - | - | `aRDwnwAt1ygAM` |
| [E1 Outdoor](models/E1_Outdoor_IPC_523SD8.md) | IPC_523SD8 | v3.1.0.3514_2406039634 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [E1 Outdoor](models/E1_Outdoor_IPC_566SD85MP.md) | IPC_566SD85MP | v3.1.0.5714_2511271358 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E1 Outdoor](models/E1_Outdoor_IPC_NT1NA45MPSD8W.md) | IPC_NT1NA45MPSD8W | v3.1.0.5714_2511271352 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E1 Outdoor Pro](models/E1_Outdoor_Pro_IPC_560SD88MPW.md) | IPC_560SD88MPW | v3.1.0.5714_2511271366 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [E1 Pro](models/E1_Pro_IPC_513SD5.md) | IPC_513SD5 | v3.0.0.2356_23062004 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | - | *(empty)* |
| [E1 Pro](models/E1_Pro_IPC_515SD5.md) | IPC_515SD5 | v3.0.0.2356_23062013 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | - | *(empty)* |
| [E1 Pro](models/E1_Pro_IPC_NT1NA45MP.md) | IPC_NT1NA45MP | v3.1.0.4417_2412122130 | ARM | 4.19.91 | 1.31.1 | 3.3.2 | 1.14.2 | `XF4sg5T82tV4k` |
| [E1 Zoom](models/E1_Zoom_IPC_515BSD6.md) | IPC_515BSD6 | v3.0.0.2356_23062008 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| [E1 Zoom](models/E1_Zoom_IPC_515SD6.md) | IPC_515SD6 | v3.0.0.2356 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| [E1 Zoom](models/E1_Zoom_IPC_566SD65MP.md) | IPC_566SD65MP | v3.1.0.3382_2404177933 | ARM | 4.19.91 | 1.31.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [Elite Series W740](models/Elite_Series_W740_IPC_NT15NA58MPW.md) | IPC_NT15NA58MPW | v3.2.0.4558_2503142026 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Fisheye Series P520](models/Fisheye_Series_P520_FE_529128M6MP_P.md) | FE_529128M6MP_P | v3.0.0.5336_2509021916 | ARM | 4.19.91 | 1.24.1 | - | - | `aRDwnwAt1ygAM` |
| [Fisheye Series W520](models/Fisheye_Series_W520_FE_529128M6MP_W.md) | FE_529128M6MP_W | v3.0.0.5336_2509021914 | ARM | 4.19.91 | 1.24.1 | - | - | `aRDwnwAt1ygAM` |
| [Floodlight Series F751W](models/Floodlight_Series_F751W_IPC_NT15NA68MPW.md) | IPC_NT15NA68MPW | v3.2.0.5607_2511041997 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Lumus Series E450](models/Lumus_Series_E450_IPC_FH1NA48MPC7.md) | IPC_FH1NA48MPC7 | v3.2.0.4243_2507079897 | ? | - | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [NVC-D12M](models/NVC-D12M_IPC_NT5NO212MP.md) | IPC_NT5NO212MP | v3.1.0.3702_2501209008 | ARM | 4.19.91 | 1.24.1 | - | - | `XF4sg5T82tV4k` |
| [NVS12W](models/NVS12W_NVR_NNT3NA58W_E.md) | NVR_NNT3NA58W_E | v3.5.1.368_24120611 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [NVS12W](models/NVS12W_NVR_NNT3NA58W_U.md) | NVR_NNT3NA58W_U | v3.5.1.368_24120610 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [NVS16](models/NVS16_N6MB01.md) | N6MB01 | v3.6.3.422_25082953 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [NVS36](models/NVS36_N5MB01.md) | N5MB01 | v3.6.3.437_25110428 | AArch64 | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [NVS4](models/NVS4_NVR_NNT3NA54P.md) | NVR_NNT3NA54P | v3.6.3.437_25092006 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [NVS8](models/NVS8_N7MB01.md) | N7MB01 | v3.6.3.422_25082949 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [P320](models/P320_IPC_NT1NA45MP.md) | IPC_NT1NA45MP | v3.1.0.5046_2506251383 | ARM | 4.19.91 | 1.31.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| [P330M](models/P330M_IPC_560B218MP_P.md) | IPC_560B218MP_P | v3.0.0.1783_23121201 | ARM | 4.19.91 | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| [P430](models/P430_IPC_560B158MP.md) | IPC_560B158MP | v3.1.0.4695_2504301441 | ARM | 4.19.91 | 1.31.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| [RLC-1212A](models/RLC-1212A_IPC_523B18128M12MP.md) | IPC_523B18128M12MP | v3.1.0.5036_2509040629 | ARM | 4.19.91 | 1.24.1 | - | 1.14.2 | `5p6FGL0H1INXw` |
| [RLC-1220A](models/RLC-1220A_IPC_523128M12MP.md) | IPC_523128M12MP | v3.1.0.861_24022105 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-1224A](models/RLC-1224A_IPC_523D8128M12MP.md) | IPC_523D8128M12MP | v3.1.0.2174_23050816 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-1240A](models/RLC-1240A_IPC_NT18NA612MPD11.md) | IPC_NT18NA612MPD11 | v3.2.0.5758_2512031764 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [RLC-410](models/RLC-410_IPC_51316M.md) | IPC_51316M | v3.0.0.2356_23062000 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| [RLC-410-5MP](models/RLC-410-5MP_IPC_51516M5M.md) | IPC_51516M5M | v3.0.0.2356_23062000 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| [RLC-410W](models/RLC-410W_IPC_30K128M4MP.md) | IPC_30K128M4MP | V3.1.0.739_22042505 | ARM | 4.9.84 | 1.20.2 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-410W-5MP](models/RLC-410W-5MP_IPC_515B16M5M.md) | IPC_515B16M5M | v3.0.0.2356_23062002 | MIPS | 4.1.0 | 1.24.1 | 1.0.2f | 1.14.2 | *(empty)* |
| [RLC-511WA](models/RLC-511WA_IPC_523128M5MP.md) | IPC_523128M5MP | v3.1.0.4381_2411301864 | ARM | 4.19.91 | 1.24.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-542WA](models/RLC-542WA_IPC_523D95MP.md) | IPC_523D95MP | v3.1.0.4381_2411301871 | ARM | 4.19.91 | 1.24.1 | - | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-810A](models/RLC-810A_IPC_523128M8MP.md) | IPC_523128M8MP | v3.1.0.956_24022103 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-810A](models/RLC-810A_IPC_56064M8MP.md) | IPC_56064M8MP | v3.1.0.5764_2512171966 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [RLC-812A](models/RLC-812A_IPC_523B188MP.md) | IPC_523B188MP | v3.1.0.920_2402207844 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-823A 16X](models/RLC-823A_16X_IPC_523SD10.md) | IPC_523SD10 | v3.1.0.2898_23110119_v1.0.0.93 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-823S2](models/RLC-823S2_IPC_NT2NA48MPSD12.md) | IPC_NT2NA48MPSD12 | v3.1.0.5714_25112712_v1.0.0.159 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [RLC-824A](models/RLC-824A_IPC_523D88MP.md) | IPC_523D88MP | v3.1.0.920_2402207921 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-830A](models/RLC-830A_IPC_560SD78MP.md) | IPC_560SD78MP | v3.1.0.2515_23082406 | ARM | 4.19.91 | 1.31.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLC-833A](models/RLC-833A_IPC_NT2NA48MP.md) | IPC_NT2NA48MP | v3.1.0.4972_2510232468 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [RLC-842A](models/RLC-842A_IPC_523D98MP.md) | IPC_523D98MP | v3.1.0.1643_2402219328 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [RLN8-410 (NVR)](models/RLN8-410_NVR_N3MB01.md) | N3MB01 | v3.5.1.368_25010352 | ARM | 4.9.118 | 1.24.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| [RP-PCT16MD](models/RP-PCT16MD_IPC_NT17NA616MPB.md) | IPC_NT17NA616MPB | v3.2.0.5770_2512231313 | AArch64 | 5.10.168 | 1.36.0 | - | - | `5p6FGL0H1INXw` |
| [RP-PCT8M](models/RP-PCT8M_IPC_NT2NA48MPB.md) | IPC_NT2NA48MPB | v3.1.0.5994_2601301346 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [RP-PCT8MD](models/RP-PCT8MD_IPC_NT17NA68MPB.md) | IPC_NT17NA68MPB | v3.2.0.5770_2512231312 | AArch64 | 5.10.168 | 1.36.0 | - | - | `5p6FGL0H1INXw` |
| [Reolink Duo 3 PoE](models/Reolink_Duo_3_PoE_IPC_NT15NA416MP.md) | IPC_NT15NA416MP | v3.0.0.4867_2505072124 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Duo 3 WiFi](models/Reolink_Duo_3_WiFi_IPC_NT15NA416MPW.md) | IPC_NT15NA416MPW | v3.0.0.4867_2505072126 | AArch64 | 5.10.168 | 1.36.0 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Duo Floodlight WiFi v2](models/Reolink_Duo_Floodlight_WiFi_v2_IPC_NT7NA58MP.md) | IPC_NT7NA58MP | v3.0.0.4410_2506058704 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [Reolink Duo WiFi](models/Reolink_Duo_WiFi_IPC_528B174MP.md) | IPC_528B174MP | v3.0.0.1388_24021901 | ARM | 4.19.91 | 1.24.1 | 1.0.2f | 1.14.2 | `XF4sg5T82tV4k` |
| [Reolink Home Hub](models/Reolink_Home_Hub_BASE_WENNT6NA5.md) | BASE_WENNT6NA5 | v3.3.0.456_25122258 | ARM | 4.19.91 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Home Hub](models/Reolink_Home_Hub_BASE_WUNNT6NA5.md) | BASE_WUNNT6NA5 | v3.3.0.456_25122248 | ARM | 4.19.91 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Home Hub Pro](models/Reolink_Home_Hub_Pro_BASE_WENNT3NA5.md) | BASE_WENNT3NA5 | v3.3.0.369_25090459 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Home Hub Pro](models/Reolink_Home_Hub_Pro_BASE_WUNNT3NA5.md) | BASE_WUNNT3NA5 | v3.3.0.369_25090486 | ARM | 4.19.148 | 1.31.1 | - | - | `aRDwnwAt1ygAM` |
| [Reolink Lumus](models/Reolink_Lumus_IPC_NT1NO24MP.md) | IPC_NT1NO24MP | v3.1.0.5047_2506271410 | ARM | 4.19.91 | 1.31.1 | - | - | `5p6FGL0H1INXw` |
| [Reolink TrackMix WiFi](models/Reolink_TrackMix_WiFi_IPC_529SD78MP.md) | IPC_529SD78MP | v3.0.0.5428_2509171974 | ARM | 4.19.91 | 1.24.1 | - | 1.14.2 | `aRDwnwAt1ygAM` |
| [V800W](models/V800W_IPC_NT2NO28MP.md) | IPC_NT2NO28MP | v3.1.0.3114_2407022284 | ARM | 4.19.91 | 1.31.1 | 1.0.2f | - | `XF4sg5T82tV4k` |
| [W320](models/W320_IPC_MS1NA45MP.md) | IPC_MS1NA45MP | v3.0.0.4348_2411261179 | ARM | 5.10.61 | 1.31.1 | - | 1.22.1 | `x` |
| [W320C](models/W320C_IPC_MS1NO25MP.md) | IPC_MS1NO25MP | v3.0.0.3078_2405089137 | ARM | 5.10.61 | 1.31.1 | - | - | `x` |
| [W330](models/W330_IPC_MS2NA48MP.md) | IPC_MS2NA48MP | v3.0.0.4348_2411261894 | ARM | 5.10.61 | 1.31.1 | - | 1.22.1 | `x` |
| [W330C](models/W330C_IPC_MS2NO28MP.md) | IPC_MS2NO28MP | v3.0.0.5031_2506270556 | ARM | - | 1.31.1 | - | - | `x` |

## Critical Vulnerabilities (All Models)

These issues are present in **every firmware analyzed**:

| Vulnerability | Severity | Details |
|---------------|----------|---------|
| Hardcoded root password | Critical | DES hash in `/etc/passwd`, no `/etc/shadow`. Only 4 unique hashes across all 91 models |
| Shared TLS private key | Critical | Same certificate baked into firmware for entire product lines. 4 unique certs across 54 models |
| No firmware signature verification | Critical | Only CRC32 + MD5 integrity checks. Any modified firmware can be flashed |
| Everything runs as root | Critical | nginx, RTSP server, device manager. all run as UID 0, no privilege separation |
| Command injection vectors | Critical | `system()` calls with user input in smbpasswd, resolv.conf, ddns-config, ifconfig |
| Super password bypass | High | `support_supper_pwd="1"` in 59/91 models. factory backdoor password |
| Amcrest/Dahua code sharing | Medium | `AmcrestToken` found in 40/91 models. Shared OEM codebase |
| Core dumps enabled | Medium | `ulimit -c unlimited` in 4 models. Memory contents written to disk |
| Developer build paths | Low | Compiler paths like `/home/username/project/` leaked in binaries |

## Root Password Hashes

Only 4 unique DES hashes protect root access across 79 models (11 additional models have **no password at all**):

| Hash | Models Using It | Count |
|------|----------------|-------|
| `aRDwnwAt1ygAM` | CX820, D340P, D340P-White, D340W, D340W-White, ... (+25 more) | 30 |
| `XF4sg5T82tV4k` | ColorX Series W320X, D500, D800, E1 Pro, E Series E340, E Series E560, ... (+18 more) | 24 |
| `5p6FGL0H1INXw` | B1200, ColorX Series P330X, Duo Series P730, E Series E330, E Series E331, ... (+15 more) | 20 |
| `x` | E Series E530X, W320, W320C, W330, W330C | 5 |
| *(empty)* | B400, B800, D500, E1, E1 Pro (x2), E1 Zoom (x2), RLC-410, RLC-410-5MP, RLC-410W-5MP | 11 |

All hashes are traditional DES crypt (13 characters), trivially crackable.
The hash `x` indicates the password field points to shadow, but the shadow files found are mostly empty or have the same weak hashes.
An **empty hash field** means passwordless root login. these 11 MIPS models allow root access without any password.

## Linux Kernel Versions

| Version | Status | Models |
|---------|--------|--------|
| 4.1.0 | **EOL. No security patches since 2018** | 11 |
| 4.9.84 | EOL. Last 4.9 LTS was 4.9.337 (2023) | 1 |
| 4.9.118 | EOL. Last 4.9 LTS was 4.9.337 (2023) | 1 |
| 4.19.91 | EOL. Last 4.19 LTS was 4.19.306 (2024) | 50 |
| 4.19.148 | EOL. Last 4.19 LTS was 4.19.306 (2024) | 9 |
| 5.10.61 | LTS (EOL Dec 2026). Current 5.10 is 5.10.238 | 6 |
| 5.10.168 | LTS (EOL Dec 2026). Current 5.10 is 5.10.238 | 12 |
| unknown | Extraction failed | 11 |

The majority of devices (62/90) run EOL 4.x kernels that no longer receive security patches.
Only the newest AArch64 and MediaTek-based platforms use the 5.10 LTS kernel.

## OpenSSL Versions

| Version | Status | Models |
|---------|--------|--------|
| OpenSSL 1.0.2f | **EOL since 2020. CRITICAL** | 24 |
| OpenSSL 3.3.2 | Current | 1 |
| not found | Uses Mbed TLS or statically linked | 66 |

## nginx Versions

| Version | Status | Models |
|---------|--------|--------|
| nginx/1.14.2 | **2018, multiple CVEs** | 28 |
| nginx/1.22.0 | 2022, older but fewer CVEs | 1 |
| nginx/1.22.1 | 2022, older but fewer CVEs | 2 |
| not found | Uses app-integrated web server | 58 |

## BusyBox Versions & Dangerous Applets

| Version | Models | Notable Applets Compiled In |
|---------|--------|-----------------------------|
| 1.20.2 | 1 | tftp, wget |
| 1.24.1 | 30 | ftpd, httpd, nc, tftp, wget |
| 1.31.1 | 45 | tftp, wget |
| 1.34.1 | 2 | tftp |
| 1.36.0 | 12 | httpd, nc, tftp, tftpd, wget |

All versions include `tftp` and `wget`. Older versions (1.24.1 and below) additionally include
`telnetd`, `ftpd`, `tftpd`, and `httpd` which enable network service persistence after exploitation.

## TLS Certificate Analysis

Certificates are baked into firmware and shared across entire product lines.
The private key is extractable from any firmware image, making TLS effectively useless.

| Key Size | Models |
|----------|--------|
| 2048 bit | 48 |
| 4096 bit | 6 |
| N/A | 36 |

Only **4 unique TLS certificates** across 54 models that have certificates.
This means many different camera models share the exact same TLS private key.

## Mbed TLS Versions

| Version | Models |
|---------|--------|
| Mbed TLS 2.28.9 | 29 |
| mbed TLS 2.24.0 | 17 |
| not found | 44 |

## Cloud & Connectivity

- **Cloud enabled**: 36 models
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


## Tools

### reolink-enc.sh

Set video encoding (H.264/H.265) on Reolink cameras via the HTTP API.

```
usage: reolink-enc.sh -u user -p pass -h host [-s stream] codec
  -u user    login username
  -p pass    login password
  -h host    camera IP or hostname
  -s stream  main or sub (default: main)
  codec      h264 or h265
```

Only works on models where `encoder_select` is not locked (`encoder_select="3"` in `dvr.xml`).

### reolink-patch-enc.sh

Patch Reolink firmware to enable H.264/H.265 codec switching on models where it is locked (`encoder_select="0"` in `dvr.xml`, e.g. E1 Pro IPC_NT1NA45MP).

```
usage: reolink-patch-enc.sh firmware.pak [output.pak]
```

Changes `encoder_select="0"` to `encoder_select="3"` in the app partition's `dvr.xml` and repacks the PAK file with updated CRC32. The hardware already supports both codecs (Novatek `kdrv_h26x.ko` kernel modules); this patch only removes the software restriction.

Requires: `pakler`, `ubireader`, `unsquashfs`, `mksquashfs`, `ubinize`

## Methodology

Each firmware was:
1. Downloaded from Reolink CDN (`home-cdn.reolink.us`)
2. Extracted using `binwalk`, `ubireader_extract_images`, and `unsquashfs`
3. Analyzed for: password hashes, TLS certificates, library versions (OpenSSL, nginx, Mbed TLS, live555, BusyBox), command injection vectors, privilege separation, cloud connectivity, developer artifacts

Firmware metadata sourced from [AT0myks/reolink-fw-archive](https://github.com/AT0myks/reolink-fw-archive).

## Key Findings

1. **Shared secrets at scale**: Only 4 root passwords and 4 TLS certificates protect 91 distinct hardware versions. Compromising one device gives credentials for dozens of models.
2. **No firmware signing**: Any attacker with network access can push malicious firmware. The OTA update mechanism uses only CRC32/MD5 integrity checks.
3. **Legacy libraries**: 24 models still ship OpenSSL 1.0.2f (EOL 2020), exposing them to years of known vulnerabilities.
4. **Universal root**: Every process runs as root. A single vulnerability in nginx, RTSP, or any network service gives full device control.
5. **OEM code sharing**: Amcrest/Dahua tokens in 40 models suggest shared IP camera firmware ancestry, meaning vulnerabilities may affect multiple brands.

