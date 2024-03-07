---
layout: default-layout
title: DSFeedback - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSFeedback of DynamsoftCameraEnhancer provides methods to trigger feedbacks from the hardware, such as vibrate and beep.
keywords: feedback, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSFeedback

The `DSFeedback` class provides methods to trigger feedbacks from the hardware, such as vibrate and beep.

## Definition

*Assembly:* DynamsoftCore.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSFeedback : NSObject
```
2. 
```swift
class Feedback : NSObject
```

## Methods

| Method | Description |
|------- |-------------|
| [`vibrate`](#vibrate) | Trigger a vibrate. |
| [`beep`](#beep) | Trigger a beep. |

### vibrate

Trigger a vibrate.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (void)vibrate;
```
2. 
```swift
class func vibrate()
```

### beep

Trigger a beep.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (void)beep;
```
2. 
```swift
class func beep()
```
