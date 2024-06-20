---
layout: default-layout
title: CameraView Class - Dynamsoft Capture Vision MAUI Edition
description: The CameraView class of DCV MAUI edition is used to display the camera preview and provides UI controlling APIs
keywords:  Torch button, scan region mask, scan laser, camera view, ui
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraView

The `CameraView` class is used to display the camera preview and provides UI controlling APIs. Users can add interactable UI elements on the view.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```java
class CameraView : View
```

## Methods & Properties

| Method | Description |
|------- |-------------|
| [`CameraView`](#cameraview-1) | The constructor. |

| Property | Type | Description |
|--------- | ---- |-------------|
| [`TorchButton`](#torchbutton) | *TorchButton* | The property that defines a torch button. User can click the button to turn on/off the torch. |
| [`TorchButtonVisible`](#torchbuttonvisible) | *bool* | The property that defines whether the torch button is visible. |
| [`ScanRegionMaskVisible`](#scanregionmaskvisible) | *bool* | The property that defines whether the scan region mask is visible. |
| [`ScanLaserVisible`](#scanlaservisible) | *bool* | The property that defines whether the scan laser is visible. |

### CameraView

The constructor. Create an instance of `CameraView`.

```csharp
CameraView();
```

**Return Value**

An instance of `CameraView`.

### TorchButton

The property that defines a torch button. User can click the button to turn on/off the torch. View [`TorchButton`]({{ site.dce_maui_api }}torch-button.html) class for how more information about how to configure the torch button.

```csharp
TorchButton TorchButton
```

### TorchButtonVisible

The property that defines whether the torch button is visible.

```csharp
bool TorchButtonVisible
```

### ScanRegionMaskVisible

The property that defines whether the scan region mask is visible.

```csharp
bool ScanRegionMaskVisible
```

### ScanLaserVisible

The property that defines whether the scan laser is visible.

```csharp
bool ScanLaserVisible
```
