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

*Assembly:* DynamsoftCameraEnhancer.xcframework

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
| [`line`](#line) | [*DSLineSegment \**]({{ site.dcv_ios_api }}core/basic-structures/line-segment.html) |Get the line information of the DSLineDrawingItem. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithLine`](#initwithline) | Create an instance of DSLineDrawingItem. |

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

### line

The property that stores the line information of the `DSLineDrawingItem` in a [`DSLineSegment`]({{ site.dcv_ios_api }}core/basic-structures/line-segment.html) object.

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

### initWithLine

Create an instance of `DSLineDrawingItem`.

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

`line`: A  [`DSLineSegment`]({{ site.dcv_ios_api }}core/basic-structures/line-segment.html) object that stores the line coordinates information.

**Return Value**

An instance of `DSLineDrawingItem`.

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

### initWithLine:coordinateBase:

Create an instance of `DSLineDrawingItem`.

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

`line`: A  [`DSLineSegment`]({{ site.dcv_ios_api }}core/basic-structures/line-segment.html) object that stores the line coordinates information.

`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `DSLineDrawingItem`.

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
