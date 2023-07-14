---
layout: default-layout
Title: QuadDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSQuadDrawingItem of Dynamsoft Camera Enhancer represents a drawing item that draws quadrilaterals on the view.
Keywords: quad drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSQuadDrawingItem

The `DSQuadDrawingItem` class is a subclass of `DSDrawingItem`. It represents a drawing item that draws quadrilaterals on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class QuadDrawingItem extends DrawingItem
```
2. 
```kotlin
class QuadDrawingItem : DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`quad`](#quad) | *DSQuadrilateral \** |Get the quadrilateral information of the `DSQuadDrawingItem`. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithQuad`](#initwithquad) | Create an instance of `DSQuadDrawingItem`. |

### quad

Get the quadrilateral information of the `DSQuadDrawingItem`.

```java
@property(strong, nonatomic, readonly) DSQuadrilateral *quad;
```
2. 
```kotlin
var quadextends Quadrilateral { get }
```

### initWithQuad

Create an instance of `DSQuadDrawingItem`.

```java
- (instancetype)initWithQuad:(DSQuadrilateral *)quad;
```
2. 
```kotlin
init(quadextends Quadrilateral)
```

**Parameters**

`quad`: A `DSQuadrilateral` object that stores the quadrilateral coordinates information.

**Return Value**

An instance of `DSQuadDrawingItem`.

**Code Snippet**

```java
DSQuadDrawingItem *item = [[DSQuadDrawingItem alloc] initWithQuad:quad];
```
2. 
```kotlin
let item = QuadDrawingItem(quad: quad)
```

### initWithQuad:coordinateBase

Create an instance of `DSQuadDrawingItem`.

```java
- (instancetype)initWithQuad:(DSQuadrilateral *)quad 
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```kotlin
init(quadextends Quadrilateral, coordinateBaseextends CoordinateBase)
```

**Parameters**

`quad`: A `DSQuadrilateral` object that stores the quadrilateral coordinates information.

`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `DSQuadDrawingItem`.

**Code Snippet**

```java
DSQuadDrawingItem *item = [[DSQuadDrawingItem alloc] initWithQuad:quad coordinateBase:base];
```
2. 
```kotlin
let item = QuadDrawingItem(quad: quad, coordinateBase: base)
```
