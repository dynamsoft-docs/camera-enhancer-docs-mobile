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

**Parameters**

**Required**

```objc
- (void)onPreviewOriginalFrame:(FramePackage*)frame;
```

**Code Snippet**

Objective-C:

```objc
[_dce addCameraListener:self];
// Add protocol requirements
- (void)onPreviewOriginalFrame:(FramePackage *) frame{
    // TODO add your code for original frame
}
- (void)onPreviewFilterFrame:(FramePackage *) frame{
    // TODO add your code for filter frame
}
- (void)onPreviewFastFrame:(FramePackage *) frame{
    // TODO add your code for fast frame
}
```

Swift:

```swift
dce.addTorchListener(self)
// Add protocol requirements
func onPreviewOriginalFrame(_ frame: FramePackage){
    // TODO add your code for original frame
}
func onPreviewFilterFrame(_ frame: FramePackage){
    // TODO add your code for filter frame
}
func onPreviewFastFrame(_ frame: FramePackage){
    // TODO add your code for fast frame
}
```

## CameraTorchListener

This is the method that handles the torch state when the torch state changes.

```objc
@protocol CameraTorchListener <NSObject>
```

**Parameters**

**Required**

```objc
- (void)didChangeTorchState:(TorchState)torchState NS_SWIFT_NAME(didChangeTorchState(torchState:));
```

**Code Snippet**

Objective-C:

```objc
[_dce addTorchListener:self];
// Add protocol requirements
- (void)didChangeTorchState:(TorchState) torchState{
    // TODO add your code for torch listener
}
```

Swift:

```swift
dce.addTorchListener(self)
// Add protocol requirements
func didChangeTorchState(torchState: TorchState){
    // TODO add your code for torch listener
}
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
