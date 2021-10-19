---
layout: default-layout
title: Dynamsoft Camera Enhancer - CameraDLSLicenseVerificationListener
description: This is the documentation - CameraDLSLicenseVerificationListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, CameraDLSLicenseVerificationListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: CameraDLSLicenseVerificationListener
---

# CameraDLSLicenseVerificationListener

The interface to handle callback when license verification messages are returned.

```java
interface com.dynamsoft.dce.CameraDLSLicenseVerificationListener
```

| Method | Description |
| ------ | ----------- |
| `DLSLicenseVerificationCallback` | The call back of the license server. |

## DLSLicenseVerificationCallback

The call back of the license server. Add the code in the callback function to react when the license server connection is successful or failed.

```java
void DLSLicenseVerificationCallback(boolean isSuccess, Exception error);
```

**Parameters**

`isSuccess`: Whether the license verification was successful.  
`error`: The error message from the license server.

**Code Snippet**

```java
cameraEnhancer.initLicenseFromDLS(dceParameters, new CameraDLSLicenseVerificationListener() {
    @Override
    public void DLSLicenseVerificationCallback(boolean isSuccess, Exception e) {
        if (!isSuccess) {
            e.printStackTrace();
        }
    }
});
```
