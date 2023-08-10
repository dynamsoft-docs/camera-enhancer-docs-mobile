---
layout: default-layout
Title: LicenseVerificationListener - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The interface LicenseVerificationListener of Dynamsoft Camera Enhancer includes methods for monitoring the license verification status.
Keywords: license verification, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# LicenseVerificationListener

The `LicenseVerificationListener` is a interface that includes methods for monitoring the license verification status.

## Definition

*Namespace:* com.dynamsoft.license

*Assembly:* DynamsoftLicense.aar

```java
interface LicenseVerificationListener
```

| Method | Description |
| ------ | ----------- |
| [`onLicenseVerified`](#onlicenseverified) | The method that is triggered when the license server returns the verification info. |

### onLicenseVerified

The method that is triggered when the license server returns the verification info.

```java
void onLicenseVerified(boolean isSuccess, Exception error);
```

**Parameters**

`[in] isSuccess`: A Boolean value indicating whether the license is verified successfully.

`[in] error`: An exception object. It carries the error code and message that describe the reason why your license activation failed.
