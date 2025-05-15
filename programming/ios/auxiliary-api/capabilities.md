---
layout: default-layout
title: DSCapabilities - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSCapabilities of DynamsoftCameraEnhancer represents the capability properties of the hardware, including the maximum zoom factor, focal length, exposure time, and ISO.
keywords: capabilities, hardware, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCapabilities

The `DSCapabilities` class represents the capability properties of the hardware, including the maximum zoom factor, focal length, exposure time, and ISO.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSCapabilities : NSObject
```
2. 
```swift
class Capabilities : NSObject
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`maxZoomFactor`](#maxzoomfactor) | *CGFloat* | The maximum zoom factor. |
| [`minFocalLength`](#minfocallength) | *CGFloat* | The minimum focal length. |
| [`maxFocalLength`](#maxfocallength) | *CGFloat* | The maximum focal length. |
| [`minExposureTime`](#minexposuretime) | *CMTime* | The minimum exposure time. |
| [`maxExposureTime`](#maxexposuretime) | *CMTime* | The maximum exposure time. |
| [`minISO`](#miniso) | *CGFloat* | The minimum ISO. |
| [`maxISO`](#maxiso) | *CGFloat* | The maximum ISO. |

### maxZoomFactor

The maximum zoom factor.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGFloat maxZoomFactor;
```
2. 
```swift
var maxZoomFactor: CGFloat { get }
```

### minFocalLength

The minimum focal length.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGFloat minFocalLength;
```
2. 
```swift
var minFocalLength: CGFloat { get }
```

### maxFocalLength

The maximum focal length.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGFloat maxFocalLength;
```
2. 
```swift
var maxFocalLength: CGFloat { get }
```

### minExposureTime

The minimum exposure time.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CMTime minExposureTime;
```
2. 
```swift
var minExposureTime: CMTime { get }
```

### maxExposureTime

The maximum exposure time.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CMTime maxExposureTime;
```
2. 
```swift
var maxExposureTime: CMTime { get }
```

### minISO

The minimum ISO.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGFloat minISO;
```
2. 
```swift
var minISO: CGFloat { get }
```

### maxISO

The maximum ISO.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, readonly) CGFloat maxISO;
```
2. 
```swift
var maxISO: CGFloat { get }
```
