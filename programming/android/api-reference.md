---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references
description: This is the documentation - Android API reference page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, API
needAutoGenerateSidebar: true
breadcrumbText: API references
needGenerateH3Content: true
noTitleIndex: true
---

# Android API references

## Primary Class - CameraEnhancer

| Method | Description |
| ------ | ----------- |
| [`initLicense`]({{site.android-api}}initialization.html#initlicense) | Sets product key and activate the SDK. |
| [`addCameraView`]({{site.android-api}}.html#) | Add camera video streaming UI. Read more from [`DCECameraView`](). |
| [`getFrameFromBuffer`]({{site.android-api}}preprocess.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`setFrameRate`]({{site.android-api}}preprocess.html#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`]({{site.android-api}}preprocess.html#getframerate) | Get the current frame rate. |
| [`getAllCameras`]({{site.android-api}}camera.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera`]({{site.android-api}}camera.html#selectcamera) | Select and active a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.android-api}}camera.html#getselectedcamera) | Get the camera ID of the current actived camera. |
| [`open`]({{site.android-api}}camera.html#open) | Turn on the current actived camera. |
| [`close`]({{site.android-api}}camera.html#close) | Turn off the current actived camera. |
| [`pause`]({{site.android-api}}camera.html#pause) | Pause the current actived  camera. |
| [`resume`]({{site.android-api}}camera.html#resume) | Resume the current actived camera. |
| [`turnOnTorch`]({{site.android-api}}camera.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.android-api}}camera.html#turnofftorch) | Turn off the torch. |
| [`addListener`]({{site.android-api}}camera.html#addlistener) | Add [`DCEFrameListener`](). |
| [`removeListener`]({{site.android-api}}camera.html#removelistener) | Remove [`DCEFrameListener`](). |
| [`getResolution`]({{site.android-api}}camera.html#getresolution) | Get the current resolution. |
| [`setResolution`]({{site.android-api}}camera.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolutionList`]({{site.android-api}}camera.html#getresolutionlist) | Get all available resolutions. |
| [`updateAdvancedSetting`]({{site.android-api}}camera.html#updateadvancedsetting) | Update advanced parameter settings including filter, sensor and focus settings from a JSON Object. |
| [`getVersion`]({{site.android-api}}camera.html#getversion) | Get the SDK version. |
| [`setFocusPosition`]({{site.android-api}}zoom-focus.html#setfocusposition) | Focus once at the input position. |
| [`setZoomRegion`]({{site.android-api}}.html#) | Set `Rect` value of the interest region. The Camera Enhancer will try to zoom in to maximize the interest area on the screen. |
| [`setZoom`]({{site.android-api}}.html#) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |

## Auxiliary Classes

- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.android-api-auxiliary}}cameraview.html)
- [`CameraEnhancerException`]({{site.android-api-auxiliary}}camera-enhancer-exception.html)

## Interfaces

- [`CameraListener`]({{ site.android-api-auxiliary }}interface-cameralistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-torchlistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.enumerations }}errorcode.html)
