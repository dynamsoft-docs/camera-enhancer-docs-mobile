---
layout: default-layout
title: TorchButton Class - Dynamsoft Capture Vision MAUI Edition
description: TorchButton class of DCV MAUI edition defines a torch button with its location, size and image.
keywords: Torch button, torch image
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# TorchButton

The TorchButton class defines a torch button with its location, size and image.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```java
class TorchButton
```

## Properties

| Property | Type | Description |
|--------- |------|-------------|
| [`X`](#x) | *double* | The x-coordinate of the torch button. |
| [`Y`](#y) | *double* | The y-coordinate of the torch button. |
| [`Width`](#width) | *double* | The width of the torch button. |
| [`Height`](#height) | *double* | The height of the torch button. |
| [`TorchOnImageSource`](#torchonimagesource) | *ImageSource* | The image source of the torch button when the torch is on. |
| [`TorchOffImageSource`](#torchoffimagesource) | *ImageSource* | The image source of the torch button when the torch is off. |

### X

The x-coordinate of the torch button.

```csharp
double X { get; set; }
```

### Y

The y-coordinate of the torch button.

```csharp
double Y { get; set; }
```

### Width

The width of the torch button.

```csharp
double Width { get; set; }
```

### Height

The height of the torch button.

```csharp
double Height { get; set; }
```

### TorchOnImageSource

The image source of the torch button when the torch is on.

```csharp
ImageSource? TorchOnImageSource { get; set; }
```

### TorchOffImageSource

The image source of the torch button when the torch is off.

```csharp
ImageSource? TorchOffImageSource { get; set; }
```
