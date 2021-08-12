---
layout: default-layout
title: Dynamsoft Camera Enhancer - Objective-C & Swift API references - Frame Preprocessing Methods
description: This is the documentation - Objective-C & Swift API references - Frame Preprocessing Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Objective-C & Swift, API references, Frame Preprocessing Methods
needAutoGenerateSidebar: true
breadcrumbText: iOS Frame Preprocessing Methods
noTitleIndex: true
---

# iOS API Reference - Frame Preprocessing Methods

| Method | Description |
|-----------------|---------------|
| [`acquireListFrame`](#acquirelistframe) | Get the latest frame from the frame queue when this API is activated. |
| [`enableFastMode`](#enablefastmode) | Set the value true/false to turn on/off DCE fast mode |
| [`enableSensorControl`](#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
|[`setSensorControlThreshold`](#setsensorcontrolthreshold)| Make settings on sensor control threshold |
| [`enableFrameFilter`](#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`setMaxFrameRate`](#setmaxframerate) | Set max frame rate |

---

## AcquireListFrame

This API is designed for users to acquire a single frame. When this API is activated, it will fetch the latest frame from the DCE frame queue.

```objectivec
- (FramePackage*)AcquireListFrame;
```

**Code Snippet**

Objective-C:

```objectivec
FramePackage *fg = [self.camera AcquireListFrame];
```

Swift:

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

Objective-C:

```objectivec
[dce enableFastMode:true];
//To check the status of DCE fast mode
[dce getEnableFastMode];
```

Swift:

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

Objective-C:

```objectivec
[dce enableSensorControl:true];
//To check the status of the DCE sensor control
BOOL res= [dce enableSensorControl];
```

Swift:

```swift
dce.enableSensorControl(true)
//To check the status of the DCE sensor control
let res = dce.enableSensorControl
```

## setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```objectivec
- (void)setSensorControlThreshold:(double)sensor NS_SWIFT_NAME(setSensorControlThreshold(_:));
```

**Parameters**

`int`: A int value that stands for the sensor filter threshold.

**Code Snippet**

Objective-C:

```objectivec
[dce setSensorControlThreshold:55];
```

Swift:

```swift
dce.setSensorControlThreshold(55)
```

## enableFrameFilter

Turn on(off) DCE filter (recommended to be true).

**Parameters**

`true`: enable the frame sharpness filter.  
`false`: disable the frame sharpness filter.

**Code Snippet**

Objective-C:

```objectivec
[dce enableFrameFilter:true];
//To check the status of the DCE frame filter
BOOL res= [dce enableFrameFilter];
```

Swift:

```swift
dce.enableFrameFilter(true)
//To check the status of the DCE frame filter
let res = dce.enableFrameFilter
```

## setMaxFrameRate

Set max frame rate.

```objectivec
- (void)setMaxFrameRate:(int)maxFrameRate NS_SWIFT_NAME(setMaxFrameRate(_:));
```

**Parameters**

`int`: A int value that stands for the max frame rate.

**Code Snippet**

Objective-C:

```objectivec
[dce setMaxFrameRate:24];
```

Swift:

```swift
dce.setMaxFrameRate(24)
```
