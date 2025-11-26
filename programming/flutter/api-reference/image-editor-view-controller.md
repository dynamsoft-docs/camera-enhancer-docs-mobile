---
layout: default-layout
title: ImageEditorViewController Class - Dynamsoft Capture Vision Flutter
description: ImageEditorViewController class of Dynamsoft Capture Vision Flutter edition is the controller for managing and interacting with an ImageEditorView instance.
keywords: camera, enhancer, barcode reader, flutter, capture vision, view
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ImageEditorViewController

`ImageEditorViewController` is the controller for managing and interacting with an [`ImageEditorView`](image-editor-view.md) instance.

Provides methods to control the native image editor platform view, including image manipulation and quadrilateral drawing operations. This controller bridges Flutter code with native platform functionality.

## Definition

*Assembly:* dynamsoft_capture_vision_flutter

```dart
class ImageEditorViewController
```

## Constructors

```dart
ImageEditorViewController(int id);
```

## Methods

| Methods | Description |
| ------- | ----------- |
| [`setImageData`](#setimagedata) | Sets the image data to be displayed and edited in the native view. |
| [`setDrawingQuads`](#setdrawingquads) | Updates the drawing quadrilaterals on a specific drawing layer. |
| [`getSelectedQuad`](#getselectedquad) | Retrieves the currently selected quadrilateral from the editor. |

### setImageData

Sets the image data to be displayed and edited in the native view.

```dart
Future<void> setImageData(ImageData imageData) async;
```

### setDrawingQuads

Updates the drawing quadrilaterals on a specific drawing layer.

```dart
Future<void> setDrawingQuads(List<Quadrilateral> drawingQuads, int drawingLayerId) async;
```

### getSelectedQuad

Retrieves the currently selected quadrilateral from the editor.

```dart
Future<Quadrilateral> getSelectedQuad() async;
```
