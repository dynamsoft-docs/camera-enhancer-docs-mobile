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
AcquireListFrame(boolean)
```

**Parameters**

`Boolean (true)`: Acquire frame from the frame queue.

**Code Snippet**

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
var x:Boolean? = mCameraEnhancer!!.enabledFastModeStatus
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
var x:Boolean? = mCameraEnhancer!!.enabledFrameFilterStatus
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
var x:Boolean? = mCameraEnhancer!!.enabledSensorControlStatus
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
