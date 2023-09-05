---
layout: default-layout
title: DSImageEditorView - Dynamsoft Core Module iOS Edition API Reference
description: The class DSImageEditorView of Dynamsoft Core Module represents an image editor view, which allows users to add interactable UI elements on the view.
keywords: image editor view, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSImageEditorView

The `DSImageEditorView` class represents an image editor view, which allows users to add interactable UI elements on the view.

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSImageEditorView : UIView
```
2. 
```swift
class ImageEditorView : UIView
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`tipConfig`](#tipconfig) | *DSTipConfig* | Set/get the tip configurations. |
| [`tipVisible`](#tipvisible) | *BOOL* | Set/get the visibility of tip. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithFrame`](#initwithframe) | Create an instance of DSCameraView. |
| [`setOriginalImage`](#setoriginalimage) | Set the original image that displayed on the view. |
| [`getOriginalImage`](#getoriginalimage) | Get the original image that displayed on the view. |
| [`getSelectedDrawingItem`](#getselecteddrawingitem) | Get the selected DrawingItem. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the specified DrawingLayer. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a new DrawingLayer. |
| [`deleteUserDefinedDrawingLayer`](#deleteuserdefineddrawinglayer) | Delete the specified drawing layer. |
| [`clearUserDefinedDrawingLayers`](#clearuserdefineddrawinglayers) | Clear all the user-defined drawing layers. |
| [`getAllDrawingLayers`](#getalldrawinglayers) | Get all the drawing layers on the view. |
| [`updateTipMessage`](#updatetipmessage) | Update the tip message. |
| [`setOriginalImageWithUIImage`](#setoriginalimagewithuiimage) | Set the original image that displayed on the view. |

### initWithFrame

Create an instance of DSImageEditorView.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithFrame:(CGRect)frame;
```
2. 
```swift
init(frame: CGRect)
```

**Parameters**

`frame`: A CGRect value that defines the position of the view.

**Return Value**

An instance of DSImageEditorView.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSImageEditorView *editorView = [[DSImageEditorView alloc] initWithFrame:frame];
```
2. 
```swift
let editorView = DSImageEditorView(frame: frame)
```

### setOriginalImage

Set the original image that displayed on the view.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setOriginalImage:(DSImageData *)imageData;
```
2. 
```swift
func setOriginalImage(_ image: DSImageData)
```

**Parameters**

`imageData`: A DSImageData object as the original.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSImageData *imageData = [[DSImageData alloc] init];
[editorView setOriginalImage:imageData];
```
2. 
```swift
let imageData = DSImageData()
editorView.setOriginalImage(imageData)
```

### getOriginalImage

Get the original image that displayed on the view.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSImageData *)getOriginalImage;
```
2. 
```swift
func getOriginalImage() -> DSImageData
```

**Return Value**

A UIImage object as the original.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSImageData *originalImage = [editorView getOriginalImage];
```
2. 
```swift
let originalImage = editorView.getOriginalImage()
```

### getSelectedDrawingItem

Get the selected DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (nullable DSDrawingItem *)getSelectedDrawingItem;
```
2. 
```swift
func getSelectedDrawingItem() -> DSDrawingItem?
```

**Return Value**

The selected DrawingItem.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingItem *selectedItem = [editorView getSelectedDrawingItem];
```
2. 
```swift
let selectedItem = editorView.getSelectedDrawingItem()
```

### getDrawingLayer

Get the specified DrawingLayer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSDrawingLayer *)getDrawingLayer:(NSInteger)layerId;
```
2. 
```swift
func getDrawingLayer(_ layerId: Int) -> DSDrawingLayer
```

**Parameters**

`layerId`: The ID of the layer that you want to get.

**Return Value**

The object of the targeting layer.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingLayer *drawingLayer = [editorView getDrawingLayer:layerId];
```
2. 
```swift
let drawingLayer = editorView.getDrawingLayer(layerId)
```

### createDrawingLayer

Create a new DrawingLayer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSDrawingLayer *)createDrawingLayer;
```
2. 
```swift
func createDrawingLayer() -> DSDrawingLayer
```

**Return Value**

The object of the layer you created.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingLayer *drawingLayer = [editorView createDrawingLayer];
```
2. 
```swift
let drawingLayer = editorView.createDrawingLayer()
```

### deleteUserDefinedDrawingLayer

Delete the specified drawing layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)deleteUserDefinedDrawingLayer:(NSInteger)layerId;
```
2. 
```swift
func deleteUserDefinedDrawingLayer(_ layerId: Int)
```

**Parameters**

`layerId`: The ID of the layer that you want to delete.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[editorView deleteUserDefinedDrawingLayer:layerId];
```
2. 
```swift
editorView.deleteUserDefinedDrawingLayer(layerId)
```

### clearUserDefinedDrawingLayers

Clear all the user-defined drawing layers.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)clearUserDefinedDrawingLayers;
```
2. 
```swift
func clearUserDefinedDrawingLayers()
```

### getAllDrawingLayers

Get all the drawing layers on the view.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSArray<DSDrawingLayer *>*)getAllDrawingLayers;
```
2. 
```swift
func getAllDrawingLayers() -> [DrawingLayer]
```

**Return Value**

All the drawing layers. The return value includes both system drawing layers and user defined drawing layers.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NSArray<DSDrawingLayer *> *drawingLayers = [editorView getAllDrawingLayers];
```
2. 
```swift
let drawingLayers = editorView.getAllDrawingLayers()
```

### updateTipMessage

Update the tip message.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)updateTipMessage:(NSString *)tipMessage;
```
2. 
```swift
func updateTipMessage(_ tipMessage: String)
```

**Parameters**

`tipMessage`: The new message that you want to display.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[editorView updateTipMessage:tipMessage];
```
2. 
```swift
editorView.updateTipMessage(tipMessage)
```

### setOriginalImageWithUIImage

Set the original image that displayed on the view.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setOriginalImageWithUIImage:(UIImage *)image;
```
2. 
```swift
func setOriginalImage(_ image: UIImage)
```

**Parameters**

`image`: A UIImage object as the original.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setOriginalImageWithUIImage:(UIImage *)image;
```
2. 
```swift
func setOriginalImage(_ image: UIImage)
```
