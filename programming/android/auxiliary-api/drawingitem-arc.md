---
layout: default-layout
title: ArcDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class ArcDrawingItem of Dynamsoft Camera Enhancer represents a drawing item that draws Arcs on the view.
keywords: Arc drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ArcDrawingItem

The `ArcDrawingItem` class is a subclass of `DrawingItem`. It represents a drawing item that draws Arcs on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class ArcDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getCentre`](#getcentre) | Get the centre of the `ArcDrawingItem`. |
| [`getRadius`](#getradius) | Get the radius of the `DrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`ArcDrawingItem`](#arcdrawingitemcentre-radius) | Create an instance of `ArcDrawingItem`. |
| [`ArcDrawingItem(coordinateBase)`](#arcdrawingitemcentre-radius-coordinatebase) | Create an instance of `ArcDrawingItem` and set the coordinate base. |

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

### getCentre

Get the centre of the `ArcDrawingItem`.

```java
android.graphics.Point getCentre(){}
```

### getRadius

Get the radius of the `DrawingItem`.

```java
int getRadius(){}
```

### getMediaType

Get the media type of the `DrawingItem`.

```java
EnumDrawingItemMeidaType getMediaType;
```

## ArcDrawingItem(centre, radius)

Create an instance of `ArcDrawingItem`.

```java
ArcDrawingItem(Point centre, int radius){}
```

**Parameters**

`centre`: The centre of the `ArcDrawingItem`.

`radius`: The radius of the `ArcDrawingItem`.

**Return Value**

An instance of `ArcDrawingItem`.

## ArcDrawingItem(centre, radius, coordinateBase)

Create an instance of `ArcDrawingItem`.

```java
ArcDrawingItem(Point centre, int radius, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`centre`: The centre of the `ArcDrawingItem`.

`radius`: The radius of the `ArcDrawingItem`.

`coordinateBase`: The coordinate base of the `ArcDrawingItem`.

**Return Value**

An instance of `ArcDrawingItem`.
