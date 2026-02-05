---
layout: default-layout
title: Resolution - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration Resolution of Dynamsoft Camera Enhancer Android describes the resolution.
keywords:  Resolution
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Resolution
---

# EnumResolution

Enumeration `Resolution` describes the resolution.

```java
@IntDef({RESOLUTION_AUTO,RESOLUTION_480P,RESOLUTION_720P,RESOLUTION_1080P,RESOLUTION_2K,RESOLUTION_4K})
@Retention(RetentionPolicy.CLASS)
public @interface EnumResolution {
   // 480P
   int RESOLUTION_480P = 1;
   // 720P
   int RESOLUTION_720P = 2;
   // 1080P
   int RESOLUTION_1080P = 3;
   // 2K
   int RESOLUTION_2K = 4;
   // 4K
   int RESOLUTION_4K = 5;
   // Set the resolution to max so that you can capture 3024*4032 size photo.
   int RESOLUTION_MAX = 6;
}
```
