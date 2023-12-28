---
layout: default-layout
title: Android 4.x Release Notes  - Dynamsoft Camera Enhancer
description: This is the documentation - Android 4.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 4.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 4.x Release Notes
permalink: /programming/android/release-note/release-notes-4.x.html
---

# Release Notes - Android 4.x

## 4.0.3 (12/28/2023)

* Fixed a bug crash bug caused by auto-zoom feature.

## 4.0.2 (12/07/2023)

* Fixed a bug where method `getSelectedDrawingItem` might not return correctly.

## 4.0.1 (10/26/2023)

* Added a new method `setDrawingItemClickListener` to class `CameraView` & `ImageEditorView`. You can set a `DrawingItemClickListener` to the view to monitor the click events of the `DrawingItems`.
* Fixed a bug where `getDrawingItems` returns the previous coordinate information when `DrawingItems` are edited on the `ImageEditorView`.
* Applied some internal changes to the resolution control and scan region UI setting APIs.

## 4.0.0 (08/10/2023)

* Refactored the camera-controlling APIs of the CameraEnhancer class.
* Refactored the UI configuration APIs.
  * Updated the scan region setting APIs. Support scan laser setting.
  * Added new features to set the coordinate base of the DrawingItems and tip messages.
  * Other minor changes on the API names and behaviors.
* Added tip configuration APIs to display tip messages.
* A new class Note has been added to enable DrawingItems to carry additional information.
