---
layout: default-layout
title: iOS FramePackage Class - Dynamsoft Camera Enhancer
description: This is the documentation - iOS FramePackage Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS FramePackage Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS FramePackage Class
---

# FramePackage

The `FramePackage` is the class that stores pixel data and further information.

```objc
@interface FramePackage : NSObject
```

| Attribute Name | Type |
|------|------|
| [`buffer`](#buffer) | NSData* |
| [`width`](#width) | NSNumber* |
| [`height`](#height) | NSNumber* |
| [`stride`](#stride) | NSNumber* |
| [`pixelFormat`](#pixelformat) | NSString* |
| [`frameID`](#frameid) | NSNumber* |
| [`fastFrameID`](#fastframeid) | NSNumber* |
| [`imageBuffer`](#imagebuffer) | CVImageBufferRef |

## buffer

Store the buffered frame data in NSData.

```objc
NSData* buffer
```

## width

Store the width of the frame.

```objc
NSNumber* width
```

## height

Store the height of the frame.

```objc
NSNumber* height
```

## stride

Store the stride of the frame.

```objc
NSNumber* stride
```

## pixelFormat

Store the pixel format of the frame.

```objc
NSString* pixelFormat
```

## frameID

Store the frame ID of the frame.

```objc
NSNumber* frameID
```

## fastFrameID

Store the fast frame ID of the frame.

```objc
NSNumber* fastFrameID
```

## imageBuffer

Store the buffered frame data in CVImageBufferRef.

```objc
CVImageBufferRef imageBuffer
```
