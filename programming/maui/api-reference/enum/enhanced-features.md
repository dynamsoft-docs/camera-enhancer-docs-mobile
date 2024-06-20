---
layout: default-layout
title: EnumEnhancedFeatures - Dynamsoft Vision Router MAUI Edition
description: The enumeration EnhancedFeatures of DCE MAUI describes the enhanced camera controlling features.
keywords: frame filter, sensor control, enhanced focus, auto zoom, smart torch
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: EnhancedFeatures
---

# Enumeration EnhancedFeatures

`EnhancedFeatures` describes the enhanced camera controlling features.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```csharp
public enum EnumEnhancedFeatures : int
{
    //Enable the Frame filter feature
    EF_FRAME_FILTER = 0x01,
    //Enable the sensor control feature
    EF_SENSOR_CONTROL = 0x02,
    //Enable the camera focus features
    EF_ENHANCED_FOCUS = 0x04,
    //Enable the autozoom feature
    EF_AUTO_ZOOM = 0x10,
    //Enable the smart torch button
    EF_SMART_TORCH = 0x20,
    // Enable all
    EF_ALL = 0x3F
}
```
