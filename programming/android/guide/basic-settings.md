---
layout: default-layout
title: Dynamsoft Camera Enhancer - Customize Camera Settings on Android
description: This is the documentation - Customize Camera Settings on Android.
keywords:  Camera Enhancer, Customize Camera Settings
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Customize Camera Settings
---

# Customize the Basic Settings

There are three classes available in Dynamsoft Camera Enhancer SDK.

| Class | Description |
| ----- | ----------- |
| `CameraEnhancer` | The class includes basic hardware control and video streaming control APIs. |
| `DCECameraView` | The class includes UI  |
| `DCEFrame` |  |

## Camera Control

### Basic Camera Settings

When using Dynamsoft Camera Enhancer (DCE), the first back-forward camera is selected as the default camera. You can switch the cameras and control the status of the cameras via camera control APIs that are available in `CameraEnhancer` class.

Use the following methods to switch cameras:

- `getAllCameras`
- `selectCamera`
- `getSelectCamera`

Use the following methods to control the camera status:

- `open`/`close`/`pause`/`resume`

### Additional Camera Settings

Specifying the scan region will help you improve processing efficiency. You can specify the scan region and display it on the UI via the following methods:

- `setScanRegion`
- `setScanRegionVisible`

The resolution, focus, zoom factor and torchlight settings are also available when using DCE.

- `setResolution`/`getResolution`
- `setZoom`
- `setFocus`
- `turnOnTorch`/`turnOffTorch`

**Sample Code**

```java
```

## UI Configurations

Common UI elements are preset in DCECameraView classes. These UI elements facilitate you when working with Dynamsoft products.

### Add Highlighted Overlays

If DCE is bound with Dynamsoft Barcode Reader, highlight **overlays** can be created automatically on the decoded barcode results based on the localization areas. You can configure the **overlay** settings via the following methods.

- `setOverlayVisible`
- `setOverlayColour`

### Torch Button

You can simply control the torchlight via the methods `turnOnTorch`/`turnOffTorch` or enable an interactive torch light control via the **torchButton** UI element. Methods are available for users to set the position, size, image and visibility of the **torchButton**. Once the **torchButton** is displayed on the UI, users can click on the **torchButton** to switch on/off the torchlight.

- `setTorchButton`
- `setTorchButtonVisible`
