---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android Frame Class
description: This is the documentation - Android Frame Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, Frame
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Frame Class
---

# Frame

This page is for `Frame` Class. `Frame` parameters store the frame data.

```Java
class com.dynamsoft.dce.Frame
```

| Method Name | Type |
| ----------- | ---- |
| [`getImageData`](#getimagedata) | byte[] |
| [`getWidth`](#getwidth) | int |
| [`getHeight`](#getheight) | int |
| [`getStrides`](#getstrides) | int[] |
| [`getPixelFormat`](#getpixelformat) | int |
| [`getFrameID`](#getframeid) | int |
| [`getQuality`](#getquality) |  |
| [`getIsCropped`](#getiscropped) | boolean |
| [`getCropRegion`](#getcropregion) |  |
| [`getOrientation`](#setorientation) |  |
| [`setImageData`](#setimagedata) | byte[] |
| [`setWidth`](#setwidth) | int |
| [`setHeight`](#setheight) | int |
| [`setStrides`](#setstrides) | int[] |
| [`setPixelFormat`](#setpixelformat) | int |
| [`setFrameID`](#setframeid) | int |
| [`setQuality`](#setquality) | [`EnumFrameQuality`]({{site.}}) |
| [`setIsCropped`](#setiscropped) | boolean |
| [`setCropRegion`](#setcropregion) |  |
| [`setOrientation`](#setorientation) |  |

## setImageData

Set the image data of the `DCEFrame` object by byte.

```java
void setImageData(byte[] imageData)
```

**Parameters**

`imageData`: A byte list that stands for the image data.

## setWidth

Set the pixel width of the `DCEFrame` object.

```java
void setWidth(int width)
```

**Parameters**

## setHeight

Set the pixel height of the `DCEFrame` object.

```java
void setHeight(int height)
```

**Parameters**

## setStrides

Set the pixel stride length of the `DCEFrame` object.

```java
void setStrides(int[] strides)
```

**Parameters**

## setPixelFormat

Set the pixel format of the `DCEFrame` object.

```java
void setPixelFormat(int pixelFormat)
```

**Parameters**

## setFrameID

Set the frameID of the `DCEFrame` object.

```java
void setFrameID(int frameID)
```

**Parameters**

## setQuality

Set the frame quality of the `DCEFrame` image.

**Parameters**

```java
void setQuality(EnumFrameQuality quality)
```

## setIsCropped

Set whether the `DCEFrame` image is cropped.

```java
void setIsCropped(boolean isCropped)
```

**Parameters**

## setCropRegion

Set the crop region of the `DCEframe` image (if the frame will be cropped).

```java
void setCropRegion(Rect region)
```

**Parameters**

## setOrientation

Set the orientation of the `DCEFrame` image (comparing with the device).

```java
void setOrientation(int orientation)
```

**Parameters**
