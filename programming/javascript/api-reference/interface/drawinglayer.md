---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - Interface DrawingLayer
description: This page shows the DrawingLayer Interface of Dynamsoft Camera Enhancer JavaScript SDK.
keywords: DrawingLayer, CameraEnhancer, api reference, javascript, js
needAutoGenerateSidebar: false
noTitleIndex: true
breadcrumbText: DrawingLayer
---

# DrawingLayer

`interface` DrawingLayer

| API Name | Description |
|---|---|
| [getId()](#getid) | Returns the ID of the DrawingLayer. |
| [addDrawingItems()](#adddrawingitems) | Adds DrawingItem(s) to the DrawingLayer. |
| [getDrawingItems()](#getdrawingitems) | Returns all DrawingItem(s) of the DrawingLayer. |
| [setDrawingItems()](#setdrawingitems) | Replaces all DrawingItem(s) of the DrawingLayer with new ones. |
| [hasDrawingItem()](#hasDrawingItem) | Checks out if a DrawingItem belongs to the layer. |
| [removeDrawingItems()](#removedrawingitems) | Removes DrawingItem(s) from the DrawingLayer. |
| [clearDrawingItems()](#cleardrawingitems) | Removes all DrawingItem(s) from the DrawingLayer. |
| [setDrawingStyle()](#setdrawingstyle) | Sets the style for the DrawingLayer or for a particular mediaType. |
| [setVisible()](#setvisible) | Shows or hides the DrawingLayer. |
| [isVisible()](#isvisible) | Returns whether the DrawingLayer is visible. |
| [renderAll()](#renderall) | Renders all DrawingItems, usually required when the style for one or more items is changed. |
| [onSelectionChange()](#onselectionchange) | An event handler that is triggered when different DrawingItem(s) gets selected/deselected on the DrawingLayer. |
| [setMode()](#setmode) | Changes the mode of the layer. |
| [getMode()](#getmode) | Returns the current mode. |

## getId

Returns the Id of the `DrawingLayer`.

```typescript
getId(): number;
```

**Code Snippet**

```js
let enhancer = await Dynamsoft.DCE.CameraEnhancer.createInstance();
let drawingLayer = enhancer.createDrawingLayer();
let drawingLayerId = drawingLayer.getId();
```

## addDrawingItems

Adds `DrawingItem`(s) to the `DrawingLayer`.

```typescript
addDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
let drawingItems = new Array(
    new DT_Rect(10, 10, 100, 100, 1),
    new DT_Text("label 1", 40, 40, 2),
    new DT_Line({x: 10, y: 50}, {x: 90, y: 50}, 3)
)
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.addDrawingItems(drawingItems);
```

**See also**

* [DrawingItem](drawingitem.md)

## getDrawingItems

Returns all `DrawingItem`(s) of the `DrawingLayer`.

```typescript
getDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
let drawingItems = drawingLayer.getDrawingItems();
```

**See also**

* [DrawingItem](drawingitem.md)

## setDrawingItems

Replaces all `DrawingItem`(s) of the `DrawingLayer` with new ones.

```typescript
setDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
let newDrawingItems = new Array(
    new DT_Rect(10, 10, 100, 100, 1),
    new DT_Text("label 1", 40, 40, 2),
    new DT_Line({x: 10, y: 50}, {x: 90, y: 50}, 3)
)
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.setDrawingItems(newDrawingItems);
```

**See also**

* [DrawingItem](drawingitem.md)

## hasDrawingItem

Checks out if a `DrawingItem` belongs to the layer.

```typescript
hasDrawingItem(drawingItem: DrawingItem): Boolean;
```

**Code Snippet**

```js
let drawingItem = new DT_Rect(10, 10, 100, 100, 1);
let drawingLayer = enhancer.getDrawingLayer(100);
let hasDrawingItem = drawingLayer.hasDrawingItem(drawingItem);
```

**See also**

* [DrawingItem](drawingitem.md)

## removeDrawingItems

Removes specific `DrawingItem`(s) from the `DrawingLayer`.

```typescript
removeDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
let drawingItems = new Array(
    new DT_Rect(10, 10, 100, 100, 1),
    new DT_Text("label 1", 40, 40, 2)
)
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.removeDrawingItems(drawingItems);
```

**See also**

* [DrawingItem](drawingitem.md)

## clearDrawingItems

Removes all `DrawingItem`(s) from the `DrawingLayer`.

```typescript
clearDrawingItems(): void;
```

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.clearDrawingItems();
```

## setDrawingStyle

Sets the style for the `DrawingLayer` or for a particular mediaType or for a specific status.

```typescript
setDrawingStyle(styleId: number, mediaType?: EnumDrawingItemMediaType, styleSelector?: string): void;
```

**Parameters**

`styleId`: specifies the style by its ID.

`mediaType`: specifies the mediaType. If undefined, the style applies to all `DrawingItem`s with the specified styleSelector. 

`styleSelector`: specifies a selector. If undefined, it means "default". The selector is a pact between the `DrawingLayer` and the one passing in the `DrawingItem`s. 

**Code Snippet**

```js
//set style 1 for all the DrawingItems on the `DrawingLayer`
drawingLayer.setDrawingStyle(1);
//set style 1 for all Rect-shape DrawingItems on the `DrawingLayer`
drawingLayer.setDrawingStyle(1, EnumDrawingItemMediaType.Rect);
//set style 1 for all selected DrawingItems on the `DrawingLayer`
drawingLayer.setDrawingStyle(1, "selected");
//set style 1 for all Rect-shape and selected DrawingItems on the `DrawingLayer`
drawingLayer.setDrawingStyle(1, EnumDrawingItemMediaType.Rect, "selected");
```

**See also**

* [DrawingStyle](drawingstyle.md)
* [EnumDrawingItemMediaType](../enum/enumdrawingitemmediatype.md)

## setVisible

Shows or hides the `DrawingLayer`. 

```typescript
setVisible(visible: boolean): void;
```

**Parameters**

`visible`: True means show, false means hide the `DrawingLayer`.

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.setVisible(flase);
```

## isVisible

Returns whether the `DrawingLayer` is visible. 

```typescript
isVisible(): boolean;
```

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
let isVisible = drawingLayer.isVisible();
```

## renderAll

Renders all `DrawingItem`s, usually required when the style for one or more items is changed.

```typescript
renderAll(): boolean;
```

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
let isRenderedAll = drawingLayer.renderAll();
```

## onSelectionChange

An event handler that is triggered when different `DrawingItem`(s) gets selected/deselected on the `DrawingLayer`.

```typescript
onSelectionChange: (selectedDrawingItems: Array<DrawingItem>, deselectedDrawingItems: Array<DrawingItem>) => void;
```

**Parameters**

`selectedDrawingItems`: specifies the selected `DrawingItem` objects.

`deselectedDrawingItems`: specifies the deselected `DrawingItem` objects. 

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.onSelectionChange = (selected, deselected) => {
    //do ...
}
```

## setMode

Changes the mode of the layer. 

```typescript
setMode(newMode: string): void;
```

**Parameters**

`newMode`: specifies the new mode. At present, the allowed values are "editor" and "viewer" and the default is "viewer".

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
drawingLayer.setMode("editor");
```

## getMode

Returns the current mode.  

```typescript
getMode(): "editor" | "viewer"; 
```

**Return value**

The mode of current `DrawingLayer`.

**Code Snippet**

```js
let drawingLayer = enhancer.getDrawingLayer(100);
let mode = drawingLayer.getMode();
```