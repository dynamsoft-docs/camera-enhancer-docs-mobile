---
layout: default-layout
title: DSTextDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSTextDrawingItem of Dynamsoft Camera Enhancer represents a text drawing item, which can be added to draw texts on the view.
keywords: text drawing item, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSTextDrawingItem

The `DSTextDrawingItem` class is a subclass of `DSDrawingItem` and represents a text drawing item, which can be added to draw texts on the view.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSTextDrawingItem : DSDrawingItem
```
2. 
```swift
class TextDrawingItem : DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`text`](#text) | *NSString \** |Get the text content of the DSTextDrawingItem. |
| [`topLeftPoint`](#topleftpoint) | *CGPoint* |Get the top-left point of the DSTextDrawingItem. |
| [`width`](#width) | *NSInteger* |Get the width of the DSTextDrawingItem. |
| [`height`](#height) | *NSInteger* |Get the height of the DSTextDrawingItem. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithText`](#initwithtext) | Create an instance of DSTextDrawingItem. |
| [`initWithText:coordinateBase:`](#initwithtextcoordinatebase) | Create an instance of DSTextDrawingItem with coordinate base. |

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

### text

Get the text content of the DSTextDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, copy, readonly) NSString *text;
```
2. 
```swift
var text: String { get }
```

### topLeftPoint

Get the top-left point of the DSTextDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, readonly) CGPoint topLeftPoint;
```
2. 
```swift
var topLeftPoint: CGPoint { get }
```

### width

Get the width of the DSTextDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, readonly) NSInteger width;
```
2. 
```swift
var width: Int { get }
```

### height

Get the height of the DSTextDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, readonly) NSInteger height;
```
2. 
```swift
var height: Int { get }
```

### initWithText

Create an instance of DSTextDrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithText:(NSString *)text
                topLeftPoint:(CGPoint)topLeftPoint
                       width:(NSInteger)width
                      height:(NSInteger)height;
```
2. 
```swift
init(text: String, topLeftPoint: CGPoint, width: Int, height: Int)
```
**Parameters**

`text`: The text content of the DSTextDrawingItem.  
`topLeftPoint`: The top-left point of the DSTextDrawingItem.  
`width`: The width of the DSTextDrawingItem.  
`height`: The height of the DSTextDrawingItem.  

**Return Value**

An instance of DSTextDrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSTextDrawingItem *item = [[DSTextDrawingItem alloc] initWithText:@"Hello, World!" topLeftPoint:CGPointMake(0, 0) width:100 height:50];
```
2. 
```swift
let item = TextDrawingItem(text: "Hello, World!", topLeftPoint: CGPoint(x: 0, y: 0), width: 100, height: 50)
```

### initWithText:coordinateBase:

Create an instance of DSTextDrawingItem with coordinate base.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithText:(NSString *)text
                topLeftPoint:(CGPoint)topLeftPoint
                       width:(NSInteger)width
                      height:(NSInteger)height
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```swift
init(text: String, topLeftPoint: CGPoint, width: Int, height: Int, coordinateBase: CoordinateBase)
```

**Parameters**

`text`: The text content of the DSTextDrawingItem.  
`topLeftPoint`: The top-left point of the DSTextDrawingItem.  
`width`: The width of the DSTextDrawingItem.  
`height`: The height of the DSTextDrawingItem.  
`coordinateBase`: The coordinate base of the DrawingItem.  

**Return Value**

An instance of `DSTextDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSTextDrawingItem *item = [[DSTextDrawingItem alloc] initWithText:@"Hello, World!" topLeftPoint:CGPointMake(0, 0) width:100 height:50 coordinateBase:DSCoordinateBase_View];
```
2. 
```swift
let item = TextDrawingItem(text: "Hello, World!", topLeftPoint: CGPoint(x: 0, y: 0), width: 100, height: 50, coordinateBase: .view)
```
