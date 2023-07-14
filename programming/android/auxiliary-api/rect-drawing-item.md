---
layout: default-layout
Title: RectDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSRectDrawingItem of Dynamsoft Camera Enhancer represents a rectangular drawing item.
Keywords: rectangle, drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSRectDrawingItem

The `DSRectDrawingItem` class is a subclass of `DSDrawingItem` that represents a rectangular drawing item.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class RectDrawingItem extends DrawingItem
```
2. 
```kotlin
class RectDrawingItem : DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`rect`](#rect) | *CGRect* |Get the rect information of the DSRectDrawingItem. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithRect`](#initwithrect) | Create an instance of DSRectDrawingItem. |
| [`initWithRect:coordinateBase`](#initwithrectcoordinatebase) | Create an instance of DSRectDrawingItem. |

### rect

Get the rect information of the DSRectDrawingItem.

```java
@property(nonatomic, readonly) CGRect rect;
```
2. 
```kotlin
var rect: CGRect { get }
```

## initWithRect

Create an instance of DSRectDrawingItem.

```java
- (instancetype)initWithRect:(CGRect)rect;
```
2. 
```kotlin
init(rect: CGRect)
```
**Parameters**

`rect`: A CGRect that defines the rect of the DSRectDrawingItem.

**Return Value**

An instance of DSRectDrawingItem.

**Code Snippet**

```java
DSRectDrawingItem *item = [[DSRectDrawingItem alloc] initWithRect:rect];
```
2. 
```kotlin
let item = RectDrawingItem(rect: rect)
```

## initWithRect:coordinateBase

Create an instance of DSRectDrawingItem.

```java
- (instancetype)initWithRect:(CGRect *)rect
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```kotlin
init(rect: UnsafeMutablePointer<CGRect>, coordinateBase: CoordinateBase)
```
**Parameters**

`rect`: A CGRect that defines the rect of the DSRectDrawingItem.

`coordinateBase`: The coordinate base of the DrawingItem.

**Return Value**

An instance of DSRectDrawingItem.

**Code Snippet**

```java
DSRectDrawingItem *item = [[DSRectDrawingItem alloc] initWithRect:rect
                                                 coordinateBase:coordinateBase];
```
2. 
```kotlin
let item = RectDrawingItem(rect: &rect, coordinateBase: coordinateBase)
```
