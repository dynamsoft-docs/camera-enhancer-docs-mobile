---
layout: default-layout
title: Android HardwareUtil Class - Dynamsoft Camera Enhancer
description: This is the documentation - Android HardwareUtil Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, HardwareUtil
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android HardwareUtil Class
permalink: /programming/android/auxiliary-api/hardwareutil.html
---

# HardwareUtil

This page is for `HardwareUtil` page. `HardwareUtil` parameters are static values that illustrate device level.

```java
class com.dynamsoft.dce.HardwareUtil
```

| Attribute Name | Value |
| -------------- | ----- |
| `DEVICEINFO_UNKNOWN` | -1 |
| `DEVICE_LEVEL_HIGH` | 2 |
| `DEVICE_LEVEL_MID` | 1 |
| `DEVICE_LEVEL_LOW` | 0 |
| `DEVICE_LEVEL_UNKNOWN` | -2 |

## Device level

**Related API**

[`getDeviceLevel`]({{ site.android-api }}camera.html#getdevicelevel)

**Code Snippet**

```java
int level;
level = mCamera.getDeviceLevel();
if (level == HardwareUtil.DEVICE_LEVEL_LOW){
    mCamera.enableFrameFilter(true);
    mCamera.enableDCEAutoFocus(true);
}
```

