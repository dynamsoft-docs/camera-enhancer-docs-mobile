---
layout: default-layout
title: DSVideoFrameListener - Dynamsoft Camera Enhancer Module iOS Edition API Reference
description: The protocol that defines methos for monitoring the video frame output.
keywords: Video frame listener, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSVideoFrameListener

The `DSVideoFrameListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSVideoFrameListener <NSObject>
```
2. 
```swift
protocol VideoFrameListener : NSObjectProtocol
```

## Methods

### onFrameOutPut

The method for monitoring the camera state and receiving call.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onFrameOutPut:(DSImageData*)frame
            timeStamp:(NSTimeInterval)timeStamp;
```
2. 
```swift
func onFrameOutPut(_ frame: DSImageData, timeStamp: NSTimeInterval)
```

**Parameters**

`frame`: The output video frame.  
`timeStamp`: The time stamp that the video frame is output.
