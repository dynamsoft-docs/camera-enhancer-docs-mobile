---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS Protocol DCEDLSLicenseVerificationDelegate
description: This is the documentation - iOS Protocol DCEDLSLicenseVerificationDelegate page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol DCEDLSLicenseVerificationDelegate
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol DCEDLSLicenseVerificationDelegate
---

# DCEDLSLicenseVerificationDelegate

Protocol for a delegate to handle callback when license verification message returned.

```objc
@protocol DCEDLSLicenseVerificationDelegate <NSObject>
```

| Method | Type | Description |
| ------ | ---- | ----------- |
| `DCEDLSLicenseVerificationCallback` | *required* | The callback of license server. |

## DCEDLSLicenseVerificationCallback

The callback of license server. Add the code in the callback function to react when the license server connection is successful or failed.

```objc
- (void)DCEDLSLicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error;
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
- (void)DCEDLSLicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error
{
    //TODO add your code for license verification
}
```
2. 
```swift
func dcedlsLicenseVerificationCallback(_ isSuccess: bool, error: Error?){
    //TODO add your code for license verification
}
```
