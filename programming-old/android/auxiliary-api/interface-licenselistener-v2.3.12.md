---
layout: default-layout
title: Android DCELicenseVerificationListener - Dynamsoft Camera Enhancer
description: This is the documentation - DCELicenseVerificationListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, DCELicenseVerificationListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: DCELicenseVerificationListener
permalink: /programming/android/auxiliary-api/interface-licenselistener-v2.3.12.html
---

# DCELicenseVerificationListener

The interface to handle callback when license verification messages are returned.

```java
interface com.dynamsoft.dce.DCELicenseVerificationListener
```

| Method | Description |
| ------ | ----------- |
| `DCELicenseVerificationCallback` | The call back of the license server. |

&nbsp;

## DCELicenseVerificationCallback

The call back of the license server. Add the code in the callback function to react when the license server connection is successful or failed.

```java
void DCELicenseVerificationCallback(boolean isSuccess, Exception error);
```

**Parameters**

`isSuccess`: Whether the license verification was successful.  
`error`: The error message from the license server.

**Code Snippet**

```java
CameraEnhancer.initLicense("Put your license here", new DCELicenseVerificationListener() {
    @Override
    public void DCELicenseVerificationCallback(boolean isSuccess, Exception e) {
        if (!isSuccess) {
            e.printStackTrace();
        }
    }
});
```
