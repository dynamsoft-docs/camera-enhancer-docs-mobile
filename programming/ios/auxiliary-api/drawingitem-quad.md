---
layout: default-layout
title: DSQuadDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSQuadDrawingItem of Dynamsoft Camera Enhancer represents a drawing item that draws quadrilaterals on the view.
keywords: quad drawing item, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSQuadDrawingItem

The `DSQuadDrawingItem` class is a subclass of `DSDrawingItem`. It represents a drawing item that draws quadrilaterals on the view.

## Definition

*Assembly:* DynamsoftCameraEnhancer.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSQuadDrawingItem : DSDrawingItem
```
2. 
```swift
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

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(strong, nonatomic, readonly) DSQuadrilateral *quad;
```
2. 
```swift
var quad: DSQuadrilateral { get }
```

### initWithQuad

Create an instance of `DSQuadDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithQuad:(DSQuadrilateral *)quad;
```
2. 
```swift
init(quad: DSQuadrilateral)
```

**Parameters**

`quad`: A `DSQuadrilateral` object that stores the quadrilateral coordinates information.

**Return Value**

An instance of `DSQuadDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSQuadDrawingItem *item = [[DSQuadDrawingItem alloc] initWithQuad:quad];
```
2. 
```swift
let item = QuadDrawingItem(quad: quad)
```

### initWithQuad:coordinateBase

Create an instance of `DSQuadDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithQuad:(DSQuadrilateral *)quad 
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```swift
init(quad: DSQuadrilateral, coordinateBase: DSCoordinateBase)
```

**Parameters**

`quad`: A `DSQuadrilateral` object that stores the quadrilateral coordinates information.

`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `DSQuadDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSQuadDrawingItem *item = [[DSQuadDrawingItem alloc] initWithQuad:quad coordinateBase:base];
```
2. 
```swift
let item = QuadDrawingItem(quad: quad, coordinateBase: base)
```
