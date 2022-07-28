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

## 3.0.0 (07/27/2022)

### Changelog

#### New

* Added callback [onWarning](../api-reference/initialization.md#onwarning) which is triggered when the running environment is not ideal.
* Added property [`isDisposed`](../api-reference/auxiliary.md#isdisposed) to indicate whether the `CameraEnhancer` instance has been disposed.
* Added method [`offAll()`](../api-reference/auxiliary.md#offall) to remove all event handlers from the specified event. If no event is specified, remove all event handlers.
* Added method [`removeScanRegionOverlayCanvas()`](../api-reference/ui.md#removescanregionoverlaycanvas) to remove the specified Canvas element which was added with `addScanRegionOverlayCanvas()`.

The following APIs are for the new feature of drawing shapes. Read more on [Draw Shapes with DCE JS](../user-guide/features/draw-shapes.md).

* Added type [`DrawingItem`](../api-reference/interface/drawingitem.md) to define basic shapes to be drawn.
* Added class `DT_Rect`, `DT_Arc`, `DT_Text`, `DT_Line`, `DT_Polygon`, `DT_Image`, and `DT_Group` to define different shapes of `DrawingItem`.
* Added interface `Point` to describe the vertices when constructing objects of `DT_Line` and `DT_Polygon`.

* Added interface [`DrawingLayer`](../api-reference/interface/drawinglayer.md) to organize items.
* Added method [`createDrawingLayer()`](../api-reference/ui.md#createdrawinglayer) to create a `DrawingLayer` object.
* Added method [`getDrawingLayer()`](../api-reference/ui.md#getdrawinglayer) to get the `DrawingLayer` specified by its ID.
* Added method [`clearDrawingLayers()`](../api-reference/ui.md#cleardrawinglayers) to remove all `DrawingLayer` objects.

* Added interface [`DrawingStyle`](../api-reference/interface/drawingstyle.md) to customize styles for drawing `DrawingItem`s.
* Added method [`createDrawingStyle()`](../api-reference/ui.md#createdrawingstyle) to create a `DrawingStyle` object and return its ID.
* Added method [`getDrawingStyle()`](../api-reference/ui.md#getdrawingstyle) to get the `DrawingStyle` specified by its ID.
* Added method [`getDrawingStyles()`](../api-reference/ui.md#getdrawingstyles) to get all `DrawingStyle` objects.
* Added method [`updateDrawingStyle()`](../api-reference/ui.md#updatedrawingstyle) to update a `DrawingStyle` specified by its ID.

* Added method [`setOriginalImage()`](../api-reference/ui.md#setoriginalimage) to set an original image to be drawn on a built-in canvas above which shapes are drawn usually based on coordinates of certain objects found on this image by other SDKs such as barcode locations found by DBR.
* Added method [`getOriginalImage()`](../api-reference/ui.md#getoriginalimage) to return the original image.
* Added method [`showOriginalImage()`](../api-reference/ui.md#showoriginalimage) to show the built-in canvas on which the original image is drawn.
* Added method [`hideOriginalImage()`](../api-reference/ui.md#hideoriginalimage) to hide the built-in canvas on which the original image is drawn.
* Added method [`deleteOriginalImage()`](../api-reference/ui.md#deleteoriginalimage) to delete the original image and remove the built-in canvas that shows it.
* Added method [`getSelectedDrawingItems()`](../api-reference/ui.md#getselecteddrawingitems) to get the selected `DrawingItem`s which will be helpful in further processing of the original image by another SDK. For example, the `DrawingItem` may refer to the boundaries of the region of interest that the user wishes to crop from the image.

On the `DrawingLayer` interface:

* Added method [`addDrawingItems()`](../api-reference/interface/drawinglayer.md#adddrawingitems) to add one or multiple `DrawingItem`s.
* Added method [`getDrawingItems()`](../api-reference/interface/drawinglayer.md#getdrawingitems) to return all `DrawingItem`s.
* Added method [`removeDrawingItems()`](../api-reference/interface/drawinglayer.md#removedrawingitems) to remove one or multiple `DrawingItem`s.
* Added method [`setDrawingItems()`](../api-reference/interface/drawinglayer.md#setdrawingitems) to set new `DrawingItem`s which means old  `DrawingItem`s will be removed.
* Added method [`hasDrawingItem()`](../api-reference/interface/drawinglayer.md#hasdrawingitem) to determine whether a `DrawingItem` exists on this `DrawingLayer`.
* Added method [`clearDrawingItems()`](../api-reference/interface/drawinglayer.md#cleardrawingitems) to remove all `DrawingItem`s from this `DrawingLayer`.
* Added method [`setMode()`](../api-reference/interface/drawinglayer.md#setmode) to switch the `DrawingLayer` between editor and viewer mode.
* Added method [`getMode()`](../api-reference/interface/drawinglayer.md#getmode) to get the current mode the `DrawingLayer` is in.
* Added method [`getId()`](../api-reference/interface/drawinglayer.md#getid) to return the ID of the `DrawingLayer`.
* Added method [`setDrawingStyle()`](../api-reference/interface/drawinglayer.md#setdrawingstyle) to use different `DrwaingStyle`s on the `DrawingLayer`.
* Added method [`setVisible()`](../api-reference/interface/drawinglayer.md#setvisible) to show or hide the `DrawingLayer`.
* Added method [`isVisible()`](../api-reference/interface/drawinglayer.md#isvisible) to return whether the `DrawingLayer` is visible.
* Added method [`renderAll()`](../api-reference/interface/drawinglayer.md#renderall) to redraw all `DrawingItem`s.
* Added event [`onSelectionChange()`](../api-reference/interface/drawinglayer.md#onselectionchange) to listen on the selection or deselection of `DrawingItem`s on the `DrawingLayer`.
