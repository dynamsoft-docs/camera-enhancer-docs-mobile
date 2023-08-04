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

## 4.0.0 (08/04/2023)

* Refactored the camera-controlling APIs of the [`CameraEnhancer`]({{ site.ios }}primary-api/camera-enhancer.html) class.
* Refactored the UI configuration APIs.
  * Updated the scan region setting APIs of the [`CameraView`]({{ site.ios }}auxiliary-api/camera-view.html) class. Added supports of scan region mask style setting and scan laser setting.
  * Added new features to set the coordinate base of the [`DrawingItems`]({{ site.ios }}auxiliary-api/drawing-item.html) and tip messages.
  * Other minor changes on the API names and behaviors.
* Added tip configuration APIs to display tip messages.
* A new class [`Note`]({{ site.ios }}auxiliary-api/note.html) has been added to enable DrawingItems to carry additional information.
