---
layout: default-layout
title: iOS 3.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - iOS 3.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS 3.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS 3.x Release Notes
permalink: /programming/ios/release-note/release-notes-3.x.html
---

# Release Notes - iOS 3.x

## 3.0.3 (02/15/2023)

* Fixed a bug where `QuadDrawingItem` is not correctly displayed.

## 3.0.2 (02/02/2023)

* Override method [`setFocus`](../primary-api/camera-enhancer.html#setfocussubsequentfocusmode) in `CameraEnhancer` class for users to specify the subsequent focus mode after triggering a focus. Enumeration [`EnumFocusMode`]({{ site.dce-enums }}focus-mode.html?lang=objc&swift) is added to specify the focus mode.
* Added a new method [`setAutoZoomRange`](../primary-api/camera-enhancer.html#setautozoomrange) in `CameraEnhancer` for users to specify a range for the auto-zoom feature of the library.
* Added an interface [`DCECameraStateListener`](../auxiliary-api/protocol-dcecamerastatelistener.html) to receive a callback when the camera state changes. You can add the protocol via a new method [`setCameraStateListener`](../primary-api/camera-enhancer.html#setcamerastatelistener).
* Added a new method [`getVisibleRegionOfVideo`](../auxiliary-api/dcecameraview.html#getvisibleregionofvideo) in `DCECameraView` class
* Deprecated method `pause` and `resume` in `CameraEnhancer` class.
* Fixed a bug that might be caused by thread blocking when using an offline license.
* Deprecated method `pause` and `resume` in `CameraEnhancer` class.
* Fixed a bug that `torchButton` was not clickable when it appeared outside `scanRegion`.
* Fixed a scan region deviation bug.
* Fixed an overlay offset bug when `DCECamearView` is smaller than the screen size.
* Fixed a bug that might cause high CPU occupancy when the camera is opened.
* Fixed a bug that `scanRegion` is not correctly set when device was rotated horizontally.
* The `video buffer` will be cleared when camera is paused or closed.

## 3.0.1 (09/29/2022)

* Added methods [`selectCamera(EnumCameraPosition)`](../primary-api/camera-enhancer.html#selectcamerawithposition) and [`getCameraPosition`](../primary-api/camera-enhancer.html#getcameraposition) for users to switch between the front-facing camera and the back-facing camera.
* Added enumeration [`EnumCameraPosition`]({{ site.dce-enums }}camera-position.html?lang=iOS).
* Added a new class [`DCEFeedback`]({{site.ios-api-auxiliary}}dcefeedback.html). The following APIs are available in the class:
  * [`vibrate`]({{site.ios-api-auxiliary}}dcefeedback.html#vibrate): Triggers a vibration.
  * [`Beep`]({{site.ios-api-auxiliary}}dcefeedback.html#beep): Triggers a beep sound.

## 3.0.0 (06/21/2022)

* Updated UI configuration APIs.
  * Added [`DCEImageEditorView`](../auxiliary-api/dceimageeditorview.html)
  * Added [`DCEDrawingLayer`](../auxiliary-api/dcedrawinglayer.html)
  * Added DrawingItem Classes
    * [`DrawingItem`](../auxiliary-api/drawingitem.html)
    * [`QuadDrawingItem`](../auxiliary-api/drawingitem-quad.html)
    * [`RectDrawingItem`](../auxiliary-api/drawingitem-rect.html)
    * [`TextDrawingItem`](../auxiliary-api/drawingitem-text.html)
  * Added [`DrawingStyle`]
  * Added [`DrawingStyleManager`]
