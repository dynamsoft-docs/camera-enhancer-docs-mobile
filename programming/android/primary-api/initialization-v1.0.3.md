---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Initialization Methods
description: This is the documentation - Android API references - Initialization Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Initialization Methods
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Initialization Methods
---

# Initialization Methods v1.0.3

| Method | Description |
| ------ | ----------- |
| [`initLicenseFromDLS`](#initLicensefromdls) | Initialize the Camera Enhancer from the license server with a license. |

## initLicenseFromDLS

Initialize the `CameraEnhancer` from the license server.

```java
void initLicenseFromDLS(CameraDLSLicenseVerificationListener listener)
```

**Parameters**

`CameraDLSLicenseVerificationListener`: The interface [`CameraDLSLicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener-v1.0.3.html).

**Code Snippet**

Java:

```java
CameraEnhancer mCameraEnhancer = new CameraEnhancer(MainActivity.this);
mCameraEnhancer.addCameraView(cameraView);
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
mCameraEnhancer = CameraEnhancer(this@MainActivity)
mCameraEnhancer!!.addCameraView(cameraView)
val info = com.dynamsoft.dce.DMDLSConnectionParameters()
info.organizationID = "Put your organizationID here."
mCameraEnhancer!!.initLicenseFromDLS(info) { isSuccess, error ->
    if (!isSuccess) {
        error.printStackTrace()
    }
}
```
