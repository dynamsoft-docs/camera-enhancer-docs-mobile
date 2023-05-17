---
layout: default-layout
title: Android Frame Class - Dynamsoft Camera Enhancer
description: This is the documentation - Android Frame Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, Frame
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Frame Class
permalink: /programming/android/auxiliary-api/dceframe-v1.0.3.html
---

# Frame

This page is for `Frame` Class. `Frame` parameters store the frame data.

```java
class com.dynamsoft.dce.Frame
```

| Method Name | Type |
| ----------- | ---- |
| [`getData`](#getdata) | byte[] |
| [`getWidth`](#getwidth) | int |
| [`getHeight`](#getheight) | int |
| [`getStrides`](#getstrides) | int[] |
| [`getFormat`](#getformat) | int |
| [`getFrameId`](#getframeid) | int |
| [`isFastFrame`](#isfastframe) | boolean |
| [`getFastFrameId`](#getfastframeid) | int |
| [`getCropRect`](#getcroprect) | Rect |
| [`getOrientation`](#getorientation) | int |
| [`getOriW`](#getoriw) | int |
| [`getOriH`](#getorih) | int |

&nbsp;

## getData

Get the frame data in byte array.

```java
byte[] getData()
```

**Return Value**

The frame byte data.


&nbsp;

## getWidth

Get the frame width in pixels.

```java
int getWidth()
```

**Return Value**

The pixel width of the frame.


&nbsp;

## getHeight

Get the frame height in pixels.

```java
int getHeight()
```

**Return Value**

The pixel height of the frame.


&nbsp;

## getStrides

Get the frame strides.

```java
int[] getStrides()
```

**Return Value**

The strides of the frame.


&nbsp;

## getFormat

Get the frame pixel format.

```java
int getFormat()
```

**Return Value**

The format of the frame.


&nbsp;

## getFrameId

Get the frame ID.

```java
int getFrameId()
```

**Return Value**

The ID of the frame.


&nbsp;

## isFastFrame

Check whether the fast mode is enabled.

```java
boolean isFastFrame()
```

**Return Value**

Whether the frame is cropped.


&nbsp;

## getFastFrameId

Get the fast frame (cropped frame) ID.

```java
int getFastFrameId()
```

**Return Value**

The ID of the fast frame (cropped frame).


&nbsp;

## getCropRect

Get the cropped Rect data (Width & height)

```java
Rect getCropRect()
```

**Return Value**

The value of the cropped frame.

&nbsp;

## getOrientation

Get the orientation (of cropped frame).

```java
int getOrientation()
```

**Return Value**

The orientation (of cropped frame).

| Orientation of the frame | Value (int) |
|--------------------------|-------|
| Vertical | 1 |
| Horizontal | 2 |

&nbsp;

## getOriW

Get the original width of the cropped frame.

```java
int getOriW()
```

**Return Value**

The pixel width of the cropped frame.

&nbsp;

## getOriH

Get the original width of the cropped frame.

```java
int getOriH()
```

**Return Value**

The pixel height of the cropped frame.
