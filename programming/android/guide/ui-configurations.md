---
layout: default-layout
title: UI Configuration - Exploring Features of Dynamsoft Camera Enhancer Android Edition.
description: This page introduce how to configure the UI with Dynamsoft Camera Enhancer Android Edition.
keywords:  Camera Enhancer, UI, overlay
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: UI configurations
permalink: /programming/android/guide/ui-configurations.html
---

# UI configurations

`DynamsoftCameraEnhancer` library provides a series of UI configuring APIs for users to add basic UI elements.

View Classes

* [`CameraView`](../auxiliary-api/dcecameraview.html): Display the captured video streaming and related UI elements.
* [`ImageEditorView`](../auxiliary-api/dceimageeditorview.html): Display an image and editable UI elements.

Auxiliary APIs

* [`DrawingItem`](../auxiliary-api/drawingitem.html): The struct for you to draw basic UI elements.
* [`DrawingLayer`](../auxiliary-api/dcedrawinglayer.html): Container of DrawingItems. You can add multiple layer to a view.
* [`DrawingStyle`](../auxiliary-api/drawingstyle.html): Defines the styles of the DrawingItems.

## Highlight Results

### Display Control

`DynamsoftCameraEnhancer` provides a layer for each Dynamsoft image processing product. You can switch the `visible` property of the layer to control whether to highlight the results.

| Layers | Description |
| --------- | ----------- |
| `DDN_LAYER_ID` | The preset DrawingLayer of Dynamsoft Document Normalizer. |
| `DBR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Barcode Reader. |
| `DLR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Label Recognizer. |

For example, you can use the following code to highlight the barcode decoding results:

```java
// Get DBR layer with the layer ID.
DrawingLayer layer = mImageEditorView.getDrawingLayer(DrawingLayer.DBR_LAYER_ID);
// Set the visible property to true.
layer.setVisible(true);
// If you want to disable the highlight of barcode decoding results, add the following line.
// layer.setVisible(false);
```

### Change the Style

There are several preset styles definded in the `DrawingStyleManager`. You can directly specify the colour with the preset styles or create your own styles.

The follow code snippet shows how to specify preset styles:

```java
// Set the default DrawingStyles of the layer.
layer.setDefaultStyle(DrawingStyleManager.STYLE_BLUE_STROKE_FILL);
// Set the default style of the layer with filter options.
layer.setDefaultStyle(DrawingStyleManager.STYLE_BLUE_STROKE_FILL, EnumDrawingItemState.DEFAULT, EnumDrawingItemMediaType.DIMT_QUADRILATERAL);
```

Create a use-defined style:

```java
int userDefinedStyle = DrawingStyleManager.createDrawingStyle(R.color.white,1f, R.color.white,R.color.white);
```

## Add More Basic Graphics

A `DrawingItem` is the basic unit that you can draw on the view. It has different subclasses so that you can create `DrawingItems` in different shapes. Here we use `QuadDrawingItem` as an example to illustrate how to draw graphics on the view.

```java
// Create an ArrayList for appending DrawingItems
ArrayList<DrawingItem> drawingItemArray = new ArrayList<DrawingItem>();
// Create a quadrilateral
Quadrilateral quad = new Quadrilateral();
// Set the coordinate information of the Quadrilateral
// quad.points[0] = new Point(0,0);
// ...
drawingItemArray.add(quad);
// You can add multiple DrawingItems to the layer.
// Set the drawingItems to the layer
layer.setDrawingItems(drawingItemArray);
```
