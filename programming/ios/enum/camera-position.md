---
layout: default-layout
title: CameraPosition - Dynamsoft Camera Enhancer iOS Enumerations
description: The enumeration CameraPosition of Dynamsoft Camera Enhancer iOS describes the camera position.
keywords:  Camera Position
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: CameraPosition
---

# CameraPosition

Enumeration `CameraPosition` describes the camera position.

<div class="sample-code-prefix template2"></div>
   >- Objective-C
   >- Swift
   >
>
```objc
typedef NS_ENUM(NSInteger, DSCameraPosition) {
   /**
     * The default back-facing camera. It is a wide-angle camera for general usage.
     */
    DSCameraPositionBack,
   /**
     * The front-facing camera.
     */
    DSCameraPositionFront,
   /**
     * The back-facing ultra-wide-angle camera. It is an ultra-wide-angle camera for macro-distance capturing.
     */
    DSCameraPositionBackUltraWide API_AVAILABLE(ios(13.0)),
   /**
     * A back-facing virtual camera. It is a vitural camera that can switch between the wide-angle camera and the ultra-wide-angle camera automatically.
     * Supported devices include: iPhone 13 Pro, iPhone 13 Pro Max, iPhone 14 Pro, iPhone 14 Pro Max, iPhone 15 Pro, iPhone 15 Pro Max.
     */
    DSCameraPositionBackDualWideAuto API_AVAILABLE(ios(13.0))
} NS_SWIFT_NAME(CameraPosition);
```
>
```swift
public enum CameraPosition : Int{
   /**
     * The back-facing camera.
     */
   back = 0
   /**
     * The front-facing camera.
     */
   front = 1
   /**
     * The back-facing ultra-wide-angle camera. It is an ultra-wide-angle camera for macro-distance capturing.
     */
   backUltraWide = 2
   /**
     * A back-facing virtual camera. It is a vitural camera that can switch between the wide-angle camera and the ultra-wide-angle camera automatically.
     * Supported devices include: iPhone 13 Pro, iPhone 13 Pro Max, iPhone 14 Pro, iPhone 14 Pro Max, iPhone 15 Pro, iPhone 15 Pro Max.
     */
   backDualWideAuto = 3
}
```
