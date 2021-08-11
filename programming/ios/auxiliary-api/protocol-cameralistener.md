---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS Protocol CameraEnhancerListener
description: This is the documentation - iOS Protocol CameraEnhancerListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol CameraEnhancerListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol CameraEnhancerListener
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

The previewed original frame callback.

```objc
- (void)onPreviewOriginalFrame:(FramePackage*)frame;
```

**Parameters**

`frame`: The frame data. View in [`FramePackage`]({{ site.ios-api-auxiliary }}framepackage.html).

**Code Snippet**

Objective-C:

```objc
[_dce addCameraListener:self];

- (void)onPreviewOriginalFrame:(FramePackage *) frame{
    // TODO add your code for original frame
}
```

Swift:

```swift
dce.addTorchListener(self)

func onPreviewOriginalFrame(_ frame: FramePackage){
    // TODO add your code for original frame
}
```

## onPreviewFilterFrame

The previewed filtered frame callback.

```objc
- (void)onPreviewFilterFrame:(FramePackage*)frame;
```

**Parameters**

`frame`: The frame data. View in [`FramePackage`]({{ site.ios-api-auxiliary }}framepackage.html).

**Code Snippet**

Objective-C:

```objc
[_dce addCameraListener:self];

- (void)onPreviewFilterFrame:(FramePackage *) frame{
    // TODO add your code for filter frame
}
```

Swift:

```swift
dce.addTorchListener(self)

func onPreviewFilterFrame(_ frame: FramePackage){
    // TODO add your code for filter frame
}
```

## onPreviewFastFrame

The previewed fast frame callback.

```objc
- (void)onPreviewFastFrame:(FramePackage*)frame;
```

**Parameters**

`frame`: The frame data. View in [`FramePackage`]({{ site.ios-api-auxiliary }}framepackage.html).

**Code Snippet**

Objective-C:

```objc
[_dce addCameraListener:self];

- (void)onPreviewFastFrame:(FramePackage *) frame{
    // TODO add your code for fast frame
}
```

Swift:

```swift
dce.addTorchListener(self)

func onPreviewFastFrame(_ frame: FramePackage){
    // TODO add your code for fast frame
}
```
