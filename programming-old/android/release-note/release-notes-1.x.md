---
layout: default-layout
title: Android 1.x Release Note - Dynamsoft Camera Enhancer
description: This is the documentation - Android 1.x Release Note page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 1.x Release Note
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 1.x Release Note
permalink: /programming/android/release-note/release-notes-1.x.html
---

# Release Notes - Android 1.x

## 1.0.3 (07/20/2021)

### New

- Add Interface `CameraDLSLicenseVerificationListener` and callback `DLSLicenseVerificationCallback` to replace `CameraLTSLicenseVerificationListener` and `LTSLicenseVerificationCallback`.
- Added class `DMDLSConnectionParameters` to replace class `DMLTSConnectionParameters`.
- Added method `initLicenseFromDLS` in `CameraEnhancer` class to replace `initLicenseFromLTS`.

## 1.0.1 (06/10/2021)

### New

- Added a new property [`products`]({{ site.android-api-auxiliary }}dlsconnection.html#products) in class `DMLTSConnectionParameters`.
- Added a new enumeration [`EnumProduct`]({{ site.dce-enums }}enum-1.html?lang=android#enumproduct).

## 1.0.0 (04/29/2021)

- Video frame queue is available.
- Supports frame cropping mode.
- Supports regular camera control.
- Supports autofocus mode.
- Supports sensor control mode.
- Supports frame sharpness filter mode.
- Supports autozoom mode.
