---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DCEFrame Class
description: This is the documentation - iOS DCEFrame Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS DCEFrame Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DCEFrame Class
---

# DCEFrame

Return the frame decode results and additional information.

```objc
@interface DCEFrame : NSObject
```

| Attribute Name | Type |
|------|------|
| [`frameData`](#buffer) | *NSData* * |
| [`width`](#width) | *NSInteger* |
| [`height`](#height) | *NSInteger* |
| [`stride`](#stride) | *NSInteger* |
| [`format`](#pixelformat) | *NSInteger* |
| [`frameID`](#frameid) | *NSInteger* |
| [`fastFrameID`](#fastframeid) | *NSInteger* |
| [`orientation`](#orientation) | *NSInteger* |
| [`imageBuffer`](#imagebuffer) | *CVImageBufferRef* |

## frameData

Store the buffered frame data in NSData.

```objectivec
NSData* buffer
```

## width

Store the width of the frame.

```objectivec
NSInteger width
```

## height

Store the height of the frame.

```objectivec
NSInteger height
```

## stride

Store the stride of the frame.

```objectivec
NSInteger stride
```

## format

Store the pixel format of the frame.

```objectivec
NSInteger format
```

**Value**

`3`: The Enumeration value of `ImagePixelFormat.EnumImagePixelFormatNV21`.  
`7`: The Enumeration value of `ImagePixelFormat.EnumImagePixelFormatARGB_8888`.

## frameID

Store the frame ID of the frame.

```objectivec
NSInteger frameID
```

## fastFrameID

Store the fast frame ID of the frame.

```objectivec
NSInteger fastFrameID
```

## orientation

Stores the orientation value

```objectivec
NSInteger orientation
```

**Value**

The following image illustrates how we defined 4 different device orientations.

<div align="center">
    <p><img src="assets/getOrientation.png" width="70%" alt="getOrientation"></p>
    <p>All orientation values</p>
</div>

## imageBuffer

Store the buffered frame data in CVImageBufferRef.

```objectivec
CVImageBufferRef imageBuffer
```
