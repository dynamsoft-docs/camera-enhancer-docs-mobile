---
layout: default-layout
title: Enumerations Camera Position - Dynamsoft Camera Enhancer
description: This is the documentation - Enumerations Camera Position page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Camera Position
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Camera Position
permalink: /programming/enumerations/enum-camera-position.html
---

# EnumCameraPosition

The enumeration that indicates the camera position.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public enum EnumCameraPosition {
   // The back-facing camera.
   CP_BACK(0),
   // The front-facing camera.
   CP_FRONT(1);
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumCameraPosition)
{
   /** The back-facing camera. */
   EnumCameraPositionBack = 0,
   /** The front-facing camera. */
   EnumCameraPositionBack = 1
};
```
>
```swift
public enum EnumCameraPosition : Int{
   /** The back-facing camera. */
   back = 0
   /** The front-facing camera. */
   front = 1
}
```
