---
layout: default-layout
title: EnhancedFeatures - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration EnhancedFeatures of Dynamsoft Camera Enhancer iOS describes the features of camera enhancer.
keywords:  Camera enhancer features
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: EnhancedFeatures
---

# EnhancedFeatures

Enumeration `EnhancedFeatures` indicates the advanced features of Dynamsoft Camera Enhancer iOS.

- `Frame Filter`: The frame sharpness filter feature of DCE. By enabling this feature, the low-quality frame will be recognized and discarded automatically.
- `Sensor Control`: The sensor filter feature of DCE. By enabling this feature, the frames will be discarded automatically while the device is shaking.
- `Enhanced Focus`: The enhanced focus feature. DCE will support the camera in triggering auto-focus.
- `Auto Zoom`: The auto-zoom feature of DCE. By enabling this feature, the camera will automatically zoom in to the interest area.
- `Smart Torch`: Add a smart torch on the UI. The torch will be hided when the environment brightness is high and displayed when the brightness is low.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSEnhancedFeatures)
{
   /**
    * Enable frame filter feature of the camera enhancer to make a filter out the low-quality frames.
    */
   DSEnhancedFeatureFrameFilter = 1 << 0,
   /**
    * Enable sensor control to filter out all the frames when the device is shaking.
    */
   DSEnhancedFeatureSensorControl = 1 << 1,
   /**
    * Enhanced focus helps low-end devices on focusing.
    */
   DSEnhancedFeatureEnhancedFocus = 1 << 2,
   /**
    * Enable the camera zoom-in automatically when barcode is far away.
    */
   DSEnhancedFeatureAutoZoom = 1 << 3,
   /**
    * Display a torch button when the environment light is low.
    */
   DSEnhancedFeatureSmartTorch = 1 << 4,
   /**
    * Enable all the enhanced features.
    */
   DSEnhancedFeatureAll = NSUIntegerMax
};
```
>
```swift
public enum EnhancedFeatures : Int{
   /**
    * Enable frame filter feature of the camera enhancer to make a filter out the low-quality frames.
    */
   frameFilter = 1 << 0
   /**
    * Enable sensor control to filter out all the frames when the device is shaking.
    */
   sensorControl = 1 << 1
   /**
    * Enhanced focus helps low-end devices on focusing.
    */
   enhancedFocus = 1 << 2
   /**
    * Enable the camera zoom-in automatically when barcode is far away.
    */
   autoZoom = 1 << 3
   /**
    * Display a torch button when the environment light is low.
    */
   smartTorch = 1 << 4
   /**
    * Enable all the enhanced features.
    */
   all = UInt.max
}
```
