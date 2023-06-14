---
layout: default-layout
title: Android Upgrade Instructions * Dynamsoft Camera Enhancer
description: This is the upgrade instructions for Dynamsoft Camera Enhancer Android edition.
keywords:  Camera Enhancer, upgrade
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Upgrade Instructions
permalink: /programming/android/upgrade-instructions.html
---

# How to Upgrade to 4.x

## From Version 3.x to 4.x

### CameraEnhancer API changes

If you are using the following APIs, you have to change your code:

The parameters or return value of the following APIs are changed:

* [`CameraEnhancer`](primary-api/camera-enhancer.md#cameraenhancer): Added parameter `CameraView cameraView`.
* [`setScanRegion`](primary-api/camera-enhancer.md#setscanregion): Changed the type of `region` from `iRegionDefinition` to `DSRect`.
* [`getScanRegion`](primary-api/camera-enhancer.md#getscanregion): Changed the type of return value from `iRegionDefinition` to `DSRect`.

The following APIs are replaced by new APIs:

* `updateAdvancedSettings`: Replaced by `initSystemSettings` and `initEnhancedSettings`.
* `getMaxZoomFactor`: Replaced by getCapabilities, which returns a `Capability` class that include `maxZoomFactor` attribute.
* `enableFeatures`: Replaced by `enableEnhancedFeatures` (renamed, no change).
* `getAllResolutions`: Replaced by `getAvailableResolutions` (renamed, no change).
* `set/getScanRegionVisible`: Replaced by a series of methods in `CameraView` class.
  * `setScanRegionMaskVisible`
  * `getScanRegionMaskVisible`
  * `setScanLaserVisible`
  * `getScanLaserVisible`

Removed:

* `isFeatureEnabled`

### CameraView API changes

`DCECameraView` is renamed to `CameraView`

If you are using the following APIs, you have to change your code:

The parameters or return value of the following APIs are changed:

Removed:

* setOverlayVisible
* getOverlayVisible
* setOverlayColour
* setViewfinderVisible
* getViewfinderVisible
* setViewfinder
