---
layout: default-layout
title: iOS API references - Dynamsoft Camera Enhancer
description: This is the documentation - iOS API references page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS API references
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS API references
---

# iOS API references

## Primary Class - CameraEnhancer

### Initialization

| Method | Description |
| ------ | ----------- |
| [`initWithView`]({{site.ios-api}}camera-enhancer.html#initwithview) | Initialize the camera enhancer with the `DCECameraView`. |
| [`initLicense`]({{site.ios-api}}camera-enhancer.html#initlicense) | Sets product key and activate the SDK. |
| [`getVersion`]({{site.ios-api}}camera-enhancer.html#getversion) | Get the SDK version. |
| [`cameraView`]({{site.ios-api}}camera-enhancer.html#cameraview) | Bind a `DCECameraView` to the camera enhancer. |

### Basic Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`getAllCameras`]({{site.ios-api}}camera-enhancer.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCameraWithPosition`]({{site.ios-api}}camera-enhancer.html#selectcamerawithposition) | Select whether to use front-facing camera or back-facing camera. |
| [`getCameraPosition`]({{site.ios-api}}camera-enhancer.html#getcameraposition) | Returns whether the front-facing camera or back-facing camera is selected. |
| [`selectCamera`]({{site.ios-api}}camera-enhancer.html#selectcamera) | Select a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.ios-api}}camera-enhancer.html#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`getCameraState`]({{site.ios-api}}camera-enhancer.html#getcamerastate) | Get the state of the currently selected camera. |
| [`open`]({{site.ios-api}}camera-enhancer.html#open) | Turn on the current selected camera. |
| [`close`]({{site.ios-api}}camera-enhancer.html#close) | Turn off the current selected camera. |
| [`pause`]({{site.ios-api}}camera-enhancer.html#pause) | Pause the current selected  camera. |
| [`resume`]({{site.ios-api}}camera-enhancer.html#resume) | Resume the current selected camera. |
| [`turnOnTorch`]({{site.ios-api}}camera-enhancer.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.ios-api}}camera-enhancer.html#turnofftorch) | Turn off the torch. |
| [`getFrameRate`]({{site.ios-api}}camera-enhancer.html#getframerate) | Get the current frame rate. |
| [`setResolution`]({{site.ios-api}}camera-enhancer.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`]({{site.ios-api}}camera-enhancer.html#getresolution) | Get the current resolution. |
| [`setZoom`]({{site.ios-api}}camera-enhancer.html#setzoom) | Set the zoom factor. Once setZoom is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`getMaxZoomFactor`]({{site.ios-api}}camera-enhancer.html#getmaxzoomfactor) | Get the maximum available zoom factor. |
| [`setAutoZoomRange`]({{site.ios-api}}camera-enhancer.html#setautozoomrange) | Set the range of auto zoom. |
| [`getAutoZoomRange`]({{site.ios-api}}camera-enhancer.html#getautozoomrange) | Get the range of auto zoom. |
| [`setFocus`]({{site.ios-api}}camera-enhancer.html#setfocus) | Set the focus position (value range from 0.0f to 1.0f) and trigger a focus at the configured position. |
| [`setFocus(subsequentFocusMode)`]({{site.ios-api}}camera-enhancer.html#setfocussubsequentFocusMode) | Trigger a focus at the targeting point and set the subsequent focus mode after focused.  |
| [`setScanRegion`]({{site.ios-api}}camera-enhancer.html#setscanregion) | Set the scan region with a RegionDefinition value. The frame will be cropped according to the scan region. |
| [`getScanRegion`]({{site.ios-api}}camera-enhancer.html#getscanregion) | Get the scan region. |
| [`scanRegionVisible`]({{site.ios-api}}camera-enhancer.html#scanregionvisible) | **Deprecated, will be removed in v3.0**. Set whether to display the **scanRegion** on the UI. |
| [`setCameraStateListener`]({{site.ios-api}}camera-enhancer.md#setcamerastatelistener) | Add a `DCECameraStateListener` to receive notification when the camera state changes. |
| [`setFrameRate`]({{site.ios-api}}camera-enhancer.html#setframerate) | **Deprecated, will be removed in v3.0**. Set the frame rate to the input value (if the input value is available for the device). |

### Frame Acquiring Methods

| Method | Description |
| ------ | ----------- |
| [`getFrameFromBuffer`]({{site.ios-api}}camera-enhancer.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`]({{site.ios-api}}camera-enhancer.html#addlistener) | Add a listener to the Camera Enhancer instance. |
| [`removeListener`]({{site.ios-api}}camera-enhancer.html#removelistener) | Remove a preciously added listener from the Camera Enhancer instance. |
| [`takePhoto`]({{site.ios-api}}camera-enhancer.html#takephoto) | Take a photo from the camera and save the image in the memory. |

### Enhanced Features

| Method | Description |
| ------ | ----------- |
| [`enableFeatures`]({{site.ios-api}}camera-enhancer.html#enablefeatures) | Enable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=objc,swift) values. |
| [`disableFeatures`]({{site.ios-api}}camera-enhancer.html#disablefeatures) | Disable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=objc,swift) values. |
| [`isFeatureEnabled`]({{site.ios-api}}camera-enhancer.html#isfeatureenabled) | Check whether the input features are enabled. |

### Advanced Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`updateAdvancedSettingsFromFile`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingsFromString`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |

## Auxiliary Classes

- [`DCECameraView`]({{site.ios-api-auxiliary}}dcecameraview.html)
- [`DCEFeedback`]({{site.ios-api-auxiliary}}dcefeedback.html)
- [`DCEFrame`]({{site.ios-api-auxiliary}}dceframe.html)
- [`iRegionDefinition`]({{site.ios-api-auxiliary}}region-definition.html)

## Protocol

- [`DCECameraStateListener`]({{ site.ios-api-auxiliary }}protocol-camerastatelistener.html)
- [`DCEFrameListener`]({{ site.ios-api-auxiliary }}protocol-dceframelistener.html)
- [`DCELicenseVerificationListener`]({{ site.ios-api-auxiliary }}protocol-licenselistener.html)
- [`DCEPhotoListener`]({{ site.ios-api-auxiliary }}protocol-dcephotolistener.html)

## Enumerations

- [`EnumCameraPosition`]({{ site.mobile-enum }}enum-camera-position.html?lang=objc,swift)
- [`EnumCameraState`]({{ site.mobile-enum }}enum-camera-state.html?lang=objc,swift)
- [`EnumDCEErrorCode`]({{ site.mobile-enum }}errorcode.html?lang=objc,swift)
- [`EnumEnhancerFeatures`]({{ site.mobile-enum }}enum-enhancer-features.html?lang=objc,swift)
- [`EnumFrameQuality`]({{ site.mobile-enum }}enum-frame-quality.html?lang=objc,swift)
- [`EnumResolution`]({{ site.mobile-enum }}enum-resolution.html?lang=objc,swift)
