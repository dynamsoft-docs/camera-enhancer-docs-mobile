---
layout: default-layout
title: ImageEditorView Class - Dynamsoft Capture Vision Flutter
description: ImageEditorView class of DCV Flutter edition represents an image editor view, which allows users to add interactable UI elements on the view.
keywords: camera, enhancer, barcode reader, flutter, capture vision, view
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ImageEditorView

`ImageEditorView` is a widget that allows users to add interactable UI elements on the view.

## Definition

*Assembly:* dynamsoft_capture_vision_flutter

```dart
class ImageEditorView extends StatefulWidget
```

## Constructors

```dart
const ImageEditorView({
  super.key,
  this.imageData,
  this.drawingQuadsByLayer,
  this.onPlatformViewCreated,
});
```

## Properties

| Property | Description |
| -------- | ----------- |
| [`imageData`](#imagedata) | The initial image to display in the editor when created. |
| [`drawingQuadsByLayer`](#drawingquadsbylayer) | Pre-populated drawing quadrilaterals organized by layer. |
| [`onPlatformViewCreated`](#onplatformviewcreated) | Callback invoked when the native platform view is successfully created. |

### imageData

The initial image to display in the editor when created.

```dart
final ImageData? imageData;
```

### drawingQuadsByLayer

Pre-populated drawing quadrilaterals organized by layer.

```dart
final Map<EnumDrawingLayerId, List<Quadrilateral>>? drawingQuadsByLayer;
```

### onPlatformViewCreated

Callback invoked when the native platform view is successfully created.

```dart
final void Function(ImageEditorViewController)? onPlatformViewCreated;
```
