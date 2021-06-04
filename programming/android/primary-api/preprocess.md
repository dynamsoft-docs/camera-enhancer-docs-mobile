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
    mCameraEnhancer.AcquireListFrame(true);
```

## Fast Mode

This API is designed for users to setup DCE fast mode. DCE fast mode will cut frames into small images that contains barcode areas to improve decoding efficiency. It is recommended to be enabled when decoding single barcodes.

```java
    //To enable fast mode
    mCamera.enableFastMode(true);
    //To get the value(status) of fast mode
    boolean x = mCamera.getEnabledFastModeStatus();
```

## enableFrameFilter

Use `enableFrameFilter` to turn on/off frame filter.

```java
    mCamera.enableFrameFilter(true);
```

To check the status of frame filter mode, please use `getEnabledFrameFilterStatus`

```java
    boolean x = mCamera.getEnabledFrameFilterStatus();
```

## setMaxFrameRate

Set max frame rate.

```java
    mCamera.setMaxFrameRate(24);
```

## enableSensorControl

Use `enableSensorControl` to turn on/off sensor control mode.

```java
    mCamera.enableSensorControl(true);
```

To check the status of sensor control mode, please use `getEnabledSensorControlStatus`

```java
    boolean x = mCamera.getEnabledSensorControlStatus();
```

## setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```java
    mCamera.setSensorControlThreshold(55);
```
