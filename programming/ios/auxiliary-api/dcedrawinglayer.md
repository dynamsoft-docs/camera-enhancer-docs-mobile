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
| [`setDrawingStyleId(styleId)`](#setdrawingstyleidstyleid) | Set the `DrawingStyle` of the `DrawingLayer` by ID. |
| [`setDrawingStyleId(styleId,state)`](#setdrawingstyleidstyleidstate) | Set the `DrawingStyle` of the `DrawingLayer` by ID. |
| [`setDrawingStyleId(styleId,state,mediaType)`](#setdrawingstyleidstyleidstatemediatype) | Set the `DrawingStyle` of the `DrawingLayer` by ID. |
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
DCEDrawingLayer* drawingLayer = [[DCEDrawingLayer alloc] initWithId: 0];
```
2. 
```swift
var drawingLayer:DCEDrawingLayer! = DCEDrawingLayer.init(id:0)
```

## id

The ID of the `DrawingLayer`.

```objc
@property (assign, nonatomic) NSInteger id;
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
NSMutableArray<DrawingItem*>* drawingItems = [drawingLayer getDrawingItems];
DrawingItem* rectDrawingItem = [[RectDrawingItem alloc] initWithRect: CGRectMake(100,100,300,300)];
DrawingItem* textDrawingItem = [[TextDrawingItem alloc] initWithText:@"Your-Text" textRect:CGRectMake(100,100,300,300)];
[drawingItems insertObject:rectDrawingItem atIndex:0];
[drawingItems insertObject:textDrawingItem atIndex:0];
[drawingLayer addDrawingItems:drawingItems coordinateSystem:EnumCoordinateSystemImage];
```
2. 
```swift
let drawingItems = drawingLayer.getDrawingItems()
let rectDrawingItem = RectDrawingItem.init(rect: CGRect(x:100, y:100, width:300, height:300))
let textDrawingItem = TextDrawingItem.init(text:"Your-Text" rect: CGRect(x:100, y:100, width:300, height:300))
drawingItems.add(rectDrawingItem)
drawingItems.add(textDrawingItem)
drawingLayer.addDrawingItems(drawingItems)
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
NSMutableArray<DrawingItem*>* drawingItems = [drawingLayer getDrawingItems];
DrawingItem* rectDrawingItem = [[RectDrawingItem alloc] initWithRect: CGRectMake(100,100,300,300)];
DrawingItem* textDrawingItem = [[TextDrawingItem alloc] initWithText:@"Your-Text" textRect:CGRectMake(100,100,300,300)];
[drawingItems insertObject:rectDrawingItem atIndex:0];
[drawingItems insertObject:textDrawingItem atIndex:0];
[drawingLayer setDrawingItems:drawingItems coordinateSystem:EnumCoordinateSystemImage];
```
2. 
```swift
let drawingItems = drawingLayer.getDrawingItems()
let rectDrawingItem = RectDrawingItem.init(rect: CGRect(x:100, y:100, width:300, height:300))
let textDrawingItem = TextDrawingItem.init(text:"Your-Text" rect: CGRect(x:100, y:100, width:300, height:300))
drawingItems.add(rectDrawingItem)
drawingItems.add(textDrawingItem)
drawingLayer.setDrawingItems(drawingItems)
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

Please view the code snippet in [`setDrawingItems`](#setdrawingitems).

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
[drawingLayer clearDrawingItems];
```
2. 
```swift
drawingLayer.clearDrawingItems()
```

&nbsp;

## setDrawingStyleId(styleId)

Specify a style ID for all available `DrawingItems`.

```objc
- (void) setDrawingStyleId:(NSInteger)styleId;
```

**Parameters**

`styleId`: The style ID.  

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[drawingLayer setDrawingStyleId:0];
```
2. 
```swift
drawingLayer.setDrawingStyleId(0)
```

&nbsp;

## setDrawingStyleId(styleId,state)

Specify a style ID for the targeting `DrawingItems`.

```objc
- (void) setDrawingStyleId:(NSInteger)styleId
                     state:(EnumDrawingItemState)state;
```

**Parameters**

`styleId`: The style ID.  
`state`: The state of the `DrawingLayer`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[drawingLayer setDrawingStyleId:0 state:EnumDrawingItemStateSelected];
```
2. 
```swift
drawingLayer.setDrawingStyleId(0, state:EnumDrawingItemState.selected)
```

&nbsp;

## setDrawingStyleId(styleId,state,mediaType)

Specify a style ID for the targeting `DrawingItems`.

```objc
- (void) setDrawingStyleId:(NSInteger)styleId
                     state:(EnumDrawingItemState)state
                mediaTypes:(NSArray*)mediaTypes;
```

**Parameters**

`styleId`: The style ID.  
`state`: The state of the `DrawingLayer`.  
`mediaType`: The media type of the `DrawingLayer`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[drawingLayer setDrawingStyleId:0 state:EnumDrawingItemStateSelected mediaType:@[@(EnumDrawingItemMediaTypeRectangle), @(EnumDrawingItemMediaTypeQuadrilateral)]];
```
2. 
```swift
drawingLayer.setDrawingStyleId(0, state:EnumDrawingItemState.selected, mediaType:[EnumDrawingItemMediaType.quadrilateral.rawValue, EnumDrawingItemMediaType.rectangle.rawValue])
```

&nbsp;

## visible

The property that stores the visibility of the `DrawingLayer`.

```objc
// When visible is true, the `DrawingLayer` is visible.
// Otherwise, the `DrawingLayer` is invisible.
@property (assign, nonatomic) BOOL visible;
```
