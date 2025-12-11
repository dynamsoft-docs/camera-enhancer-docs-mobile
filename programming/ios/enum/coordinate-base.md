---
layout: default-layout
title: CoordinateBase - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration CoordinateBase of Dynamsoft Camera Enhancer iOS describes the coordinate base.
keywords:  Coordinate base
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CoordinateBase
---

# CoordinateBase

Enumeration `CoordinateBase` describes the camera position.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSCoordinateBase) {
   /**
    * Image coordinate.
    */
   DSCoordinateBaseImage = 0,
   /**
    * View coordinate.
    */
   DSCoordinateBaseView = 1
};
```
>
```swift
public enum CoordinateBase : Int{
   /**
    * Image coordinate.
    */
   image = 0
   /**
    * View coordinate.
    */
   view = 1
}
```
