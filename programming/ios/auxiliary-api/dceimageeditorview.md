---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DCEImageEditorView Class
description: This is the documentation - iOS DCEImageEditorView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, DCEImageEditorView
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DCEImageEditorView Class
---

# DCEImageEditorView

`DCEImageEditorView` is the class that enable users to add UI configurations on a static image.

| Method Name | Description |
| ----------- | ----------- |
| [`setOriginalImage`](#setoriginalimage) | Set the background image of the view with an original image. |
| [`getOriginalImage`](#getoriginalimage) | Get the current backgroud image. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the `DCEDrawingLayer` instance with the layer ID. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a user defined `DCEDrawingLayer` instance. |
| [`getSelectedDrawingItem`](#getselecteddrawingitem) | Get the selected drawing item. |

## setOriginalImage

```objc
- (void) setOriginalImage:(ImageData)imageData;
```

**Parameters**

`imageData`: The `imageData` of the image.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_imageEditorView setOriginalImage:imageData];
```
2. 
```swift
imageEditorView.setOriginalImage(imageData)
```

## getOriginalImage

```objc
- (ImageData*) getOriginalImage;
```

**Return Value**

The `imageData` of the image.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
ImageData* imageData = [imageEditorView getOriginalImage];
```
2. 
```swift
let imageData = imageEditorView.getOriginalImage()
```

## getDrawingLayer

```objc
- (DCEDrawingLayer*) getDrawingLayer:(NSInteger)id;
```

**Parameters**

`id`: The id of the drawing layer.

**Return Value**

The targeting instance of `DCEDrawingLayer`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DCEDrawingLayer* drawingLayer = [imageEditorView getDrawingLayer];
```
2. 
```swift
let drawingLayer = imageEditorView.getDrawingLayer()
```

## createDrawingLayer

```objc
- (DCEDrawingLayer*) createDrawingLayer;
```

**Return Value**

A user-defined drawing layer.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DCEDrawingLayer* drawingLayer = [imageEditorView createDrawingLayer];
```
2. 
```swift
let drawingLayer = imageEditorView.createDrawingLayer()
```

## getSelectedDrawingItem

```objc
- (DrawingItem*) getSelectedDrawingItem;
```

**Return Value**

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DrawingItem* item = [imageEditorView getSelectedDrawingItem];
```
2. 
```swift
let item = imageEditorView.getSelectedDrawingItem()
```
