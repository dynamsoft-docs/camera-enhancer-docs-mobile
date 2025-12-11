---
layout: default-layout
title: DrawingItemMediaType - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration DrawingItemMediaType of Dynamsoft Camera Enhancer iOS describes the media type of DrawingItems.
keywords:  DrawingItem, media type
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: DrawingItemMediaType
---

# DrawingItemMediaType

The enumeration `DrawingItemMediaType` describes the media type of DrawingItems.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSDrawingItemMediaType) {
   /**
    * The mediate type of the DrawingItem is rectangle.
    */
   DSDrawingItemMediaTypeRectangle = 1,
   /**
    * The mediate type of the DrawingItem is quadrilateral.
    */
   DSDrawingItemMediaTypeQuadrilateral = 2,
   /**
    * The mediate type of the DrawingItem is text.
    */
   DSDrawingItemMediaTypeText = 4,
   /**
    * The mediate type of the DrawingItem is line.
    */
   DSDrawingItemMediaTypeLine = 8
};
```
>
```swift
public enum DrawingItemMediaType : Int{
   /**
    * The mediate type of the DrawingItem is rectangle.
    */
   rectangle = 1
   /**
    * The mediate type of the DrawingItem is quadrilateral.
    */
   quadrilateral = 2
   /**
    * The mediate type of the DrawingItem is text.
    */
   text = 4
   /**
    * The mediate type of the DrawingItem is line.
    */
   line = 8
}
```
