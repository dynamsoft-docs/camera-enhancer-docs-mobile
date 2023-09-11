---
layout: default-layout
title: Android Camera Enhancer Library - Dynamsoft Camera Enhancer Documents
description: This is the main page of Camera Enhancer API Reference for Android SDK.
keywords: api reference, Android, camera enhancer
needAutoGenerateSidebar: true
needGenerateH3Content: true
breadcrumbText: Android Camera Enhancer
noTitleIndex: true
permalink: /programming/android/auxiliary-api/index-v3.0.3.html
---

# Camera Enhancer API Reference

`DynamsoftCameraEnhancer` is the libary that provides camera control and UI configuration APIs.

## Components

**Main Class**

| Classes | Description |
| ------- | ----------- |
| [`DynamsoftCameraEnhancer`](camera-enhancer.html) | The main class that includes camera control APIs. Features like frame filtering can be enabled via this class. |

**UI Classes**

| Classes | Description |
| ------- | ----------- |
| [`DCECameraView`](dcecameraview.html) | UI view class that displays video streaming. UI configuration APIs are available for users to visualize the detected results on the video streaming. |
| [`DCEImageEditorView`](dceimageeditorview.html) | UI view class that displays images. UI configuration APIs are available for users to highlight the detected results on the view with quadrilateral elements. The border of the quadrilaterals can be edited so that user can further accurate the detected results. |

<div align="center">
    <p><img src="../../../../assets/dce-ddn-view.gif" width="30%" alt="edit"></p>
    <p>DynamsoftCameraEnhancer UI View</p>
</div>

**Auxiliary Classes**

| Classes | Description |
| ------- | ----------- |
| [`DCEFrame`](dceframe.html) | The struct that `DynamsoftCameraEnhancer` stores the video frames. It contains the image data and other information of the video frame. |
| [`DCEDrawingLayer`](dcedrawinglayer.html) | The layers that contains `DrawingItems`. Users can add configurations for the `DrawingItems` via `DCEDrawingLayer` |
| [`DrawingItem`](drawingitem.html) | The`DrawingItems` are elements that can be added the UI. |
| [`QuadDrawingItem`](drawingitem-quad.html) | A subclass of `DrawingItem`. Users can add `QuadDrawingItems` to the layer to display quadrilateral elements on the view. |
| [`RectDrawingItem`](drawingitem-rect.html) | A subclass of `DrawingItem`. Users can add `RectDrawingItems` to the layer to display rectangle elements on the view. |
| [`TextDrawingItem`](drawingitem-text.html) | A subclass of `DrawingItem`. Users can add `TextDrawingItems` to the layer to display text box on the view. |
| [`DrawingStyle`](drawingstyle.html) | `DrawingStyle` stores colour, font and other detailed styles of `DrawingItems`. |
| [`DrawingStyleManager`](drawingstylemanager.html) | The class for users to create and adjust `DrawingStyles`. |
| [`CameraEnhancerException`](camera-enhancer-exception.html) | Exception for signaling camera enhancer errors. |

**Interface**

| Classes | Description |
| ------- | ----------- |
| [`DCEFrameListener`](interface-dceframelistener.html) | The interface to handle callback when previewed frame callback is returned. |
| [`DCECameraStateListener`](interface-dcecamerastatelistener.html) | The interface to handle callback when camera state changes. |
