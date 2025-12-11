---
layout: default-layout
title: CameraPosition - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration CameraPosition of Dynamsoft Camera Enhancer Android describes the camera position.
keywords:  Camera Position
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CameraPosition
---

# CameraPosition

Enumeration `CameraPosition` describes the camera position.

```java
@IntDef({CP_FRONT,CP_BACK})
@Retention(RetentionPolicy.CLASS)
public @interface EnumCameraPosition {
   // The back-facing camera.
   int CP_BACK= 0;
   // The front-facing camera.
   int CP_FRONT = 1;
}
```
