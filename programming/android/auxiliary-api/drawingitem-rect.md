---
layout: default-layout
Title: RectDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class RectDrawingItem of Dynamsoft Camera Enhancer represents a rectangular drawing item.
Keywords: rectangle, drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# RectDrawingItem

The `RectDrawingItem` class is a subclass of `DrawingItem` that represents a rectangular drawing item.

## Definition

*Assembly:* package com.dynamsoft.dce

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
