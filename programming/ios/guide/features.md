---
layout: default-layout
title: Advanced Features on iOS - Dynamsoft Camera Enhancer
description: This is the documentation - Enable Advanced Features on iOS.
keywords:  Camera Enhancer, Advanced Features on iOS
needAutoGenerateSidebar: true
needGenerateH3Content: true
noTitleIndex: true
breadcrumbText: Advanced Features
permalink: /programming/ios/guide/features.html
---

# Advanced Features

On this page, you will read about how to use advanced features of Dynamsoft Camera Enhancer and how they help you on obtaining higher quality video streaming. A valid license is required when using the advanced features.

## Advanced Features Summary

All the advanced feaatures are defined in enumeration `EnumEnhancerFeatures`. Currently, they are available as follow:

| Feature | Enumeration Member (Objective-C) | Enumeration Member (Swift) | Value |
| ------- | ------ | ----- | ----- |
| [Frame Filter](#frame-filter) | `EnhancedFeatureFrameFilter` | `frameFilter` | 0x01 |
| [Sensor Control](#sensor-control) | `EnhancedFeatureSensorControl` | `sensorControl` | 0x02 |
| [Enhanced Focus](#enhanced-focus) | `EnhancedFeatureEnhancedFocus` | `enhancedFocus` | 0x04 |
| [Auto Zoom](#auto-zoom) | `EnhancedFeatureAutoZoom` | `autoZoom` | 0x10 |
| [Smart Torch](#smart-torch) | `EnhancedFeatureSmartTorch` | `smartTorch` | 0x20 |

## How to Use

- Enable: Trigger method `enableEnhancedFeatures` with the enumeration members of the features that you want to enable.
- Disable: Trigger method `disableEnhancedFeatures` with the enumeration members of the features that you want to disable.

Sample code:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
// To enable features
[_dce enableEnhancedFeatures:EnhancedFeatureFrameFilter | EnhancedFeatureSensorControl error: &error];
// To disable features
[_dce disableEnhancedFeatures:EnhancedFeatureFrameFilter | EnhancedFeatureSensorControl];
```
2. 
```swift
// To enable features
dce.enableEnhancedFeatures(EnumEnhancerFeatures.frameFilter.rawValue | EnumEnhancerFeatures.sensorControl.rawValue, error: &error)
// To disable features
dce.disableEnhancedFeatures(EnumEnhancerFeatures.frameFilter.rawValue | EnumEnhancerFeatures.sensorControl.rawValue)
```

- You can enable or disable multiple features at one time.
- When an enabled feature is enabled again, it remains enabled.
- When a feature is disabled more than once, it remains disabled.

## Advanced Features Details

### Frame Filter

All the frames in the video streaming are quickly evaluated and the majority of the blurry frames will be filtered out. You can enable this feature when your mobile device is always moving. The average time consumption on evaluating each video frame is less than 10ms.

### Sensor Control

The mobile sensor can help on filtering out all the frames that are produced when the device is shaking. It will get better effects when enabled together with **Frame Filter**.

### Enhanced Focus

This feature can assist the camera in its focus. It is recommended to be enabled on low-end devices.

### Auto Zoom

**Auto Zoom** feature is specially designed for decoding barcodes from long distances. The camera will zoom in automatically to enlarge the region of interest when a barcode is detected far away. The **Auto Zoom** feature might not work ideally when processing the documents or the text areas. Please disable this feature if the targets are not barcodes.

### Smart Torch

**Smart Torch** feature controls the visibility of the torch button created by `setTorchButton` method. The torch button will be displayed automatically when the environment light level is low. Otherwise, the torch button is hidden. The feature doesn't control the status of the mobile torch. Users have to click on the torch button to turn on the torch.
