---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - UI APIs
description: This is the main page of Dynamsoft Camera Enhancer JavaScript SDK UI.
keywords: camera enhancer, UI, javascript, js
needAutoGenerateSidebar: true
needGenerateH3Content: true
noTitleIndex: true
breadcrumbText: UI
---

# UI Manipulation

## DrawingItem

```typescript
type DrawingItem = DT_Rect | DT_Arc | DT_Text | DT_Line | DT_Polygon | DT_Group | DT_Image;
```

## DT_Rect

```typescript
class DT_Rect { 

  public constructor(x: number, y: number, width: number, height: number, styleId?: number) { }; 

  x: number; 

  y: number;

  width: number; 

  height: number; 

  mediaType: EnumDrawingItemMediaType.Rect; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Arc

```typescript
class DT_Arc { 

  constructor(x: number, y: number, radius: number, startAngle: number, endAngle: number, styleId?: number) { }; 

  x: number; 

  y: number; 

  radius: number; 

  startAngle: number; 

  endAngle: number; 

  mediaType: EnumDrawingItemMediaType.Arc; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Text

```typescript
class DT_Text { 

  public constructor(text: string, x: number, y: number, styleId?: number) { } 

  x: number; 

  y: number;

  text: string; 

  mediaType: EnumDrawingItemMediaType.Text; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Line

```typescript
class DT_Line { 

  public constructor(startPoint: Point, endPoint: Point, styleId?: number) { } 

  startPoint: c; 

  endPoint: : Point; 

  mediaType: EnumDrawingItemMediaType.Line; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Polygon

```typescript
class DT_Polygon { 

  public constructor(vertices: Array<Point>, styleId?: number) { } 

  vertices: Array<Point>; 

  mediaType: EnumDrawingItemMediaType.Polygon; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Group

```typescript
class DT_Group { 

  public constructor(childItems: Array<DrawingItem>) { } 

  childItems: Array<DT_Rect | DT_Line | DT_Arc | DT_Text | DT_Polygon>; 

  mediaType: EnumDrawingItemMediaType.Group; 

  styleSelector?: string; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```

## DT_Image

```typescript
class DT_Image { 

  //NOTE: If an DT_Image instance has been constructed with an image, it can be replaced later with either an HTMLImageElement or an HTMLCanvasElement. In other words, an HTMLVideoElement can only be used during the constructing. 

  public constructor(HTMLImageElement | HTMLCanvasElement | HTMLVideoElement, x: number, y: number, styleId?: number) { } 

  x: number; 

  y: number;

  image: HTMLImageElement | HTMLCanvasElement | HTMLVideoElement; 

  mediaType: EnumDrawingItemMediaType.Image; 

  styleSelector?: string; 

  styleId?: number; 

  readonly drawingLayerId: number; //Only assigned after it's added to a layer 

} 
```
