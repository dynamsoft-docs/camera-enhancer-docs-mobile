---
layout: default-layout
title: ImageEditorView Class - Dynamsoft Capture Vision MAUI Edition
description: The ImageEditorView class of DCV MAUI edition is used to display an image and related UI elements.
keywords:  Torch button, scan region mask, scan laser, camera view, ui
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ImageEditorView

The `ImageEditorView` class is used to display an image and related UI elements.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
class ImageEditorView : View
```

## Methods & Properties

| Method | Description |
|------- |-------------|
| [`ImageEditorView`](#imageeditorview-1) | The constructor. |
| [`GetDrawingLayer`](#getdrawinglayer) | Get the specified `DrawingLayer`. |

| Property | Type | Description |
|--------- | ---- |-------------|
| [`OriginalImage`](#originalimage) | *ImageData* | The original image that displayed on the view. |
| [`SelectedDrawingItem`](#selecteddrawingitem) | *DrawingItem* | The selected [`DrawingItem`](drawingitem.md) on the view. |

### ImageEditorView

The constructor. Create an instance of `ImageEditorView`.

```csharp
ImageEditorView();
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

### OriginalImage

The origial image that displayed on the view.

```csharp
ImageData OriginalImage{ get; set; }
```

### SelectedDrawingItem

The selected [`DrawingItem`](drawingitem.md) on the view.

```csharp
DrawingItem SelectedDrawingItem { get; }
```
