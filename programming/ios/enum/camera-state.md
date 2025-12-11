---
layout: default-layout
title: CameraState - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration CameraState of Dynamsoft Camera Enhancer iOS describes the camera state.
keywords:  Camera state
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CameraState
---

# CameraState

Enumeration `CameraState` describes the camera state.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSCameraState)
{
   /**
    * The camera is opening.
    */
   DSCameraStateOpening = 0,
   /**
    * The camera is opened.
    */
   DSCameraStateOpened = 1,
   /**
    * The camera is closing.
    */
   DSCameraStateClosing = 2,
   /**
    * The camera is closed.
    */
   DSCameraStateClosed = 3
};
```
>
```swift
public enum CameraState : Int{
   /**
    * The camera is opening.
    */
   opening = 0
   /**
    * The camera is opened.
    */
   opened = 1
   /**
    * The camera is closing.
    */
   closing = 2
   /**
    * The camera is closed.
    */
   closed = 3
}
```
