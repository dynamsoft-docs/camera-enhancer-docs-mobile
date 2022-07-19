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

**Region and Video**

| API Name | Description |
|---|---|
| [getVisibleRegion()](#getvisibleregion) | Returns a `Region` object which specifies which part of the original video is shown in the video element. |
| [addScanRegionOverlayCanvas()](#addscanregionoverlaycanvas) | Adds a canvas of the same size as the scan area directly above the scan area. |
| [removeScanRegionOverlayCanvas()](#removescanregionoverlaycanvas) | Removes the specified Canvas element. |
| [ifShowScanRegionMask](#ifshowscanregionmask) | Returns or sets whether the scan region mask is shown. |
| [ifShowScanRegionLaser](#ifshowscanregionlaser) | Returns or sets whether the laser indicator is shown in the scan region. |
| [setScanRegionMaskStyle()](#setscanregionmaskstyle) | Sets the styles for the scan region mask. |
| [setVideoFit()](#setvideofit) | Sets the `object-fit` CSS property of the video element. |
| [getVideoFit()](#getvideofit) | Returns the value of the `object-fit` CSS property of the video element. |

**ViewDecorator**

| API Name | Description |
|---|---|
| [setViewDecorator()](#setviewdecorator) | Sets and shows the view decorator. |
| [getViewDecorator()](#getviewdecorator) | Gets what view decorator is shown. |
| [setViewDecoratorLineWidth()](#setviewdecoratorlinewidth) | Sets the line width for drawing the view decorator. |
| [setViewDecoratorStrokeStyle()](#setviewdecoratorstrokestyle) | Sets the stroke style for drawing the view decorator.. |
| [setViewDecoratorFillStyle()](#setviewdecoratorfillstyle) | Sets the fill style for drawing the view decorator. |
| [setViewDecoratorMaskFillStyle()](#setviewdecoratormaskfillstyle) | Sets the fill style for drawing the ask for the view decorator. |

**DrawingLayer**

| API Name | Description |
|---|---|
| [createDrawingLayer()](#createdrawinglayer) | Creates a DrawingLayer object. |
| [getDrawingLayer()](#getdrawinglayer) | Gets the `DrawingLayer` specified by its ID. |
| [getDrawingLayers()](#getdrawinglayers) | Returns an array of all DrawingLayer objects. |
| [clearDrawingLayers()](#cleardrawinglayers) | Removes all `DrawingLayer` objects. |

**DrawingStyle**

| API Name | Description |
|---|---|
| [createDrawingStyle()](#createdrawingstyle) | Creates a new DrawingStyle object and returns its ID. |
| [getDrawingStyle()](#getdrawingstyle) | Returns the DrawingStyle object specified by its ID. |
| [getDrawingStyles()](#getdrawingstyles) | Returns all DrawingStyle objects. |
| [updateDrawingStyle()](#updatedrawingstyle) | Updates an existing DrawingStyle specified by its ID. |

**View or Edit**

| API Name | Description |
|---|---|
| [setOriginalImage()](#setoriginalimage) | Sets the original image to be drawn on the editor canvas.  |
| [getOriginalImage()](#getoriginalimage) | Returns the original image shown on the editor canvas. |
| [showOriginalImage()](#showoriginalimage) | Shows the original image. |
| [hideOriginalImage()](#hideoriginalimage) | Hides the original image. |
| [deleteOriginalImage()](#deleteoriginalimage) | Deletes the original image and removes the canvas that shows it. |
| [getSelectedDrawingItems()](#getselecteddrawingitems) | Returns the selected `DrawingItem` objects. |

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

Adds a canvas of the same size as the scan region directly above the scan region.

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

## removeScanRegionOverlayCanvas

Removes the specified Canvas element.

```typescript
removeScanRegionOverlayCanvas(cvs: HTMLCanvasELement): void;
```

**Parameters**

`cvs` : specifies the canvas.

**Return value**

None.

**Code Snippet**

```js
let cvs = enhancer.addScanRegionOverlayCanvas();
//...
enhancer.removeScanRegionOverlayCanvas(cvs);
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

`maskStyle` : specifies the new style. Read more on [strokeStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle) and [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

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

`objectFit` : specifies the new fit type. At present, only "cover" and "contain" are allowed. Check out more on [object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit).

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

`type` : specifies the decorator type. Allowed values are "rectangle" , "focus" , "crossline" , "crosshair" , ["rectangle", "crossline"], ["rectangle", "crosshair"], ["focus", "crossline"] and ["focus", "crosshair"]. If passed an empty string, the decorator is cleared.

`area` : specifies where to place the decorator. It accepts 4 values:
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

`type` : specifies the decorator type. Allowed values are "rectangle" , "focus" , "crossline" and "crosshair".

`width` : specifies the line width.

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

`type` : specifies the decorator type. Allowed values are "rectangle" , "focus" , "crossline" and "crosshair".

`strokeStyle` : specifies the stroke style. Read more on [strokeStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/strokeStyle).

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

`type` : specifies the decorator type. Allowed values are "rectangle" and "focus".

`fillStyle` : specifies the fill style. Read more on [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

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

`type` : specifies the decorator type. Allowed values are "rectangle" and "focus".

`fillStyle` : specifies the fill style. Read more on [fillStyle](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

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

Creates a `DrawingLayer` object.

```typescript
createDrawingLayer(): DrawingLayer;
```

**Return value**

The visible layer represented by a `DrawingLayer` object.

**Code Snippet**

```js
let newDrawingLayer = enhancer.createDrawingLayer();
```

**See also**

* [DrawingLayer](interface/drawinglayer.md)

## getDrawingLayer

Returns an existing `DrawingLayer` specified by its ID. IDs start at 100 for the first custom `DrawingLayer`, 101 for the next, and so on.

```typescript
getDrawingLayer(drawingLayerId: number): DrawingLayer;
```

**Parameters**

`drawingLayerId` : specifies the `DrawingLayer` id.

**Return value**

The `DrawingLayer` object specified by its input id.

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
```

**See also**

* [DrawingLayer](interface/drawinglayer.md)

## getDrawingLayers

Returns all the `DrawingLayer`s.

```typescript
getDrawingLayer(): Array<DrawingLayer>;
```

**Parameters**

none.

**Return value**

The array of all the `DrawingLayer` objects.

**Code Snippet**

```js
let drawingLayers = enhancer.getDrawingLayers();
```

**See also**

* [DrawingLayer](interface/drawinglayer.md)

## clearDrawingLayers

Removes all the `DrawingLayer` objects.

```typescript
clearDrawingLayers(): void;
```

**Code Snippet**

```js
enhancer.clearDrawingLayers();
```

**See also**

* [DrawingLayer](interface/drawinglayer.md)

## createDrawingStyle

Creates a new `DrawingStyle` object and returns its ID.

```typescript
createDrawingStyle(styleDefinition: DrawingStyle): number; 
```

**Parameters**

`styleDefinition` : defines a `DrawingStyle` object.

**Return value**

The id of the created `DrawingStyle`.

**Code Snippet**

```js
let styleID = enhancer.createDrawingStyle({    
    lineWidth: 1.0,
    fillStyle: " rgba(73, 173, 245, 0.8)",
    strokeStyle: " rgba(73, 173, 245, 1)",
    paintMode: "fill",
    fontSize: 100, 
    fontFamily: "sans-serif"
});
```

**See also**

* [DrawingStyle](interface/drawingstyle.md)

## getDrawingStyle

Returns the `DrawingStyle` object specified by its Id.

> The SDK comes with 8 default styles with the IDs 1 ~ 8, check [DrawingStyle](interface/drawingstyle.md) for more information.

```typescript
getDrawingStyle(styleId: number): DrawingStyle; 
```

**Parameters**

`styleId` : specifies a `DrawingStyle`.

**Return value**

The `DrawingStyle` specified by the input id.

**Code Snippet**

```js
// Change `styleId` to one that you know exists at runtime. 
let drawingStyle = enhancer.getDrawingStyle(100);
```

**See also**

* [DrawingStyle](interface/drawingstyle.md)

## getDrawingStyles

Returns all `DrawingStyle` objects.

```typescript
getDrawingStyles(): Array<DrawingStyle>; 
```

**Return value**

The array of all of the `DrawingStyle` objects of current `CameraEnhancer`.

**Code Snippet**

```js
let drawingStyles = enhancer.getDrawingStyles();
```

**See also**

* [DrawingStyle](interface/drawingstyle.md)

## updateDrawingStyle

Updates an existing `DrawingStyle` specified by its ID. You can update all properties of the `DrawingStyle` or you can update just a few of them. Check the code snippet for more information.

> The update takes effect immediately.

```typescript
updateDrawingStyle(styleId: number, styleDefinition: DrawingStyle): void; 
```

**Parameters**

`styleId` : specifies a `DrawingStyle` which needs to be updated.

`styleDefinition` : Defines a new `DrawingStyle` object.

**Code Snippet**

```js
// Change the whole style
enhancer.updateDrawingStyle(100,  {
    fillStyle: "rgba(100, 75, 245, 0.3)",
    fontFamily: "sans-serif",
    fontSize: 25,
    lineWidth: 2,
    paintMode: "strokeAndFill",
    strokeStyle: "rgba(73, 173, 245, 1)"
});
// Only change the fontSize
enhancer.updateDrawingStyle(100, { fontSize: 30 });
```

**See also**

* [DrawingStyle](interface/drawingstyle.md)

## setOriginalImage

Sets an image to be drawn on a canvas built into the UI. Call showOriginalImage() to show it.

```typescript
setOriginalImage(imageData: Uint8Array | Uint8ClampedArray | HTMLCanvasElement, width: number, height: number): void; 
```

**Parameters**

`imageData` : specifies the image data in format of `Uint8Array`, `Uint8ClampedArray` or `HTMLCanvasElement`.

`width`: specifies the width of the image data.

`height`: specifies the height of the image data.

**Code Snippet**

```js
let currentFrame = enhancer.getFrame();
let cvs = currentFrame.toCanvas();
enhancer.setOriginalImage(cvs, cvs.width, cvs.height);
```

## getOriginalImage

Returns the original image.

```typescript
getOriginalImage(): {imageData: Uint8Array, width: number, height: number}; 
```

**Return value**

The current original image in `Uint8Array` format and its dimensions.

**Code Snippet**

```js
let image = enhancer.getOriginalImage();
```

## deleteOriginalImage

Deletes the original image.

```typescript
async deleteOriginalImage(): Promise<void>; 
```

**Code Snippet**

```js
await enhancer.deleteOriginalImage();
```

## showOriginalImage

Shows the original image.

```typescript
showOriginalImage(): void; 
```

**Code Snippet**

```js
enhancer.showOriginalImage();
```

## hideOriginalImage

Hides the original image.

```typescript
async hideOriginalImage(): Promise<void>; 
```

**Code Snippet**

```js
await enhancer.hideOriginalImage();
```

## getSelectedDrawingItems

Returns the selected `DrawingItem` objects. These items can be from any `drawingLayer` but they share the same `styleSelector` which is "selected".

```typescript
getSelectedDrawingItems(): Array<DrawingItem>; 
```

**Return value**

The array of current selected `DrawingItem` objects.

**Code Snippet**

```js
let drawingItems = enhancer.getSelectedDrawingItems();
```

**See also**

* [DrawingItem](interface/drawingitem.md)
