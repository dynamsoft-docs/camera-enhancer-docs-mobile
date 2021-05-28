---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android HardwareUtil Class
description: This is the documentation - Android HardwareUtil Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, HardwareUtil
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android HardwareUtil
---

# HardwareUtil

This page is for `HardwareUtil` page. `HardwareUtil` parameters are static values that illustrate device level.

## Method

| Name | Value |
|------|------|
| `DEVICEINFO_UNKNOWN` | -1 |
| `DEVICE_LEVEL_HIGH` | 2 |
| `DEVICE_LEVEL_MID` | 1 |
| `DEVICE_LEVEL_LOW` | 0 |
| `DEVICE_LEVEL_UNKNOWN` | -1 |

### Device level

```java
int level;
level = mCamera.getDeviceLevel();
if (level == HardwareUtil.DEVICE_LEVEL_LOW){
    mCamera.enableFrameFilter(true);
    mCamera.enableDCEAutoFocus(true);
}
```
