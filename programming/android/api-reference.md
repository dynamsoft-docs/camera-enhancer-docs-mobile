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
| [`CameraEnhancer`]({{site.android-api}}index.html##cameraenhancer) | Initialize the `CameraEnhancer` object. |
| [`initLicense`]({{site.android-api}}index.html#initlicense) | Sets product key and activate the SDK. |
| [`getVersion`]({{site.android-api}}index.html#getversion) | Get the SDK version. |
| [`setCameraView`]({{site.android-api}}index.html#setcameraview) | Sets camera video streaming UI. Read more from [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html). |
| [`getCameraView`]({{site.android-api}}index.html#setcameraview) | Gets camera video streaming UI. Read more from [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html). |
| [`getAllCameras`]({{site.android-api}}index.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera`]({{site.android-api}}index.html#selectcamera) | Select and active a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.android-api}}index.html#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`open`]({{site.android-api}}index.html#open) | Turn on the current selected camera. |
| [`close`]({{site.android-api}}index.html#close) | Turn off the current selected camera. |
| [`pause`]({{site.android-api}}index.html#pause) | Pause the current selected  camera. |
| [`resume`]({{site.android-api}}index.html#resume) | Resume the current selected camera. |
| [`turnOnTorch`]({{site.android-api}}index.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.android-api}}index.html#turnofftorch) | Turn off the torch. |
| [`getFrameFromBuffer`]({{site.android-api}}index.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`]({{site.android-api}}index.html#addlistener) | Add [`DCEFrameListener`](). |
| [`removeListener`]({{site.android-api}}index.html#removelistener) | Remove [`DCEFrameListener`](). |
| [`setFrameRate`]({{site.android-api}}index.html#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`]({{site.android-api}}index.html#getframerate) | Get the current frame rate. |
| [`getResolution`]({{site.android-api}}index.html#getresolution) | Get the current resolution. |
| [`setResolution`]({{site.android-api}}index.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolutionList`]({{site.android-api}}index.html#getresolutionlist) | Get all available resolutions. |
| [`setFocus`]({{site.android-api}}index.html#setfocus) | Focus once at the input position. |
| [`setZoom`]({{site.android-api}}.html#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`updateAdvancedSettingFromFile`]({{site.android-api}}index.html#updateadvancedsettingfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingFromString`]({{site.android-api}}index.html#updateadvancedsettingfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |

## Auxiliary Classes

- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.android-api-auxiliary}}dcecameraview.html)
- [`CameraEnhancerException`]({{site.android-api-auxiliary}}camera-enhancer-exception.html)

## Interfaces

- [`DCEFrameListener`]({{ site.android-api-auxiliary }}interface-dceframelistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.enumerations }}errorcode.html)
