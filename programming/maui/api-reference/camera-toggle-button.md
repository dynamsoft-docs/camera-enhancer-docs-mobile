---
layout: default-layout
title: CameraToggleButton Class - Dynamsoft Capture Vision MAUI Edition
description: CameraToggleButton class of DCV MAUI edition defines a camera toggle button with its location, size and image.
keywords: camera toggle button, camera toggle image
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraToggleButton

The CameraToggleButton class defines a camera toggle button with its location, size and image.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
class CameraToggleButton
```

## Properties & Methods

| Property | Type | Description |
|--------- |------|-------------|
| [`X`](#x) | *double* | The x-coordinate of the camera toggle button. |
| [`Y`](#y) | *double* | The y-coordinate of the camera toggle button. |
| [`Width`](#width) | *double* | The width of the camera toggle button. |
| [`Height`](#height) | *double* | The height of the camera toggle button. |
| [`CameraToggleImageSource`](#cameratoggleimagesource) | *ImageSource* | The image source of the camera toggle button. |

| Method | Description |
|------- |-------------|
| [`CameraToggleButton`](#cameratogglebutton-1) | The constructors. |

### X

The x-coordinate of the camera toggle button.

```csharp
double X { get; set; }
```

### Y

The y-coordinate of the camera toggle button.

```csharp
double Y { get; set; }
```

### Width

The width of the camera toggle button.

```csharp
double Width { get; set; }
```

### Height

The height of the camera toggle button.

```csharp
double Height { get; set; }
```

### CameraToggleImageSource

The image source of the camera toggle button.

```csharp
ImageSource? CameraToggleImageSource { get; set; }
```

### CameraToggleButton

The constructors.

```csharp
CameraToggleButton();
CameraToggleButton(double x, double y, double width, double height, ImageSource? cameraToggleImageSource);
```
