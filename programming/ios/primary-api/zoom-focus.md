---
layout: default-layout
title: Dynamsoft Camera Enhancer - Objective-C & Swift API references - Focus & Zoom Setting
description: This is the documentation - Objective-C & Swift API references - Focus & Zoom Setting page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Objective-C & Swift API references, Zoom, Focus
needAutoGenerateSidebar: true
breadcrumbText: iOS Focus & Zoom Methods
---

# iOS API Reference - Focus & Zoom Methods

## setDefaultAutoFocusPosition

Set the position you want to auto focus at. This setting will replace the default focus value and always focus on the set point.

```objc
- (void)setDefaultAutoFocusPosition:(CGPoint)point NS_SWIFT_NAME(setDefaultAutoFocusPosition(_:));
```

**Parameters**

`float`: A float value that stands for the X coordinate of the focus position.  
`float`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

Objective-C:

```objectivec
[dce setAutoFocusPosition:CGPointMake(0.5, 0.5)];
```

Swift:

```Swift
dce.setAutoFocusPosition(CGPoint(x: 0.5, y: 0.5))
```

## setManualFocusPosition

Set the position you want to manually focus at. This focus position only takes effect once each time this code is called.

```objc
- (void)setManualFocusPosition:(CGPoint)point NS_SWIFT_NAME(setManualFocusPosition(_:));
```

**Parameters**

`float`: A float value that stands for the X coordinate of the focus position.  
`float`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

Objective-C:

```objectivec
[dce setManualFocusPosition:CGPointMake(0.5, 0.5)];
```

Swift:

```Swift
dce.setManualFocusPosition(CGPoint(x: 0.5, y: 0.5))
```

## setFocalLength

Set focal length (float). The range of focal length is from 0 to 1. The value is a precentage. If user sets `setFocalLength(0.5);` it means the focal length will be 50% of the maxium focal length of the camera. Please note, If this API is called to set a focal length, the focal length will be fixed and all other auto focus mode will be disabled. To quit this fixed focal length mode, please set the focal length into -1.

```objc
- (void)setFocalLength:(float)len NS_SWIFT_NAME(setFocalLength(_:));
```

**Parameters**

`float`: A float value between 0 to 10 that stands for the focal length. You can input -1 to quit the fixed focal length mode.

**Code Snippet**

Objective-C:

```objectivec
[dce setFocalLength:0.8];
```

Swift:

```Swift
dce.setFocalLength = 0.8
```

## enableDCEAutoFocus

This API is designed to turn on DCE autofocus mode which is specially designed and is separate from the systems default autofocus mode. DCE autofocus and the default autofocus can work together at the same time without any conflict. The above focus settings are also available for controlling system default autofocus. To turn on DCE autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableDCEAutoFocus;
```

**Parameters**

`true`: Enable the DCE autofocus.
`false`: Disable the DCE autofocus.

**Code Snippet**

Objective-C:

```objectivec
[dce enableDCEAutoFocus:true];
//To check the status of DCE autofocus.
bool res = [dce enableDCEAutoFocus];
```

Swift:

```Swift
dce.enableDCEAutoFocus = true
//To check the status of DCE autofocus.
let res = dce.enableDCEAutoFocus
```

## enableDefaultAutoFocus

This API is designed for controlling the system default autofocus. To turn off default autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableDefaultAutoFocus;
```

**Parameters**

`true`: Enable the default autofocus.
`false`: Disable the default autofocus.

**Code Snippet**

Objective-C:

```objectivec
[dce enableDefaultAutoFocus:false];
//To check the status of system default autofocus.
bool res = [dce enableDefaultAutoFocus];
```

Swift:

```Swift
dce.enableDefaultAutoFocus = false
//To check the status of system default autofocus.
let res = dce.enableDefaultAutoFocus
```

## enableRegularAutoFocus

Regular autofocus is an advanced setting that enables the camera to autofocus for every 3 seconds. It is contained in DCE autofocus. When DCE autofocus is enabled, regular autofocus is enabled as well. To turn off regular autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableRegularAutoFocus;
```

**Parameters**

`true`: Enable the regular autofocus.
`false`: Disable the regular autofocus.

**Code Snippet**

Objective-C:

```objectivec
[dce enableRegularAutoFocus:false];
//To check the status of DCE autofocus.
bool res = [dce enableRegularAutoFocus];
```

Swift:

```Swift
dce.enableRegularAutoFocus = false
//To check the status of DCE regular autofocus.
let res = dce.enableRegularAutoFocus
```

## setRegularAutoFocusParam

Set the focus interval and termination time for the regular autofocus.

```objc
- (void)setRegularAutoFocusParam:(int)focusTimems terminateFocusByTime:(int)terminateFocusByTime NS_SWIFT_NAME(setRegularAutoFocusParam(_:terminateFocusByTime:));
```

**Parameters**

`int`: Default value is 3000 (millisecond), which means the camera will auto focus for every 3000 milliseconds.
`int`: Default value is 500 (millisecond), which means the camera will not focus once again within 500 milliseconds.

**Code Snippet**

```objectivec
//The camera will autofocus for every 3s. It won't focus for a second time within 500ms.
[_dce setRegularAutoFocusParam:3000 terminateFocusByTime:500];
```

Swift:

```Swift
dce.setRegularAutoFocusParam(3000, terminateFocusByTime: 500)
```

## enableAutoFocusOnSharpnessChange

This API is another advanced setting that enables the camera to autofocus when a change in sharpness is detected between contiguous frames. The same happens with regular autofocus, this focus mode is also enabled by default when DCE auto focus is enabled. To turn off camera autofocus when sharpness changes:

```objc
@property (nonatomic, assign) BOOL enableAutoFocusOnSharpnessChange;
```

**Parameters**

`true`: Enable the sharpness autofocus.
`false`: Disable the sharpness autofocus.

**Code Snippet**

Objective-C:

```objectivec
[dce enableAutoFocusOnSharpnessChange:false];
//To check the status of DCE sharpness focus.
bool res = [dce enableAutoFocusOnSharpnessChange];
```

Swift:

```Swift
dce.enableAutoFocusOnSharpnessChange = false
//To check the status of DCE sharpness focus.
let res = dce.enableAutoFocusOnSharpnessChange
```

## enableAutoZoom

DCE auto zoom mode can be enabled if user is using DCE to enhance decode performance. The auto zoom mode is based on decode region predicted algorithm. In DCE auto zoom mode, If the lastest decoded frame is predicted to contain a barcode but failing to decode, DCE will control the camera to zoom in to approach the barcode region. To enable auto zoom mode:

```objc
@property (nonatomic, assign) BOOL enableAutoZoom;
```

**Parameters**

`true`: Enable the autozoom.
`false`: Disable the autozoom.

**Code Snippet**

Objective-C:

```objectivec
[dce enableAutoZoom:true];
//To check the status of DCE autozoom.
bool res = [dce enableAutoZoom];
```

Swift:

```Swift
dce.enableAutoZoom = true
//To check the status of DCE autozoom.
let res = dce.enableAutoZoom
```

## setZoomFactor

To set the zoom factor (float).

```objc
- (void)setZoomFactor:(CGFloat)zoomFactor;
```

**Parameters**

`float`: A float value that stands for the zoom factor.

**Code Snippet**

Objective-C:

```objectivec
[dce setZoomFactor:1.5];
```

Swift:

```Swift
dce.setZoomFactor = 1.5
```
