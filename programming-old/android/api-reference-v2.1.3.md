---
layout: default-layout
title: Android API references - Dynamsoft Camera Enhancer
description: This is the documentation - Android API reference page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, API
needAutoGenerateSidebar: true
breadcrumbText: API references
needGenerateH3Content: true
noTitleIndex: true
permalink: /programming/android/api-reference-v2.1.3.html
---

# Android API references

## Primary Class - CameraEnhancer

### Initialization

| Method | Description |
| ------ | ----------- |
| [`CameraEnhancer`]({{site.android-api}}camera-enhancer.html#cameraenhancer) | Initialize the `CameraEnhancer` object. |
| [`initLicense`]({{site.android-api}}camera-enhancer.html#initlicense) | Sets product key and activate the SDK. |
| [`getVersion`]({{site.android-api}}camera-enhancer.html#getversion) | Get the SDK version. |

### Basic Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`getAllCameras`]({{site.android-api}}camera-enhancer.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera`]({{site.android-api}}camera-enhancer.html#selectcamera) | Select and active a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.android-api}}camera-enhancer.html#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`getCameraState`]({{site.android-api}}camera-enhancer.html#getcamerastate) | Get the state of the currently selected camera. |
| [`open`]({{site.android-api}}camera-enhancer.html#open) | Turn on the current selected camera. |
| [`close`]({{site.android-api}}camera-enhancer.html#close) | Turn off the current selected camera. |
| [`pause`]({{site.android-api}}camera-enhancer.html#pause) | Pause the current selected  camera. |
| [`resume`]({{site.android-api}}camera-enhancer.html#resume) | Resume the current selected camera. |
| [`turnOnTorch`]({{site.android-api}}camera-enhancer.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.android-api}}camera-enhancer.html#turnofftorch) | Turn off the torch. |
| [`setFrameRate`]({{site.android-api}}camera-enhancer.html#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`]({{site.android-api}}camera-enhancer.html#getframerate) | Get the current frame rate. |
| [`getResolutionList`]({{site.android-api}}camera-enhancer.html#getresolutionlist) | Get all available resolutions. |
| [`setResolution`]({{site.android-api}}camera-enhancer.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`]({{site.android-api}}camera-enhancer.html#getresolution) | Get the current resolution. |
| [`setZoom`]({{site.android-api}}camera-enhancer.html#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`setFocus`]({{site.android-api}}camera-enhancer.html#setfocus) | Set the focus position (value range from 0.0f to 1.0f) and trigger a focus at the configured position. |
| [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion) | Set the scan region with a RegionDefinition value. The frame will be cropped according to the scan region. |
| [`getScanRegion`]({{site.android-api}}camera-enhancer.html#getscanregion) | Get the scan region. |
| [`setScanRegionVisible`]({{site.android-api}}camera-enhancer.html#setscanregionvisible) | Set whether to display the **scanRegion** on the UI. |
| [`getScanRegionVisible`]({{site.android-api}}camera-enhancer.html#getscanregionvisible) | Get whether the **scanRegion** will be displayed on the UI. |

### Frame Acquiring Methods

| Method | Description |
| ------ | ----------- |
| [`getFrameFromBuffer`]({{site.android-api}}camera-enhancer.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`]({{site.android-api}}camera-enhancer.html#addlistener) | Add a listener to the Camera Enhancer instance. |
| [`removeListener`]({{site.android-api}}camera-enhancer.html#removelistener) | Remove a preciously added listener from the Camera Enhancer instance. |

### Enhanced Features

| Method | Description |
| ------ | ----------- |
| [`enableFeatures`]({{site.android-api}}camera-enhancer.html#enablefeatures) | Enable DCE features with Enumeration value. |
| [`disableFeatures`]({{site.android-api}}camera-enhancer.html#disablefeatures) | Disable DCE features with Enumeration value. |
| [`isFeatureEnabled`]({{site.android-api}}camera-enhancer.html#isfeatureenabled) | Returns a boolean value that means whether the feature(s) you input is (are) enabled. |

### Camera UI Methods

| Method | Description |
| ------ | ----------- |
| [`setCameraView`]({{site.android-api}}camera-enhancer.html#setcameraview) | Sets camera video streaming UI. Read more from [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html). |
| [`getCameraView`]({{site.android-api}}camera-enhancer.html#setcameraview) | Gets camera video streaming UI. Read more from [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html). |

### Advanced Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`updateAdvancedSettingsFromFile`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingsFromString`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |

## Auxiliary Classes

- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html)
- [`RegionDefinition`]({{site.android-api-auxiliary}}region-definition.html)
- [`CameraEnhancerException`]({{site.android-api-auxiliary}}camera-enhancer-exception.html)

## Interfaces

- [`DCEFrameListener`]({{ site.android-api-auxiliary }}interface-dceframelistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.dce-enums }}error-code.html?lang=android)
- [`EnumFrameQuality`]({{ site.dce-enums }}video-frame-quality.html?lang=android)
- [`EnumCameraState`]({{ site.dce-enums }}camera-state.html?lang=android)
- [`EnumEnhancerFeatures`]({{ site.dce-enums }}enhanced-features.html?lang=android)
- [`EnumResolution`]({{ site.dce-enums }}resolution.html?lang=android)
