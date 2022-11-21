---
layout: default-layout
title: Dynamsoft Camera Enhancer - Enumerations Enhancer Features
description: This is the documentation - Enumerations Enhancer Features page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Enhancer Features
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Enhancer Features
---

# EnumEnhancerFeatures

The enumeration that indicates the advanced features of Dynamsoft Camera Enhancer.

- `Frame Filter`: The frame sharpness filter feature of DCE. By enabling this feature, the low-quality frame will be recognized and discarded automatically.
- `Sensor Control`: The sensor filter feature of DCE. By enabling this feature, the frames will be discarded automatically while the device is shaking.
- `Enhanced Focus`: The enhanced focus feature. DCE will support the camera in triggering auto-focus.
- `Fast Mode`: The fast mode of DCE. By enabling the fast mode, the frames will be cropped to speed up the following processing.
- `Auto Zoom`: The auto-zoom feature of DCE. By enabling this feature, the camera will automatically zoom in to the interest area.
- `Smart Torch`: Add a smart torch on the UI. The torch will be hided when the environment brightness is high and displayed when the brightness is low.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public class EnumEnhancerFeatures {
   // The frame sharpness filter feature.
   public static final int EF_FRAME_FILTER = 1;
   // The sensor filter feature.
   public static final int EF_SENSOR_CONTROL = 2;
   // The enhanced focus feature.
   public static final int EF_ENHANCED_FOCUS = 4;
   // The fast mode of DCE.
   public static final int EF_FAST_MODE = 8;
   // The auto-zoom feature.
   public static final int EF_AUTO_ZOOM = 16;
   // Add a smart torch on the UI.
   public static final int EF_SMART_TORCH = 32;
   // The combined value of all the features.
   public static final int EF_ALL = 63;
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumEnhancerFeatures)
{
   /** The frame sharpness filter feature. */
   EnumFRAME_FILTER = 0X01,
   /** The sensor filter feature. */
   EnumSENSOR_CONTROL = 0X02,
   /** The enhanced focus feature. */
   EnumENHANCED_FOCUS = 0X04,
   /** The fast mode of DCE. */
   EnumFAST_MODE = 0X08,
   /** The auto-zoom feature. */
   EnumAUTO_ZOOM = 0X10,
   /** Add a smart torch on the UI. */
   EnumSMART_TORCH = 0X20,
   /** The combined value of all the features. */
   EnumALL = 0X3F
};
```
>
```swift
public enum EnumEnhancerFeatures : Int{
   /** The frame sharpness filter feature. */
   EnumFRAME_FILTER = 0X01
   /** The sensor filter feature. */
   EnumSENSOR_CONTROL = 0X02
   /** The enhanced focus feature. */
   EnumENHANCED_FOCUS = 0X04
   /** The fast mode of DCE. */
   EnumFAST_MODE = 0X08
   /** The auto-zoom feature. */
   EnumAUTO_ZOOM = 0X10
   /** Add a smart torch on the UI. */
   EnumSMART_TORCH = 0X20
   /** The combined value of all the features. */
   EnumALL = 0X3F
}
```
