---
layout: default-layout
title: iOS RectDrawingItem Class - Dynamsoft Camera Enhancer Documents
description: This is the documentation - iOS RectDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, RectDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS RectDrawingItem Class
permalink: /programming/ios/auxiliary-api/drawingitem-rect-v3.0.3.html
---

# RectDrawingItem

`RectDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `RectDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface RectDrawingItem (DrawingItem)
```
2. 
```swift
class RectDrawingItem : DrawingItem
```

| Method Name | Description |
| ----------- | ----------- |
| [`initWithRect`](#initwithrect) | The constructor of `RectDrawingItem`. Initialize the instance of `RectDrawingItem`. |
| [`rect`](#rect) | The property that indicates the `Rect` of the `RectDrawingItem`. |
| [`drawingStyleId`](#drawingstyleid) | Get the drawing style of the current `DrawingItem`. |
| [`state`](#state) | Set the state of the current `DrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the current `DrawingItem`. |

&nbsp;

## initWithRect

The constructor of `RectDrawingItem`. Initialize the instance of `RectDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype) initWithRect:(CGRect)rect;
```
2. 
```swift
init(rect: CGRect)
```

**Parameters**

`rect`: A `Rect` that indicates the location of the `RectDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DrawingItem* drawingItem = [[RectDrawingItem alloc] initWithRect:rect];
```
2. 
```swift
let drawingItem = RectDrawingItem.init(rect:rect)
```

&nbsp;

## rect

The property that indicates the `Rect` of the `RectDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic, readonly) CGRect rect;
```
2. 
```swift
var rect: CGRect { get }
```


&nbsp;

## drawingStyleId

The property that identifies the ID of the `DrawingStyle`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) NSInteger drawingStyleId;
```
2. 
```swift
var drawingStyleId: Int { get set }
```

&nbsp;

## state

The property that indicates the state of the `DrawingItem`. View all available `DrawingItem` states in [`EnumDrawingItemState`]({{ site.ios_camera_enhancer }}enum-drawing-item-state.html).

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) EnumDrawingItemState state;
```
2. 
```swift
var state: EnumDrawingItemState { get set }
```

&nbsp;

## getMediaType

Get the media type of the `DrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (EnumDrawingItemMediaType) getMediaType;
```
2. 
```swift
func getMediaType() -> EnumDrawingItemMediaType
```

**Return Value**

The media type of the `DrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
EnumDrawingItemMediaType mediaType = [drawingItem getMediaType];
```
2. 
```swift
let mediaType = drawingItem.getMediaType()
```
