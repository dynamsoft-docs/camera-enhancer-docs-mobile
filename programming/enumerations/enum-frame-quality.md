---
layout: default-layout
title: Enumerations Frame Quality - Dynamsoft Camera Enhancer
description: This is the documentation - Enumerations Frame Quality page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Frame Quality
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Frame Quality
---

# EnumFrameQuality

## Declarations

The enumeration that indicates the frame quality.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public class EnumFrameQuality {
   // The DCEFrame quality is high.
   public static final int FQ_HIGH = 0;
   // The DCEFrame quality is low.
   public static final int FQ_LOW = 1;
   // The DCEFrame quality is unknown because the frame filter feature is not enabled.
   public static final int FQ_UNKNOWN = 2;
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumFrameQuality)
{
   /** The DCEFrame quality is high. */
   EnumFRAME_QUALITY_HIGH = 0,
   /** The DCEFrame quality is low. */
   EnumFRAME_QUALITY_LOW = 1,
   /** The DCEFrame quality is unknown because the frame filter feature is not enabled. */
   EnumFRAME_QUALITY_UNKNOWN = 2
};
```
>
```swift
public enum EnumFrameQuality : Int{
   /** The DCEFrame quality is high. */
   EnumFRAME_QUALITY_HIGH = 0
   /** The DCEFrame quality is low. */
   EnumFRAME_QUALITY_LOW = 1
   /** The DCEFrame quality is unknown because the frame filter feature is not enabled. */
   EnumFRAME_QUALITY_UNKNOWN = 2
}
```
