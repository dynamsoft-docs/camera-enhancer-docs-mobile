---
layout: default-layout
title: DrawingItemState - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration DrawingItemState of Dynamsoft Camera Enhancer Android describes the state of DrawingItems.
keywords:  DrawingItem, state
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: DrawingItemState
---

# DrawingItemState

Enumeration `DrawingItemState` describes the state of DrawingItems.

```java
@IntDef({DIS_DEFAULT,DIS_SELECTED})
@Retention(RetentionPolicy.CLASS)
public @interface EnumDrawingItemState {
   // The state of the DrawingItem is the default state.
   int DIS_DEFAULT = 1;
   // The state of the DrawingItem is selected.
   int DIS_SELECTED = 2;
}
```
