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

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
class CameraView : View
```

## Methods & Properties

| Method | Description |
|------- |-------------|
| [`CameraView`](#cameraview-1) | The constructor. |
| [`GetDrawingLayer`](#getdrawinglayer) | Get the specified `DrawingLayer`. |

| Property | Type | Description |
|--------- | ---- |-------------|
| [`CameraToggleButton`](#cameratogglebutton) | *CameraToggleButton* | The property that defines a camera toggle button. User can click the button to switch between the front and back forward cameras. |
| [`CameraToggleButtonVisible`](#cameratogglebuttonvisible) | *bool* | The property that defines whether the camera toggle button is visible. |
| [`TorchButton`](#torchbutton) | *TorchButton* | The property that defines a torch button. User can click the button to turn on/off the torch. |
| [`TorchButtonVisible`](#torchbuttonvisible) | *bool* | The property that defines whether the torch button is visible. |
| [`ScanRegionMaskVisible`](#scanregionmaskvisible) | *bool* | The property that defines whether the scan region mask is visible. |
| [`ScanLaserVisible`](#scanlaservisible) | *bool* | The property that defines whether the scan laser is visible. |

### CameraView

The constructor. Create an instance of `CameraView`.

```csharp
CameraView();
```

### GetDrawingLayer

Get the specified `DrawingLayer`.

```csharp
DrawingLayer GetDrawingLayer(EnumDrawingLayerId id);
```

**Parameters**

`[in] id`: One of the [`EnumDrawingLayerId`]({{ site.dce_maui_api }}enum/drawing-layer-id.html) member that specifies the ID of the layer that you want to get.

**Return Value**

The `DrawingLayer` instance.

### CameraToggleButton

The property that defines a torch button. User can click the button to switch between the front and back forward cameras. View [`CameraToggleButton`]({{ site.dce_maui_api }}camera-toggle-button.html) class for how more information about how to configure the camera toggle button.

```csharp
CameraToggleButton CameraToggleButton { get; set; }
```

### CameraToggleButtonVisible

The property that defines whether the camera toggle button is visible.

```csharp
bool CameraToggleButtonVisible { get; set; }
```

### TorchButton

The property that defines a torch button. User can click the button to turn on/off the torch. View [`TorchButton`]({{ site.dce_maui_api }}torch-button.html) class for how more information about how to configure the torch button.

```csharp
TorchButton TorchButton { get; set; }
```

### TorchButtonVisible

The property that defines whether the torch button is visible.

```csharp
bool TorchButtonVisible { get; set; }
```

### ScanRegionMaskVisible

The property that defines whether the scan region mask is visible.

```csharp
bool ScanRegionMaskVisible { get; set; }
```

### ScanLaserVisible

The property that defines whether the scan laser is visible.

```csharp
bool ScanLaserVisible { get; set; }
```
