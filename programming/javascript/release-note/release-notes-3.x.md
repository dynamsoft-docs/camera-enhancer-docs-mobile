---
layout: default-layout
title: Dynamsoft Camera Enhancer - JavaScript 3.x Release Notes 
description: This is the Release Notes page for Dynamsoft Camera Enhancer JavaScript SDK.
keywords:  camera enhancer, release notes, javascript
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: v3.x Release Notes
---

# Release Notes - JavaScript 3.x

## 3.0.0 (07/21/2022)

<div class="fold-panel-prefix"></div>

### Version Highlights <i class="fa fa-caret-down"></i>

<div class="fold-panel-start"></div>

{%- include release-notes/product-highlight-3.0.0.md -%}

<div class="fold-panel-end"></div>

### Changelog

#### New

* Added property `isDisposed` to indicate whether the `CameraEnhancer` instance has been disposed.
* Added method `offAll()` to remove all event handlers from the specified event. If no event is specified, remove all event handlers.
* Added method `removeScanRegionOverlayCanvas()` to remove the specified Canvas element.

* Added interface `DrawingLayer` to organize items whinch are drawn for same purposes.
* Added method `createDrawingLayer()` to create a `DrawingLayer` object and put it in an array of `DrawingLayer` objects.
* Added method `getDrawingLayer()` to get the `DrawingLayer` specified by the input id.
* Added method `clearDrawingLayers()` to remove all `DrawingLayer` objects.

* Added type `DrawingItem` to define items to be drawn.
* Added class `DT_Rect`, `DT_Arc`, `DT_Text`, `DT_Line`, `DT_Polygon`, `DT_Group` and `DT_Image` to define different shapes of `DrawingItem`.
* Added enum `EnumDrawingItemMediaType ` to specify types for different `DrawingItem`.
* Added interface `Point` to simplify input coordinate arguments when construct objects of `DT_Line` and `DT_Polygon`.

* Added interface `DrawingStyle` to customize styles for `DrawingItem`.
* Added method `createDrawingStyle()` to create a `DrawingStyle` object and return its id.
* Added method `getDrawingStyle()` to get the `DrawingStyle` specified by input id.
* Added method `getDrawingStyles()` to get all `DrawingStyle` objects.
* Added method `updateDrawingStyle()` to get specified `DrawingStyle` updated.

* Added method `switchUIMode()` to switch between editor and viewer mode. Default is viewer mode.
* Added method `getUIMode()` to get the current UI mode.
* Added method `setOriginalImage()` to set an original image to be drawn on the editor canvas.
* Added method `getOriginalImage()` to get the original image shown on the editor canvas.
* Added method `deleteOriginalImage()` to delete the original image and remove the canvas that shows it.
* Added method `getSelectedDrawingItems()` to get the selected `DrawingItem` object(s).
