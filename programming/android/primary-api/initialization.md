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

# Initialization Methods

| Method | Description |
| ------ | ----------- |
| [`initLicense`](#initLicense) | Initialize the Camera Enhancer from the license server with a license. |

## initLicenseFromDLS

Initialize the `CameraEnhancer` from the license server.

```java
void initLicense(DCELicenseVerificationListener listener)
```

**Parameters**

`DCELicenseVerificationListener`: The interface [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener.html).

**Code Snippet**

Java:

```java
CameraEnhancer mCameraEnhancer = new CameraEnhancer(MainActivity.this);
mCameraEnhancer.addCameraView(cameraView);
// Please use your own license to replace the public trial license.
mCameraEnhancer.initLicense("Put your license here", new DCELicenseVerificationListener() {
    @Override
    public void DCELicenseVerificationCallback(boolean isSuccess, Exception error) {
        if(!isSuccess){ error.printStackTrace(); }
    }
});
```

Kotlin:

```kotlin
mCameraEnhancer = CameraEnhancer(this@MainActivity)
mCameraEnhancer!!.addCameraView(cameraView)
mCameraEnhancer!!.initLicense(info) { isSuccess, error ->
    if (!isSuccess) {
        error.printStackTrace()
    }
}
```
