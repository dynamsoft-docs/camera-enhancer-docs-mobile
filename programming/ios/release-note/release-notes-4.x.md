---
layout: default-layout
title: iOS 4.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - iOS 4.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS 4.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS 4.x Release Notes
permalink: /programming/ios/release-note/release-notes-4.x.html
---

# Release Notes - iOS 4.x

## 4.2.0 (03/07/2024)

* Internal changes to be compatible with `DynamsoftCaptureVisionRouter` v2.2.10.

## 4.0.2 (12/07/2023)

* Some internal changes.

## 4.0.1 (10/26/2023)

* Added a new method `setDrawingItemClickListener` to class `CameraView` & `ImageEditorView`. You can set a `DrawingItemClickListener` to the view to monitor the click events of the `DrawingItems`.
* Fixed a bug where `getDrawingItems` returns the previous coordinate information when `DrawingItems` are edited on the `ImageEditorView`.
* Applied some internal changes to the resolution control and scan region UI setting APIs.

## 4.0.0 (08/10/2023)

* Refactored the camera-controlling APIs of the [`CameraEnhancer`]({{ site.ios }}primary-api/camera-enhancer.html) class.
* Refactored the UI configuration APIs.
  * Updated the scan region setting APIs of the [`CameraView`]({{ site.ios }}auxiliary-api/dcecameraview.html) class. Added supports of scan region mask style setting and scan laser setting.
  * Added new features to set the coordinate base of the [`DrawingItems`]({{ site.ios }}auxiliary-api/drawingitem.html) and tip messages.
  * Other minor changes on the API names and behaviors.
* Added tip configuration APIs to display tip messages.
* A new class [`Note`]({{ site.ios }}auxiliary-api/note.html) has been added to enable DrawingItems to carry additional information.
