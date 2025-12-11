---
layout: default-layout
title: CoordinateBase - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration CoordinateBase of Dynamsoft Camera Enhancer Android describes the coordinate base.
keywords:  Coordinate base
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CoordinateBase
---

# CoordinateBase

Enumeration `CoordinateBase` describes the camera position.

```java
@IntDef({CB_IMAGE,CB_VIEW})
@Retention(RetentionPolicy.CLASS)
public @interface EnumCoordinateBase {
   // pixel, percentage
   int CB_IMAGE = 0;
   // DP
   int CB_VIEW = 1;
}
```
