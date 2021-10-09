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
| [`getQuality`](#getquality) | [`EnumFrameQuality`]({{site.barcode-enum}}enum-frame-quality.html) |
| [`getIsCropped`](#getiscropped) | boolean |
| [`getCropRegion`](#getcropregion) | Rect |
| [`getOrientation`](#setorientation) | int |
| [`setImageData`](#setimagedata) | byte[] |
| [`setWidth`](#setwidth) | int |
| [`setHeight`](#setheight) | int |
| [`setStrides`](#setstrides) | int[] |
| [`setPixelFormat`](#setpixelformat) | int |
| [`setFrameID`](#setframeid) | int |
| [`setQuality`](#setquality) | [`EnumFrameQuality`]({{site.barcode-enum}}enum-frame-quality.html) |
| [`setIsCropped`](#setiscropped) | boolean |
| [`setCropRegion`](#setcropregion) | Rect |
| [`setOrientation`](#setorientation) | int |

## getImageData

Get the pixel data of the `DCEFrame` image.

```java
byte[] getImageData()
```

**Return Value**

The method returns the pixel data of the `DCEFrame` object in a byte list.

## getWidth

Get the pixel width of the `DCEFrame` image.

```java
int getWidth()
```

**Return Value**

The method returns the pixel length of the `DCEFrame` image.

## getHeight

Get the pixel height of the `DCEFrame` image.

```java
int getHeight()
```

**Return Value**

The method returns the pixel height of the `DCEFrame` image.

## getStrides

Get the stride of the `DCEFrame` image by the Y (luminance) component.

```java
int getHeight()
```

**Return Value**

The method returns the YUV components value of the DCEFrame image.

**Remarks**

`strides[0]` is the Y component of the image which equals the stride of the image. `strides[1]` and `strides[2]` are the U (blue projection) and V (red projection) components of the image.

## getPixelFormat

Get the pixel format of the `DCEFrame` image. Currently, the output format of `DCEFrame` is always NV21.

```java
int setPixelFormat()
```

**Return Value**

The method returns an int value that refers to the enumeration value of [`ImagePixelFormat`]({{site.barcode-enum}}other-enums.html#imagepixelformat) (view the enumeration members in Dynamsoft Barcode Reader documents).

## getFrameID

Get the `frameID` of the `DCEFrame` object.

```java
int setFrameID()
```

**Return Value**

The method returns an int value that means the `frameID` of the `DCEFrame`.

## getQuality

Get the frame quality of the `DCEFrame` image. User have to enable the frame filter feature to get the quality (high/low) of the `DCEFrame`. Otherwise, the frame quality will be unknown.

```java
EnumFrameQuality setQuality()
```

**Return Value**

The method returns an enumeration value in [`EnumFrameQuality`]({{site.barcode-enum}}enum-frame-quality.html).

**Remarks**

Users can get all the original DCEFrame via `DCEFrameListener` but only high-quality frame can be acquired from the DCE video buffer if frame filter is enabled. In another word, when frame filter feature is enabled, the frame quality will always be high if they are acquired by triggering `getFrameFromBuffer`.

## getIsCropped

Get a boolean value that means whether the `DCEFrame` image is cropped. The frames can be cropped if `fast mode` is enabled.

```java
boolean getIsCropped()
```

**Return Value**

A boolean value. `True` means the image of `DCEFrame` is cropped and `false` means the image of the `DCEFrame` is an original frame.

## getCropRegion

Get the crop region of the `DCEFrame` image (if the image is cropped).

```java
Rect getCropRegion()
```

**Return Value**

A Rect value that stores the crop region. If the `DCEFrame` image is not cropped, the value will be null.

## getOrientation

Set the orientation of the `DCEFrame` image.

```java
int getOrientation()
```

**Return Value**

Int value that means the rotation angle of the `DCEFrame` image. The value is 0, 90, 180 or 270 with depends on the device orientation.

<div align="center">
    <p><img src="assets/getOrientation.png" width="70%" alt="getOrientation"></p>
    <p>All examples of the orientation</p>
</div>

## setImageData

Set the pixel data of the `DCEFrame` image.

```java
void setImageData(byte[] imageData)
```

**Parameters**

`imageData`: A byte list that storing the image pixel data.

## setWidth

Set the pixel width of the `DCEFrame` object.

```java
void setWidth(int width)
```

**Parameters**

`width`: The pixel value that stands for the width of the `DCEFrame` image.

## setHeight

Set the pixel height of the `DCEFrame` object.

```java
void setHeight(int height)
```

**Parameters**

`height`: The pixel value that stands for the height of the `DCEFrame` image.

## setStrides

Set the pixel stride length of the `DCEFrame` object.

```java
void setStrides(int[] strides)
```

**Parameters**

`strides`: The pixel values that stand for the strides of the `DCEFrame` image.

## setPixelFormat

Set the pixel format of the `DCEFrame` object.

```java
void setPixelFormat(int pixelFormat)
```

**Parameters**

`pixelFormat`: The pixelFormat of the `DCEFrame`. View more in Dynamsoft Barcode Reader Enumeration [`ImagePixelFormat`]({{site.barcode-enum}}other-enums.html#imagepixelformat)

## setFrameID

Set the `frameID` of the `DCEFrame` object.

```java
void setFrameID(int frameID)
```

**Parameters**

`frameID`: An int value that stands for the `frameID` of the `DCEFrame`.

## setQuality

Set the frame quality of the `DCEFrame` image.

```java
void setQuality(EnumFrameQuality quality)
```

**Parameters**

`quality`: An `Enumeration` value that means the frame quality. Read more in `EnumFrameQuality`.

## setIsCropped

Set whether the `DCEFrame` image is cropped.

```java
void setIsCropped(boolean isCropped)
```

**Parameters**

`isCropped`: A boolean value that means whether the `DCEFrame` is cropped.

## setCropRegion

Set the crop region of the `DCEframe` image (if the frame is cropped).

```java
void setCropRegion(Rect region)
```

**Parameters**

`cropRegion`: A Rect value that means crop area of the `DCEFrame` image (if the frame is cropped).

## setOrientation

Set the orientation of the `DCEFrame` image.

```java
void setOrientation(int orientation)
```

**Parameters**

`orientation`: Int value that means the rotation angle of the `DCEFrame` image.
