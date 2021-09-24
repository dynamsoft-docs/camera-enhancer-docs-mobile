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

### [Initialization]({{site.android-api}}initialization.html)

| Method | Description |
| ------ | ----------- |
| [`initLicense`]({{site.android-api}}initialization.html#initlicense) | Initialize the Camera Enhancer from the license server with a license. |

### [Frame preprocessing methods]({{site.android-api}}preprocess.html)

| Method | Description |
| ------ | ----------- |
| [`getFrameFromBuffer`]({{site.android-api}}preprocess.html#acquirebufferedframe) | Get the latest frame from the buffer. |
| [`setFrameRate`]({{site.android-api}}preprocess.html#setframerate) | Set max frame rate. |
| [`getFrameRate`]({{site.android-api}}preprocess.html#getframerate) | Set max frame rate. |

### [Regular camera methods]({{site.android-api}}camera.html)

| Method | Description |
| ------ | ----------- |
| [`updateAdvancedSetting`]({{site.android-api}}camera.html#updateadvancedsetting) | Update camera, filter and focus settings from Json String. |
| [`getVersion`]({{site.android-api}}camera.html#getversion) | Check current DCE version |

| getAllCameras ||
| [`open`]({{site.android-api}}camera.html#open) | Turn on the selected or default camera. |
| [`close`]({{site.android-api}}camera.html#close) | Turn off the selected or default camera. |
| [`pause`]({{site.android-api}}camera.html#pause) | Pause the selected or default camera. |
| [`resume`]({{site.android-api}}camera.html#resume) | Resume the selected or default camera. |
| [`addListener`]({{site.android-api}}camera.html#addcameralistener) | Add camera listener (on preview original, filtered or fast frames). |
| [`removeListener`]({{site.android-api}}camera.html#removecameralistener) | Remove camera listener. |
| [`getResolution`]({{site.android-api}}camera.html#getresolution) | Get current resolution setting. |
| [`setResolution`]({{site.android-api}}camera.html#setresolution) | Set resolution. |
| [`getResolutionList`]({{site.android-api}}camera.html#getresolutionlist) | Get all available resolutions |

### [Focus & zoom methods]({{site.android-api}}zoom-focus.html)

| Method | Description |
| ------ | ----------- |
| [`setFocusPosition`]({{site.android-api}}zoom-focus.html#setfocusposition) | Set auto focus position (Change the default auto focus position). |

## Auxiliary Classes

- [`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html)
- [`DCECameraView`]({{site.android-api-auxiliary}}cameraview.html)
- [`CameraEnhancerException`]({{site.android-api-auxiliary}}camera-enhancer-exception.html)

## Interfaces

- [`CameraListener`]({{ site.android-api-auxiliary }}interface-cameralistener.html)
- [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-torchlistener.html)

## Enumerations

- [`EnumDCEErrorCode`]({{ site.enumerations }}errorcode.html)
