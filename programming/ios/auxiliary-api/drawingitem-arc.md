---
layout: default-layout
title: ArcDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class ArcDrawingItem of Dynamsoft Camera Enhancer represents a drawing item that draws Arcs on the view.
keywords: Arc drawing item, Objective-C, Swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ArcDrawingItem

The `ArcDrawingItem` class is a subclass of `DrawingItem`. It represents a drawing item that draws Arcs on the view.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSArcDrawingItem : DSDrawingItem
```
2. 
```swift
class ArcDrawingItem : DSDrawingItem
```

## Methods & Attributes

| Method | Description |
|------- |-------------|
| [`initWithDrawingStyleId`](#initwithdrawingstyleid) | Create an instance of `ArcDrawingItem` with style, state, centre and radius. |
| [`initWithCentre`](#initwithcentre) | Create an instance of `ArcDrawingItem` with centre and radius. |

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`centre`](#centre) | *CGPoint* | The centre of the `ArcDrawingItem`. |
| [`radius`](#radius) | *CGFloat* | The radius of the `ArcDrawingItem`. |

## Interited Methods

The following methods are inherited from the superclass [`DrawingItem`](drawingitem.html).

| Method | Description |
|------- |-------------|
| [`setDrawingStyleId`](drawingitem.html#setdrawingstyleid) | Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer. |
| [`getDrawingStyleId`](drawingitem.html#getdrawingstyleid) | Get the DrawingStyle of the `DrawingItem`. |
| [`setState`](drawingitem.html#setstate) | Set the state of the `DrawingItem`. |
| [`getState`](drawingitem.html#getstate) | Get the state of the `DrawingItem`. |
| [`getCoordinateBase`](drawingitem.html#getcoordinatebase) | Get the coordinate base of the `DrawingItem`. The coordinate base is image by default. |
| [`getMediaType`](drawingitem.html#getmediatype) | Get the media type of the `DrawingItem`. |
| [`addNote`](drawingitem.html#addnote) | Add a note to the `DrawingItem`. |
| [`getNote`](drawingitem.html#getnote) | Get the specified `Note`. |
| [`hasNote`](drawingitem.html#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](drawingitem.html#updatenote) | Update the content of the specified `Note`. |
| [`deleteNote`](drawingitem.html#deletenote) | Remove the specified `Note` with the specified name. |
| [`getAllNotes`](drawingitem.html#getallnotes) | Get all `Notes` of this DrawingItem. |
| [`clearNotes`](drawingitem.html#clearnotes) | Remove all `Notes` of this DrawingItem. |

### initWithDrawingStyleId

Create an instance of `ArcDrawingItem` with style, state, centre and radius.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithDrawingStyleId:(NSUInteger)styleId
                                 state:(DSDrawingItemState)state
                                centre:(CGPoint)centre
                                radius:(CGFloat)radius;
```
2. 
```swift
func initWithDrawingStyleId(styleId: UInt, state: DSDrawingItemState, centre: CGPoint, radius: CGFloat) -> ArcDrawingItem
```

**Parameters**

`styleId`: The drawing style ID of the `ArcDrawingItem`. If the style ID is 0, the `ArcDrawingItem` will use the default style.

`state`: The state of the `ArcDrawingItem`.

`centre`: The centre of the `ArcDrawingItem`.

`radius`: The radius of the `ArcDrawingItem`.

**Return Value**

An `ArcDrawingItem` object.

### initWithCentre

Create an instance of `ArcDrawingItem` with centre and radius.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithCentre:(CGPoint)centre radius:(CGFloat)radius;
```
2. 
```swift
func initWithCentre(centre: CGPoint, radius: CGFloat) -> ArcDrawingItem
```

**Parameters**

`centre`: The centre of the `ArcDrawingItem`.

`radius`: The radius of the `ArcDrawingItem`.

**Return Value**

An `ArcDrawingItem` object.

### centre

Get the centre of the `ArcDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign, readonly) CGPoint centre;
```
2. 
```swift
var centre: CGPoint { get }
```

### radius

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign, readonly) CGFloat radius;
```
2. 
```swift
var radius: CGFloat { get }
```
