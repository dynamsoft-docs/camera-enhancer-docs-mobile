---
layout: default-layout
title: Android Upgrade Instructions- Dynamsoft Camera Enhancer
description: This is the documentation of Android upgrade instructionspage of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android upgrade instructions
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android API references
permalink: /programming/android/upgrade-instruction.html
---

# How to Upgrade from 2.x to 4.x

## Update License Activation Code

License activation API are removed from `DynamsoftCameraEnhancer` library. Please use the `LicenseManager` of `DynamsoftLicense` instead.

1. Include the library

   ```java
   dependencies {
       implementation 'com.dynamsoft:dynamsoftlicense:3.0.0@aar'
   }
   ```

2. Initialize the license in your code.

   ```java
   LicenseManager.initLicense(LICENSE, this, (isSuccess, error) -> {
       if (!isSuccess) {
           Log.e(TAG, "InitLicense Error: " + error);
       }
   });
   ```

## Re-write your Code Based on the API References

The APIs of `DynamsoftCameraEnhancer` are refactored. Please follow the [API reference](api-reference.md) to update your code.

### CameraEnhancer API changes

The following APIs are changed on parameters and return values:

* [`CameraEnhancer`](primary-api/camera-enhancer.html#cameraenhancer): Added parameter `CameraView cameraView`.
* [`setScanRegion`](primary-api/camera-enhancer.html#setscanregion): Changed the type of `region` from `iRegionDefinition` to [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html).
* [`getScanRegion`](primary-api/camera-enhancer.html#getscanregion): Changed the type of return value from `iRegionDefinition` to [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html).
  * `set/getScanRegionVisible`: Replaced by a series of methods in `CameraView` class.
    * `setScanRegionMaskVisible`
    * `getScanRegionMaskVisible`
    * `setScanLaserVisible`
    * `getScanLaserVisible`

### UI Configuring API changes

* `DCECameraView` is renamed to `CameraView`.
* Added a new view class `ImageEditorView`.

Read [How to configure UI](guide/ui-configurations.html) for more details about the API changes.
