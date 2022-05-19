---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS 3.x Release Notes 
description: This is the documentation - iOS 3.x Release Notes page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS 3.x Release Notes
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS 3.x Release Notes
---

# Release Notes - iOS 3.x

## 3.0.0 (05/19/2022)

### Highlights

{%- include release-notes/product-highlight-3.0.0.md -%}

<div align="center">
  <p><img src="assets/edit.png" width="40%" alt="Fast-mode"></p>
  <p>Edit quadrilateral on DCEImageEditorView</p>
</div>

### Changelog

#### New

- Added class [`DCEImageEditorView`]({{ site.ios-api-auxiliary }}dceimageeditorview.html). Users can add `DCEDrawingLayers` on the `DCEImageEdiorView`.
- Added class [`DCEDrawingLayer`]({{ site.ios-api-auxiliary }}dcedrawinglayer.html). Users can add `DrawingItems` on the `DCEDrawingLayer`.
- Added class [`DrawingItem`]({{ site.ios-api-auxiliary }}drawingitem.html) and subclasses [`RectDrawingItem`]({{ site.ios-api-auxiliary }}drawingitem-rect.html), [`QuadDrawingItem`]({{ site.ios-api-auxiliary }}drawingitem-quad.html) and [`TextDrawingItem`]({{ site.ios-api-auxiliary }}drawingitem-text.html) for users to create UI elements.
- Added class [`DrawingStyleManager`]({{ site.ios-api-auxiliary }}drawingstylemanager.html) and [`DrawingStyle`]({{ site.ios-api-auxiliary }}drawingstyle.html) for users to change the styles of the DrawingItems.
- Added method [`getDrawingLayer`]({{ site.ios-api-auxiliary }}dcecameraview.html#getDrawingLayer) and [`createDrawingLayer`]({{ site.ios-api-auxiliary }}dcecameraview.html#createdrawinglayer) to class [`DCECameraView`]({{ site.ios-api-auxiliary }}dcecameraview.html) for users to edit the layers.
- Added enumerations [`EnumDrawingItemState`]({{ site.enumerations }}enum-drawing-item-state.html) and [`EnumDrawingMediaType`]({{ site.enumerations }}enum-drawing-item-media-type.html).
- Added dependency of `DynamsoftCore`.

#### Deprecate

- `DCECameraView.overlayVisible`
- `DCECameraView.setOverlayColour`
- `DCECameraView.vierfinderVisible`
- `DCECameraView.setViewfinder`
- `DynamsoftCameraEnhancer.initLicense`

#### Removed

- `CameraEnhancer.setFrameRate`
- `EnumResolution.EnumRESOLUTION_HIGH`
- `EnumResolution.EnumRESOLUTION_MID`
- `EnumResolution.EnumRESOLUTION_LOW`
