---
layout: default-layout
title: EnumResolution - Dynamsoft Capture Vision MAUI Edition
description: The enumeration EnumResolution of Dynamsoft Capture Vision MAUI describes the camera resolutions.
keywords: resolution
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Resolution
---

# EnumResolution

`Resolution` describes the focus mode.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```csharp
public enum EnumResolution : int
{
    RESOLUTION_AUTO = 0,
    RESOLUTION_480P = 1,
    // 720*1280
    RESOLUTION_720P = 2,
    // 1920*1080. Default
    RESOLUTION_1080P = 3,
    // 3840*2160
    RESOLUTION_4K = 4,
    // 4032*3024. For taking photos
    RESOLUTION_MAX = 5
}
```
