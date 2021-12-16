---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android 2.x Release Notes 
description: This is the documentation - Android 2.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 2.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 2.x Release Notes
---

# Release Notes - Android 2.x

## 2.1.0 (12/15/2021)

### Highlights

- Added class scan region configuration APIs and `RegionDefinition` for users to set the region of interest. The frames will be cropped based on the scan region to accelerate the further frame processing.
- Fast mode setting parameters are opened for users to set via `updateAdvancedSettings`. The fast mode will be more flexible.

### Changelog

#### Added

- Added method [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion) and [`getScanRegion`]({{site.android-api}}camera-enhancer.html#getscanregion) to [`CameraEnhancer`]({{site.android-api}}camera-enhancer.html) class for users to set or get the region of interest. The scan region will determine how frames will be cropped.
- Added class [`RegionDefinition`]({{site.android-api-auxiliary}}region-definition.html). The class will be used to define the parameters for method [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion).
- Added method [`setScanRegionVisible`]({{site.android-api}}camera-enhancer.html#setscanregionvisible) and [`getScanRegionVisible`]({{site.android-api}}camera-enhancer.html#getscanregionvisible) to control and check the visibility of the scan region.
- Added method [`setTorchButton`]({{site.android-api-auxiliary}}dcecameraview.html#settorchbutton) to [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html) class for users to set the position of the torch button. Methods [`setTorchButtonVisible`]({{site.android-api-auxiliary}}dcecameraview.html#settorchbuttonvisible) and [`getTorchButtonVisible`]({{site.android-api-auxiliary}}dcecameraview.html#gettorchbuttonvisible) are added to set and check the visibility of the torch button.
- Extended the JSON template of [`updateAdvancedSettingsFromFile`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromfile) and [`updateAdvancedSettingsFromString`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromstring). Added fast mode configuration parameters to the template.

## 2.0.0 (10/19/2021)

### Highlights

- Simplified the usage of camera-control APIs. The new APIs are easier to use and cover more scenarios.
- Simplified the usage of camera enhancer features. Users can enable all required features via the method `enableFeatures` by inputting the combined enumeration value.
- Extended the features of `DCECameraView`. Users can add and personalize the overlays and viewfinder on the camera UI.
- Extended the features of `DCEFrame`. `DCEFrame` will store more frame information to cover more scenarios. In addition, the method `toBitmap` is added to enable users to convert `DCEFrame` to a visible image.
- The camera UI will display a fuzzified image instead of the previously captured image when the camera UI is quit and resumed.

### Changelog

#### Improved

- Updated the mechanism of the video buffer. The capability of real-time frame processing and transferring is improved.

#### Fixed

- Fixed a bug that might cause incorrect device count.

#### Breaking Change(s)

- Added method [`initLicense`]({{site.android-api}}camera-enhancer.html#initlicense) to replace `initLicenseFromDLS`.
- Upgraded the [`basic camera-control APIs`]({{site.android-api}}camera-enhancer.html#basic-camera-control-methods).
- Upgraded the usage of [`camera enhancer features`]({{site.android-api}}camera-enhancer.html#enhanced-features).
- Renamed class `CameraView` to [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html). The features of the class are extended as well.
- Renamed class `Frame` to [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html). The features of the class are extended as well.
