---
layout: default-layout
title: iOS Protocol CameraEnhancerListener - Dynamsoft Camera Enhancer
description: This is the documentation - iOS Protocol CameraEnhancerListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol CameraEnhancerListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol CameraEnhancerListener
permalink: /programming/ios/auxiliary-api/protocol-dceframelistener-v1.0.3.html
---

# CameraEnhancerListener

The protocol to handle callback when previewed frame callback is returned.

```objc
@protocol CameraEnhancerListener <NSObject>
```

| Method | Type | Description |
| ------ | ---- | ----------- |
| [`onPreviewOriginalFrame`](#onrrevieworiginalframe) | *required* | The previewed original frame callback. |
| [`onPreviewFilterFrame`](#onpreviewfilterframe) | *optional* | The previewed filtered frame callback. |
| [`onPreviewFastFrame`](#onpreviewfastframe) | *optional* | The previewed cropped frame callback. |

## onPreviewOriginalFrame

The previewed original frame callback. Add code to use the original frames.

```objc
- (void)onPreviewOriginalFrame:(FramePackage*)frame;
```

**Parameters**

`Original frames`: The data of original frame(s). The Camera Enhancer can make preprocessing on video frames. In this callback function, the input parameters are the original frames that are captured by the camera.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_dce addCameraListener:self];
- (void)onPreviewOriginalFrame:(FramePackage *) frame{
    // TODO add your code for original frame
}
```
2. 
```swift
dce.addTorchListener(self)
func onPreviewOriginalFrame(_ frame: FramePackage){
    // TODO add your code for original frame
}
```

**See also**

- [`FramePackage`]({{ site.ios-api-auxiliary }}dceframe.html)

## onPreviewFilterFrame

The previewed filtered frame callback. Add code to use the filtered frames.

```objc
- (void)onPreviewFilterFrame:(FramePackage*)frame;
```

**Parameters**

`Filtered frames`: The data of filtered frame(s). The Camera Enhancer can make preprocessing on video frames. If the frame filter processing is enabled, the input parameter of this function will be the filtered frames.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_dce addCameraListener:self];
- (void)onPreviewFilterFrame:(FramePackage *) frame{
    // TODO add your code for filter frame
}
```
2. 
```swift
dce.addTorchListener(self)
func onPreviewFilterFrame(_ frame: FramePackage){
    // TODO add your code for filter frame
}
```

**See also**

- [`FramePackage`]({{ site.ios-api-auxiliary }}dceframe.html)
- [`enableFrameFilter`]({{site.ios-api}}preprocess.html#enableframefilter)

## onPreviewFastFrame

The previewed fast frame callback. Add code to use the cropped frames.

```objc
- (void)onPreviewFastFrame:(FramePackage*)frame;
```

**Parameters**

`Fast frames`: The data of cropped frame(s). The Camera Enhancer can make preprocessing on video frames. If the fast mode is enabled, the input parameter of this function will be the specially cropped frames.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_dce addCameraListener:self];
- (void)onPreviewFastFrame:(FramePackage *) frame{
    // TODO add your code for fast frame
}
```
2. 
```swift
dce.addTorchListener(self)
func onPreviewFastFrame(_ frame: FramePackage){
    // TODO add your code for fast frame
}
```

**See also**

- [`FramePackage`]({{ site.ios-api-auxiliary }}dceframe.html)
- [`enableFastMode`]({{site.ios-api}}preprocess.html#enablefastmode)
