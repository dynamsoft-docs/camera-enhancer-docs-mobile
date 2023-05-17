---
layout: default-layout
title: EnumFocusMode - Dynamsoft Camera Enhancer
description: This is the documentation - EnumFocusMode page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Focus Mode
needAutoGenerateSidebar: true
breadcrumbText: EnumFocusMode
permalink: /programming/enumerations/enum-focus-mode.html
---

# EnumFocusMode

The enumeration that indicates the focus mode.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public enum EnumFocusMode {
   // Lock the focal length.
   FM_LOCKED(1),
   // Keep continuous auto-focus.
   FM_CONTINUOUS_AUTO(2);
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumFocusMode)
{
   /** Lock the focal length. */
   FM_LOCKED = 1,
   /** Keep continuous auto-focus. */
   FM_CONTINUOUS_AUTO = 2
};
```
>
```swift
public enum EnumFocusMode : Int{
   /** Lock the focal length. */
   FM_LOCKED = 1
   /** Keep continuous auto-focus. */
   FM_CONTINUOUS_AUTO = 2
}
```
