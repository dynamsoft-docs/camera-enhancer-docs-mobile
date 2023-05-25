---
layout: default-layout
title: Enumerations Camera State - Dynamsoft Camera Enhancer
description: This is the documentation - Enumerations Camera State page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Camera State
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Camera State
permalink: /programming/enumerations/enum-camera-state.html
---

# EnumCameraState

The enumeration that indicates the camera state.

<div class="sample-code-prefix template2"></div>
   >- Android
   >- Objective-C
   >- Swift
   >
>
```java
public enum EnumCameraState {
   OPENING(0),
   OPENED(1),
   CLOSING(2),
   CLOSED(3);
}
```
>
```objc
typedef NS_ENUM(NSInteger, EnumCameraState)
{
   /** The camera is opening.*/
   EnumCAMERA_STATE_OPENING NS_SWIFT_NAME(EnumCAMERA_STATE_OPENING)  = 0,
   /** The camera is opened.*/
   EnumCAMERA_STATE_OPENED  NS_SWIFT_NAME(EnumCAMERA_STATE_OPENED)   = 1,
   /** The camera is closing.*/
   EnumCAMERA_STATE_CLOSING  NS_SWIFT_NAME(EnumCAMERA_STATE_CLOSING)   = 2,
   /** The camera is closed.*/
   EnumCAMERA_STATE_CLOSED  NS_SWIFT_NAME(EnumCAMERA_STATE_CLOSED)   = 3
};
```
>
```swift
public enum EnumCameraState : Int{
   /** The camera is opening.*/
   EnumCAMERA_STATE_OPENING = 0
   /** The camera is opened.*/
   EnumCAMERA_STATE_OPENED = 1
   /** The camera is closing.*/
   EnumCAMERA_STATE_CLOSING = 2
   /** The camera is closed.*/
   EnumCAMERA_STATE_CLOSED = 3
}
```
