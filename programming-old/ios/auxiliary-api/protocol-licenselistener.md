---
layout: default-layout
Title: DSLicenseVerificationListener - Dynamsoft Camera Enhancer iOS Edition API Reference
Description: The protocol DSLicenseVerificationListener of Dynamsoft Camera Enhancer includes methods for monitoring the license verification status.
Keywords: license verification, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSLicenseVerificationListener

The `DSLicenseVerificationListener` is a protocol that includes methods for monitoring the license verification status.

## Definition

*Assembly:* DynamsoftLicense.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSLicenseVerificationListener <NSObject>
```
2. 
```swift
protocol LicenseVerificationListener : NSObjectProtocol
```

| Method | Description |
| ------ | ----------- |
| [`onLicenseVerified`](#onlicenseverified) | The method that is triggered when the license server returns the verification info. |

### onLicenseVerified

The method that is triggered when the license server returns the verification info.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onLicenseVerified:(BOOL)isSuccess error:(NSError * _Nullable)error;
```
2. 
```swift
func onLicenseVerified(_ isSuccess: Bool, error: Error?)
```

**Parameters**

`isSuccess`: A Boolean value indicating whether the license is verified successfully.

`error`: An NSError pointer. It carries the error code and message that describe the reason why your license activation failed.
