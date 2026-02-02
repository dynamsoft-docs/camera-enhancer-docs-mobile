---
layout: default-layout
title: DSFocusListener - DynamsoftCameraEnhancer iOS Edition API Reference
description: The protocol that includes methods for monitoring the focus status.
keywords: Focus listener, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSFocusListener

The `DSFocusListener` protocol includes methods for monitoring the focus status and receiving focus completion events.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSFocusListener <NSObject>
```
2. 
```swift
protocol FocusListener : NSObjectProtocol
```

## Methods

| Method | Description |
|------- |-------------|
| [`onFocusFinished`](#onfocusfinished) | The method for receiving notifications when a focus operation is completed. |

### onFocusFinished

The method for receiving notifications when a focus operation is completed.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onFocusFinished:(CGPoint)focusPoint;
```
2. 
```swift
func onFocusFinished(_ focusPoint: CGPoint)
```

**Parameters**

`focusPoint`: A `CGPoint` object that represents the coordinates of the focus point.

**Remarks**

If a new focus request is triggered before the previous one completes, the previous request will be canceled, and only the final successfully completed focus operation will invoke this callback.

This callback is triggered under the following conditions:

- Always triggered when calling `setFocus(Point, FocusModeLocked)`
- Might be triggered when performing tap-to-focus
- Never triggered when calling `setFocus(Point, FocusModeContinuousAuto)`
