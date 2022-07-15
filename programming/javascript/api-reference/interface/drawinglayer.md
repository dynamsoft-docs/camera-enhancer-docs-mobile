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
| [removeDrawingItems()](#removedrawingitems) | Removes DrawingItem(s) from the DrawingLayer. |
| [setDrawingItems()](#setdrawingitems) | Replaces all DrawingItem(s) of the DrawingLayer with new ones. |
| [getDrawingItems()](#getdrawingitems) | Returns all DrawingItem(s) of the DrawingLayer. |
| [hasDrawingItem()](#hasDrawingItem) | Checks out if a DrawingItem belongs to the layer. |
| [clearDrawingItems()](#cleardrawingitems) | Removes all DrawingItem(s) of the DrawingLayer. |
| [setDrawingStyle()](#setdrawingstyle) | Sets the style for the DrawingLayer or for a particular mediaType. |
| [setVisible()](#setvisible) | Shows or hides the DrawingLayer. |
| [isVisible()](#isvisible) | Returns whether the DrawingLayer is visible. |
| [renderAll()](#renderall) | Renders all DrawingItems, usually required when the style for one or more items is changed. |
| [onSelectionChange()](#onselectionchange) | An event handler that is triggered when different DrawingItem(s) gets selected/deselected on the DrawingLayer. |

## getId

Returns the Id of the `DrawingLayer`.

```typescript
getId(): number;
```

**Code Snippet**

```js
let id = drawingLayer.getId();
```

## addDrawingItems

Adds `DrawingItem`(s) to the `DrawingLayer`.

```typescript
addDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
drawingLayer.addDrawingItems(YOUR_DRAWING_ITEMS);
```

**See also**

* [DrawingItem](../ui.md#drawingitem)

## removeDrawingItems

Removes specific `DrawingItem`(s) from the `DrawingLayer`.

```typescript
removeDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
drawingLayer.removeDrawingItems(YOUR_DRAWING_ITEMS);
```

## setDrawingItems

Replaces all `DrawingItem`(s) of the `DrawingLayer` with new ones.

```typescript
setDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
drawingLayer.setDrawingItems(YOUR_DRAWING_ITEMS);
```

## getDrawingItems

Returns all `DrawingItem`(s) of the `DrawingLayer`.

```typescript
getDrawingItems(drawingItems: Array<DrawingItem>): void;
```

**Code Snippet**

```js
var arr = drawingLayer.getDrawingItems();
```

## hasDrawingItem

Checks out if a `DrawingItem` belongs to the layer.

```typescript
hasDrawingItem(drawingItem: DrawingItem): Boolean;
```

**Code Snippet**

```js
var flag = drawingLayer.hasDrawingItem();
```

## clearDrawingItems

Removes all `DrawingItem`(s) of this `DrawingLayer`.

```typescript
clearDrawingItems(): void;
```

**Code Snippet**

```js
drawingLayer.clearDrawingItems();
```

## setDrawingStyle

Sets the style for this `DrawingLayer` or for a particular mediaType.

```typescript
setDrawingStyle(styleId: number, mediaType?: EnumDrawingItemMediaType, styleSelector?: string): void;
```

**Parameters**

`styleId`: Specifies the style by its ID.

`mediaType`: Specifies the mediaType. If undefined, the style applies to all `DrawingItem`s with the specified styleSelector. 

`styleSelector`: Specifies a selector. If undefined, it means "default". The selector is a pact between the `DrawingLayer` and the one passing in the `DrawingItem`s. 

**Code Snippet**

```js
drawingLayer.setDrawingStyle(DRAWING_STYLE_ID, MEDIA_TYPE_ENUM, STYLE_SELECTOR);
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
drawingLayer.setVisible(flase);
```

## isVisible

Returns whether the `DrawingLayer` is visible. 

```typescript
isVisible(): boolean;
```

**Code Snippet**

```js
var flag = drawingLayer.isVisible();
```

## renderAll

Renders all `DrawingItem`s, usually required when the style for one or more items is changed.

```typescript
renderAll(): boolean;
```

**Code Snippet**

```js
drawingLayer.renderAll();
```

## onSelectionChange

An event handler that is triggered when different `DrawingItem`(s) gets selected/deselected on the `DrawingLayer`.

```typescript
onSelectionChange: (selectedDrawingItems: Array<DrawingItem>, deselectedDrawingItems: Array<DrawingItem>) => void;
```

**Parameters**

`selectedDrawingItems`: Specifies the selected `DrawingItem` objects.

`deselectedDrawingItems`: Specifies the deselected `DrawingItem` objects. 

**Code Snippet**

```js
drawingLayer.onSelectionChange = (SELECTED_DRAWING_ITEMS, DESELECTED_DRAWING_ITEMS) => {
    //do ...
}
```

