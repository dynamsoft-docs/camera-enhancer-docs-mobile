---
layout: default-layout
title: Enable Features on Android - Dynamsoft Camera Enhancer
description: This is the documentation - Enable Dynamsoft Camera Enhancer Features on Android.
keywords:  Camera Enhancer, Enable Features on Android
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Enable Features
---

# Enable Dynamsoft Camera Enhancer Features

On this page, you will read about how to use advanced features of Dynamsoft Camera Enhancer and how they help you on obtaining higher quality video streaming. A valid license is required when using the advanced features.

## Advanced Features Summary

All the advanced feaatures are defined in enumeration `EnumEnhancerFeatures`. Currently, they are available as follow:

| Feature | Enumeration Member | Value |
| ------- | ------ | ----- |
| [Frame Filter](#frame-filter) | `EnumFRAME_FILTER` | 0x01 |
| [Sensor Control](#sensor-control) | `EnumSENSOR_CONTROL` | 0x02 |
| [Enhanced Focus](#enhanced-focus) | `EnumENHANCED_FOCUS` | 0x04 |
| [Fast Mode](#fast-mode) | `EnumFAST_MODE` | 0x08 |
| [Auto Zoom](#auto-zoom) | `EnumAUTO_ZOOM` | 0x10 |
| [Smart Torch](#smart-torch) | `EnumSMART_TORCH` | 0x20 |

## How to Use

- Enable: Trigger method `enableFeatures` with the enumeration members of the features that you want to enable.
- Disable: Trigger method `disableFeatures` with the enumeration members of the features that you want to disable.
- Check status: Trigger method `isFeatureEnabled` with the enumeration members of the features that you want to check.

Sample code:

```java
// To enable features
mCameraEnhancer.enableFeatures(EnumEnhancerFeatures.EF_FRAME_FILTER | EnumEnhancerFeatures.EF_AUTO_ZOOM);
// To disable features
mCameraEnhancer.disableFeatures(EnumEnhancerFeatures.EF_FRAME_FILTER | EnumEnhancerFeatures.EF_AUTO_ZOOM);
```

- You can enable or disable multiple features at one time.
- When an enabled feature is enabled again, it remains enabled.
- When a feature is disabled more than once, it remains disabled.

## Frame Filter

All the frames in the video streaming are quickly evaluated and the majority of the blurry frames will be filtered out. You can enable this feature when your mobile device is always moving. The average time consumption on evaluating each video frame is less than 10ms.

## Sensor Control

The mobile sensor can help on filtering out all the frames that are produced when the device is shaking. It will get better effects when enabled together with **Frame Filter**.

## Enhanced Focus

This feature can assist the camera in its focus. It is recommended to be enabled on low-end devices.

## Fast Mode

The video frames are cropped into small sizes when the **Fast Mode** is enabled. The feature will sharply improve the processing efficiency When the targeting areas are always located in the middle of the video. The average time consumption on cropping each frame is less than 10ms.

## Auto Zoom

**Auto Zoom** feature is specially designed for decoding barcodes from long distances. The camera will zoom in automatically to enlarge the region of interest when a barcode is detected far away. The **Auto Zoom** feature might not work ideally when processing the documents or the text areas. Please disable this feature if the targets are not barcodes.

## Smart Torch

**Smart Torch** feature controls the visibility of the torch button created by `setTorchButton` method. The torch button will be displayed automatically when the environment light level is low. Otherwise, the torch button is hidden. The feature doesn't control the status of the mobile torch. Users have to click on the torch button to turn on the torch.
