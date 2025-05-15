---
layout: default-layout
title: DSDrawingLayer - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSDrawingLayer of Dynamsoft Camera Enhancer represents a drawing layer, which is used for managing and controlling drawing items.
keywords: drawing layer, Dynamsoft Camera Enhancer, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingLayer

The `DSDrawingLayer` class represents a drawing layer, which is used for managing and controlling drawing items.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NS_ASSUME_NONNULL_BEGIN
@interface DSDrawingLayer : NSObject
```
2. 
```swift
class DrawingLayer : NSObject
```

## Constants

| Constants | Description |
| --------- | ----------- |
| `DDN_LAYER_ID` | The preset DrawingLayer of Dynamsoft Document Normalizer. |
| `DBR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Barcode Reader. |
| `DLR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Label Recognizer. |
| `USER_REFINED_LAYER_BASE_ID` | The IDs of user defined Drawinglayers start from 100. |

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`layerId`](#layerid) | *NSInteger* |Get the layer ID of the layer. |
| [`visible`](#visible) | *BOOL* | Set/get the visibility of the layer. |
| [`drawingItems`](#drawingitems) | *NSArray<DrawingItem *> \** | Set/get the drawing items on the layer. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithId`](#initwithid) | Create an DrawingLayer with the specified ID. |
| [`addDrawingItems`](#adddrawingitems) | Add a group of DrawingItem to the layer. |
| [`setDrawingItems`](#setdrawingitems) | Set the DrawingItems to be displayed on the layer. |
| [`getDrawingItems`](#getdrawingitems) | Get all the DrawingItems on the layer. |
| [`setDefaultStyle(style)`](#setdefaultstylestyle) | Set the default style of the layer. |
| [`setDefaultStyle(style,state,mediaType)`](#setdefaultstylestylestatemediatype) | Set the default style of the layer with filter options. |
| [`clearDrawingItems`](#cleardrawingitems) | Remove all DrawingItems from the layer. |

### layerId

Get the layer ID of the layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic, readonly) NSInteger layerId;
```
2. 
```swift
var layerId: Int { get }
```

### visible

Set/get the visibility of the layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) BOOL visible;
```
2. 
```swift
var visible: Bool { get set }
```

### drawingItems

Set/get the drawing items on the layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (atomic, copy, nullable) NSArray<DSDrawingItem *> *drawingItems;
```
2. 
```swift
var drawingItems: [DrawingItem] { get set }
```

### initWithId

Create an DrawingLayer with the specified ID.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithId:(NSInteger)layerId;
```
2. 
```swift
init(id layerId: Int)
```

**Parameters**

`layerId`: The ID of the layer.

### addDrawingItems

Add a group of DrawingItem to the layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)addDrawingItems:(NSArray<DSDrawingItem *> *)items;
```
2. 
```swift
func addDrawingItems(_ items: [DSDrawingItem])
```
**Parameters**

`items`: An array of DrawingItems to be added to the layer.

### setDefaultStyle(style)

Set the default style of the layer. A DrawingItem on the layer will use the default style if it doesn't hold a style attribute.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setDefaultStyle:(NSUInteger)styleId;
```
2. 
```swift
func setDefaultStyle(_ styleId: UInt)
```

**Parameters**

`styleId`: An ID of DrawingStyle.

### setDefaultStyle(style,state,mediaType)

Set the default style of the layer with filter options. A DrawingItem on the layer will use the default style if it doesn't hold a style attribute.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setDefaultStyle:(NSUInteger)styleId
               forState:(NSUInteger)state
                forType:(NSUInteger)type;
```
2. 
```swift
func setDefaultStyle(_ styleId: UInt, forState drawingItemState: UInt, forType drawingItemMediaType: UInt)
```

**Parameters**

`styleId`: An ID of DrawingStyle.  
`forState`: Specify a group of DrawingItem state. It filters which kinds of DrawingItems will use this default style.  
`forType`: Specify a group of DrawingItem media type. It filters which kinds of DrawingItems will use this default style.

### clearDrawingItems

Remove all DrawingItems from the layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)clearDrawingItems;
```
2. 
```swift
func clearDrawingItems()
```
