---
layout: default-layout
title: RectDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class RectDrawingItem of Dynamsoft Camera Enhancer represents a rectangular drawing item.
keywords: rectangle, drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# RectDrawingItem

The `RectDrawingItem` class is a subclass of `DrawingItem` that represents a rectangular drawing item.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
class RectDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getRect`](#getrect) | Get the rect information of the `RectDrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`RectDrawingItem(rect)`](#rectdrawingitemrect) | Create an instance of `RectDrawingItem`. |
| [`RectDrawingItem(rect,coordinateBase)`](#rectdrawingitemrectcoordinatebase) | Create an instance of `RectDrawingItem`. |

## Interited Methods

The following methods are inherited from the superclass [`DrawingItem`](drawingitem.html).

| Method | Description |
|------- |-------------|
| [`setDrawingStyleId`](drawingitem.html#setdrawingstyleid) | Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer. |
| [`getDrawingStyleId`](drawingitem.html#getdrawingstyleid) | Get the DrawingStyle of the `DrawingItem`. |
| [`setState`](drawingitem.html#setstate) | Set the state of the `DrawingItem`. |
| [`getState`](drawingitem.html#getstate) | Get the state of the `DrawingItem`. |
| [`getCoordinateBase`](drawingitem.html#getcoordinatebase) | Get the coordinate base of the `DrawingItem`. The coordinate base is image by default. |
| [`getMediaType`](drawingitem.html#getmediatype) | Get the media type of the `DrawingItem`. |
| [`addNote`](drawingitem.html#addnote) | Add a note to the `DrawingItem`. |
| [`getNote`](drawingitem.html#getnote) | Get the specified `Note`. |
| [`hasNote`](drawingitem.html#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](drawingitem.html#updatenote) | Update the content of the specified `Note`. |
| [`deleteNote`](drawingitem.html#deletenote) | Remove the specified `Note` with the specified name. |
| [`getAllNotes`](drawingitem.html#getallnotes) | Get all `Notes` of this DrawingItem. |
| [`clearNotes`](drawingitem.html#clearnotes) | Remove all `Notes` of this DrawingItem. |

### getRect

Get the rect information of the `RectDrawingItem`.

```java
android.graphics.Rect getRect(){}
```

### getMediaType

Get the media type of the `DrawingItem`.

```java
EnumDrawingItemMeidaType getMediaType;
```

### RectDrawingItem(rect)

Create an instance of `RectDrawingItem`.

```java
RectDrawingItem(android.graphics.Rect rect){}
```

**Parameters**

`rect`: A `android.graphics.Rect` object that stores the rect coordinates information.

**Return Value**

An instance of `RectDrawingItem`.

## RectDrawingItem(rect,coordinateBase)

Create an instance of `RectDrawingItem`.

```java
RectDrawingItem(android.graphics.Rect rect, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`rect`: A `android.graphics.Rect` object that stores the rect coordinates information.  
`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `RectDrawingItem`.
