---
layout: default-layout
title: Dynamsoft Camera Enhancer - Upgrade Instructions for Android
description: This is the upgrade instructions for Dynamsoft Camera Enhancer Android edition.
keywords:  Camera Enhancer, upgrade
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Upgrade Instructions
---

# How to Upgrade

## From Version 1.x to 2.x

License initialization method and the license item are updated for 2.x versions. Please contact us for the new license key and use the following code to initialize the Camera Enhancer license.

```java
CameraEnhancer.initLicense("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9", new DCELicenseVerificationListener() {
    @Override
    public void DCELicenseVerificationCallback(boolean isSuccess, Exception error) {
        if(!isSuccess){
            error.printStackTrace();
        }
    }
});
```

If you can using Camera Enhancer features like frame filter or camera control APIs in the old versions, it is recommended to check the APIs reference for the new APIs.

| Methods in 1.x Versions | Methods in 2.x Versions |
| ----------------------- | ----------------------- |
| `AcquireListFrame` | `getFrameFromBuffer` |
| `getCameraCurrentStatus`, `getCameraDesiredStatus`, `setCameraDesiredStatus` | `getCameraStatus` `open`, `close` |
| `pauseCamera`, `resumeCamera` | `pause`, `resume` |
| `getTorchCurrentState`, `getTorchDesiredState`, `setTorchDesiredState`, `addTorchListener` | `turnOnTorch`, `turnOffTorch` |
| `AcquireListFrame` | `` |
