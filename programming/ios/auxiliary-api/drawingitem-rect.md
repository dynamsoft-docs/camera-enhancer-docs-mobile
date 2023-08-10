---
layout: default-layout
Title: DSRectDrawingItem - Dynamsoft Camera Enhancer iOS Edition API Reference
Description: The class DSRectDrawingItem of Dynamsoft Camera Enhancer represents a rectangular drawing item.
Keywords: rectangle, drawing item, objective-c, swift
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
