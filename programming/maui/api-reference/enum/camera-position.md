---
layout: default-layout
title: EnumCameraPosition - Dynamsoft Capture Vision MAUI Edition
description: The enumeration CameraPosition of DCE MAUI describes the camera position.
keywords: Camera Position, front forward, back forward
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CameraPosition
---

# Enumeration CameraPosition

`CameraPosition` describes the camera position.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```csharp
public enum EnumCameraPosition : int
{
    // The back-facing camera.
    CP_BACK = 0,
    // The front-facing camera.
    CP_FRONT = 1
    /**
     * The back-facing ultra-wide-angle camera. It is an ultra-wide-angle camera for macro-distance capturing.
     */
    CP_BACK_ULTRA_WIDE,
    /**
     * A back-facing virtual camera. It is a vitural camera that can switch between the wide-angle camera and the ultra-wide-angle camera automatically.
     * Supported devices include: iPhone 13 Pro, iPhone 13 Pro Max, and all subsequent Pro and Pro Max models.
     */
    CP_BACK_DUAL_WIDE_AUTO
}
```
