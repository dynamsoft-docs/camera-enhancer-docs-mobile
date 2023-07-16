---
layout: default-layout
Title: LineDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class LineDrawingItem of Dynamsoft Camera Enhancer represents a line drawing item used for drawing line segments on the view.
Keywords: line drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# LineDrawingItem

The `LineDrawingItem` class is a subclass of `DrawingItem` and represents a line drawing item used for drawing line segments on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class LineDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getLine`](#line) | Get the line information of the LineDrawingItem. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`LineDrawingItem`](#initwithline) | Create an instance of LineDrawingItem. |
| [`LineDrawingItem(coordinateBase)`](#linedrawingitemcoordinatebase) | Create an instance of LineDrawingItem. |

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

## LineDrawingItem

Create an instance of `LineDrawingItem`.

```java
LineDrawingItem(com.dynamsoft.core.LineSegment line){}
```

**Parameters**

`line`: A `LineSegment` object that stores the line coordinates information.

**Return Value**

An instance of `LineDrawingItem`.

## LineDrawingItem(coordinateBase)

Create an instance of `LineDrawingItem`.

```java
LineDrawingItem(com.dynamsoft.core.LineSegment line, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`line`: A `LineSegment` object that stores the line coordinates information.  
`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `LineDrawingItem`.
