---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS API references
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
| [`selectCamera(EnumCameraPosition)`]({{site.ios-api}}camera-enhancer.html#selectcameraenumcameraposition) | Select whether to use front-facing camera or back-facing camera. |
| [`selectCamera(String)`]({{site.ios-api}}camera-enhancer.html#selectcamerastring) | Select a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.ios-api}}camera-enhancer.html#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`getCameraState`]({{site.ios-api}}camera-enhancer.html#getcamerastate) | Get the state of the currently selected camera. |
| [`open`]({{site.ios-api}}camera-enhancer.html#open) | Turn on the current selected camera. |
| [`close`]({{site.ios-api}}camera-enhancer.html#close) | Turn off the current selected camera. |
| [`pause`]({{site.ios-api}}camera-enhancer.html#pause) | Pause the current selected  camera. |
| [`resume`]({{site.ios-api}}camera-enhancer.html#resume) | Resume the current selected camera. |
| [`turnOnTorch`]({{site.ios-api}}camera-enhancer.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.ios-api}}camera-enhancer.html#turnofftorch) | Turn off the torch. |

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
| [`enableFeatures`]({{site.ios-api}}camera-enhancer.html#enablefeatures) | Enable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.enumerations}}enum-enhancer-features.html) values. |
| [`disableFeatures`]({{site.ios-api}}camera-enhancer.html#disablefeatures) | Disable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.enumerations}}enum-enhancer-features.html) values. |
| [`isFeatureEnabled`]({{site.ios-api}}camera-enhancer.html#isfeatureenabled) | Check whether the input features are enabled. |

### Advanced Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`getFrameRate`]({{site.ios-api}}camera-enhancer.html#getframerate) | Get the current frame rate. |
| [`setResolution`]({{site.ios-api}}camera-enhancer.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`]({{site.ios-api}}camera-enhancer.html#getresolution) | Get the current resolution. |
| [`setZoom`]({{site.ios-api}}camera-enhancer.html#setzoom) | Set the zoom factor. Once setZoom is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`getMaxZoomFactor`]({{site.ios-api}}camera-enhancer.html#getmaxzoomfactor) | Get the maximum available zoom factor. |
| [`setFocus`]({{site.ios-api}}camera-enhancer.html#setfocus) | Set the focus position (value range from 0.0f to 1.0f) and trigger a focus at the configured position. |
| [`setScanRegion`]({{site.ios-api}}camera-enhancer.html#setscanregion) | Set the scan region with a RegionDefinition value. The frame will be cropped according to the scan region. |
| [`getScanRegion`]({{site.ios-api}}camera-enhancer.html#getscanregion) | Get the scan region. |
| [`scanRegionVisible`]({{site.ios-api}}camera-enhancer.html#scanregionvisible) | Set whether to display the **scanRegion** on the UI. |
| [`updateAdvancedSettingsFromFile`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingsFromString`]({{site.ios-api}}camera-enhancer.html#updateadvancedsettingsfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |
| [`setFrameRate`]({{site.ios-api}}camera-enhancer.html#setframerate) | **Deprecated**. Set the frame rate to the input value (if the input value is available for the device). |

## Auxiliary Classes

- [`DCEFrame`]({{site.ios-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.ios-api-auxiliary}}dcecameraview.html)
- [`DCEFeedback`]({{site.ios-api-auxiliary}}dcefeedback.html)
- [`iRegionDefinition`]({{site.ios-api-auxiliary}}region-definition.html)

## Interfaces

- [`DCEFrameListener`]({{ site.ios-api-auxiliary }}protocol-dceframelistener.html)
- [`DCEPhotoListener`]({{ site.ios-api-auxiliary }}protocol-dcephotolistener.html)
- [`DCELicenseVerificationListener`]({{ site.ios-api-auxiliary }}protocol-licenselistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.enumerations }}errorcode.html)
- [`EnumFrameQuality`]({{ site.enumerations }}enum-frame-quality.html)
- [`EnumCameraState`]({{ site.enumerations }}enum-camera-state.html)
- [`EnumEnhancerFeatures`]({{ site.enumerations }}enum-enhancer-features.html)
- [`EnumResolution`]({{ site.enumerations }}enum-resolution.html)
- [`EnumCameraPosition`]({{ site.enumerations }}enum-camera-position.html)
