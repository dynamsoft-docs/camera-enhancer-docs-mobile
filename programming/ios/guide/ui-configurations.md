---
layout: default-layout
title: UI Configuration - Exploring Features of Dynamsoft Camera Enhancer iOS Edition.
description: This page introduce how to configure the UI with Dynamsoft Camera Enhancer iOS Edition.
keywords:  Camera Enhancer, UI, overlay
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: UI configurations
permalink: /programming/ios/guide/ui-configurations.html
---

# UI configurations

`DynamsoftCameraEnhancer` library provides a series of UI configuring APIs for users to add basic UI elements.

View Classes

* [`CameraView`](../auxiliary-api/dcecameraview.html): Display the captured video streaming and related UI elements.
* [`ImageEditorView`](../auxiliary-api/dceimageeditorview.html): Display an image and editable UI elements.

Auxiliary APIs

* [`DrawingItem`](../auxiliary-api/drawingitem.html): The struct for you to draw basic UI elements.
* [`DrawingLayer`](../auxiliary-api/drawinglayer.html): Container of DrawingItems. You can add multiple layer to a view.
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

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
// Get the layer first.
DSDrawingLayer *layer = [self.cameraView getDrawingLayer:DSDrawingLayerIdDBR];
// Set the visible property to true or false to control the visibility.
layer.visible = false;
```
2. 
```swift
// Get the layer first.
layer = cameraView.getDrawingLayer(DrawingLayerId.DLR.rawValue)
// Set the visible property to true or false to control the visibility.
layer.visible = false
```

### Change the Style

There are several preset styles definded in the `DrawingStyleManager`. You can directly specify the colour with the preset styles or create your own styles.

The follow code snippet shows how to specify preset styles:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
// Change the style of the layer.
[layer setDefaultStyle:DSDrawingStyleIdBlueStroke];
// Set the default style of the layer with filter options.
[layer setDefaultStyle:DSDrawingStyleIdOrangeStroke forState:DSDrawingItemStateSelected forType:DSDrawingItemMediaTypeQuadrilateral];
```
2. 
```swift
// Change the style of the layer.
layer.setDefaultStyle(DrawingStyleId.blueStroke.rawValue)
// Set the default style of the layer with filter options.
layer?.setDefaultStyle(DrawingStyleId.blueStroke.rawValue, forState: DrawingItemState.default.rawValue, forType: DrawingItemMediaType.line.rawValue)
```

Create a use-defined style:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
// Create a new DrawingStyle via the DrawingStyleManager.
NSInteger userDefinedStyle = [DSDrawingStyleManager createDrawingStyle:UIColor.blueColor strokeWidth:2 fillColor:UIColor.blueColor textColor:UIColor.blueColor font:UIFontTextStyleTitle1];
```
2. 
```swift
// Create a new DrawingStyle via the DrawingStyleManager.
let styleID = DrawingStyleManager.createDrawingStyle(UIColor.red, strokeWidth: 1, fill: UIColor.init(red: 255, green: 0, blue: 0, alpha: 0.1), textColor: UIColor.red, font:UIFont.systemFont(ofSize: 1) )
```

## Add More Basic Grahpics

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

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NSMutableArray<DSDrawingItem*>* items = [[NSMutableArray alloc] init];
// Create an array of point
// NSArray *pointArray = @[@(CGPointMake(0, 0)), ...];
DSQuadrilateral *quad = [[DSQuadrilateral alloc] initWithPointArray:pointArray];
DSQuadDrawingItem *item = [[DSQuadDrawingItem alloc] initWithQuadrilateral:quad];
[items addObject:item];
[layer setDrawingItems:items];
```
2. 
```swift
// Create a QuadDrawingItem
// let quad = Quadrilateral.init(pointArray: [CGPoint(x: 0, y: 0), ...])
let quadDrawingItem = QuadDrawingItem.init(quadrilateral: quad)
layer?.drawingItems = [quadDrawingItem]
```
