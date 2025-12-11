---
layout: default-layout
title: EnhancedFeatures - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration EnhancedFeatures of Dynamsoft Camera Enhancer Android describes the features of camera enhancer.
keywords:  Camera enhancer features
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: EnhancedFeatures
---

# EnhancedFeatures

Enumeration `EnhancedFeatures` indicates the advanced features of Dynamsoft Camera Enhancer Android.

- `Frame Filter`: The frame sharpness filter feature of DCE. By enabling this feature, the low-quality frame will be recognized and discarded automatically.
- `Sensor Control`: The sensor filter feature of DCE. By enabling this feature, the frames will be discarded automatically while the device is shaking.
- `Enhanced Focus`: The enhanced focus feature. DCE will support the camera in triggering auto-focus.
- `Auto Zoom`: The auto-zoom feature of DCE. By enabling this feature, the camera will automatically zoom in to the interest area.
- `Smart Torch`: Add a smart torch on the UI. The torch will be hided when the environment brightness is high and displayed when the brightness is low.

```java
@Retention(RetentionPolicy.CLASS)
public @interface EnumEnhancedFeatures {
   //Enable the Frame filter feature of DCE
   int EF_FRAME_FILTER = 0x01;
   //Enable the sensor control feature of DCE
   int EF_SENSOR_CONTROL = 1 << 1;
   //Enable the camera focus features of DCE
   int EF_ENHANCED_FOCUS = 1 << 2;
   //Enable the autozoom feature
   int EF_AUTO_ZOOM = 1 << 3;
   //Enable the smart torch button
   int EF_SMART_TORCH = 1 << 4;
   // All.
   int EF_ALL = 0x1F;
}
```

> [!Note]
>
> Value changed in v3.2.1000:
> - Changed `EF_AUTO_ZOOM` from `1 << 4` to `1 << 3`.
> - Changed `EF_SMART_TORCH` from `1 << 5` to `1 << 4`.
> - Changed `EF_ALL` from `0x3F` to `0x1F`.
