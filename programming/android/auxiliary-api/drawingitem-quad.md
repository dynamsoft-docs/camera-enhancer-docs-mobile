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

### getQuad

Get the quad information of the `QuadDrawingItem`.

```java
com.dynamsoft.core.Quadrilateral getQuad(){}
```

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
