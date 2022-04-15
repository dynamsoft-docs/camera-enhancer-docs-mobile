---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DCEDrawingLayer Class
description: This is the documentation - Android DCEDrawingLayer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DCEDrawingLayer
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DCEDrawingLayer Class
---

# DCEDrawingLayer

```java
class com.dynamsoft.dce.DCEDrawingLayer
```

| Method Name | Description |
| ----------- | ----------- |
| [`getId`](#getid) | Get the layer ID of the layer. |
| [`addDrawingItems`](#adddrawingitems) | Add a list of drawing items to the layer. These drawing items will be appended to the drawing item list of the current layer. |
| [`setDrawingItems`](#setdrawingitems) | Set a list of drawing items to the layer. These drawing items will replace the previous drawing items of the current layer. |
| [`getDrawingItems`](#getdrawingitems) | Get all available drawing items in the layer. |
| [`clearDrawingItems`](#cleardrawingitems) | Clear all available drawing items in the layer. |
| [`setDrawingStyle`](#setdrawingstyle) |  |
| [`getDrawingStyle`] |  |
| [`setVisible`](#setvisible) | Set the visibility of the layer. |
| [`isVisible`](#isvisible) | Get the visibility of the layer. |

&nbsp;

## getId

Get the layer ID of the layer.

```java
public int getId();
```

**Return Value**

The id of the `DrawingLayer`. It can be one of the following:

- `DEFAULT_LAYER_ID`
- `DDN_LAYER_ID`
- `DBR_LAYER_ID`
- `DLR_LAYER_ID`

**Code Snippet**

```java
DCEDrawingLayer drawingLayer = dceImageEditorView.createDrawingLayer();
int id = drawingLayer.getId();
```

&nbsp;

## addDrawingItems

Add a list of drawing items to the layer. These drawing items will be appended to the drawing item list of the current layer.

```java
public void addDrawingItems(Arraylist<DrawingItem> items); 
```

**Parameters**

`items`: A list of drawing items.

**Code Snippet**

```java
ArrayList<DrawingItem> drawingItems = new ArrayList<DrawingItem>();
drawingItems.add(drawingItem_1);
drawingItems.add(drawingItem_2);
drawingItems.add(drawingItem_3);
drawingLayer.addDrawingItems(drawingItems);
```

&nbsp;

## setDrawingItems

Set a list of drawing items to the layer. These drawing items will replace the previous drawing items of the current layer.

```java
public void setDrawingItems(Arraylist<DrawingItem> items); 
```

**Parameters**

`items`: A list of drawing items.

**Code Snippet**

```java
ArrayList<DrawingItem> drawingItems = new ArrayList<DrawingItem>();
drawingItems.add(drawingItem_1);
drawingItems.add(drawingItem_2);
drawingItems.add(drawingItem_3);
drawingLayer.setDrawingItems(drawingItems);
```

&nbsp;

## getDrawingItems

Get all available drawing items in the layer.

```java
public Arraylist<DrawingItem> getDrawingItems();
```

**Return Value**

A list that includes all available drawing items.

**Code Snippet**

```java
ArrayList<DrawingItem> drawingItems = dceDrawingLayer.getDrawingItems();
```

&nbsp;

## clearDrawingItems

Clear all available drawing items in the layer.

```java
public void clearDrawingItems();
```

**Code Snippet**

```java
drawingLayer.clearDrawingItems();
```

&nbsp;

## setDrawingStyle

&nbsp;

## getDrawingStyle

&nbsp;

## setVisible

Set the visibility of the layer.

```java
public void setVisible(boolean visible);
```

**Parameters**

`visible`:

- true: The layer will be visible
- false: The layer will be invisible.

**Code Snippet**

```java
drawingLayer.setVisible(true);
```

&nbsp;

## isVisible

Get the visibility of the layer.

```java
public boolean isVisible();
```

**Return Value**

- true: The layer is visible.
- false: The layer is invisible.

**Code Snippet**

```java
boolean visible = drawingLayer.isVisible();
```
