---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android Interface
description: This is the documentation - Android Interface page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android Interface
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Interface
---

# Interface

## CameraListener

Get frames through the `CameraListener`.

```java
void onPreviewOriginalFrame(Frame var1);
void onPreviewFilterFrame(Frame var1);
void onPreviewFastFrame(Frame var1);
```

**Parameters**

`frame`: Use `onPreviewOriginalFrame` to get the original `frame`. Use `onPreviewFilterFrame` to get the filtered `frame`. Use `onPreviewFastFrame` to get the filtered and cropped `frame`.

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

## CameraDLSLicenseVerificationListener

This is the method that handles callback when Dynamsoft License Server returns.

**Parameters**

`isSuccess`: Whether the license verification was successful.
`error`: The error message from license server.

Java:

```java
com.dynamsoft.dce.DMDLSConnectionParameters info = new com.dynamsoft.dce.DMDLSConnectionParameters();
info.organizationID = "Put your organizationID here.";
mCameraEnhancer.initLicenseFromDLS(info,new CameraDLSLicenseVerificationListener() {
    @Override
    public void DLSLicenseVerificationCallback(boolean isSuccess, Exception error) {
        if(!isSuccess){ error.printStackTrace(); }
    }
});
```

Kotlin:

```kotlin
val info = com.dynamsoft.dce.DMDLSConnectionParameters()
info.organizationID = "Put your organizationID here."
mCameraEnhancer!!.initLicenseFromDLS(info) { isSuccess, error ->
    if (!isSuccess) {
        error.printStackTrace()
    }
}
```

## TorchListener

This is the method that handles the torch state when the torch state changes.

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
