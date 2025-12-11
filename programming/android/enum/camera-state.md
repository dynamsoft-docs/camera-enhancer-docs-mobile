---
layout: default-layout
title: CameraState - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration CameraState of Dynamsoft Camera Enhancer Android describes the camera state.
keywords:  Camera state
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CameraState
---

# CameraState

Enumeration `CameraState` describes the camera state.

```java
@IntDef({OPENING,OPENED,CLOSING,CLOSED})
@Retention(RetentionPolicy.CLASS)
public @interface EnumCameraState {
   // The camera is opening.
   int OPENING = 0;
   // The camera is opened.
   int OPENED = 1;
   // The camera is closing.
   int CLOSING = 2;
   // The camera is closed.
   int CLOSED = 3;
}
```
