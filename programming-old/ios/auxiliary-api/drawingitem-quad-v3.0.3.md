---
layout: default-layout
title: iOS QuadDrawingItem Class - Dynamsoft Camera Enhancer Documents
description: This is the documentation - iOS QuadDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, QuadDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS QuadDrawingItem Class
permalink: /programming/ios/auxiliary-api/drawingitem-quad-v3.0.3.html
---

# QuadDrawingItem

`QuadDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `QuadDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface QuadDrawingItem (DrawingItem)
```
2. 
```swift
class QuadDrawingItem : DrawingItem
```

| Method Name | Description |
| ----------- | ----------- |
| [`initWithQuad`](#initwithquad) | The constructor of `QuadDrawingItem`. Initialize the instance of `QuadDrawingItem`. |
| [`quad`](#quad) | The `Quadrilateral` property that indicates the position of the `QuadDrawingItem`. |
| [`drawingStyleId`](#drawingstyleid) | Get the drawing style of the current `DrawingItem`. |
| [`state`](#state) | Set the state of the current `DrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the current `DrawingItem`. |

&nbsp;

## initWithQuad

The constructor of `QuadDrawingItem`. Initialize the instance of `QuadDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype) initWithQuad:(Quadrilateral*)quad;
```
2. 
```swift
init(quad: iQuadrilateral)
```

**Parameters**

`quad`: A `Quadrilateral` that includes the position of the `QuadDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DrawingItem* drawingItem = [[QuadDrawingItem alloc] initWithQuad:quad];
```
2. 
```swift
let drawingItem = QuadDrawingItem.init(quad:quad)
```

&nbsp;

## quad

The `Quadrilateral` property that indicates the position of the `QuadDrawingItem`.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic, readonly) Quadrilateral* quad; 
```
2. 
```swift
var quad: iQuadrilateral { get }
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
