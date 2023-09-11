---
layout: default-layout
title: DSCameraEnhancerModule - Dynamsoft Core Module iOS Edition API Reference
description: The class DSCameraEnhancerModule of Dynamsoft Core Module represents the camera enhancer module, which provides general functions for the camera enhancer.
keywords: camera enhancer, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraEnhancerModule

The `DSCameraEnhancerModule` class defines general functions of the camera enhancer module.

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSCameraEnhancerModule : NSObject
```
2. 
```swift
class CameraEnhancerModule : NSObject
```

## Methods

| Method | Description |
|------- |-------------|
| [`getVersion`](#getversion) | Get the version of Dynamsoft Camera Enhancer. |

## getVersion

Get the version of Dynamsoft Camera Enhancer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (NSString *)getVersion;
```
2. 
```swift
class func getVersion() -> String
```

**Return Value**

The version of Dynamsoft Camera Enhancer.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NSString *version = [DSCameraEnhancerModule getVersion];
```
2. 
```swift
let version = CameraEnhancerModule.getVersion()
```
