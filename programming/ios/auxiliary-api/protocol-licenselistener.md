---
layout: default-layout
title: iOS Protocol DCELicenseVerificationListener - Dynamsoft Camera Enhancer
description: This is the documentation - iOS Protocol DCELicenseVerificationListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol DCELicenseVerificationListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol DCELicenseVerificationListener
---

# DCELicenseVerificationListener

Protocol for a delegate to handle callback when license verification message returned.

```objc
@protocol DCELicenseVerificationListener <NSObject>
```

| Method | Type | Description |
| ------ | ---- | ----------- |
| `DCELicenseVerificationCallback` | *required* | The callback of license server. |

## DCELicenseVerificationCallback

The callback of license server. Add the code in the callback function to react when the license server connection is successful or failed.

```objc
- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error;
```

**Parameters**

`[in,out] isSuccess`: Whether the license verification was successful.  
`[in,out] error`: The error message from license server.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error
{
   //TODO add your code for license verification
}
```
2. 
```swift
func dceLicenseVerificationCallback(_ isSuccess: bool, error: Error?){
   //TODO add your code for license verification
}
```
