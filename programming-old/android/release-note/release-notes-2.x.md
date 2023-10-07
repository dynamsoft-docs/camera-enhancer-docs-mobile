---
layout: default-layout
title: Android 2.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - Android 2.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 2.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 2.x Release Notes
permalink: /programming/android/release-note/release-notes-2.x.html
---

# Release Notes - Android 2.x

## 2.3.11 (02/14/2023)

### Fixed

- Fixed a crash bug on the devices that do not support 16:9 size resolution.

## 2.3.10 (12/13/2022)

### New

- Override method [`setFocus`](../primary-api/camera-enhancer.html#setfocussubsequentfocusmode) in `CameraEnhancer` class for users to specify the subsequent focus mode after triggering a focus. Enumeration [`EnumFocusMode`]({{ site.dce-enums }}focus-mode.html?lang=android) is added to specify the focus mode.
- Added a new method [`setAutoZoomRange`](../primary-api/camera-enhancer.html#setautozoomrange) in `CameraEnhancer` for users to specify a range for the auto-zoom feature of the library.
- Added an interface [`DCECameraStateListener`](../auxiliary-api/interface-dcecamerastatelistener.html) to receive a callback when the camera state changes. You can add the protocol via a new method [`setCameraStateListener`](../primary-api/camera-enhancer.html#setcamerastatelistener).
- Added a new method [`getVisibleRegionOfVideo`](../auxiliary-api/dcecameraview.html#getvisibleregionofvideo) in `DCECameraView` class

### Deprecated

- Deprecated method `pause` and `resume` in `CameraEnhancer` class.

### Fixed

- Fixed a bug that might cause thread blocking when using an offline license.
- Fixed a bug that UI might be blocked when the screen is locked and reopened.
- Fixed a bug that might cause memory churn when the instance/thread was created frequently.

## 2.3.5 (11/04/2022)

- Fixed a bug that might throws exception when triggering `CameraEnhancer.close` after triggering `CameraEnhancer.pause`.

## 2.3.4 (09/22/2022)

- Fixed a bug that camera might not be opened after camera permission is allowed.

## 2.3.3 (08/18/2022)

### Fixed

- Fixed a bug that might cause camera crash when the `DCECameraView` is quit without destroying.

- Fixed a deformation bug of `DCECameraView` when the screen rotated.

## 2.3.2 (08/02/2022)

### New

- Added methods [`selectCamera(EnumCameraPosition)`](../primary-api/camera-enhancer.html#selectcameraenumcameraposition) and [`getCameraPosition`](../primary-api/camera-enhancer.html#getcameraposition) for users to switch between the front-facing camera and the back-facing camera.
- Added enumeration [`EnumCameraPosition`]({{ site.dce-enums }}camera-position.html?lang=android).

### Fixed

- Fixed a null pointer bug that might occur when rotating the `DCECameraView`.
- Fixed a crash bug when some methods are called in child thread.

## 2.3.0 (06/28/2022)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.3.0.md -%}

<div class="fold-panel-end"></div>

### Changelog

- Added the following APIs for capturing photos:
  - [`DCEPhotoListener`]({{site.android-api-auxiliary}}interface-dcephotolistener.html): The interface that includes method [`photoOutputCallback`]({{site.android-api-auxiliary}}interface-dcephotolistener.html#photooutputcallback) which is triggered when a photo is captured. JPEG-encoded photo can be received via the method [`photoOutputCallback`]({{site.android-api-auxiliary}}interface-dcephotolistener.html#photooutputcallback).
  - [`takePhoto`]({{site.android-api}}camera-enhancer.html#takephoto): Triggers photo capturing.
- Added a new class [`DCEFeedback`]({{site.android-api-auxiliary}}dcefeedback.html). The following APIs are available in the class:
  - [`vibrate`]({{site.android-api-auxiliary}}dcefeedback.html#vibrate): Triggers a vibration.
  - [`Beep`]({{site.android-api-auxiliary}}dcefeedback.html#beep): Triggers a beep sound.
- Added a new method [`getMaxZoomFactor`]({{site.android-api}}camera-enhancer.html#getmaxzoomfactor) which returns the maximum available zoom factor of the device.

## 2.1.4 (05/26/2022)

### New

- Added support for [ISO and exposure time settings]({{ site.reference }}).

### Fixed

- Fixed the memory leaks caused by the misuse of the Context instance.
- Fixed a bug where some delay might happen in initiating licenses when using along with Dynamsoft Barcode Reader Mobile Edition.

### Deprecated

- `CameraEnhancer.setFrameRate`

## 2.1.3 (03/02/2022)

### Fixed

- Fixed a bug that might cause a crash on Android emulator when used together with `DynamsoftBarcodeReader`.

## 2.1.1 (12/28/2021)

### New

- Added a new feature `SMART_TORCH`. Users can enable this feature via the method [`enableFeatures`]({{site.android-api}}camera-enhancer.html#enablefeatures) by specifying `EF_SMART_TORCH`. When `SMART_TORCH` is enabled, a torch button will be displayed automatically when the environment light level is low. Users can click on the torch button to turn on/off the torchlight.
- Overwrite `DCECameraView` method [`setTorchButton`]({{site.android-api-auxiliary}}dcecameraview.html#settorchbutton). Users can set the position, size and image of the torch button. The previous `setTorchButton` method is deprecated.

### Fixed

- Fixed a bug that might affect the processing speed.
- Fixed a bug that `enableFeatures` might not have effects.

## 2.1.0 (12/16/2021)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.1.0.md -%}

<div class="fold-panel-end"></div>

### Changelog

#### Added

- Added method [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion) and [`getScanRegion`]({{site.android-api}}camera-enhancer.html#getscanregion) to [`CameraEnhancer`]({{site.android-api}}camera-enhancer.html) class for users to set or get the region of interest. The scan region will determine how frames will be cropped.
- Added class [`RegionDefinition`]({{site.android-api-auxiliary}}region-definition.html). The class will be used to define the parameters for method [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion).
- Added method [`setScanRegionVisible`]({{site.android-api}}camera-enhancer.html#setscanregionvisible) and [`getScanRegionVisible`]({{site.android-api}}camera-enhancer.html#getscanregionvisible) to control and check the visibility of the scan region.
- Added method [`setTorchButton`]({{site.android-api-auxiliary}}dcecameraview.html#settorchbutton) to [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html) class for users to set the position of the torch button. Methods [`setTorchButtonVisible`]({{site.android-api-auxiliary}}dcecameraview.html#settorchbuttonvisible) and [`getTorchButtonVisible`]({{site.android-api-auxiliary}}dcecameraview.html#gettorchbuttonvisible) are added to set and check the visibility of the torch button.
- Extended the JSON template of [`updateAdvancedSettingsFromFile`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromfile) and [`updateAdvancedSettingsFromString`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromstring). Added fast mode configuration parameters to the template.

## 2.0.0 (10/19/2021)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.0.0.md -%}

<div class="fold-panel-end"></div>

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
