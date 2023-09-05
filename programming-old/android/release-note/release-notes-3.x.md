---
layout: default-layout
title: Android 3.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - Android 3.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 3.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 3.x Release Notes
permalink: /programming/android/release-note/release-notes-3.x.html
---

# Release Notes - Android 3.x

## 3.0.3 (02/15/2023)

* Fixed a crash bug on the devices that do not support 16:9 size resolution.

## 3.0.2 (02/02/2023)

* Override method [`setFocus`](../primary-api/camera-enhancer.html#setfocussubsequentfocusmode) in `CameraEnhancer` class for users to specify the subsequent focus mode after triggering a focus. Enumeration [`EnumFocusMode`]({{ site.dce-enums }}focus-mode.html?lang=android) is added to specify the focus mode.
* Added a new method [`setAutoZoomRange`](../primary-api/camera-enhancer.html#setautozoomrange) in `CameraEnhancer` for users to specify a range for the auto-zoom feature of the library.
* Added an interface [`DCECameraStateListener`](../auxiliary-api/protocol-dcecamerastatelistener.html) to receive a callback when the camera state changes. You can add the protocol via a new method [`setCameraStateListener`](../primary-api/camera-enhancer.html#setcamerastatelistener).
* Added a new method [`getVisibleRegionOfVideo`](../auxiliary-api/dcecameraview.html#getvisibleregionofvideo) in `DCECameraView` class
* Deprecated method `pause` and `resume` in `CameraEnhancer` class.
* Fixed a bug that might cause thread blocking when using an offline license.
* Fixed a bug that UI might be blocked when the screen is locked and reopened.
* Fixed a bug that might cause memory churn when the instance/thread was created frequently.
* Fixed a bug that might throws exception when triggering `CameraEnhancer.close` after triggering `CameraEnhancer.pause`.
* Fixed a bug that camera might not be opened after camera permission is allowed.
* Fixed a bug that might cause camera crash when the `DCECameraView` is quit without destroying.
* Fixed a deformation bug of `DCECameraView` when the screen rotated.

## 3.0.1 (09/29/2022)

* Added methods [`selectCamera(EnumCameraPosition)`](../primary-api/camera-enhancer.html#selectcameraenumcameraposition) and [`getCameraPosition`](../primary-api/camera-enhancer.html#getcameraposition) for users to switch between the front-facing camera and the back-facing camera.
* Added enumeration [`EnumCameraPosition`]({{ site.dce-enums }}camera-position.html?lang=android).
* Added a new class [`DCEFeedback`]({{site.android-api-auxiliary}}dcefeedback.html). The following APIs are available in the class:
  * [`vibrate`]({{site.android-api-auxiliary}}dcefeedback.html#vibrate): Triggers a vibration.
  * [`Beep`]({{site.android-api-auxiliary}}dcefeedback.html#beep): Triggers a beep sound.
* Added the following APIs for capturing photos:
  * [`DCEPhotoListener`]({{site.android-api-auxiliary}}interface-dcephotolistener.html): The interface that includes method [`photoOutputCallback`]({{site.android-api-auxiliary}}interface-dcephotolistener.html#photooutputcallback) which is triggered when a photo is captured. JPEG-encoded photo can be received via the method [`photoOutputCallback`]({{site.android-api-auxiliary}}interface-dcephotolistener.html#photooutputcallback).
  * [`takePhoto`]({{site.android-api}}camera-enhancer.html#takephoto): Triggers photo capturing.
* Fixed a null pointer bug that might occur when rotating the `DCECameraView`.
* Fixed a crash bug when some methods are called in child thread.

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
