---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DrawingItem Class
description: This is the documentation - iOS DrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, DrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DrawingItem Class
---

# DrawingItem

```objc
@interface DrawingItem
```

| Method Name | Description |
| ----------- | ----------- |
| [`drawingStyleId`](#drawingstyle) | Get the drawing style of the current `DrawingItem`. |
| [`state`](#state) | Set the state of the current `DrawingItem`. |
| [`coordinateSystem`](#coordinatesystem) | Get the coordinate system of the current `DrawingItem`. |
| [`mediaType`](#mediatype) | Get the media type of the current `DrawingItem`. |

&nbsp;

## drawingStyleId

The property that identifies the ID of the `DrawingStyle`.

```objc
@property (assign, nonatomic) NSInteger drawingStyleId;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

&nbsp;

## state

The property that indicates the state of the `DrawingItem`. View all available `DrawingItem` states in [`EnumDrawingItemState`]({{ site.enumerations }}enum-drawing-item-state.html).

```objc
@property (assign, nonatomic) EnumDrawingItemState state;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

&nbsp;

## coordinateSystem

The property that indicates the coordinate system of the `DrawingItem`. It can be the image coordinate or the view coordinate. View all available `DrawingItem` coordinate systems in [`EnumCoordinateSystem`]({{ site.enumerations }}enum-coordinate-system.html).

```objc
@property (assign, nonatomic) EnumCoordinateSystem coordinateSystem;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

## mediaType

The property that indicates the media type of the `DrawingItem`.

```objc
@property (assign, nonatomic, readonly) EnumDrawingItemMeidaType mediaType;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```
