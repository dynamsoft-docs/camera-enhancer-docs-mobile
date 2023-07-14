---
layout: default-layout
Title: LineDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSLineDrawingItem of Dynamsoft Camera Enhancer represents a line drawing item used for drawing line segments on the view.
Keywords: line drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSLineDrawingItem

The `DSLineDrawingItem` class is a subclass of `DSDrawingItem` and represents a line drawing item used for drawing line segments on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class LineDrawingItem extends DrawingItem
```
2. 
```kotlin
class LineDrawingItem extends DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`line`](#line) | *DSLineSegment \** |Get the line information of the DSLineDrawingItem. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithLine`](#initwithline) | Create an instance of DSLineDrawingItem. |

### line

Get the line information of the DSLineDrawingItem.

```java
@property(nonatomic, readonly) DSLineSegment *line;
```
2. 
```kotlin
var lineextends LineSegment { get }
```

## initWithLine

Create an instance of DSLineDrawingItem.

```java
- (instancetype)initWithLine:(DSLineSegment *)line;
```
2. 
```kotlin
init(lineextends LineSegment)
```
**Parameters**

`line`: A DSLineSegment object that stores the line coordinates information.

**Return Value**

An instance of DSLineDrawingItem.

**Code Snippet**

```java
DSLineSegment *line = [[DSLineSegment alloc] init];
DSLineDrawingItem *item = [[DSLineDrawingItem alloc] initWithLine:line];
```
2. 
```kotlin
let line = DSLineSegment()
let item = DSLineDrawingItem(line: line)
```

## initWithLine:coordinateBase:

Create an instance of DSLineDrawingItem.

```java
- (instancetype)initWithLine:(DSLineSegment *)line
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```kotlin
init(lineextends LineSegment, coordinateBaseextends CoordinateBase)
```
**Parameters**

`line`: A DSLineSegment object that stores the line coordinates information.

`coordinateBase`: The coordinate base of the DrawingItem.

**Return Value**

An instance of DSLineDrawingItem.

**Code Snippet**

```java
DSLineSegment *line = [[DSLineSegment alloc] init];
DSLineDrawingItem *item = [[DSLineDrawingItem alloc] initWithLine:line coordinateBase:DSCoordinateBaseView];
```
2. 
```kotlin
let line = DSLineSegment()
let item = DSLineDrawingItem(line: line, coordinateBase: .view)
```
