---
layout: default-layout
Title: ImageEditorView - Dynamsoft Core Module Android Edition API Reference
Description: The class ImageEditorView of Dynamsoft Core Module represents an image editor view, which allows users to add interactable UI elements on the view.
Keywords: image editor view, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ImageEditorView

The `ImageEditorView` class represents an image editor view, which allows users to add interactable UI elements on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class ImageEditorView : UIView
```

## Methods

| Method | Description |
|------- |-------------|
| [`ImageEditorView`](#initwithframe) | Create an instance of CameraView. |
| [`setOriginalImage`](#setoriginalimage) | Set the original image that displayed on the view. |
| [`setOriginalImage(bitmapImage)`](#setoriginalimagebitmapimage) | Set the original image that displayed on the view. |
| [`getOriginalImage`](#getoriginalimage) | Get the original image that displayed on the view. |
| [`getSelectedDrawingItem`](#getselecteddrawingitem) | Get the selected DrawingItem. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the specified DrawingLayer. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a new DrawingLayer. |
| [`deleteUserDefinedDrawingLayer`](#deleteuserdefineddrawinglayer) | Delete the specified drawing layer. |
| [`clearUserDefinedDrawingLayers`](#clearuserdefineddrawinglayers) | Clear all the user-defined drawing layers. |
| [`setOriginalImage(bitmapImage)`](#setoriginalimagebitmapimage) | Set the original image that displayed on the view. |
| [`updateTipMessage`](#updatetipmessage) | Update the tip message. |
| [`setTipConfig`](#settipconfig) | Set/get the tip configurations. |
| [`getTipConfig`](#gettipconfig) | Set/get the tip configurations. |
| [`setTipVisible`](#settipvisible) | Set the visibility of tip. |
| [`isTipVisible`](#istipvisible) | Get the visibility of tip. |

### initWithFrame

The consturctor. Create an instance of `ImageEditorView`.

```java
ImageEditorView(android.content.Context context){}
```

**Parameters**

`context`: The context of the view.

**Return Value**

An instance of `ImageEditorView`.

### setOriginalImage

Set the original image that displayed on the view.

```java
void setOriginalImage(com.dynamsoft.core.ImageData imageData){}
```

**Parameters**

`imageData`: A `com.dynamsoft.core.ImageData` object as the original.

### setOriginalImage(bitmapImage)

Set the original image that displayed on the view with a Bitmap.

```java
void setOriginalImage(Bitmap bitmapImage){}
```

**Parameters**

`bitmapImage`: A `Bitmap` object as the original.

### getOriginalImage

Get the original image that displayed on the view.

```java
com.dynamsoft.core.ImageData getOriginalImage(){}
```

**Return Value**

A `com.dynamsoft.core.ImageData` object as the original image.

**Code Snippet**

### getSelectedDrawingItem

Get the selected DrawingItem.

```java
DrawingItem getSelectedDrawingItem(){}
```

**Return Value**

The selected `DrawingItem`.

### getDrawingLayer

Get the specified DrawingLayer.

```java
DrawingLayer getDrawingLayer(int id){}
```

**Parameters**

`id`: The ID of the layer that you want to get.

**Return Value**

The object of the targeting layer.

### createDrawingLayer

Create a new DrawingLayer.

```java
DrawingLayer createDrawingLayer(){}
```

**Return Value**

The object of the layer you created.

### deleteUserDefinedDrawingLayer

Delete the specified drawing layer.

```java
void deleteUserDefinedDrawingLayer(int id){}
```

**Parameters**

`id`: The ID of the layer that you want to delete.

### clearUserDefinedDrawingLayers

Clear all the user-defined drawing layers.

```java
void clearUserDefinedDrawingLayers(){}
```

### updateTipMessage

Update the tip message.

```java
void updateTipMessage(String tipMessage){}
```

**Parameters**

`tipMessage`: The new message that you want to display.

### setTipConfig

Set/get the tip configurations.

```java
void setTipConfig(TipConfig tipConfig);
```

**Parameters**

`tipConfig`: A `TipConfig` object that stores the tip configuration.

### getTipConfig

Set/get the tip configurations.

```java
TipConfig getTipConfig();
```

**Return Value**

Get a `TipConfig` object that stores the tip configuration.

### setTipVisible

Set the visibility of tip.

```java
void setTipVisible(boolean isVisible);
```

**Parameters**

`isVisible`: A boolean value that indicate the tip is visible.

### isTipVisible

Get the visibility of tip.

```java
boolean isTipVisible();
```

**Return Value**

A boolean value that indicate the tip is visible.
