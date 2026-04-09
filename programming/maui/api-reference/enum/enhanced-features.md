---
layout: default-layout
title: EnumEnhancedFeatures - Dynamsoft Capture Vision MAUI Edition
description: The enumeration EnhancedFeatures of DCE MAUI describes the enhanced camera controlling features.
keywords: frame filter, sensor control, enhanced focus, auto zoom, smart torch
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: EnhancedFeatures
---

# EnumEnhancedFeatures

`EnhancedFeatures` describes the enhanced camera controlling features.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```csharp
public enum EnumEnhancedFeatures : int
{
    //Enable the Frame filter feature
    EF_FRAME_FILTER = 1 << 0,
    //Enable the sensor control feature
    EF_SENSOR_CONTROL = 1 << 1,
    //Enable the camera focus features
    EF_ENHANCED_FOCUS = 1 << 2,
    //Enable the autozoom feature
    EF_AUTO_ZOOM = 1 << 3,
    //Enable the smart torch button
    EF_SMART_TORCH = 1 << 4,
    // Enable all
    EF_ALL = int.MaxValue
}
```
