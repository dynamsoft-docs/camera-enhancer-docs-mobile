---
layout: default-layout
title: DrawingItemMediaType - Dynamsoft Camera Enhancer Android Enumerations
description: The enumeration DrawingItemMediaType of Dynamsoft Camera Enhancer Android describes the media type of DrawingItems.
keywords:  DrawingItem, media type
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: DrawingItemMediaType
---

# DrawingItemMediaType

The enumeration `DrawingItemMediaType` describes the media type of DrawingItems.

```java
@Retention(RetentionPolicy.CLASS)
public @interface EnumDrawingItemMediaType {
   // The mediate type of the DrawingItem is rectangle.
   int DIMT_RECTANGLE = 1;
   // The mediate type of the DrawingItem is quadrilateral.
   int DIMT_QUADRILATERAL = 2;
   // The mediate type of the DrawingItem is text.
   int DIMT_TEXT = 4;
   // The mediate type of the DrawingItem is line.
   int DIMT_LINE = 8;
}
```
