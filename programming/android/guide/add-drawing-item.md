---
layout: default-layout
title: Configure Zoom & Focus Settings - Exploring Features of Dynamsoft Camera Enhancer Android Edition.
description: This page introduce how to configure zoom & focus settings with Dynamsoft Camera Enhancer Android Edition.
keywords:  Camera Enhancer, Zoom, Focus
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Zoom & Focus
permalink: /programming/android/guide/add-drawing-item.html
---

# Add DrawingItem

```java
// Create ImageEditorView
private ImageEditorView mImageEditorView;
mImageEditorView = findViewById(R.id.editor_view);

// Create an ArrayList for appending DrawingItems
ArrayList<DrawingItem> drawingItemArray = new ArrayList<DrawingItem>();

// Suppose you receive a series of detected quad result items as quadResultItems.
DetectedQuadResultItem[] quadResultItems = result.getItems();

for (int i=0; i <= quadResultItems.length; i++)
{
    // Create quadDrawingItem with location attribute in DetectedQuadResultItem.
    QuadDrawingItem quadItem = new QuadDrawingItem(r.location);

    // Create RectDrawingItem with bounding rect of the Quad.
    // RectDrawingItem rectItem = new RectDrawingItem(r.location.getBoundingRect());

    // Optional, you can set DrawingStyle for your DrawingItem.
    quadItem.setDrawingStyleId(DrawingStyleManager.STYLE_BLUE_STROKE_FILL);
    // rectItem.setDrawingStyleId(DrawingStyleManager.STYLE_ORANGE_STROKE_FILL);

    drawingItemArray.add(quadItem);
}
// Get DDN layer with Layer ID and add the drawing items.
DrawingLayer layer = mImageEditorView.getDrawingLayer(DCEDrawingLayer.DDN_LAYER_ID);
layer.setDrawingItems(drawingItemArray);

// Set the default DrawingStyles of the layer.
layer.setDefaultStyle(DrawingStyleManager.STYLE_BLUE_STROKE_FILL);
layer.setDefaultStyle(DrawingStyleManager.STYLE_BLUE_STROKE_FILL, EnumDrawingItemState.DEFAULT);
layer.setDefaultStyle(DrawingStyleManager.STYLE_BLUE_STROKE_FILL, EnumDrawingItemState.DEFAULT, EnumDrawingItemMediaType.DIMT_QUADRILATERAL);
```
