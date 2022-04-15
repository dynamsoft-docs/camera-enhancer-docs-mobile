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

`DCEImageEditorView` is the class that enable users to add UI configurations on a static image.

| Method Name | Description |
| ----------- | ----------- |
| [`setOriginalImage`](#setoriginalimage) | Set the background image of the view with an original image. |
| [`getOriginalImage`](#getoriginalimage) | Get the current backgroud image. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the `DCEDrawingLayer` instance with the layer ID. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a user defined `DCEDrawingLayer` instance. |
| [`getSelectedDrawingItem`](#getselecteddrawingitem) | Get the selected drawing item. |
| [`getDrawingStyle`](#getdrawingstyle) | Get the `DrawingStyle` instance with the style ID. |
| [`getAllDrawingStyles`](#getalldrawingstyles) | Get all the available `DrawingStyle` in a list. |
| [`createDrawingStyle`](#createdrawingstyle) | Create a user defined `DrawingStyle` instance. |

&nbsp;

## setOriginalImage

Set the background image of the view with an original image.

```java
public void setOriginalImage(ImageData imageData);
```

**Parameters**

`imageData`: The `imageData` of the image.

**Code Snippet**

```java
mIEV = (DCEImageEditorView) findViewById(R.id.iev);
mImgData = getIntent().getIntExtra("imagedata");
mIEV.setOriginalImage(mImgData);
```

&nbsp;

## getOriginalImage

Get the current backgroud image.

```java
public ImageData getOriginalImage();
```

**Return Value**

The `imageData` of the image.

**Code Snippet**

```java
DCEDrawingLayer layer = imageEditorView.getDrawingLayer();
```

&nbsp;

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

An instance of `DCEDrawingLayer`.

**Code Snippet**

```java
DCEDrawingLayer drawingLayer = dceImageEditorView.getDrawingLayer(2);
```

&nbsp;

## createDrawingLayer

Create a user defined `DrawingLayer` instance.

```java
public DCEDrawingLayer createDrawingLayer();
```

**Return Value**

An instance of `DCEDrawingLayer`.

**Code Snippet**

```java
DCEDrawingLayer drawingLayer = dceImageEditorView.createDrawingLayer();
```

&nbsp;

## getSelectedDrawingItem

Get the user selected `DrawingItem`.

```java
public DrawingItem getSelectedDrawingItem();
```

**Return Value**

An instance of `DrawingItem`.

**Code Snippet**

```java
DrawingItem drawingItem = dceImageEditorView.getSelectedDrawingItem();
```

&nbsp;

## getDrawingStyle

Get the `DrawingStyle` instance with the style ID.

```java
public DrawingStyle getDrawingStyle(int styleId);
```

**Parameters**

`styleId`: The ID of the target `DrawingStyle`.

**Return Value**

An instance of `DrawingStyle`.

**Code Snippet**

```java
DrawingStyle style = dceImageEditorView.getDrawingStyle(0);
```

&nbsp;

## getAllDrawingStyles

Get all the available `DrawingStyle` in a list.

```java
public ArrayList<DrawingStyle> getAllDrawingStyles();
```

**Return Value**

An `ArrayList` that includes all the available `DrawingStyles`.

**Code Snippet**

```java
ArrayList<DrawingStyle> drawingStyles = dceImageEditorView.getAllDrawingStyles();
```

&nbsp;

## createDrawingStyle

Create a user defined `DrawingStyle` instance.

```java
public DrawingStyle createDrawingStyle(int strokeColour, int strokeWidth, int fillColour, int textColour, int fontSize, String fontFamily);
```

**Parameters**

`strokeColour`: The stroke colour.
`strokeWidth`: The width of the stroke (measured by px).
`fillColour`: The fill colour.
`textColour`: The text colour.
`fontSize`: The font size (measured by sp).
`fontFamily`: The font family.

**Code Snippet**

```java
DrawingStyle drawingStyle = dceImageEditorView.createDrawingStyle(0xff00ff00,2,0xff00ff00,0xff00ff00,12,"sans-serif")
```
