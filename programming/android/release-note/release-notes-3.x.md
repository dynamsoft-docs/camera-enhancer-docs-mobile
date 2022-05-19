---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android 3.x Release Notes 
description: This is the documentation - Android 3.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android 3.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Android 3.x Release Notes
---

# Release Notes - Android 3.x

## 3.0.0 (05/19/2022)

### Highlights

{%- include release-notes/product-highlight-3.0.0.md -%}

<div align="center">
  <p><img src="assets/edit.png" width="40%" alt="Fast-mode"></p>
  <p>Edit quadrilateral on DCEImageEditorView</p>
</div>

### Changelog

#### New

- Added class [`DCEImageEditorView`]({{ site.android-api-auxiliary }}dceimageeditorview.html). Users can add `DCEDrawingLayers` on the `DCEImageEdiorView`.
- Added class [`DCEDrawingLayer`]({{ site.android-api-auxiliary }}dcedrawinglayer.html). Users can add `DrawingItems` on the `DCEDrawingLayer`.
- Added class [`DrawingItem`]({{ site.android-api-auxiliary }}drawingitem.html) and subclasses [`RectDrawingItem`]({{ site.android-api-auxiliary }}drawingitem-rect.html), [`QuadDrawingItem`]({{ site.android-api-auxiliary }}drawingitem-quad.html) and [`TextDrawingItem`]({{ site.android-api-auxiliary }}drawingitem-text.html) for users to create UI elements.
- Added class [`DrawingStyleManager`]({{ site.android-api-auxiliary }}drawingstylemanager.html) and [`DrawingStyle`]({{ site.android-api-auxiliary }}drawingstyle.html) for users to change the styles of the DrawingItems.
- Added method [`getDrawingLayer`]({{ site.android-api-auxiliary }}dcecameraview.html#getDrawingLayer) and [`createDrawingLayer`]({{ site.android-api-auxiliary }}dcecameraview.html#createdrawinglayer) to class [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html) for users to edit the layers.
- Added enumerations [`EnumDrawingItemState`]({{ site.enumerations }}enum-drawing-item-state.html) and [`EnumDrawingMediaType`]({{ site.enumerations }}enum-drawing-item-media-type.html).
- Added dependency of `DynamsoftCore`.

#### Deprecated

- `DCECameraView.setOverlayVisible`
- `DCECameraView.getOverlayVisible`
- `DCECameraView.setOverlayColour`
- `DCECameraView.setViewfinderVisible`
- `DCECameraView.getViewfinderVisible`
- `DCECameraView.setViewfinder`
- `CameraEnhancer.initLicense`

#### Removed

- `CameraEnhancer.setFrameRate`
