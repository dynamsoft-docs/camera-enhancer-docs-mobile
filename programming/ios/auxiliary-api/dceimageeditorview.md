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
| [`getDrawingStyle`](#getdrawingstyle) | Get the `DrawingStyle` instance with the style ID. |
| [`getAllDrawingStyles`](#getalldrawingstyles) | Get all the available `DrawingStyle` in a list. |
| [`createDrawingStyle`](#createdrawingstyle) | Create a user defined `DrawingStyle` instance. |

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

```
2. 
```swift

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

```
2. 
```swift

```

## getDrawingLayer

```objc
- (DCEDrawingLayer) getDrawingLayer:(NSInteger)id;
```

**Parameters**

**Return Value**

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

## createDrawingLayer

```objc
- (DCEDrawingLayer) createDrawingLayer;
```

**Return Value**

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

```
2. 
```swift

```

## getDrawingStyle

```objc

```

**Parameters**

**Return Value**

**Code Snippet**

## getAllDrawingStyles

```objc

```

**Parameters**

**Return Value**

**Code Snippet**

## createDrawingStyle

```objc

```

**Parameters**

**Return Value**

**Code Snippet**
