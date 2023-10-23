---
layout: default-layout
title: DSRectDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSRectDrawingItem of Dynamsoft Camera Enhancer represents a rectangular drawing item.
keywords: rectangle, drawing item, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSRectDrawingItem

The `DSRectDrawingItem` class is a subclass of `DSDrawingItem` that represents a rectangular drawing item.

## Definition

*Assembly:* DynamsoftCameraEnhancer.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSRectDrawingItem : DSDrawingItem
```
2. 
```swift
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

### rect

Get the rect information of the DSRectDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGRect rect;
```
2. 
```swift
var rect: CGRect { get }
```

## initWithRect

Create an instance of DSRectDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithRect:(CGRect)rect;
```
2. 
```swift
init(rect: CGRect)
```
**Parameters**

`rect`: A CGRect that defines the rect of the DSRectDrawingItem.

**Return Value**

An instance of DSRectDrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSRectDrawingItem *item = [[DSRectDrawingItem alloc] initWithRect:rect];
```
2. 
```swift
let item = RectDrawingItem(rect: rect)
```

## initWithRect:coordinateBase

Create an instance of DSRectDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithRect:(CGRect *)rect
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```swift
init(rect: UnsafeMutablePointer<CGRect>, coordinateBase: CoordinateBase)
```
**Parameters**

`rect`: A CGRect that defines the rect of the DSRectDrawingItem.

`coordinateBase`: The coordinate base of the DrawingItem.

**Return Value**

An instance of DSRectDrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSRectDrawingItem *item = [[DSRectDrawingItem alloc] initWithRect:rect
                                                 coordinateBase:coordinateBase];
```
2. 
```swift
let item = RectDrawingItem(rect: &rect, coordinateBase: coordinateBase)
```
