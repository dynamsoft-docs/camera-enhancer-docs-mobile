---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS 2.x Release Notes 
description: This is the documentation - iOS 2.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS 2.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS 2.x Release Notes
---

# Release Notes - iOS 2.x

## 2.0.0 (10/19/2021)

### Highlights

- Simplified the usage of camera-control APIs. The new APIs are easier to use and covers more scenarios.
- Simplified the usage of camera enhancer features. Users can enable all required features via the method `enableFeatures` by inputting the combined enumeration value.
- Extended the features of `DCECameraView`. Users can add and personalize the overlays and viewfinder on the camera UI.
- Extended the features of `DCEFrame`. `DCEFrame` will store more frame information to cover more scenarios. In addition, the method `toBitmap` is added to enable users to convert `DCEFrame` to a visible image.

### Changelog

#### Improved

- Updated the mechanism of the video buffer. The capability of real-time frame processing and transferring is improved.

#### Breaking Change(s)

- Added method [`initLicense`]({{site.iOS-api}}index.html#initlicense) to replace `initLicenseFromDLS`.
- Upgraded the [`basic camera-control APIs`]({{site.iOS-api}}index.html#basic-Camera-control-methods).
- Upgraded the usage of [`camera enhancer features`]({{site.iOS-api}}index.html#enhanced-features).
- Renamed class `CameraView` to [`DCECameraView`]({{site.iOS-api-auxiliary}}dcecameraview.html). The features of the class are extended as well.
- Renamed class `Frame` to [`DCEFrame`]({{site.iOS-api-auxiliary}}dceframe.html). The features of the class are extended as well.
