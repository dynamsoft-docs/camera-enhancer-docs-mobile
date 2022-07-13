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

# UI Class

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

# UI APIs

| API Name | Description |
|---|---|
| [getVisibleRegion()](#getvisibleregion) | Returns a `Region` object which specifies which part of the original video is shown in the video element. |
| [addScanRegionOverlayCanvas()](#addscanregionoverlaycanvas) | Add a canvas of the same size as the scan area directly above the scan area. |
| [ifShowScanRegionMask](#ifshowscanregionmask) | Returns or sets whether the scan region mask is shown. |
| [ifShowScanRegionLaser](#ifshowscanregionlaser) | Returns or sets whether the laser indicator is shown in the scan region. |
| [setScanRegionMaskStyle()](#setscanregionmaskstyle) | Sets the styles for the scan region mask. |
| [setVideoFit()](#setvideofit) | Sets the `object-fit` CSS property of the video element. |
| [getVideoFit()](#getvideofit) | Returns the value of the `object-fit` CSS property of the video element. |

## ViewDecorator Setting
| API Name | Description |
|---|---|
| [setViewDecorator()](#setviewdecorator) | Sets and shows the view decorator. |
| [getViewDecorator()](#getviewdecorator) | Gets what view decorator is shown. |
| [setViewDecoratorLineWidth()](#setviewdecoratorlinewidth) | Sets the line width for drawing the view decorator. |
| [setViewDecoratorStrokeStyle()](#setviewdecoratorstrokestyle) | Sets the stroke style for drawing the view decorator.. |
| [setViewDecoratorFillStyle()](#setviewdecoratorfillstyle) | Sets the fill style for drawing the view decorator. |
| [setViewDecoratorMaskFillStyle()](#setviewdecoratormaskfillstyle) | Sets the fill style for drawing the ask for the view decorator. |

## DrawingLayer Setting
| API Name | Description |
|---|---|
| [createDrawingLayer()](#createdrawinglayer) | Creates a DrawingLayer object and put it in an array of DrawingLayers. |
| [getDrawingLayer()](#getdrawinglayer) | Gets the DrawingLayer specified by its ID. |
| [clearDrawingLayers()](#cleardrawinglayers) | Removes all DrawingLayers. |

## DrawingStyle Setting
| API Name | Description |
|---|---|
| [createDrawingStyle()](#createdrawingstyle) | Creates a new DrawingStyle object and returns its ID. |
| [getDrawingStyle()](#getdrawingstyle) | Returns the DrawingStyle object specified by its Id. |
| [getDrawingStyles()](#getdrawingstyles) | Returns all DrawingStyle objects. |
| [updateDrawingStyle()](#updatedrawingstyle) | Updates an existing DrawingStyle specified by its ID. |

## UI Mode Setting
| API Name | Description |
|---|---|
| [switchUIMode()](#switchuimode) | Switches between editor mode and viewer mode. |
| [getUIMode()](#getuimode) | Returns the current UI mode. |
| [setOriginalImage()](#setoriginalimage) | Sets the original image to be drawn on the editor canvas.  |
| [getOriginalImage()](#getoriginalimage) | Returns the original image shown on the editor. |
| [deleteOriginalImage()](#deleteoriginalimage) | Deletes the original image and remove the canvas that shows it. |
| [getSelectedDrawingItems()](#getselecteddrawingitems) | Returns the selected DrawingItem object(s). |

## getVisibleRegion

Returns a `Region` object which specifies which part of the original video is shown in the video element.

```typescript
getVisibleRegion(inPixels?: boolean): Region;
```

**Parameters**

`inPixels`: [optional] The coordinate type. If omitted or set to `false`, the returned coordinates are represented by percentage, otherwise, by pixels.

**Return value**

The visible region represented by a `Region` object.

**Code Snippet**

```js
enhancer.getVisibleRegion();
```

**See also**

* [Region](interface/region.md)

## addScanRegionOverlayCanvas

Add a canvas of the same size as the scan area directly above the scan area.

```typescript
addScanRegionOverlayCanvas(): Canvas;
```

**Parameters**

None.

**Return value**

The added `Canvas` object.

**Code Snippet**

```js
let cvs = enhancer.addScanRegionOverlayCanvas();
let ctx = cvs.getContext('2d');
ctx.fillStyle = "white";
ctx.font = '50px serif';
ctx.fillText('Dynamsoft Camera Enhancer', 50, 90);
```

## ifShowScanRegionMask

Returns or sets whether the scan region mask is shown.

```typescript
ifShowScanRegionMask: boolean;
```

## ifShowScanRegionLaser

Returns or sets whether the laser indicator is shown in the scan region.

> This API only works when the viewer element contains the elements with the class names `dce-scanarea` and `dce-scanlight` (like the built-in viewer).

```typescript
ifShowScanRegionLaser: boolean;
```

## setScanRegionMaskStyle

Sets the styles for the scan region mask.

```typescript
setScanRegionMaskStyle(maskStyle: any): void;
```

**Parameters**

`maskStyle` : specify the new style. Read more on [strokeStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle) and [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

**Return value**

None.

**Code Snippet**

```js
enhancer.setScanRegionMaskStyle({
    lineWidth: 5,
    strokeStyle: "white",
    fillStyle: "rgba(50,50,50,0.3)"
});
```

## setVideoFit

Sets the `object-fit` CSS property of the video element.

```typescript
setVideoFit(objectFit: string): void;
```

**Parameters**

`objectFit` : specify the new fit type. At present, only "cover" and "contain" are allowed. Check out more on [object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit).

**Return value**

None.

**Code Snippet**

```js
enhancer.setVideoFit("cover");
```

## getVideoFit

Returns the value of the `object-fit` CSS property of the video element.

```typescript
getVideoFit(): string;
```

**Parameters**

None.

**Return value**

The value of the `object-fit` CSS property.

**Code Snippet**

```js
enhancer.getVideoFit();
```

## setViewDecorator

Sets and shows the view decorator.

```typescript
setViewDecorator(type: string | string[], area: Area): void;
```

**Parameters**

`type` : specify the decorator type. Allowed values are "rectangle" , "focus" , "crossline" , "crosshair" , ["rectangle", "crossline"], ["rectangle", "crosshair"], ["focus", "crossline"] and ["focus", "crosshair"]. If passed an empty string, the decorator is cleared.

`area` : specify where to place the decorator. It accepts 4 values:
* `x`,     `y`: top-left point of the decorator in percentage (0~100) of the width/height of the viewer.
* `width`,     `height`: size of the decorator in percentage (0~100) of the width/height of the viewer.

**Return value**

None.

**Code Snippet**

```js
let area = {
    x: 5,
    y: 10,
    width: 90,
    height: 80
};
enhancer.setViewDecorator(["rectangle", "crosshair"], area);
```

**See also**

* [Area](interface/area.md)

## getViewDecorator

Gets what view decorator is shown.

```typescript
getViewDecorator(): {type: string[], area: Area, canvas: Canvas};
```

**See also**

* [Area](interface/area.md)

## setViewDecoratorLineWidth

Sets the line width for drawing the view decorator.

```typescript
setViewDecoratorLineWidth(type: string, width: number): void;
```

**Parameters**

`type` : specify the decorator type. Allowed values are "rectangle" , "focus" , "crossline" and "crosshair".

`width` : specify the line width.

**Return value**

None.

**Code Snippet**

```js
let area = {
    x: 5,
    y: 10,
    width: 90,
    height: 80
};
enhancer.setViewDecoratorLineWidth("rectangle", 10);
enhancer.setViewDecorator(["rectangle", "crosshair"], area);
```

## setViewDecoratorStrokeStyle

Sets the stroke style for drawing the view decorator.

```typescript
setViewDecoratorStrokeStyle(type: string, strokeStyle: string): void;
```

**Parameters**

`type` : specify the decorator type. Allowed values are "rectangle" , "focus" , "crossline" and "crosshair".

`strokeStyle` : specify the stroke style. Read more on [strokeStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle).

**Return value**

None.

**Code Snippet**

```js
let area = {
    x: 5,
    y: 10,
    width: 90,
    height: 80
};
enhancer.setViewDecoratorStrokeStyle("rectangle", "white");
enhancer.setViewDecorator(["rectangle", "crosshair"], area);
```

## setViewDecoratorFillStyle

Sets the fill style for drawing the view decorator.

```typescript
setViewDecoratorFillStyle(type: string, fillStyle: string): void;
```

**Parameters**

`type` : specify the decorator type. Allowed values are "rectangle" and "focus".

`fillStyle` : specify the fill style. Read more on [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

**Return value**

None.

**Code Snippet**

```js
let area = {
    x: 5,
    y: 10,
    width: 90,
    height: 80
};
enhancer.setViewDecoratorFillStyle("rectangle", "rgba(50,50,50,0.3)");
enhancer.setViewDecorator(["rectangle", "crosshair"], area);
```

## setViewDecoratorMaskFillStyle

Sets the fill style for drawing the ask for the view decorator.

```typescript
setViewDecoratorMaskFillStyle(type: string, fillStyle: string): void;
```

**Parameters**

`type` : specify the decorator type. Allowed values are "rectangle" and "focus".

`fillStyle` : specify the fill style. Read more on [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

**Return value**

None.

**Code Snippet**

```js
let area = {
    x: 5,
    y: 10,
    width: 90,
    height: 80
};
enhancer.setViewDecoratorMaskFillStyle("rectangle", "rgba(50,50,50,0.3)");
enhancer.setViewDecorator(["rectangle", "crosshair"], area);
```

## createDrawingLayer

Creates a `DrawingLayer` object and put it in an array of DrawingLayers.

```typescript
createDrawingLayer(): DrawingLayer;
```

**Return value**

The visible layer represented by a `DrawingLayer` object.

**Code Snippet**

```js
enhancer.createDrawingLayer();
```

## getDrawingLayer

Returns the `DrawingLayer` specified by its ID. If not found, and the ID is 1, 2 or 3, the layer will be created and returned. 

```typescript
getDrawingLayer(drawingLayerId: number): DrawingLayer;
```

**Parameters**

`drawingLayerId` : specify the `DrawingLayer` id.

**Return value**

The `DrawingLayer` object specified by its input id.

**Code Snippet**

```js
enhancer.getDrawingLayer(YOUR_LAYER_ID);
```

**See also**

* [DrawingLayer](interface/drawinglayer.md)

## clearDrawingLayers

Removes all the `DrawingLayer`s.

```typescript
clearDrawingLayers(): void;
```

**Code Snippet**

```js
enhancer.clearDrawingLayers();
```

## createDrawingStyle

Creates a new `DrawingStyle` object and returns its ID. 

```typescript
createDrawingStyle(styleDefinition: DrawingStyle): number; 
```

**Parameters**

`styleDefinition` : Define a `DrawingStyle` object.

**Return value**

The id of the created `DrawingStyle`.

**Code Snippet**

```js
var drawingStyleId = enhancer.createDrawingStyle(YOUR_DRAWING_STYLE);
```

## getDrawingStyle

Returns the `DrawingStyle` object specified by its Id.

```typescript
getDrawingStyle(styleId: number): DrawingStyle; 
```
**Parameters**

`styleId` : specify a `DrawingStyle`.

**Return value**

The `DrawingStyle` specified by the input id.

**Code Snippet**

```js
var drawingStyle = enhancer.getDrawingStyle(YOUR_STYLE_ID);
```

## getDrawingStyles

Returns all `DrawingStyle` objects.

```typescript
getDrawingStyles(): Array<DrawingStyle>; 
```

**Return value**

An array of all of the `DrawingStyle` objects.

**Code Snippet**

```js
var drawingStyles = enhancer.getDrawingStyles();
```

## updateDrawingStyle

Updates an existing `DrawingStyle` specified by its ID.

```typescript
updateDrawingStyle(styleId: number, styleDefinition: DrawingStyle): void; 
```

**Parameters**

`styleId` : specify a `DrawingStyle` which needs to be updated.

`styleDefinition` : Define a new `DrawingStyle` object.

**Code Snippet**

```js
enhancer.updateDrawingStyle(YOUR_STYLE_ID, YOUR_NEW_DRAWING_STYLE);
```

## switchUIMode

Switches between editor mode and viewer mode.

```typescript
switchUIMode(newMode: string): void; 
```

**Parameters**

`newMode` : specify the mode to switch to. Allowed values are ""editor" and "viewer". 

**Code Snippet**

```js
enhancer.switchUIMode("editor");
```

## getUIMode

Returns the current UI mode.

```typescript
getUIMode(): "editor" | "viewer"; 
```

**Return value**

A string of the current mode's name.

**Code Snippet**

```js
var mode = enhancer.getUIMode();
```

## setOriginalImage

Sets an original image to be drawn on the editor canvas.

```typescript
setOriginalImage(imageData: Uint8Array | Uint8ClampedArray | HTMLCanvasElement, width: number, height: number): void; 
```

**Parameters**

`imageData` : specifies the image data in format of `Uint8Array`, `Uint8ClampedArray` or `HTMLCanvasElement`.

`width`: specifies the width of the image data.

`height`: specifies the height of the image data.

**Code Snippet**

```js
enhancer.setOriginalImage(AN_IMAGE_DATA);
```

## getOriginalImage

Returns the original image shown on the editor.

```typescript
getOriginalImage(): Uint8Array; 
```

**Return value**

The current original image in `Uint8Array` format.

**Code Snippet**

```js
var image = enhancer.getOriginalImage();
```

## deleteOriginalImage

Deletes the original image and remove the canvas that shows it. 

```typescript
deleteOriginalImage(): void; 
```

**Code Snippet**

```js
enhancer.deleteOriginalImage();
```

## getSelectedDrawingItems

Returns the selected `DrawingItem` object(s).

```typescript
getSelectedDrawingItems(): Array<DrawingItem>; 
```

**Return value**

An array of current selected `DrawingItem` object(s).

**Code Snippet**

```js
var drawingItems = enhancer.getSelectedDrawingItems();
```
