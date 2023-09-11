---
layout: default-layout
title: DSLineDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSLineDrawingItem of Dynamsoft Camera Enhancer represents a line drawing item used for drawing line segments on the view.
keywords: line drawing item, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSLineDrawingItem

The `DSLineDrawingItem` class is a subclass of `DSDrawingItem` and represents a line drawing item used for drawing line segments on the view.

## Definition

*Assembly:* DynamsoftCameraEnhancer.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSLineDrawingItem : DSDrawingItem
```
2. 
```swift
class LineDrawingItem : DSDrawingItem
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

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) DSLineSegment *line;
```
2. 
```swift
var line: DSLineSegment { get }
```

## initWithLine

Create an instance of DSLineDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithLine:(DSLineSegment *)line;
```
2. 
```swift
init(line: DSLineSegment)
```
**Parameters**

`line`: A DSLineSegment object that stores the line coordinates information.

**Return Value**

An instance of DSLineDrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSLineSegment *line = [[DSLineSegment alloc] init];
DSLineDrawingItem *item = [[DSLineDrawingItem alloc] initWithLine:line];
```
2. 
```swift
let line = DSLineSegment()
let item = DSLineDrawingItem(line: line)
```

## initWithLine:coordinateBase:

Create an instance of DSLineDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithLine:(DSLineSegment *)line
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```swift
init(line: DSLineSegment, coordinateBase: DSCoordinateBase)
```
**Parameters**

`line`: A DSLineSegment object that stores the line coordinates information.

`coordinateBase`: The coordinate base of the DrawingItem.

**Return Value**

An instance of DSLineDrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSLineSegment *line = [[DSLineSegment alloc] init];
DSLineDrawingItem *item = [[DSLineDrawingItem alloc] initWithLine:line coordinateBase:DSCoordinateBaseView];
```
2. 
```swift
let line = DSLineSegment()
let item = DSLineDrawingItem(line: line, coordinateBase: .view)
```
