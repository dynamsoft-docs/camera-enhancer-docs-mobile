---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android Frame Class
description: This is the documentation - Android Frame Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, Frame
needAutoGenerateSidebar: true
breadcrumbText: Android Frame
---

# Frame

Exception for signalling camera enhancer errors

## Method

| Name | Type |
|------|------|
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

## getData

Get the frame data in byte array.

```java
Frame frame;
byte[] data = frame.getData();
```

## getWidth

Get the frame width in pixels.

```java
int width = frame.getWidth();
```

## getHeight

Get the frame height in pixels.

```java
int height = frame.getHeight(); 
```

## getStrides

Get the frame strides.

```java
int[] strides = frame.getStrides();
```

## getFormat

Get the frame pixel format.

```java
int format = frame.getFormat();
```

## getFrameId

Get the frame ID.

```java
int frameid = frame.getFrameId(); 
```

## isFastFrame

Check whether the fast mode is enabled.

```java
boolean isfastframe = frame.isFastFrame();
```

## getFastFrameId

Get the fast frame (cropped frame) ID.

```java
int fastframeid = frame.getFastFrameId();
```

## getCropRect

Get the cropped Rect data (Width & height)

```java
Rect croprect = frame.getCropRect();
```

## getOrientation

Get the orientation (of cropped frame).

| Orientation of the frame | Value |
|--------------------------|-------|
| Vertical | 1 |
| Horizontal | 2 |

```java
int orientation = frame.getOrientation();
```

## getOriW

Get the original width of the cropped frame.

```java
int originalwidth = frame.getOriW();
```

## getOriH

Get the original width of the cropped frame.

```java
int originalheight = frame.getOriH();
```
