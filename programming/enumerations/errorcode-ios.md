---
layout: default-layout
title: Dynamsoft Camera Enhancer - Enumerations Error code
description: This is the documentation - Enumerations Error code page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Error code
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Error code
---

# Enumerations Error code

The error code returned by the library.

| Error Code | Value | Description |
|------------------|-------|-------------|
| `EnumCameraErrorCode_OK`  | 0 | Successful. |
| `EnumCameraErrorCode_UNKNOWN` | -10000 | Unknown error. |
| `EnumCameraErrorCode_LICENSE_INVALID` | -10001 | The licence is invalid. |
| `EnumCameraErrorCode_LICENSE_EXPIRED` | -10002 | The licence has expired. |
| `EnumCameraErrorCode_CAMERA_MODULE_NOT_EXIST` | -10003 | Camera module does not exist. |
| `EnumCameraErrorCode_FILE_NOT_FOUND` | -10004 | Failed to access the fail path. |
| `EnumCameraErrorCode_JSON_PARSE_FAILED` | -10005 | Failed to parse the JSON data. |
| `EnumCameraErrorCode_CAMERA_ID_NOT_EXIST` | -10006 | The input value does not exist in the camera ID list. |
| `EnumCameraErrorCode_PARAMETER_VALUE_INVALID` | -10038 | The input parameter is invalid. |
| `EnumCameraErrorCode_LICENSEKEY_NOT_MATCHED` | -10043 | The license key does not match the license content. |
| `EnumCameraErrorCode_REQUESTED_FAILED` | -10044 | The license key does not match the license content. |
| `EnumCameraErrorCode_NO_SENSOR` | -10045 | The mobile sensor is not available. |
| `EnumCameraErrorCode_NO_LICENSE` | -20000 | There is no license specified. |
| `EnumCameraErrorCode_HANDSHAKE_CODE_INVALID` | -20001 | Handshake code is invalid. |
| `EnumCameraErrorCode_LICENSE_BUFFER_FAILED` | -20002 | Failed to read or write license buffer. |
| `EnumCameraErrorCode_LICENSE_SYNC_FAILED` | -20003 | Failed to synchronize license info with Dynamsoft License Server. |
| `EnumCameraErrorCode_DEVICE_NOT_MATCH` | -20004 | Device does not match with license buffer. |
| `EnumCameraErrorCode_BIND_DEVICE_FAILED` | -20005 | Failed to bind device. |
| `EnumCameraErrorCode_LICENSE_INTERFACE_CONFLICT` | -20006 | Interface InitLicense can not be used together with other license initiation interfaces. |
| `EnumCameraErrorCode_LICENSE_CLIENT_DLL_MISSING` | -20007 | The license client dll is missing. |
| `EnumCameraErrorCode_INSTANCE_COUNT_OVER_LIMITED` | -20008 | The number of instances used has exceeded the limit. |
| `EnumCameraErrorCode_LICENSE_INIT_SEQUENCE_FAILED` | -20009 | Interface InitLicense has to be called before creating any SDK objects. |
| `EnumCameraErrorCode_TRIAL_LICENSE` | -20010 | Using a trial license. |
| `EnumCameraErrorCode_FAILED_TO_REACH_DLS` | -20200 | Fail to connect to Dynamsoft License Server. |
