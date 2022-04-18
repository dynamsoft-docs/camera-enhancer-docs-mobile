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
| [`initWithId`](#dcedrawinglayer) | The constructor of the `DCEDrawingLayer` class. |
| [`id`](#id) | Get the `DrawingLayer` ID of the `DrawingLayer`. |
| [`addDrawingItems`](#adddrawingitems) | Add a list of `DrawingItems` to the `DrawingLayer`. These `DrawingItems` will be appended to the `DrawingItem` list of the current `DrawingLayer`. |
| [`setDrawingItems`](#setdrawingitems) | Set a list of `DrawingItems` to the `DrawingLayer`. These `DrawingItems` will replace the previous `DrawingItems` of the current `DrawingLayer`. |
| [`getDrawingItems`](#getdrawingitems) | Get all available `DrawingItems` in the `DrawingLayer`. |
| [`clearDrawingItems`](#cleardrawingitems) | Clear all available `DrawingItems` in the `DrawingLayer`. |
| [`setDrawingStyleId`](#setdrawingstyle) | Set the style of the `DrawingLayer` by ID. |
| [`visible`](#visible) | The property that stores the visibility of the `DrawingLayer`. |

&nbsp;

## initWithId

The constructor of the `DCEDrawingLayer` class. Initialize the instance of the `DCEDrawingLayer` class.

```objc
- (instancetype) initWithId:(NSInteger)id;
```

**Parameters**

`id`: Indicates the id of the layer.

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

## id

Get the ID of the `DrawingLayer`.

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

&nbsp;

## addDrawingItems

Add a list of `DrawingItems` to the `DrawingLayer`. These `DrawingItems` will be appended to the `DrawingItem` list of the current `DrawingLayer`.

```objc
- (void) addDrawingItems:(NSArray<DrawingItem*>*)items; 
```

**Parameters**

`items`: A list of `DrawingItems`.

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

## setDrawingItems

Set a list of `DrawingItems` to the `DrawingLayer`. These `DrawingItems` will replace the previous `DrawingItems` of the current `DrawingLayer`.

```objc
- (void) setDrawingItems:(NSArray<DrawingItem*>*)items; 
```

**Parameters**

`items`: A list of `DrawingItems`.

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

## getDrawingItems

Get all available `DrawingItems` in the `DrawingLayer`.

```objc
- (NSArray<DrawingItem*>* _Nullable) getDrawingItems;
```

**Return Value**

A list that includes all available `DrawingItems`.

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

## clearDrawingItems

Clear all available `DrawingItems` in the `DrawingLayer`.

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

&nbsp;

## setDrawingStyleId

Set the style of the `DrawingLayer` by ID.

```objc
- (void) setDrawingStyleId:(NSInteger)styleId;
// Or
- (void) setDrawingStyleId:(NSInteger)styleId
                     state:(EnumDrawingItemState)state;
// Or
- (void) setDrawingStyleId:(NSInteger)styleId
                     state:(EnumDrawingItemState)state
                mediaTypes:(NSArray*)mediaTypes;
```

**Parameters**

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

## visible

The property that stores the visibility of the `DrawingLayer`.

```objc
// When visible is true, the `DrawingLayer` is visible.
// Otherwise, the `DrawingLayer` is invisible.
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
