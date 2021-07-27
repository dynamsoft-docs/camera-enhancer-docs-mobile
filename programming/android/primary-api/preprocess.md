---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Filter Methods
description: This is the documentation - Android API references - Filter Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Filter
needAutoGenerateSidebar: true
breadcrumbText: Android Filter Methods
---

# Android API Reference - Frame Preprocessing Methods

## AcquireListFrame

This API is designed for users to acquire a single frame. When this API is activated, it will fetch the latest frame from the DCE frame queue.

```java
com.dynamsoft.dce.CameraEnhancer.AcquireListFrame(boolean)
```

**Parameters**

- `Boolean`: Input true to acquire frame from the frame queue.

Java:

```java
mCameraEnhancer.AcquireListFrame(true);
```

Kotlin:

```kotlin
mCameraEnhancer!!.AcquireListFrame(true)
```

## enableFastMode

This API is designed for users to setup DCE fast mode. DCE fast mode will cut frames into small images that contains barcode areas to improve decoding efficiency. It is recommended to be enabled when decoding single barcodes.

```java
com.dynamsoft.dce.CameraEnhancer.enableFastMode(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

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
com.dynamsoft.dce.CameraEnhancer.getEnabledFastModeStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledFastModeStatus();
```

Kotlin:

```kotlin
var x:Boolean? = mCameraEnhancer!!.enabledFastModeStatus
```

## enableFrameFilter

Use `enableFrameFilter` to turn on/off frame filter.

```java
com.dynamsoft.dce.CameraEnhancer.enableFrameFilter(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

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
com.dynamsoft.dce.CameraEnhancer.getEnabledFrameFilterStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledFrameFilterStatus();
```

Kotlin:

```kotlin
var x:Boolean? = mCameraEnhancer!!.enabledFrameFilterStatus
```

## setMaxFrameRate

Set max frame rate.

```java
com.dynamsoft.dce.CameraEnhancer.setMaxFrameRate(int)
```

**Parameters**

- `Frame Rate`: A int value that stands for the max frame rate.

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
com.dynamsoft.dce.CameraEnhancer.enableSensorControl(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

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
com.dynamsoft.dce.CameraEnhancer.getEnabledSensorControlStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledSensorControlStatus();
```

Kotlin:

```kotlin
var x:Boolean? = mCameraEnhancer!!.enabledSensorControlStatus
```

## setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```java
com.dynamsoft.dce.CameraEnhancer.setSensorControlThreshold(int)
```

**Parameters**

- `Threshold`: A int value that stands for the sensor filter threshold.

**Code Snippet**

Java:

```java
mCameraEnhancer.setSensorControlThreshold(55);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setSensorControlThreshold(55)
```
