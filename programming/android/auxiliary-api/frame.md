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

| Attribute | Type |
| ----------- | ---- |
| [`getFrameData`](#getframedata) | byte[] |
| [`getWidth`](#getwidth) | int |
| [`getHeight`](#getheight) | int |
| [`getStrides`](#getstrides) | int[] |
| [`getFormat`](#getformat) | int |
| [`getFrameId`](#getframeid) | int |
| [`getFastFrameId`](#getfastframeid) | int |
| [`getOrientation`](#getorientation) | int |

## getFrameData

Get the value of the frame data in Byte array. You can also access the data via property `frameData`.

**Return Value**

`byte[]`: The frame byte data.

**Code Snippet**

Java:

```java
byte[] data = DCEFrame.getFrameData();
```

Kotlin:

```kotlin
var data: ByteArray? = DCEFrame!!.frameData
```

## getWidth

Get the frame width in pixels.

**Return Value**

`int`: The pixel width of the frame.

**Code Snippet**

Java:

```java
int width = DCEFrame.getWidth();
```

Kotlin:

```kotlin
var width: Int? = DCEFrame!!.width
```

## getHeight

Get the frame height in pixels.

**Return Value**

`int`: The pixel height of the frame.

**Code Snippet**

Java:

```java
int height = DCEFrame.getHeight(); 
```

Kotlin:

```kotlin
var height: Int? = DCEFrame!!.height
```

## getStrides

Get the frame strides.

**Return Value**

`int[]`: The strides of the frame.

**Code Snippet**

Java:

```java
int[] strides = DCEFrame.getStrides();
```

Kotlin:

```kotlin
var strides: IntArray? = DCEFrame!!.strides
```

## getFormat

Get the frame pixel format.

**Return Value**

`int`: The format of the frame.

**Code Snippet**

Java:

```java
int format = DCEFrame.getFormat();
```

Kotlin:

```kotlin
var format: Int? = DCEFrame!!.format
```

## getFrameId

Get the frame ID.

**Return Value**

`int`: The ID of the frame.

**Code Snippet**

Java:

```java
int frameid = DCEFrame.getFrameId(); 
```

Kotlin:

```kotlin
var frameid: Int? = DCEFrame!!.frameId
```

## getFastFrameId

Get the fast frame (cropped frame) ID.

**Return Value**

`int`: The ID of the fast frame (cropped frame).

**Code Snippet**

Java:

```java
int fastframeid = DCEFrame.getFastFrameId();
```

Kotlin:

```kotlin
var fastframeid: Int? = DCEFrame!!.fastFrameId
```

## getOrientation

Get the orientation (of cropped frame).

**Return Value**

| Orientation of the frame | Value (int) |
|--------------------------|-------|
| Vertical | 1 |
| Horizontal | 2 |

**Code Snippet**

Java:

```java
int orientation = DCEFrame.getOrientation();
```

Kotlin:

```kotlin
var orientation: Int? = DCEFrame!!.getOrientation
```
