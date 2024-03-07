---
layout: default-layout
title: DSCameraStateListener - DynamsoftCameraEnhancer iOS Edition API Reference
description: The protocol that includes methods for monitoring the camera state.
keywords: camera state, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraStateListener

The `DSCameraStateListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* DynamsoftCore.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSCameraStateListener <NSObject>
```
2. 
```swift
protocol CameraStateListener : NSObjectProtocol
```

## Methods

| Method | Description |
|------- |-------------|
| [`onCameraStateChanged`](#oncamerastatechanged) | The method for monitoring the camera state and receiving call. |

### onCameraStateChanged

The method for monitoring the camera state and receiving call.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onCameraStateChanged:(DSCameraState)currentState;
```
2. 
```swift
func onCameraStateChanged(_ currentState: DSCameraState)
```

**Parameters**

`currentState`: The current camera state.
