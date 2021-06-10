---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DCECaptureView Class
description: This is the documentation - Android DCECaptureView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android DCECaptureView Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Interface
---

# Interface

## CameraListener

From `CameraListener` user can get preprocessed frames.

- `onPreviewOriginalFrame`: Get the original frame.
- `onPreviewFilterFrame`: Get the filtered frame.
- `onPreviewFastFrame`: Get the filtered and cropped frame.

```java
void com.dynamsoft.dce.CameraListener
```

Java:

```java
    mCameraEnhancer.addCameraListener(new CameraListener() {
        @Override
        public void onPreviewOriginalFrame(Frame frame) {}
        @Override
        public void onPreviewFilterFrame(Frame frame) {}
        @Override
        public void onPreviewFastFrame(Frame frame) {}
    });
```

Kotlin:

```kotlin
    mCameraEnhancer!!.addCameraListener(object : CameraListener {
        override fun onPreviewOriginalFrame(frame: Frame) {}
        override fun onPreviewFilterFrame(frame: Frame) {}
        override fun onPreviewFastFrame(frame: Frame) {}
    })
```

## CameraLTSLicenseVerificationListener

This is the method that handles callback when license tracking server returns.

- `isSuccess`: Whether the license verification was successful.
- `error`: The error message from license server.

```java
void com.dynamsoft.dce.CameraLTSLicenseVerificationListener
```

## TorchListener

This is the method that handles torch state when the torch state changes.

```java
void com.dynamsoft.dce.TorchListener
```

Java:

```java
    mCameraEnhancer.addTorchListener(new TorchListener() {
        @Override
        public void onTorchStateChanged(TorchState torchState) {
                
        }
    });
```

Kotlin:

```kotlin
    mCameraEnhancer!!.addTorchListener(object : TorchListener {
        override fun onTorchStateChanged(TorchState: torchState) {}
    })
```
