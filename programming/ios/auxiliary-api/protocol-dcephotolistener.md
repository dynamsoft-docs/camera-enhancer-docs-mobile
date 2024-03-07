---
layout: default-layout
title: DSPhotoListener - DynamsoftCameraEnhancer iOS Edition API Reference
description: The protocol DSPhotoListener of DynamsoftCameraEnhancer defines the methods for monitoring the photo output.
keywords: photo listener, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSPhotoListener

The `DSPhotoListener` protocol defines the methods for monitoring the photo output.

## Definition

*Assembly:* DynamsoftCore.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSPhotoListener <NSObject>
```
2. 
```swift
protocol PhotoListener : NSObjectProtocol
```

## Methods

| Method | Description |
|------- |-------------|
| [`onPhotoOutput`](#onphotooutput) | The method for monitoring the photo output. |

### onPhotoOutput

The method for monitoring the photo output.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onPhotoOutput:(NSData *)jpegBytes;
```
2. 
```swift
func onPhotoOutput(_ jpegBytes: Data)
```

**Parameters**

`jpegBytes`: The captured photo as JPEG bytes.
