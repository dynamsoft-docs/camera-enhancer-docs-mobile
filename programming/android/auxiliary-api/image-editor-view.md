---
layout: default-layout
Title: ImageEditorView - Dynamsoft Core Module Android Edition API Reference
Description: The class DSImageEditorView of Dynamsoft Core Module represents an image editor view, which allows users to add interactable UI elements on the view.
Keywords: image editor view, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSImageEditorView

The `DSImageEditorView` class represents an image editor view, which allows users to add interactable UI elements on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class ImageEditorView : UIView
```
2. 
```kotlin
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

```java
- (instancetype)initWithFrame:(CGRect)frame;
```
2. 
```kotlin
init(frame: CGRect)
```

**Parameters**

`frame`: A CGRect value that defines the position of the view.

**Return Value**

An instance of DSImageEditorView.

**Code Snippet**

```java
DSImageEditorView *editorView = [[DSImageEditorView alloc] initWithFrame:frame];
```
2. 
```kotlin
let editorView = DSImageEditorView(frame: frame)
```

### setOriginalImage

Set the original image that displayed on the view.

```java
- (void)setOriginalImage:(DSImageData *)imageData;
```
2. 
```kotlin
func setOriginalImage(_ imageextends ImageData)
```

**Parameters**

`imageData`: A DSImageData object as the original.

**Code Snippet**

```java
DSImageData *imageData = [[DSImageData alloc] init];
[editorView setOriginalImage:imageData];
```
2. 
```kotlin
let imageData = DSImageData()
editorView.setOriginalImage(imageData)
```

### getOriginalImage

Get the original image that displayed on the view.

```java
- (DSImageData *)getOriginalImage;
```
2. 
```kotlin
func getOriginalImage() -> DSImageData
```

**Return Value**

A UIImage object as the original.

**Code Snippet**

```java
DSImageData *originalImage = [editorView getOriginalImage];
```
2. 
```kotlin
let originalImage = editorView.getOriginalImage()
```

### getSelectedDrawingItem

Get the selected DrawingItem.

```java
- (nullable DSDrawingItem *)getSelectedDrawingItem;
```
2. 
```kotlin
func getSelectedDrawingItem() -> DSDrawingItem?
```

**Return Value**

The selected DrawingItem.

**Code Snippet**

```java
DSDrawingItem *selectedItem = [editorView getSelectedDrawingItem];
```
2. 
```kotlin
let selectedItem = editorView.getSelectedDrawingItem()
```

### getDrawingLayer

Get the specified DrawingLayer.

```java
- (DSDrawingLayer *)getDrawingLayer:(NSInteger)layerId;
```
2. 
```kotlin
func getDrawingLayer(_ layerId: Int) -> DSDrawingLayer
```

**Parameters**

`layerId`: The ID of the layer that you want to get.

**Return Value**

The object of the targeting layer.

**Code Snippet**

```java
DSDrawingLayer *drawingLayer = [editorView getDrawingLayer:layerId];
```
2. 
```kotlin
let drawingLayer = editorView.getDrawingLayer(layerId)
```

### createDrawingLayer

Create a new DrawingLayer.

```java
- (DSDrawingLayer *)createDrawingLayer;
```
2. 
```kotlin
func createDrawingLayer() -> DSDrawingLayer
```

**Return Value**

The object of the layer you created.

**Code Snippet**

```java
DSDrawingLayer *drawingLayer = [editorView createDrawingLayer];
```
2. 
```kotlin
let drawingLayer = editorView.createDrawingLayer()
```

### deleteUserDefinedDrawingLayer

Delete the specified drawing layer.

```java
- (void)deleteUserDefinedDrawingLayer:(NSInteger)layerId;
```
2. 
```kotlin
func deleteUserDefinedDrawingLayer(_ layerId: Int)
```

**Parameters**

`layerId`: The ID of the layer that you want to delete.

**Code Snippet**

```java
[editorView deleteUserDefinedDrawingLayer:layerId];
```
2. 
```kotlin
editorView.deleteUserDefinedDrawingLayer(layerId)
```

### clearUserDefinedDrawingLayers

Clear all the user-defined drawing layers.

```java
- (void)clearUserDefinedDrawingLayers;
```
2. 
```kotlin
func clearUserDefinedDrawingLayers()
```

### getAllDrawingLayers

Get all the drawing layers on the view.

```java
- (NSArray<DSDrawingLayer *>*)getAllDrawingLayers;
```
2. 
```kotlin
func getAllDrawingLayers() -> [DrawingLayer]
```

**Return Value**

All the drawing layers. The return value includes both system drawing layers and user defined drawing layers.

**Code Snippet**

```java
NSArray<DSDrawingLayer *> *drawingLayers = [editorView getAllDrawingLayers];
```
2. 
```kotlin
let drawingLayers = editorView.getAllDrawingLayers()
```

### updateTipMessage

Update the tip message.

```java
- (void)updateTipMessage:(NSString *)tipMessage;
```
2. 
```kotlin
func updateTipMessage(_ tipMessage: String)
```

**Parameters**

`tipMessage`: The new message that you want to display.

**Code Snippet**

```java
[editorView updateTipMessage:tipMessage];
```
2. 
```kotlin
editorView.updateTipMessage(tipMessage)
```

### setOriginalImageWithUIImage

Set the original image that displayed on the view.

```java
- (void)setOriginalImageWithUIImage:(UIImage *)image;
```
2. 
```kotlin
func setOriginalImage(_ image: UIImage)
```

**Parameters**

`image`: A UIImage object as the original.

**Code Snippet**

```java
- (void)setOriginalImageWithUIImage:(UIImage *)image;
```
2. 
```kotlin
func setOriginalImage(_ image: UIImage)
```
