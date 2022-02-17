---
layout: default-layout
title: Dynamsoft Camera Enhancer - Enable Features on iOS
description: This is the documentation - Enable Dynamsoft Camera Enhancer Features on iOS.
keywords:  Camera Enhancer, Enable Features on iOS
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Enable Features
---

# Enable Dynamsoft Camera Enhancer Features

DCE features can promote the quality of video streaming to improve the efficiency of image processing.

On this page, you will read:

- All available features of Dynamsoft Camera Enhancer.
- How to use these features.

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

## How to Enable DCE Features

`enableFeatures` and `disableFeatures` is the method designed for controlling DCE features. The required parameter of the method is a combined value of `EnumEnhancerFeatures` members. Currently, the members of `EnumEnhancerFeatures` are available as follow:

| Member | Value |
| ------ | ----- |
| `EnumFRAME_FILTER` | 0x01 |
| `EnumSENSOR_CONTROL` | 0x02 |
| `EnumENHANCED_FOCUS` | 0x04 |
| `EnumFAST_MODE` | 0x08 |
| `EnumAUTO_ZOOM` | 0x10 |
| `EnumSMART_TORCH` | 0x20 |
| `EnumALL` | 0x3f |

Sample code:

```objc
// To enable features
[_dce enableFeatures:EnumEnhancerFeatures.EnumFRAME_FILTER | EnumEnhancerFeatures.EnumSENSOR_CONTROL error: &error];
// To disable features
[_dce disableFeatures:EnumEnhancerFeatures.EnumFRAME_FILTER | EnumEnhancerFeatures.EnumSENSOR_CONTROL];
```

```swift
// To enable features
dce.enableFeatures(EnumEnhancerFeatures.EnumFRAME_FILTER | EnumEnhancerFeatures.EnumSENSOR_CONTROL, error: &error)
// To disable features
dce.disableFeatures(EnumEnhancerFeatures.EnumFRAME_FILTER | EnumEnhancerFeatures.EnumSENSOR_CONTROL)
```

- An valid license is required to enable these features.
- You can enable or disable multiple features at one time.
- When an enabled feature is enabled again, it remains enabled.
- When a feature is disabled more than once, it remains disabled.
