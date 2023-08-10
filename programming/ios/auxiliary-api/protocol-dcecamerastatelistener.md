---
layout: default-layout
Title: DSCameraStateListener - Dynamsoft Core Module iOS Edition API Reference
Description: The protocol that includes methods for monitoring the camera state.
Keywords: camera state, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraStateListener

The `DSCameraStateListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* DynamsoftCore.framework

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

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[listener onCameraStateChanged:currentState];
```
2. 
```swift
listener.onCameraStateChanged(currentState)
```
