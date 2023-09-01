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

## From Version 2.x to 4.x

### CameraEnhancer API changes

The following APIs are changed on parameters and return values:

* [`CameraEnhancer`](primary-api/camera-enhancer.html#cameraenhancer): Added parameter `CameraView cameraView`.
* [`setScanRegion`](primary-api/camera-enhancer.html#setscanregion): Changed the type of `region` from `iRegionDefinition` to `DSRect`.
* [`getScanRegion`](primary-api/camera-enhancer.html#getscanregion): Changed the type of return value from `iRegionDefinition` to `DSRect`.

The following APIs are replaced by new APIs:

* `updateAdvancedSettings`: Replaced by `initSystemSettings` and `initEnhancedSettings`.
* `getMaxZoomFactor`: Replaced by getCapabilities, which returns a `Capability` class that include `maxZoomFactor` attribute.
* `enableFeatures`: Replaced by `enableEnhancedFeatures` (renamed, no other change).
* `getAllResolutions`: Replaced by `getAvailableResolutions` (renamed, no other change).
* `set/getScanRegionVisible`: Replaced by a series of methods in `CameraView` class.
  * `setScanRegionMaskVisible`
  * `getScanRegionMaskVisible`
  * `setScanLaserVisible`
  * `getScanLaserVisible`

Removed:

* `isFeatureEnabled`

### CameraView API changes

`DCECameraView` is renamed to `CameraView`. The constructor is renamed to `CameraView()`.

The following APIs are replaced with new UI configuration APIs. Read [How to draw graphics on the views](guide/add-drawing-item.html) for more details.

* `setOverlayVisible`
* `getOverlayVisible`
* `setOverlayColour`
* `setViewfinderVisible`
* `getViewfinderVisible`
* `setViewfinder`

### Other Changes

Removed

* `RegionDefinition`: Replaced by `DSRect`
* `DCEFrame`: Replaced by `ImageData`. The auxiliary attributes are stored in `VideoFrameTag` of `ImageData`.
* `DCEFeedback`: Replaced by `Feedback` (renamed, no other change).
* `DCEFrameListener`: Replaced by `VideoFrameListener` (renamed, no other change).
* `DCECameraStateListener`: Replaced by `CameraStateListener` (renamed, no other change).
* `DCEPhotoListener`: Replaced by `CameraStateListener` (renamed, no other change).
* `DCELicenseVerificationListener`: Replaced by `LicenseVerficationListener` in `LicenseUtility` class.
