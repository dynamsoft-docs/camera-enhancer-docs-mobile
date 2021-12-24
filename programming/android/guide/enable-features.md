---
layout: default-layout
title: Dynamsoft Camera Enhancer - Enable Features on Android
description: This is the documentation - Enable Dynamsoft Camera Enhancer Features on Android.
keywords:  Camera Enhancer, Enable Features on Android
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Enable Features
---

# Enable Dynamsoft Camera Enhancer Features

In addition to the basic camera control APIs, Dynamsoft Camera Enhancer (DCE) have some features that need a valid license to drive. DCE features include:

- Frame Filter: Filter out blurry frames.
- Sensor Control: Discard all the frames when device is shaking.
- Enhanced Focus: Enhanced the camera focus ability (recommended on low-end devices).
- Fast Mode: Crop the frames into different small size.
- Auto Zoom: Auto zoom to approach the region of interest.
- Smart Torch: Show/hide a torch button when environment light level is low/high.

## How to Enable DCE Features

`enableFeatures` and `disableFeatures` is the method designed for controlling DCE features. The required parameter of the method is a combined value of `EnumEnhancerFeatures` members. Currently, the members of `EnumEnhancerFeatures` are available as follow:

| Member | Value |
| ------ | ----- |
| `EF_FRAME_FILTER` | 0x01 |
| `EF_SENSOR_CONTROL` | 0x02 |
| `EF_ENHANCED_FOCUS` | 0x04 |
| `EF_FAST_MODE` | 0x08 |
| `EF_AUTO_ZOOM` | 0x10 |
| `EF_SMART_TORCH` | 0x20 |
| `EF_ALL` | 0x3f |

Sample code:

```java
// To enable features
mCameraEnhancer.enableFeatures(EnumEnhancerFeatures.EF_FRAME_FILTER | EnumEnhancerFeatures.EF_AUTO_ZOOM);
// To disable features
mCameraEnhancer.disableFeatures(EnumEnhancerFeatures.EF_FRAME_FILTER | EnumEnhancerFeatures.EF_AUTO_ZOOM);
```

- You can enable or disable multiple features at one time.
- When a enabled feature is enabled again , it remains enabled.
- When a feature is disabled more than once, it remains disabled.
