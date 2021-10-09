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
| [`imageData`](#imagedata) | *NSData* * |
| [`width`](#width) | *NSInteger* |
| [`height`](#height) | *NSInteger* |
| [`stride`](#stride) | *NSInteger* |
| [`pixelFormat`](#pixelformat) | *NSInteger* |
| [`frameID`](#frameid) | *NSInteger* |
| [`quality`](#quality) | [`EnumFrameQuality`]({{site.barcode-enum}}enum-frame-quality.html) |
| [`isCropped`](#iscropped) | *BOOL* |
| [`cropRegion`](#cropregion) | *CGRect* |
| [`orientation`](#orientation) | *NSInteger* |

## imageData

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

## pixelFormat

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

## quality

The property that stores the quality of the `DCEFrame` image. User have to enable the frame filter feature to get the quality (high/low) of the `DCEFrame`. Otherwise, the frame quality will be unknown. View more in enumeration [`EnumFrameQuality`]({{site.barcode-enum}}enum-frame-quality.html).

```objectivec
EnumFrameQuality quality
```

## isCropped

## cropRegion

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
