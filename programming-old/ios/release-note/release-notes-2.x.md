---
layout: default-layout
title: iOS 2.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - iOS 2.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS 2.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS 2.x Release Notes
permalink: /programming/ios/release-note/release-notes-2.x.html
---

# Release Notes - iOS 2.x

## 2.3.20 (03/27/2023)

### Fixed

- Fixed a bug that might cause thread blocking on the simulator.

## 2.3.12 (03/16/2023)

### Fixed

- Fixed a display bug when the display orientation is landscape.

## 2.3.11 (01/10/2023)

### Fixed

- Fixed a bug that the **scan region** is not removed from `DCECameraView` when it is canceled.

## 2.3.10 (12/13/2022)

### New

- Override method [`setFocus`](../primary-api/camera-enhancer.html#setfocussubsequentfocusmode) in `CameraEnhancer` class for users to specify the subsequent focus mode after triggering a focus. Enumeration [`EnumFocusMode`]({{ site.dce-enums }}focus-mode.html?lang=objc,swift) is added to specify the focus mode.
- Added a new method [`setAutoZoomRange`](../primary-api/camera-enhancer.html#setautozoomrange) in `CameraEnhancer` for users to specify a range for the auto-zoom feature of the library.
- Added a protocol [`DCECameraStateListener`](../auxiliary-api/protocol-dcecamerastatelistener.html) to receive a callback when the camera state changes. You can add the protocol via a new method [`setCameraStateListener`](../primary-api/camera-enhancer.html#setcamerastatelistener).
- Added a new method [`getVisibleRegionOfVideo`](../auxiliary-api/dcecameraview.html#getvisibleregionofvideo) in `DCECameraView` class

### Fix

- Fixed a bug that might be caused by thread blocking when using an offline license.

### Deprecated

- Deprecated method `pause` and `resume` in `CameraEnhancer` class.

## 2.3.5 (11/15/2022)

### Fixed

- Fixed a bug that `torchButton` was not clickable when it appeared outside `scanRegion`.

## 2.3.4 (11/04/2022)

### Fixed

- Fixed a scan region deviation bug.
- Fixed an overlay offset bug when `DCECamearView` is smaller than the screen size.
- Fixed a bug that might cause high CPU occupancy when the camera is opened.

## 2.3.3 (09/22/2022)

### Changed

- The `video buffer` will be cleared when camera is paused or closed.

### Fixed

- Fixed a bug that `scanRegion` is not correctly set when device was rotated horizontally.

## 2.3.2 (08/02/2022)

### New

- Added a property [`cameraView`](../primary-api/camera-enhancer.html#cameraview) for users to bind a `DCECameraView` object to the `DynamsoftCameraEnhancer` object.
- Added methods [`selectCameraWithPosition`](../primary-api/camera-enhancer.html#selectcamerawithposition) and [`getCameraPosition`](../primary-api/camera-enhancer.html#getcameraposition) for users to switch between the front-facing camera and the back-facing camera.
- Added enumeration [`EnumCameraPosition`]({{ site.dce-enums }}camera-position.html?lang=objc,swift).

### Changed

- Changed the rotation control of `DCECameraView` from manual handling to system handling.

## 2.3.1 (07/11/2022)

### Fixed

- Added x86_64 architecture back to the framework which was missing in 2.3.0.

## 2.3.0 (06/28/2022)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.3.0.html -%}

<div class="fold-panel-end"></div>

### Changelog

- Added the following APIs for capturing photos:
  - [`DCEPhotoListener`]({{site.ios-api-auxiliary}}protocol-dcephotolistener.html): The protocol that includes method [`photoOutputCallback`]({{site.ios-api-auxiliary}}protocol-dcephotolistener.html#photooutputcallback) which is triggered when a photo is captured. JPEG-encoded photo can be received via the method [`photoOutputCallback`]({{site.ios-api-auxiliary}}protocol-dcephotolistener.html#photooutputcallback).
  - [`takePhoto`]({{site.ios-api}}camera-enhancer.html#takephoto): Triggers photo capturing.
- Added a new class [`DCEFeedback`]({{site.ios-api-auxiliary}}dcefeedback.html). The following APIs are available in the class:
  - [`vibrate`]({{site.ios-api-auxiliary}}dcefeedback.html#vibrate): Triggers a vibration.
  - [`Beep`]({{site.ios-api-auxiliary}}dcefeedback.html#beep): Triggers a beep sound.
- Added a new method [`getMaxZoomFactor`]({{site.ios-api}}camera-enhancer.html#getmaxzoomfactor) which returns the maximum available zoom factor of the device.

## 2.1.4 (05/26/2022)

### New

- Added support for [ISO and exposure time settings]({{ site.reference }}).

### Fixed

- Fixed the memory leaks caused by incorrectly destroying NSTimer instances.
- Fixed a bug where some delay might happen in initiating licenses when using along with Dynamsoft Barcode Reader Mobile Edition.

### Deprecated

- `CameraEnhancer.setFrameRate`
- `EnumResolution.EnumResolution_HIGH`
- `EnumResolution.EnumResolution_MID`
- `EnumResolution.EnumResolution_LOW`

## 2.1.3 (03/02/2022)

### Fixed

- Fixed a bug that might offset the position of highlight overlays on the decoded barcodes when used together with `DynamsoftBarcodeReader`.

## 2.1.1 (12/28/2021)

### New

- Added a new feature `SMART_TORCH`. Users can enable this feature via the method [`enableFeatures`]({{site.ios-api}}camera-enhancer.html#enablefeatures) by specifying `EnumSMART_TORCH`. When `SMART_TORCH` is enabled, a torch button will be displayed automatically when the environment light level is low. Users can click on the torch button to turn on/off the torchlight.
- Overwrite `DCECameraView` method [`setTorchButton`]({{site.ios-api-auxiliary}}dcecameraview.html#settorchbutton). Users can set the position, size and image of the torch button. The previous `setTorchButton` method is deprecated.

### Fixed

- Fixed a bug that might affect the processing speed.
- Fixed a bug that `enableFeatures` might not have effects.

## 2.1.0 (12/16/2021)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.1.0.html -%}

<div class="fold-panel-end"></div>

### Changelog

#### New

- Added method [`setScanRegion`]({{site.ios-api}}camera-enhancer.html#setscanregion) and [`getScanRegion`]({{site.ios-api}}camera-enhancer.html#getscanregion) to [`CameraEnhancer`]({{site.ios-api}}camera-enhancer.html) class for users to set or get the region of interest. The scan region will determine how frames will be cropped.
- Added class [`iRegionDefinition`]({{site.ios-api-auxiliary}}region-definition.html). The class will be used to define the parameters for method [`setScanRegion`]({{site.ios-api}}camera-enhancer.html#setscanregion).
- Added property [`scanRegionVisible`]({{site.ios-api}}camera-enhancer.html#scanregionvisible) to control and check the visibility of the scan region.
- Added method [`setTorchButton`]({{site.ios-api-auxiliary}}dcecameraview.html#settorchbutton) to [`DCECameraView`]({{site.ios-api-auxiliary}}dcecameraview.html) class for users to set the position of the torch button. Property [`torchButtonVisible`]({{site.ios-api-auxiliary}}dcecameraview.html#torchbuttonvisible) is added to set and check the visibility of the torch button.
- Extended the JSON template of [`updateAdvancedSettingsFromFile`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromfile) and [`updateAdvancedSettingsFromString`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromstring). Added fast mode configuration parameters to the template.

## 2.0.0 (10/19/2021)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-2.0.0.html -%}

<div class="fold-panel-end"></div>

### Changelog

#### Improved

- Updated the mechanism of the video buffer. The capability of real-time frame processing and transferring is improved.

#### Breaking Change(s)

- Added method [`initLicense`]({{site.ios-api}}camera-enhancer.html#initlicense) to replace `initLicenseFromDLS`.
- Upgraded the [`basic camera-control APIs`]({{site.ios-api}}camera-enhancer.html#basic-camera-control-methods).
- Upgraded the usage of [`camera enhancer features`]({{site.ios-api}}camera-enhancer.html#enhanced-features).
- Renamed class `CameraView` to [`DCECameraView`]({{site.ios-api-auxiliary}}dcecameraview.html). The features of the class are extended as well.
- Renamed class `Frame` to [`DCEFrame`]({{site.ios-api-auxiliary}}dceframe.html). The features of the class are extended as well.
