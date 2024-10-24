---
layout: default-layout
title: QuadDrawingItem Class - Dynamsoft Capture Vision MAUI Edition
description: The QuadDrawingItem class of DCV MAUI edition describes a quad that can be drawn on the view.
keywords:  Torch button, scan region mask, scan laser, camera view, ui
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# QuadDrawingItem

The `QuadDrawingItem` class describes a quad that can be drawn on the view.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
class QuadDrawingItem : DrawingItem
```

## Methods & Properties

| Method | Description |
|------- |-------------|
| [`QuadDrawingItem`](#quaddrawingitem-1) | The constructor. |

| Property | Type | Description |
|--------- | ---- |-------------|
| [`Quad`](#quad) | *ImageData* | Get the quad information of the `QuadDrawingItem`. |

The following property is inherited from `DrawingItem`

| Property | Type | Description |
|--------- | ---- |-------------|
| [`DrawingStyleId`](#drawingstyleid) | `int` | The style id of the drawing item. |

### QuadDrawingItem

The constructor.

```csharp
QuadDrawingItem(Quadrilateral quad);
```

### Quad

Get the quad information of the `QuadDrawingItem`.

```csharp
Quadrilateral Quad { get; }
```

### DrawingStyleId

The style id of the drawing item. View all available IDs via [EnumDrawingStyleId](enum/drawing-style-id.html).

```csharp
int DrawingStyleId { get; set; }
```
