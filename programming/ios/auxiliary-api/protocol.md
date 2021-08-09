---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS Protocol
description: This is the documentation - iOS Protocol page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS Protocol
---

# Protocol

## CameraEnhancerListener

```objc
@protocol CameraEnhancerListener <NSObject>
```

## CameraTorchListener

This is the method that handles the torch state when the torch state changes.

```objc
@protocol CameraTorchListener <NSObject>
```

**Code Snippet**

Objective-C:

```objc
```

Swift:

```swift
```

## DCEDLSLicenseVerificationDelegate

The callback of Dynamsoft License Server.

```objc
@protocol DCEDLSLicenseVerificationDelegate <NSObject>
```

**Parameters**

`[in,out] isSuccess`: Whether the license verification was successful.
`[in,out] error`: The error message from license server.

**Code Snippet**

Objective-C:

```objc
- (void)DCEDLSLicenseVerificationCallback:(bool)isSuccess error:(NSError * _Nullable)error
{
    //TODO add your code for license verification
}
```

Swift:

```swift
func dcedlsLicenseVerificationCallback(_ isSuccess: bool, error: Error?){
    //TODO add your code for license verification
}
```
