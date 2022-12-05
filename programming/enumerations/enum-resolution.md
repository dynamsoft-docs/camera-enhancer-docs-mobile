---
layout: default-layout
title: Enumerations Resolution - Dynamsoft Camera Enhancer
description: This is the documentation - Enumerations Resolution page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Resolution
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Resolution
---

# EnumResolution

The enumeration that indicates the resolution.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public enum EnumResolution {
   // Use the default resolution. Generally, the default resolution is 1080P.
   RESOLUTION_AUTO(0),
   // The 480P resolution. Generally, the video frame size is about 360*640.
   RESOLUTION_480P(1),
   // The 720P resolution. Generally, the video frame size is about 720*1280.
   RESOLUTION_720P(2),
   // The 1080P resolution. Generally, the video frame size is about 1080*1920.
   RESOLUTION_1080P(3),
   // The 2K resolution. Generally, the video frame size is about 1080*1920.
   RESOLUTION_2K(4),
   // The 4K resolution. Generally, the video frame size is about 2160*3840.
   RESOLUTION_4K(5);
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumResolution)
{
   /** Use the default resolution. Generally, the default resolution is 1080P. */
   EnumRESOLUTION_AUTO = 0,
   /** The 480P resolution. Generally, the video frame size is about 480*640. */
   EnumRESOLUTION_480P = 1,
   /** The 720P resolution. Generally, the video frame size is about 720*1280. */
   EnumRESOLUTION_720P = 2,
   /** The 1080P resolution. Generally, the video frame size is about 1080*1920. */
   EnumRESOLUTION_1080P = 0,
   /** The 1080P resolution. Generally, the video frame size is about 2160*3840. */
   EnumRESOLUTION_4K = 1
};
```
>
```swift
public enum EnumResolution : Int{
   /** Use the default resolution. Generally, the default resolution is 1080P. */
   EnumRESOLUTION_AUTO = 0,
   /** The 480P resolution. Generally, the video frame size is about 480*640. */
   EnumRESOLUTION_480P = 1,
   /** The 720P resolution. Generally, the video frame size is about 720*1280. */
   EnumRESOLUTION_720P = 2,
   /** The 1080P resolution. Generally, the video frame size is about 1080*1920. */
   EnumRESOLUTION_1080P = 0,
   /** The 1080P resolution. Generally, the video frame size is about 2160*3840. */
   EnumRESOLUTION_4K = 1
}
```
