---
layout: default-layout
title: LineDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class LineDrawingItem of Dynamsoft Camera Enhancer represents a line drawing item used for drawing line segments on the view.
keywords: line drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# LineDrawingItem

The `LineDrawingItem` class is a subclass of `DrawingItem` and represents a line drawing item used for drawing line segments on the view.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
class LineDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getLine`](#getline) | Get the line information of the LineDrawingItem. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`LineDrawingItem`](#linedrawingitemline) | Create an instance of LineDrawingItem. |
| [`LineDrawingItem(line,coordinateBase)`](#linedrawingitemlinecoordinatebase) | Create an instance of LineDrawingItem. |

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

### getLine

Get the line information of the LineDrawingItem.

```java
com.dynamsoft.core.LineSegment getLine(){}
```

### getMediaType

Get the media type of the `DrawingItem`.

```java
EnumDrawingItemMeidaType getMediaType;
```

### LineDrawingItem(line)

Create an instance of `LineDrawingItem`.

```java
LineDrawingItem(com.dynamsoft.core.LineSegment line){}
```

**Parameters**

`line`: A [`LineSegment`]({{ site.dcv_android_api }}core/basic-structures/line-segment.html) object that stores the line coordinates information.

**Return Value**

An instance of `LineDrawingItem`.

### LineDrawingItem(line,coordinateBase)

Create an instance of `LineDrawingItem`.

```java
LineDrawingItem(com.dynamsoft.core.LineSegment line, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`line`: A [`LineSegment`]({{ site.dcv_android_api }}core/basic-structures/line-segment.html) object that stores the line coordinates information.  
`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `LineDrawingItem`.
