---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS Protocol DCELicenseVerificationDelegate
description: This is the documentation - iOS Protocol DCELicenseVerificationDelegate page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol DCELicenseVerificationDelegate
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol DCELicenseVerificationDelegate
---

# DCELicenseVerificationDelegate

Protocol for a delegate to handle callback when license verification message returned.

```objc
@protocol DCELicenseVerificationDelegate <NSObject>
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

Objective-C:

```objc
- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error
{
    //TODO add your code for license verification
}
```

Swift:

```swift
func dceLicenseVerificationCallback(_ isSuccess: bool, error: Error?){
    //TODO add your code for license verification
}
```
