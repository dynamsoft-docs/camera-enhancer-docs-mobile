---
layout: default-layout
title: DrawingItemState - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration DrawingItemState of Dynamsoft Camera Enhancer iOS describes the state of DrawingItems.
keywords:  DrawingItem, state
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: DrawingItemState
---

# DrawingItemState

Enumeration `DrawingItemState` describes the state of DrawingItems.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSDrawingItemState) {
   /**
    * The state of the DrawingItem is the default state.
    */
   DSDrawingItemStateDefault = 1,
   /**
    * The state of the DrawingItem is selected.
    */
   DSDrawingItemStateSelected = 2
};
```
>
```swift
public enum EnumDrawingItemState : Int{
   /**
    * The state of the DrawingItem is the default state.
    */
   default = 1
   /**
    * The state of the DrawingItem is selected.
    */
   selected = 2
}
```
