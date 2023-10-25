---
layout: default-layout
title: Set a Scan Region - Exploring Features of Dynamsoft Camera Enhancer iOS Edition.
description: This page introduce how to set a scan region with Dynamsoft Camera Enhancer iOS Edition.
keywords:  Camera Enhancer, scan region
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Set ScanRegion
permalink: /programming/ios/guide/scan-region.html
---

# How to Set a Scan Region

## Set a Scan Region

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSRect *scanRegion = [[DSRect alloc] init];
scanRegion.top = 0.3;
scanRegion.bottom = 0.7;
scanRegion.left = 0.15;
scanRegion.right = 0.85;
scanRegion.measuredInPercentage = true;
[self.dce setScanRegion:scanRegion error:&error];
```
2. 
```swift
let scanRegion = Rect.init()
scanRegion.top = 0.3
scanRegion.bottom = 0.7
scanRegion.left = 0.15
scanRegion.right = 0.85
scanRegion.measuredInPercentage = true
try? dce.setScanRegion(scanRegion)
```

## Add Scan Region Mask & Scan Laser on Camera View

Use the following code to set scan region mask and scan laser.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[self.cameraView setScanRegionMaskVisible:true];
[self.cameraView setScanLaserVisible:true];
UIColor *strokeColor = [[UIColor alloc] initWithRed:255 green:167 blue:0 alpha:1];
UIColor *surroundingColor = [[UIColor alloc] initWithRed:0 green:0 blue:0 alpha:0.1];
[self.cameraView setScanRegionMaskStyle:strokeColor strokeWidth:1 surroundingColour:surroundingColor];
```
2. 
```swift
cameraView.scanRegionMaskVisible = true
cameraView.scanLaserVisible = true
cameraView.setScanRegionMaskStyle(UIColor.init(red: 255, green: 167, blue: 0, alpha: 1), strokeWidth: 1, surroundingColour: UIColor.init(red: 0, green: 0, blue: 0, alpha: 0.1))
```

## Configure your own Scan Region UI

You can either use the CameraView to create the scan region UI or draw it youself.

Since the scan region is set for the video streaming, its coordinate system might not be the same with the view coordinate system. You can use the following code to get the scan region Rect under the view coordinate system:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
CGRect rect = [self.dce convertRectToViewCoordinates:scanRegion];
```
2. 
```swift
let rect:CGRect = dce.convertRectToViewCoordinates(scanRegion)
```

You can disable the default scan region UI with the following code:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[self.cameraView setScanRegionMaskVisible:false];
[self.cameraView setScanLaserVisible:false];
```
2. 
```swift
cameraView.scanRegionMaskVisible = false
cameraView.scanLaserVisible = false
```
