---
layout: default-layout
title: Enumerations for version 1.x - Dynamsoft Camera Enhancer
description: This is the documentation - Enumerations for version 1.x of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations
needAutoGenerateSidebar: true
breadcrumbText: Enumerations
---

# Enumerations

## CameraState

| Member (Android & iOS) | Value | Description |
|-----------------------|-------|-------------|
| `CAMERA_STATE_OFF` | 0 | Set camera off. |
| `CAMERA_STATE_ON` | 1 | Set camera on. |

## CameraPosition

| Member (Android & iOS) | Value | Description |
|-----------------------|-------|-------------|
| `CAMERA_POSITION_USER` | 0 | Use front camera. |
| `CAMERA_POSITION_WORLD` | 1 | Use back camera. |

## TorchState

| Member (Android & iOS) | Value | Description |
|-----------------------|-------|-------------|
| `TORCH_STATE_OFF` | 0 | Turn off torch. |
| `TORCH_STATE_ON` | 1 | Turn on torch. |
| `TORCH_STATE_AUTO` | 2 | Auto turn on/off torch. |

## Resolution

| Member (Android & iOS) | Value | Description |
|------------------------|-------|-------------|
| `RESOLUTION_AUTO` | 0 | Set resolution auto. |
| `RESOLUTION_480P` | 1 | Set resolution at 480p. |
| `RESOLUTION_720P` | 2 | Set resolution at 720p. |
| `RESOLUTION_1080P` | 3 | Set resolution at 1080p. |
| `RESOLUTION_2K` (Android Only) | 4 | Set resolution at 2k. |
| `RESOLUTION_4K` | 5 | Set resolution at 4k. |

## HardwareUtil

| Member (Android Only) | Value | Description |
|-----------------------|-------|-------------|
| `DEVICEINFO_UNKNOWN` | -1 | The device info is unavailable. |
| `DEVICE_LEVEL_HIGH` | 2 | The device level is detected to be high. |
| `DEVICE_LEVEL_MID` | 1 | The device level is detected to be medium. |
| `DEVICE_LEVEL_LOW` | 0 | The device level is detected to be low. |
| `DEVICE_LEVEL_UNKNOWN` | -2 | The device level is unavailable. |

## EnumDMChargeWay

| Member | Value | Description |
|--------|-------|-------------|
| `DM_CW_AUTO` | 0 | The charge way is automatically determined by the license server. |
| `DM_CW_DEVICE_COUNT` | 1 | Charges by the count of devices. |
| `DM_CW_CONCURRENT_DEVICE_COUNT` | 3 | Charges by the count of concurrent devices. |
| `DM_CW_APP_DOMAIN_COUNT` | 6 | Charges by the count of app domains. |
| `DM_CW_ACTIVE_DEVICE_COUNT` | 8 | Charges by the count of active devices. |

## EnumProduct

| Member | Value | Description |
|--------|-------|-------------|
| `PROD_DBR` | 0x01 | Product DBR. |
| `PROD_DLR` | 0x02 | Product DLR. |
| `PROD_DWT` | 0x04 | Product DWT. |
| `PROD_DCE` | 0x08 | Product DCE. |
| `PROD_DPS` | 0x10 | Product DPS |
| `PROD_ALL` | 0xffff | Product All |

## EnumCameraDMUUIDGenerationMethod

| Member | Value | Description |
|--------|-------|-------------|
| `DM_UUIDGM_RANDOM` | 1 | Generates UUID with random values. |
| `DM_UUIDGM_HARDWARE` | 2 | Generates UUID based on hardware info. |

## ErrorCode

| Error Code | Value | Description |
|------------|-------|-------------|
| `DCE_OK` | 0 | Successful. |
| `DCE_LICENSE_INVALID` | -10001 | The licence is invalid. |
| `DCE_LICENSE_EXPIRED` | -10002 | The licence has expired. |
| `DCE_NOT_EXIST_CAMERA_MODULE` | -10003 | Camera module does not exist. |
| `DCE_NOT_FOUND_FILE` | -10004 | File is not found. |
| `DCE_FILE_FORMAT_ERROR` | -10005 | File format error. |
| `DCE_LICENSEKEY_NOT_MATCHED` | -10043 | The license key does not match the license content. |
| `DCE_REQUEST_FAILED` | -10044 | The license key does not match the license content. |
| `DM_NO_LICENSE` | -20000 | There is no license specified. |
| `DM_HANDSHAKE_CODE_INVALID` | -20001 | Handshake code is invalid. |
| `DM_LICENSE_BUFFER_FAILED` | -20002 | Failed to read or write license buffer. |
| `DM_LICENSE_SYNC_FAILED` | -20003 | Failed to synchronize license info with Dynamsoft License Server. |
| `DM_DEVICE_NOT_MATCH` | -20004 | Device does not match with license buffer. |
| `DM_BIND_DEVICE_FAILED` | -20005 | Failed to bind device. |
| `DM_LICENSE_INTERFACE_CONFLICT` | -20006 | Interface InitLicense can not be used together with other license initiation interfaces. |
| `DM_LICENSE_CLIENT_DLL_MISSING` | -20007 | The license client dll is missing. |
| `DM_INSTANCE_COUNT_OVER_LIMITED` | -20008 | The number of instances used has exceeded the limit. |
| `DM_LICENSE_INIT_SEQUENCE_FAILED` | -20009 | Interface InitLicense has to be called before creating any SDK objects. |
| `DM_TRIAL_LICENSE` | -20010 | Using a trial license. |
| `DM_FAILED_TO_REACH_DLS` | -20200 | Fail to connect to Dynamsoft License Server. |
