---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DCEImageEditorView Class
description: This is the documentation - Android DCEImageEditorView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DCEImageEditorView
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DCEImageEditorView Class
---

# DCEImageEditorView

| Method Name | Description |
| ----------- | ----------- |
| [`getDrawingLayer`](#getdrawinglayer) | Get the `DCEDrawingLayer` instance with the layer ID. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a user defined `DCEDrawingLayer` instance. |
| [`getSelectedDrawingItem`](#getselecteddrawingitem) | Get the selected drawing item. |
| [`getDrawingStyle`](#getdrawingstyle) | Get the `DrawingStyle` instance with the style ID. |
| [`getAllDrawingStyles`](#getalldrawingstyles) | Get all the available `DrawingStyle` in a list. |
| [`createDrawingStyle`](#createdrawingstyle) | Create a user defined `DrawingStyle` instance. |

## setOriginalImage

Set the background image of the view with an original image.

## getOriginalImage

Get the current backgroud image.

## getDrawingLayer

Get the instance of the target `DrawingLayer`. The target `DrawingLayer` will be created if it does not exist.

```java
public DCEDrawingLayer getDrawingLayer(int id);
```

**Parameters**

`id`: The id of the `DrawingLayer`. It should be one of the following:

- `DEFAULT_LAYER_ID`
- `DDN_LAYER_ID`
- `DBR_LAYER_ID`
- `DLR_LAYER_ID`

**Return Value**

**Code Snippet**

## createDrawingLayer

Create a user defined `DrawingLayer` instance.

## getSelectedDrawingItem

## getDrawingStyle

## getAllDrawingStyles

## createDrawingStyle
