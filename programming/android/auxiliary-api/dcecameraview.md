---
layout: default-layout
title: CameraView - Dynamsoft Camera SDK API Reference
description: The class CameraView of Dynamsoft Camera SDK represents a camera view that displays the camera preview and provides UI controlling APIs.
keywords: camera view, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraView

The `CameraView` class is used to display the camera preview and provides UI controlling APIs. Users can add interactable UI elements on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class CameraView
```

## Methods

| Method | Description |
|------- |-------------|
| [`CameraView`](#cameraview) | Create an instance of `CameraView`. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the specified `DrawingLayer`. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a new `DrawingLayer`. |
| [`getVisibleRegionOfVideo`](#getvisibleregionofvideo) | Get the visible region of the video streaming. |
| [`setTorchButton`](#settorchbutton) | Add a torch button on your view. |
| [`setCameraToggleButton`](#setcameratogglebutton) | Add a camera toggle button on your view for switching between front and back cameras. |
| [`deleteUserDefinedDrawingLayer`](#deleteuserdefineddrawinglayer) | Delete the specified drawing layer. |
| [`clearUserDefinedDrawingLayers`](#clearuserdefineddrawinglayers) | Clear all the user-defined drawing layers. |
| [`getAllDrawingLayers`](#getalldrawinglayers) | Get all the drawing layers on the view. |
| [`setScanRegionMaskStyle`](#setscanregionmaskstyle) | Set the style of the scan region mask. |
| [`setTorchButtonVisible`](#settorchbuttonvisible) | Set/get the visibility of the torch button. |
| [`getTorchButtonVisible`](#gettorchbuttonvisible) | Set/get the visibility of the torch button. |
| [`setCameraToggleButtonVisible`](#setcameratogglebuttonvisible) | Set/get the visibility of the camera toggle button. |
| [`getCameraToggleButtonVisible`](#getcameratogglebuttonvisible) | Set/get the visibility of the camera toggle button. |
| [`setScanRegionMaskVisible`](#setscanregionmaskvisible) | Set/get the visibility of the scan region mask. |
| [`isScanRegionMaskVisible`](#isscanregionmaskvisible) | Set/get the visibility of the scan region mask. |
| [`setScanLaserVisible`](#setscanlaservisible) | Set the visibility of the scan laser. |
| [`isScanLaserVisible`](#isscanlaservisible) | Get the visibility of the scan laser. |
| [`setTipConfig`](#settipconfig) | Set/get the tip configurations. |
| [`getTipConfig`](#gettipconfig) | Set/get the tip configurations. |
| [`setTipVisible`](#settipvisible) | Set the visibility of tip. |
| [`isTipVisible`](#istipvisible) | Get the visibility of tip. |
| [`updateTipMessage`](#updatetipmessage) | Update the tip message. |
| [`setDrawingItemClickListener`](#setdrawingitemclicklistener) | Set a [`DrawingItemClickListener`](interface-click-listener.md) to receive callback when [`DrawingItems`](drawingitem.md) on the view are clicked. |

### CameraView

The constructor. Create an instance of `CameraView`.

```java
CameraView(android.content.Context context);
```

**Parameters**

`frame`: A CGRect value that defines the position of the view.

**Return Value**

An instance of `CameraView`.

### getDrawingLayer

Get the specified `DrawingLayer`.

```java
DrawingLayer getDrawingLayer(int id);
```

**Parameters**

`layerId`: The ID of the layer that you want to get.

**Return Value**

The object of the targeting layer.

### createDrawingLayer

Create a new `DrawingLayer`.

```java
DrawingLayer createDrawingLayer();
```

**Return Value**

The object of the layer you created.

### getVisibleRegionOfVideo

Get the visible region of the video streaming.

```java
DSRect getVisibileRegionOfVideo();
```

**Return Value**

A [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) object (measuredInPercentage = 1) that defines the visible region of the video.

### setTorchButton

Add a torch button on your view. If you are using enhanced feature - smart torch, the style of this torch button will be applied to the smart torch as well.

```java
void setTorchButton(Point torchButtonPosition, int width, int height, Drawable torchOnImage, Drawable torchOffImage);
```

**Parameters**

`torchButtonPosition`: Set the top-left point of the torch button.  
`width`: Set the width of the torch button.  
`height`: Set the height of the torch button.  
`torchOnImage`: The torch button image that you want to display when the torch is on.  
`torchOffImage`: The torch button image that you want to display when the torch is off.  

### setTorchButtonVisible

Set the visibility of the torch button.

```java
void setTorchButtonVisible(boolean isTorchButtonVisible);
```

**Parameters**

`isTorchButtonVisible`: A boolean value that indicate the torch button is visible.

### getTorchButtonVisible

Get the visibility of the torch button.

```java
boolean getTorchButtonVisible();
```

**Return Value**

A boolean value that indicate the torch button is visible.

### setCameraToggleButton

Add a camera toggle button on your view for switching between front and back camera.

```java
void setCameraToggleButton(Point cameraToggleButtonPosition);
void setCameraToggleButton(Point cameraToggleButtonPosition, int width, int height, Drawable cameraToggleImage);
```

**Parameters**

`cameraToggleButtonPosition`: Set the top-left point of the camera toggle button.  
`width`: Set the width of the camera toggle button.  
`height`: Set the height of the camera toggle button.  
`cameraToggleImage`: The camera toggle button image that you want to display.

### setCameraToggleButtonVisible

Set the visibility of the camera toggle button.

```java
void setCameraToggleButtonVisible(boolean isCameraToggleButtonVisible);
```

**Parameters**

`isCameraToggleButtonVisible`: A boolean value that indicates whether the camera toggle button is visible.

### getCameraToggleButtonVisible

Get the visibility of the camera toggle button.

```java
boolean getCameraToggleButtonVisible();
```

**Return Value**

A boolean value that indicates whether the camera toggle button is visible.

### deleteUserDefinedDrawingLayer

Delete the specified drawing layer.

**Parameters**

`frame`: The ID of the layer that you want to delete.

```java
void deleteUserDefinedDrawingLayer(int id);
```

### clearUserDefinedDrawingLayers

Clear all the user-defined drawing layers.

```java
void clearUserDefinedDrawingLayers();
```

### getAllDrawingLayers

Get all the drawing layers on the view.

**Return Value**

All the drawing layers. The return value includes both system drawing layers and user defined drawing layers.

```java
DrawingLayer[] getAllDrawingLayers();
```

### setScanRegionMaskVisible

Set the visibility of the scan region mask.

```java
void setScanRegionMaskVisible(boolean isScanRegionVisible);
```

**Parameters**

`isScanRegionVisible`: A boolean value that indicates whether the scan region mask is visible.

### isScanRegionMaskVisible

Get the visibility of the scan laser.

```java
boolean isScanRegionMaskVisible();
```

**Return Value**

A boolean value that indicates whether the scan region mask is visible.

### setScanRegionMaskStyle

Set the style of the scan region mask.

```java
void setScanRegionMaskStyle(int strokeColor, int surroundingColour, float strokeWidth);
```

**Parameters**

`strokeColour`: The stroke colour of the scan region box.  
`surroundingColour`: The colour of the mask around the scan region.  
`strokeWidth`: The width of the stroke.  

### setScanLaserVisible

Set the visibility of the scan laser.

```java
void setScanLaserVisible(boolean isScanRegionVisible);
```

**Parameters**

`isScanRegionVisible`: A boolean value that indicates whether the scan laser is visible.

### isScanLaserVisible

Get the visibility of the scan laser.

```java
boolean isScanLaserVisible();
```

**Return Value**

A boolean value that indicates whether the scan laser is visible.

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

### updateTipMessage

Update the tip message. The new tip message will be immediately displayed on the view. Generally, tip messages are uploaded internally.

```java
void updateTipMessage(String tipMessage);
```

**Parameters**

`tipMessage` The new message that you want to display.

### setDrawingItemClickListener

Set a [`DrawingItemClickListener`](interface-click-listener.md) to receive callback when [`DrawingItems`](drawingitem.md) on the view are clicked.

```java
void setDrawingItemClickListener(DrawingItemClickListener clickListener)
```

**Parameters**

`clickListener`: An interface instance of [`DrawingItemClickListener`](interface-click-listener.md).
