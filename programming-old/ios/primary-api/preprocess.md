---
layout: default-layout
ignore: true
title: Frame Preprocessing Methods - Dynamsoft Camera Enhancer - Objective-C & Swift API references
description: This is the documentation - Objective-C & Swift API references - Frame Preprocessing Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Objective-C & Swift, API references, Frame Preprocessing Methods
needAutoGenerateSidebar: true
breadcrumbText: iOS Frame Preprocessing Methods
noTitleIndex: true
permalink: /programming/ios/primary-api/preprocess.html
---

# iOS API Reference - Frame Preprocessing Methods

> You are viewing a history document page of DCE v1.0.3.

| Method | Description |
|-----------------|---------------|
| [`acquireListFrame`](#acquirelistframe) | Get the latest frame from the frame queue when this API is activated. |
| [`enableFastMode`](#enablefastmode) | Set the value true/false to turn on/off DCE fast mode |
| [`enableSensorControl`](#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
| [`setSensorControlThreshold`](#setsensorcontrolthreshold) | Make settings on sensor control threshold |
| [`enableFrameFilter`](#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`setMaxFrameRate`](#setmaxframerate) | Set max frame rate |

---

## AcquireListFrame

This API is designed for users to acquire a single frame. When this API is activated, it will fetch the latest frame from the DCE frame queue.

```objc
- (FramePackage*)AcquireListFrame;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
FramePackage *fg = [self.camera AcquireListFrame];
```
2. 
```swift
let fg = self.dce.acquireListFrame()
```

## enableFastMode

This API is designed for users to setup DCE fast mode. DCE fast mode will cut frames into small images that contains barcode areas to improve decode efficiency. It is recommended to be enabled when decoding a single barcode.

```objc
@property (nonatomic, assign) BOOL enableFastMode;
```

**Parameters**

`true`: enable the fast mode.  
`false`: disable the fast mode.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableFastMode:true];
//To check the status of DCE fast mode
[dce getEnableFastMode];
```
2. 
```swift
dce.enableFastMode = true
```

## enableSensorControl

Turn on (off) sensor control

```objc
@property (nonatomic, assign) BOOL enableSensorControl;
```

**Parameters**

`true`: enable the sensor filter.  
`false`: disable the sensor filter.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableSensorControl:true];
//To check the status of the DCE sensor control
BOOL res= [dce enableSensorControl];
```
2. 
```swift
dce.enableSensorControl(true)
//To check the status of the DCE sensor control
let res = dce.enableSensorControl
```

## setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```objc
- (void)setSensorControlThreshold:(double)sensor NS_SWIFT_NAME(setSensorControlThreshold(_:));
```

**Parameters**

`int`: A int value that stands for the sensor filter threshold.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setSensorControlThreshold:55];
```
2. 
```swift
dce.setSensorControlThreshold(55)
```

## enableFrameFilter

Turn on(off) DCE filter (recommended to be true).

**Parameters**

`true`: enable the frame sharpness filter.  
`false`: disable the frame sharpness filter.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableFrameFilter:true];
//To check the status of the DCE frame filter
BOOL res= [dce enableFrameFilter];
```
2. 
```swift
dce.enableFrameFilter(true)
//To check the status of the DCE frame filter
let res = dce.enableFrameFilter
```

## setMaxFrameRate

Set max frame rate.

```objc
- (void)setMaxFrameRate:(int)maxFrameRate NS_SWIFT_NAME(setMaxFrameRate(_:));
```

**Parameters**

`int`: A int value that stands for the max frame rate.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setMaxFrameRate:24];
```
2. 
```swift
dce.setMaxFrameRate(24)
```
