---
layout: default-layout
title: Android Upgrade Instructions - Dynamsoft Camera Enhancer
description: This is the upgrade instructions for Dynamsoft Camera Enhancer Android edition.
keywords:  Camera Enhancer, upgrade
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Upgrade Instructions
permalink: /programming/android/upgrade-instructions-v2.3.10.html
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

For API changes, it is recommended to check the [APIs reference](api-reference.html) for the new APIs.
