---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DCEDrawingLayer Class
description: This is the documentation - iOS DCEDrawingLayer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, DCEDrawingLayer
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DCEDrawingLayer Class
---

# DCEDrawingLayer

| Method Name | Description |
| ----------- | ----------- |
| [`id`](#id) | Get the layer ID of the layer. |
| [`addDrawingItems`](#adddrawingitems) | Add a list of drawing items to the layer. These drawing items will be appended to the drawing item list of the current layer. |
| [`setDrawingItems`](#setdrawingitems) | Set a list of drawing items to the layer. These drawing items will replace the previous drawing items of the current layer. |
| [`getDrawingItems`](#getdrawingitems) | Get all available drawing items in the layer. |
| [`clearDrawingItems`](#cleardrawingitems) | Clear all available drawing items in the layer. |
| [`setDrawingStyle`](#setdrawingstyle) |  |
| [`getDrawingStyle`] |  |
| [`visible`](#visible) | The property that stores the visibility of the layer. |

## id

Get the layer ID of the layer.

```objc
@property (assign, nonatomic) NSInteger id;
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

## addDrawingItems

Add a list of drawing items to the layer. These drawing items will be appended to the drawing item list of the current layer.

```objc
- (void) addDrawingItems:(NSArray<DrawingItem*>*)items; 
```

**Parameters**

`items`: A list of drawing items.

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

## setDrawingItems

Set a list of drawing items to the layer. These drawing items will replace the previous drawing items of the current layer.

```objc
- (void) setDrawingItems:(NSArray<DrawingItem*>*)items; 
```

**Parameters**

`items`: A list of drawing items.

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

## getDrawingItems

Get all available drawing items in the layer.

```objc
- (NSArray<DrawingItem*>* _Nullable) getDrawingItems;
```

**Return Value**

A list that includes all available drawing items.

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

## clearDrawingItems

Clear all available drawing items in the layer.

```objc
- (void) clearDrawingItems;
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

## setDrawingStyle

## getDrawingStyle

## visible

The property that stores the visibility of the layer.

```objc
// When visible is true, the layer is visible.
// Otherwise, the layer is invisible.
@property (assign, nonatomic) BOOL visible;
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
