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
| [`initLicense`]({{site.android-api}}index.html#initlicense) | Initialize Dynamsoft Camera Enhancer with a valid license. |
| [`addCameraView`]({{site.android-api}}index.html#addcameraview) | Add camera video streaming UI. Read more from [`DCECameraView`](). |
| [`getFrameFromBuffer`]({{site.android-api}}index.html#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`setFrameRate`]({{site.android-api}}index.html#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`]({{site.android-api}}index.html#getframerate) | Get the current frame rate. |
| [`getAllCameras`]({{site.android-api}}index.html#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera`]({{site.android-api}}index.html#selectcamera) | Select and active a camera from the camera list with the camera ID. |
| [`getSelectedCamera`]({{site.android-api}}index.html#getselectedcamera) | Get the camera ID of the current actived camera. |
| [`open`]({{site.android-api}}index.html#open) | Turn on the current actived camera. |
| [`close`]({{site.android-api}}index.html#close) | Turn off the current actived camera. |
| [`pause`]({{site.android-api}}index.html#pause) | Pause the current actived  camera. |
| [`resume`]({{site.android-api}}index.html#resume) | Resume the current actived camera. |
| [`turnOnTorch`]({{site.android-api}}index.html#turnontorch) | Turn on the torch. |
| [`turnOffTorch`]({{site.android-api}}index.html#turnofftorch) | Turn off the torch. |
| [`addListener`]({{site.android-api}}index.html#addlistener) | Add [`DCEFrameListener`](). |
| [`removeListener`]({{site.android-api}}index.html#removelistener) | Remove [`DCEFrameListener`](). |
| [`getResolution`]({{site.android-api}}index.html#getresolution) | Get the current resolution. |
| [`setResolution`]({{site.android-api}}index.html#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolutionList`]({{site.android-api}}index.html#getresolutionlist) | Get all available resolutions. |
| [`updateAdvancedSetting`]({{site.android-api}}index.html#updateadvancedsetting) | Update advanced parameter settings including filter, sensor and focus settings from a JSON Object. |
| [`getVersion`]({{site.android-api}}index.html#getversion) | Get the SDK version. |
| [`setFocus`]({{site.android-api}}index.html#setfocus) | Focus once at the input position. |
| [`setZoom`]({{site.android-api}}.html#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |

## Auxiliary Classes

- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.android-api-auxiliary}}cameraview.html)
- [`CameraEnhancerException`]({{site.android-api-auxiliary}}camera-enhancer-exception.html)

## Interfaces

- [`CameraListener`]({{ site.android-api-auxiliary }}interface-cameralistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-torchlistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.enumerations }}errorcode.html)
