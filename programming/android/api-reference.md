---
layout: default-layout
title: Android API references - Dynamsoft Camera Enhancer
description: This is the documentation - Android API references page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android API references
permalink: /programming/android/api-reference.html
---

# Android API references

## Primary Class - CameraEnhancer

### Initialization

| Method | Description |
| ------ | ----------- |
| [`initWithView`]({{site.android-api}}camera-enhancer.html#initwithview) | Initialize the camera enhancer with the `DCECameraView`. |
| [`initLicense`]({{site.android-api}}camera-enhancer.html#initlicense) | Sets product key and activate the SDK. |
| [`getVersion`]({{site.android-api}}camera-enhancer.html#getversion) | Get the SDK version. |
| [`cameraView`]({{site.android-api}}camera-enhancer.html#cameraview) | Bind a `DCECameraView` to the camera enhancer. |

### Basic Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`getAllCameras`]({{site.android-api}}camera-enhancer.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCameraWithPosition`]({{site.android-api}}camera-enhancer.html#selectcamerawithposition) | Select whether to use front-facing camera or back-facing camera. |
| [`getCameraPosition`]({{site.android-api}}camera-enhancer.html#getcameraposition) | Returns whether the front-facing camera or back-facing camera is selected. |
| [`selectCamera`]({{site.android-api}}camera-enhancer.html#selectcamera) | Select a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.android-api}}camera-enhancer.html#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`getCameraState`]({{site.android-api}}camera-enhancer.html#getcamerastate) | Get the state of the currently selected camera. |
| [`open`]({{site.android-api}}camera-enhancer.html#open) | Turn on the current selected camera. |
| [`close`]({{site.android-api}}camera-enhancer.html#close) | Turn off the current selected camera. |
| [`turnOnTorch`]({{site.android-api}}camera-enhancer.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.android-api}}camera-enhancer.html#turnofftorch) | Turn off the torch. |
| [`getFrameRate`]({{site.android-api}}camera-enhancer.html#getframerate) | Get the current frame rate. |
| [`setResolution`]({{site.android-api}}camera-enhancer.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`]({{site.android-api}}camera-enhancer.html#getresolution) | Get the current resolution. |
| [`setZoom`]({{site.android-api}}camera-enhancer.html#setzoom) | Set the zoom factor. Once setZoom is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`getMaxZoomFactor`]({{site.android-api}}camera-enhancer.html#getmaxzoomfactor) | Get the maximum available zoom factor. |
| [`autoZoomRange`]({{site.android-api}}camera-enhancer.html#autozoomrange) | The property for getting/setting the range of auto zoom. |
| [`setFocus`]({{site.android-api}}camera-enhancer.html#setfocus) | Set the focus position (value range from 0.0f to 1.0f) and trigger a focus at the configured position. |
| [`setFocus(subsequentFocusMode)`]({{site.android-api}}camera-enhancer.html#setfocussubsequentFocusMode) | Trigger a focus at the targeting point and set the subsequent focus mode after focused.  |
| [`setScanRegion`]({{site.android-api}}camera-enhancer.html#setscanregion) | Set the scan region with a RegionDefinition value. The frame will be cropped according to the scan region. |
| [`getScanRegion`]({{site.android-api}}camera-enhancer.html#getscanregion) | Get the scan region. |
| [`scanRegionVisible`]({{site.android-api}}camera-enhancer.html#scanregionvisible) | Set whether to display the **scanRegion** on the UI. |
| [`setCameraStateListener`]({{site.android-api}}camera-enhancer.md#setcamerastatelistener) | Add a `DCECameraStateListener` to receive notification when the camera state changes. |
| [`setFrameRate`]({{site.android-api}}camera-enhancer.html#setframerate) | **Deprecated, will be removed in v3.0**. Set the frame rate to the input value (if the input value is available for the device). |
| [`pause`]({{site.android-api}}camera-enhancer.html#pause) | **Deprecated, will be removed in v3.0**. Pause the current selected  camera. |
| [`resume`]({{site.android-api}}camera-enhancer.html#resume) | **Deprecated, will be removed in v3.0**. Resume the current selected camera. |

### Frame Acquiring Methods

| Method | Description |
| ------ | ----------- |
| [`getFrameFromBuffer`]({{site.android-api}}camera-enhancer.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`]({{site.android-api}}camera-enhancer.html#addlistener) | Add a listener to the Camera Enhancer instance. |
| [`removeListener`]({{site.android-api}}camera-enhancer.html#removelistener) | Remove a preciously added listener from the Camera Enhancer instance. |
| [`takePhoto`]({{site.android-api}}camera-enhancer.html#takephoto) | Take a photo from the camera and save the image in the memory. |

### Enhanced Features

| Method | Description |
| ------ | ----------- |
| [`enableFeatures`]({{site.android-api}}camera-enhancer.html#enablefeatures) | Enable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=java-android,kotlin) values. |
| [`disableFeatures`]({{site.android-api}}camera-enhancer.html#disablefeatures) | Disable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=java-android,kotlin) values. |
| [`isFeatureEnabled`]({{site.android-api}}camera-enhancer.html#isfeatureenabled) | Check whether the input features are enabled. |

### Advanced Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`updateAdvancedSettingsFromFile`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingsFromString`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |

## Auxiliary Classes

- [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html)
- [`DCEFeedback`]({{site.android-api-auxiliary}}dcefeedback.html)
- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`iRegionDefinition`]({{site.android-api-auxiliary}}region-definition.html)

## Protocol

- [`DCECameraStateListener`]({{ site.android-api-auxiliary }}protocol-camerastatelistener.html)
- [`DCEFrameListener`]({{ site.android-api-auxiliary }}protocol-dceframelistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}protocol-licenselistener.html)
- [`DCEPhotoListener`]({{ site.android-api-auxiliary }}protocol-dcephotolistener.html)

## Enumerations

- [`EnumCameraPosition`]({{ site.mobile-enum }}enum-camera-position.html?lang=java-android,kotlin)
- [`EnumCameraState`]({{ site.mobile-enum }}enum-camera-state.html?lang=java-android,kotlin)
- [`EnumDCEErrorCode`]({{ site.mobile-enum }}errorcode.html?lang=java-android,kotlin)
- [`EnumEnhancerFeatures`]({{ site.mobile-enum }}enum-enhancer-features.html?lang=java-android,kotlin)
- [`EnumFrameQuality`]({{ site.mobile-enum }}enum-frame-quality.html?lang=java-android,kotlin)
- [`EnumResolution`]({{ site.mobile-enum }}enum-resolution.html?lang=java-android,kotlin)
