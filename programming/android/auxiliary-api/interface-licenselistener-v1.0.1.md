---
layout: default-layout
title: Android CameraLTSLicenseVerificationListener - Dynamsoft Camera Enhancer
description: This is the documentation - CameraLTSLicenseVerificationListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, CameraLTSLicenseVerificationListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: CameraLTSLicenseVerificationListener
---


# CameraLTSLicenseVerificationListener

The interface to handle callback when license verification messages are returned.

```java
interface com.dynamsoft.dce.CameraLTSLicenseVerificationListener
```

| Method | Description |
| ------ | ----------- |
| `LTSLicenseVerificationCallback` | The call back of the license server. |

## LTSLicenseVerificationCallback

The call back of the license server. Add the code in the callback function to react when the license server connection is successful or failed.

```java
void LTSLicenseVerificationCallback(boolean isSuccess, Exception error);
```

**Parameters**

`isSuccess`: Whether the license verification was successful.  
`error`: The error message from the license server.

**Code Snippet**

```java
cameraEnhancer.initLicenseFromLTS(dceParameters, new CameraLTSLicenseVerificationListener() {
    @Override
    public void LTSLicenseVerificationCallback(boolean isSuccess, Exception e) {
        if (!isSuccess) {
            e.printStackTrace();
        }
    }
});
```
