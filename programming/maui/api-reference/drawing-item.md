---
layout: default-layout
title: DrawingItem Class - Dynamsoft Capture Vision MAUI Edition
description: The DrawingItem class of DCV MAUI edition is an abstract class that describes a basic UI element on the view.
keywords:  Torch button, scan region mask, scan laser, camera view, ui
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DrawingItem

The `DrawingItem` class is an abstract class that describes a basic UI element on the view.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CameraEnhancer.Maui

```java
abstract class DrawingItem 
```

## Properties

| Property | Type | Description |
|--------- | ---- |-------------|
| [`DrawingStyleId`](#drawingstyleid) | `int` | The style id of the drawing item. |

### DrawingStyleId

The style id of the drawing item. View all available IDs via [EnumDrawingStyleId](enum/drawing-style-id.html).

```csharp
int DrawingStyleId { get; set; }
```
