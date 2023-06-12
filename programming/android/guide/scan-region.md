---
layout: default-layout
title: Set a Scan Region - Exploring Features of Dynamsoft Camera Enhancer Android Edition.
description: This page introduce how to set a scan region with Dynamsoft Camera Enhancer Android Edition.
keywords:  Camera Enhancer, Customize Camera Settings
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Set a Scan Region
permalink: /programming/android/guide/scan-region.html
---

# How to Set a Scan Region

## Set a Scan Region

```java
DSRect region = new DSRect();
region.left = 15;
region.right = 85;
region.top = 30;
region.bottom = 70;
region.isMeasuredInPercentage = true;
try {
    mCameraEnhancer.setScanRegion(region);
} catch (CameraEnhancerException e) {
    e.printStackTrace();
}
```

## Add Scan Region Mask & Scan Laser on Camera View

Use the following code to set scan region mask and scan laser.

```java
cameraView.setScanRegionMaskVisible(true);
cameraView.setScanLaserVisible(true);
cameraView.setScanRegionMaskStyle(R.color.scan_region_stroke, R.color.scan_region_mask, 1f);
```

Remember to add your colours in your **res/values/color.xml** file.

```xml
<resources>
    <color name="scan_region_stroke">#49F549</color>
    <color name="scan_region_mask">#49F5494d</color>
</resources>
```

## Configure your own Scan Region UI

You can either use the CameraView to create the scan region UI or draw it youself.

Since the scan region is set for the video streaming, its coordinate system might not be the same with the view coordinate system. You can use the following code to get the scan region Rect under the view coordinate system:

```java
DSRect region = new DSRect();
region.left = 15;
region.right = 85;
region.top = 30;
region.bottom = 70;
region.isMeasuredInPercentage = true;
try {
    mCameraEnhancer.setScanRegion(region);
} catch (CameraEnhancerException e) {
    e.printStackTrace();
}
// Use mScanRegionRect to set your own scan region UI.
android.graphics.Rect mScanRegionRect = cameraView.convertRectToViewCoordinates(DSRect);
```

You can disable the default scan region UI with the following code:

```java
cameraView.setScanRegionMaskVisible(false);
cameraView.setScanLaserVisible(false);
```
