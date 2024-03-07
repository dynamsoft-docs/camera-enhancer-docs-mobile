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

*Assembly:* DynamsoftCameraEnhancer.xcframework

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

## Interited Attributes

The following attributes are inherited from the base class [`DrawingItem`](drawingitem.html).

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`drawingStyleId`](drawingitem.html#drawingstyleid) | *NSInteger* | The DrawingStyle of the DrawingItem. If a DrawingItem holds a drawingStyleId, it will not use the default style of its layer. |
| [`state`](drawingitem.html#state) | *DSDrawingItemState* | The state of the DrawingItem. |
| [`CoordinateBase`](drawingitem.html#coordinatebase) | *DSCoordinateBase* | The coordinate base of the DrawingItem. The coordinate base is image by default. |

## Interited Methods

The following methods are inherited from the base class [`DrawingItem`](drawingitem.html).

| Method | Description |
|------- |-------------|
| [`getMediaType`](drawingitem.html#getmediatype) | Get the media type of the DrawingItem. |
| [`addNote`](drawingitem.html#addnote) | Add a note to the DrawingItem. |
| [`getNote`](drawingitem.html#getnote) | Get the specified DSNote. |
| [`hasNote`](drawingitem.html#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](drawingitem.html#updatenote) | Update the content of the specified DSNote. |
| [`deleteNote`](drawingitem.html#deletenote) | Remove the specified DSNote with the specified name. |
| [`getAllNotes`](drawingitem.html#getallnotes) | Get all DSNotes of this DrawingItem. |
| [`clearNotes`](drawingitem.html#clearnotes) | Remove all DSNotes of this DrawingItem. |

### quad

The property that stores the coordinate information of the `DSQuadDrawingItem` in a [`DSQuadrilateral`]({{ site.dcv_ios_api }}core/basic-structures/quadrilateral.html) object.

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

`quad`: A [`DSQuadrilateral`]({{ site.dcv_ios_api }}core/basic-structures/quadrilateral.html) object that stores the quadrilateral coordinates information.

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

`quad`: A [`DSQuadrilateral`]({{ site.dcv_ios_api }}core/basic-structures/quadrilateral.html) object that stores the quadrilateral coordinates information.

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
