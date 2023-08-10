---
layout: default-layout
title: Android Upgrade Instructions- Dynamsoft Camera Enhancer
description: This is the documentation of Android upgrade instructionspage of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android upgrade instructions
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android API references
permalink: /programming/android/upgrade-instruction.html
---

# How to Upgrade

## From v2.x/v3.x to v4.x

### Update License Activation Code

License activation API are removed from `DynamsoftCameraEnhancer` library. Please use the `LicenseManager` of `DynamsoftLicense` instead.

1. Include the library

   ```java
   dependencies {
       implementation 'com.dynamsoft:dynamsoftlicense:3.0.0@aar'
   }
   ```

2. Initialize the license in your code.

   ```java
   LicenseManager.initLicense(LICENSE, this, (isSuccess, error) -> {
       if (!isSuccess) {
           Log.e(TAG, "InitLicense Error: " + error);
       }
   });
   ```

### Re-write your Code Based on the API References

The APIs of `DynamsoftCameraEnhancer` are refactored. Please follow the [API reference](api-reference.md) to update your code.
