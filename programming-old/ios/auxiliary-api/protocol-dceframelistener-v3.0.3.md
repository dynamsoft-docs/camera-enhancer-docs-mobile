---
layout: default-layout
title: iOS Protocol DCEFrameListener - Dynamsoft Camera Enhancer Documents
description: This is the documentation - iOS Protocol DCEFrameListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol DCEFrameListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol DCEFrameListener
permalink: /programming/ios/auxiliary-api/protocol-dceframelistener-v3.0.3.html
---

# DCEFrameListener

The protocol to handle callback when previewed frame callback is returned.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol CameraEnhancerListener <NSObject>
```
2. 
```swift
protocol DCECameraStateListener : NSObjectProtocol
```

| Method | Type | Description |
| ------ | ---- | ----------- |
| [`frameOutPutCallback`](#frameoutputcallback) | *required* | Callback when the `DCEFrame` is output. |

## frameOutPutCallback

Callback when the `DCEFrame` is output.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)frameOutPutCallback:(DCEFrame*)frame timeStamp:(NSTimeInterval)timeStamp;
```
2. 
```swift
func frameOutPutCallback(_ frame: DCEFrame, timeStamp: TimeInterval)
```

**Parameters**

`frame`: The parameter is the original `DCEFrame` with detailed frame information. View more in [`DCEFrame`](dceframe.html) class.  
`timeStamp`: The time stamp that records when the DCEFrame is output.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_dce addListener:self];
- (void)frameOutPutCallback:(DCEFrame *)frame timeStamp:(NSTimeInterval)timeStamp{
    // TODO add your code
}
```
2. 
```swift
dce.addListener(self)
func frameOutPutCallback(_ frame: DCEFrame, timeStamp: TimeInterval){
    // TODO add your code
}
```

**See also**

- [`DCEFrame`](dceframe.html)
