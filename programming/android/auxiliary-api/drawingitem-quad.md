---
layout: default-layout
title: QuadDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class QuadDrawingItem of Dynamsoft Camera Enhancer represents a drawing item that draws quadrilaterals on the view.
keywords: quad drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# QuadDrawingItem

The `QuadDrawingItem` class is a subclass of `DrawingItem`. It represents a drawing item that draws quadrilaterals on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class QuadDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getQuad`](#getquad) | Get the quad information of the `QuadDrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`QuadDrawingItem`](#quaddrawingitemquad) | Create an instance of `QuadDrawingItem`. |
| [`QuadDrawingItem(coordinateBase)`](#quaddrawingitemquadcoordinatebase) | Create an instance of `QuadDrawingItem`. |

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

### getQuad

Get the quad information of the `QuadDrawingItem`.

```java
com.dynamsoft.core.Quadrilateral getQuad(){}
```

**Return Value**

A [`Quadrilateral`]({{ site.dcv_android_api }}core/basic-structures/quadrilateral.html) object that stores the coodrinates of the `QuadDrawingItem`.

### getMediaType

Get the media type of the `DrawingItem`.

```java
EnumDrawingItemMeidaType getMediaType;
```

## QuadDrawingItem(quad)

Create an instance of `QuadDrawingItem`.

```java
QuadDrawingItem(com.dynamsoft.core.Quadrilateral quad){}
```

**Parameters**

`quad`: A `com.dynamsoft.core.Quadrilateral` object that stores the quad coordinates information.

**Return Value**

An instance of `QuadDrawingItem`.

## QuadDrawingItem(quad,coordinateBase)

Create an instance of `QuadDrawingItem`.

```java
QuadDrawingItem(com.dynamsoft.core.Quadrilateral quad, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`quad`: A `com.dynamsoft.core.Quadrilateral` object that stores the quad coordinates information.  
`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `QuadDrawingItem`.
