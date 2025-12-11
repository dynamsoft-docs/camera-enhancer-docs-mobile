---
layout: default-layout
title: FocusMode - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration FocusMode of Dynamsoft Camera Enhancer iOS describes the focus mode.
keywords:  Focus mode
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: FocusMode
---

# FocusMode

Enumeration `FocusMode` describes the focus mode.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSFocusMode){
   /**
    * Lock the focal length.
    */
   DSFocusModeLocked           =   1,
   /**
    * Enable the continuous auto-focus.
    */
   DSFocusModeContinuousAuto     =   2
};
```
>
```swift
public enum FocusMode : Int{
   /**
    * Lock the focal length.
    */
   locked           =   1
   /**
    * Enable the continuous auto-focus.
    */
   continuousAuto     =   2
}
```
