---
layout: default-layout
title: Resolution - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration Resolution of Dynamsoft Camera Enhancer iOS describes the resolution.
keywords:  Resolution
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Resolution
---

# EnumResolution

Enumeration `Resolution` describes the resolution.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSResolution)
{
   /**
    * Deprecated
    */
   DSResolutionAuto = 0,
   /**
    * Set the video streaming to the 480P resolution.
    */
   DSResolution480P = 1,
   /**
    * Set the video streaming to the 720P resolution.
    */
   DSResolution720P = 2,
   /**
    * Set the video streaming to the 480P resolution.
    */
   DSResolution1080P = 3,
   /**
    * Set the video streaming to the 4K resolution.
    */
   DSResolution4K = 4
};
```
>
```swift
public enum Resolution : Int{
   /**
    * Deprecated
    */
   auto = 0
   /**
    * Set the video streaming to the 480P resolution.
    */
   480P = 1
   /**
    * Set the video streaming to the 720P resolution.
    */
   720P = 2
   /**
    * Set the video streaming to the 480P resolution.
    */
   1080P = 3
   /**
    * Set the video streaming to the 4K resolution.
    */
   4K = 4
}
```
