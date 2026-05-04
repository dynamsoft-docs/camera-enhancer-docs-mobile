---
layout: default-layout
title: DSVideoFrameListener - Dynamsoft Camera Enhancer Module iOS Edition API Reference
description: "Learn what the Dceframelistener protocol does in Dynamsoft Camera Enhancer iOS SDK and how it helps monitor camera, frame, or click events for modern web."
keywords: Video frame listener, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSVideoFrameListener

The `DSVideoFrameListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* DynamsoftCore.xcframework

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

| Method | Description |
|------- |-------------|
| [`onFrameOutPut`](#onframeoutput) | The method for monitoring the output of video frames. |

### onFrameOutPut

The method for monitoring the output of video frames.

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

`frame`: The output video frame in an [`DSImageData`]({{ site.dcv_ios_api }}core/basic-structures/image-data.html) object.  
`timeStamp`: The time stamp that the video frame is output.
