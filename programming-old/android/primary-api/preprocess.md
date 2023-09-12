---
layout: default-layout
ignore: true
title: Filter Methods - Dynamsoft Camera Enhancer Android API references
description: This is the documentation - Android API references - Filter Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Filter
needAutoGenerateSidebar: true
breadcrumbText: Android Filter Methods
noTitleIndex: true
permalink: /programming/android/primary-api/preprocess.html
---

# Frame Preprocessing Methods

| Method | Description |
| ------ | ----------- |
| [`AcquireListFrame`](#AcquireListFrame) | Fetch a frame from the video buffer. |
| [`enableFastMode`](#enablefastmode) | Set true/false to turn on/off DCE fast mode. |
| [`getEnabledFastModeStatus`](#getenabledfastmodestatus) | Get the current status of fast mode (on/off). |
| [`enableFrameFilter`](#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`getEnabledFrameFilterStatus`](#getenabledframefilterstatus) | Get the status (on/off) of DCE frame filter mode. |
| [`setMaxFrameRate`](#setmaxframerate) | Set max frame rate. |
| [`enableSensorControl`](#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
| [`getEnabledSensorControlStatus`](#getenabledsensorcontrolstatus) | Get the status (on/off) of DCE sensor control mode. |
| [`setSensorControlThreshold`](#setsensorcontrolthreshold) | Enable user to change sensor sensitivity (default value is 50). |

## AcquireListFrame

Fetch a single buffered frame from the video buffer.

```java
AcquireListFrame(boolean);
```

**Parameters**

`true`: If the video buffer is empty, the method will wait for the next added frame.
`false`: If the video buffer is empty, the method will return an empty value.

**Return Value**

[`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html): This method returns the buffered frame data. The frame data includes the image data, width, height, strides and other frame information.

**Code Snippet**

Java:

```java
mCameraEnhancer.AcquireListFrame();
```

Kotlin:

```kotlin
mCameraEnhancer!!.AcquireListFrame
```

## enableFastMode

This API is designed for users to set up DCE fast mode. DCE fast mode will cut frames into small images that contain barcode areas to improve decoding efficiency. It is recommended to be enabled when decoding single barcodes.

```java
enableFastMode(boolean)
```

**Parameters**

`true`: Enable the fast-mode.  
`false`: Disable the fast-mode.

**Code Snippet**

Java:

```java
mCameraEnhancer.enableFastMode(true);
```

Kotlin:

```kotlin
mCameraEnhancer!!.enableFastMode(true)
```

## getEnabledFastModeStatus

Get the status of the fast mode.

```java
getEnabledFastModeStatus()
```

**Return Value**

`true`: The fast-mode is enabled.  
`false`: The fast-mode is disabled.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledFastModeStatus();
```

Kotlin:

```kotlin
var x:boolean? = mCameraEnhancer!!.enabledFastModeStatus
```

## enableFrameFilter

Use `enableFrameFilter` to turn on/off frame filter.

```java
enableFrameFilter(boolean)
```

**Parameters**

`true`: Enable the frame filter.  
`false`: Disable the frame filter.

**Code Snippet**

Java:

```java
mCameraEnhancer.enableFrameFilter(true);
```

Kotlin:

```kotlin
mCameraEnhancer!!.enableFrameFilter(true)
```

## getEnabledFrameFilterStatus

Get the frame filter status.

```java
getEnabledFrameFilterStatus()
```

**Return Value**

`true`: The frame filter is enabled.  
`false`: The frame filter is disabled.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledFrameFilterStatus();
```

Kotlin:

```kotlin
var x:boolean? = mCameraEnhancer!!.enabledFrameFilterStatus
```

## setMaxFrameRate

Set max frame rate.

```java
setMaxFrameRate(int)
```

**Parameters**

`int`: A int value that stands for the max frame rate.

**Code Snippet**

Java:

```java
mCameraEnhancer.setMaxFrameRate(24);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setMaxFrameRate(24)
```

## enableSensorControl

Use `enableSensorControl` to turn on/off sensor control mode.

```java
enableSensorControl(boolean)
```

**Parameters**

`true`: Enable the sensor filter.  
`false`: Disable the sensor filter.

**Code Snippet**

Java:

```java
mCameraEnhancer.enableSensorControl(true);
```

Kotlin:

```kotlin
mCameraEnhancer!!.enableSensorControl(true)
```

## getEnabledSensorControlStatus

Get the status of sensor control mode.

```java
getEnabledSensorControlStatus()
```

**Return Value**

`true`: The sensor filter is enabled.  
`false`: The sensor filter is disabled.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledSensorControlStatus();
```

Kotlin:

```kotlin
var x:boolean? = mCameraEnhancer!!.enabledSensorControlStatus
```

## setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```java
setSensorControlThreshold(int)
```

**Parameters**

`int`: A int value that stands for the sensor filter threshold.

**Code Snippet**

Java:

```java
mCameraEnhancer.setSensorControlThreshold(55);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setSensorControlThreshold(55)
```
