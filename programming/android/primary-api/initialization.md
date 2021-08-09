---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - CameraEnhancer Class
description: This is the documentation - Android API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, CameraEnhancer Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraEnhancer Class
---

# Initialization Methods

## initLicenseFromDLS

Initialize the `CameraEnhancer` from the license server.

```java
void initLicenseFromDLS(DMDLSConnectionParameters dlsInfo, CameraDLSLicenseVerificationListener listener)
```

**Parameters**

`DMDLSConnectionParameters`: The class [`DMDLSConnectionParameters`]({{site.android-api-auxiliary}}dls-connection.html) parameters.
`CameraDLSLicenseVerificationListener`: The interface [`CameraDLSLicenseVerificationListener`]({{ site.android-api-auxiliary }}interface.html#cameradlslicenseverificationlistener).

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
