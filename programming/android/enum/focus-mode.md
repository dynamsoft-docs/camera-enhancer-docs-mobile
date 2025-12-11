---
layout: default-layout
title: FocusMode - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration FocusMode of Dynamsoft Camera Enhancer Android describes the focus mode.
keywords:  Focus mode
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: FocusMode
---

# FocusMode

Enumeration `FocusMode` describes the focus mode.

```java
@IntDef({FM_LOCKED,FM_CONTINUOUS_AUTO})
@Retention(RetentionPolicy.CLASS)
public @interface EnumFocusMode {
   // Lock the focal length.
   int FM_LOCKED = 1;
   // Keep continuous auto-focus.
   int FM_CONTINUOUS_AUTO = 2;
}
```
