---
layout: default-layout
title: DrawingLayer Class - Dynamsoft Capture Vision MAUI Edition
description: The DrawingLayer class of DCV MAUI edition is the container of DrawingItems.
keywords:  Torch button, scan region mask, scan laser, camera view, ui
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DrawingLayer

The `DrawingLayer` class is the container of the [`DrawingItems`](drawing-item.html).

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
class DrawingLayer
```

## Methods & Properties

| Method | Description |
|------- |-------------|
| [`ClearDrawingItems`](#cleardrawingitems) | Clear all the [`DrawingItems`](drawing-item.html) on the layer. |
| [`SetDefaultStyle`](#setdefaultstyle) | Set the default style of the layer with a style id. |

| Property | Type | Description |
|--------- | ---- |-------------|
| [`Id`](#id) | *int* | The ID of the layer. |
| [`DrawingItems`](#drawingitems) | *IList<DrawingItem>* | A list contains all the `DrawingItems` on the layer. |
| [`Visible`](#visible) | bool** | A bool value determines whether the layer is visible. |

### ClearDrawingItems

Clear all the `DrawingItems` on the layer.

```csharp
void ClearDrawingItems();
```

### SetDefaultStyle

Set the default style of the layer with a style id. View all available IDs via [EnumDrawingStyleId](enum/drawing-style-id.html).

```csharp
void SetDefaultStyle(int styleId);
```

### Id

The ID of the layer.

```csharp
int Id { get; }
```

### DrawingItems

A list contains all the `DrawingItems` on the layer.

```csharp
IList<DrawingItem> DrawingItems { get; set; }
```

### Visible

A bool value determines whether the layer is visible.

```csharp
bool Visible { get; set; }
```
