---
layout: default-layout
title: Dynamsoft Camera Enhancer - Release Note
description: This is the documentation - Release Note page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Release Note
needAutoGenerateSidebar: true
needGenerateH3Content: false
noTitleIndex: true
breadcrumbText: Release Note
---

# Release Notes

## 2.1.0 (12/xx/2021)

### Highlights

- Added class scan region configuration APIs and `RegionDefinition` for users to set the region of interest. The frames will be cropped based on the scan region to accelerate the further frame processing.
- APIs are added to `DCECameraView` class to control whether and where to display a torch button.
- Fast mode setting parameters are opened for users to set via `updateAdvancedSettings`. The fast mode will be more flexible.

### Editions

| -- | -- | -- |
| [JavaScript]({{ site.js-rn }}release-notes-2.x.html#210-12xx2021) | [Android]({{ site.android-release-note }}release-notes-2.x.html#210-12xx2021) | [iOS]({{ site.ios-release-note }}release-notes-2.x.html#210-12xx2021) |

## 2.0.0 (10/19/2021)

### Highlights

- Simplified the usage of camera-control APIs. The new APIs are easier to use and covers more scenarios.
- Simplified the usage of camera enhancer features. Users can enable all required features via the method `enableFeatures` by inputting the combined enumeration value.
- Extended the features of `DCECameraView`. Users can add and personalize the overlays and viewfinder on the camera UI.
- Extended the features of `DCEFrame`. `DCEFrame` will store more frame information to cover more scenarios. In addition, the method `toBitmap/toUIImage` is added to enable users to convert `DCEFrame` to a system built-in image object.

### Editions

| -- | -- | -- |
| [JavaScript]({{ site.js-rn }}release-notes-2.x.html#200-10202021) | [Android]({{ site.android-release-note }}release-notes-2.x.html#200-10192021) | [iOS]({{ site.ios-release-note }}release-notes-2.x.html#200-10192021) |

## 1.0.3 (07/20/2021)

### Highlights

- Updated the names of license activation APIs.

| -- | -- |
| [Android]({{ site.android-release-note }}release-notes-1.x.html#103-07202021) | [iOS]({{ site.ios-release-note }}release-notes-1.x.html#103-07202021) |

## 1.0.1 (06/10/2021)

### Highlights

- Added a new property `products` in `DMLTSConnectionParameters`.
- Added a new enumeration `EnumProduct`.

| -- | -- |
| [Android]({{ site.android-release-note }}release-notes-1.x.html#101-06102021) | [iOS]({{ site.ios-release-note }}release-notes-1.x.html#101-06102021) |

## 1.0.0 (04/29/2021)

### Highlights

- Dynamsoft Camera Enhancer is released. The following features are available:
  - Video Buffer
  - Frame Filter
  - Fast Mode
  - Auto-Zoom
  - Enhanced-Focus

| -- | -- |
| [Android]({{ site.android-release-note }}release-notes-1.x.html#100-04292021) | [iOS]({{ site.ios-release-note }}release-notes-1.x.html#100-04292021) |
