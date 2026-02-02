---
layout: default-layout
title: DrawingLayer - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class DrawingLayer of Dynamsoft Camera Enhancer represents a drawing layer, which is used for managing and controlling drawing items.
keywords: drawing layer, Dynamsoft Camera Enhancer, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DrawingLayer

The `DrawingLayer` class represents a drawing layer, which is used for managing and controlling drawing items.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
class DrawingLayer
```

## Constants

| Constants | Description |
| --------- | ----------- |
| `DDN_LAYER_ID` | The preset DrawingLayer of Dynamsoft Document Normalizer. |
| `DBR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Barcode Reader. |
| `DLR_LAYER_ID` | The preset DrawingLayer of Dynamsoft Label Recognizer. |
| `USER_REFINED_LAYER_BASE_ID` | The IDs of user defined Drawinglayers start from 100. |

## Methods

| Method | Description |
|------- |-------------|
| [`DrawingLayer`](#drawinglayer) | Create an DrawingLayer with the specified ID. |
| [`getId`](#getid) | Get the layer ID of the layer. |
| [`setVisible`](#setvisible) | Set/get the visibility of the layer. |
| [`isVisible`](#isvisible) | Set/get the visibility of the layer. |
| [`addDrawingItems`](#adddrawingitems) | Add a group of DrawingItem to the layer. |
| [`setDrawingItems`](#setdrawingitems) | Set the DrawingItems to be displayed on the layer. |
| [`getDrawingItems`](#getdrawingitems) | Get all the DrawingItems on the layer. |
| [`setDefaultStyle(style)`](#setdefaultstylestyle) | Set the default style of the layer. |
| [`setDefaultStyle(style,state,mediaType)`](#setdefaultstylestylestatemediatype) | Set the default style of the layer with filter options. |
| [`clearDrawingItems`](#cleardrawingitems) | Remove all DrawingItems from the layer. |

### DrawingLayer

Create an DrawingLayer with the specified ID.

```java
DrawingLayer(int id){}
```

### getId

Get the layer ID of the layer.

```java
int getId(){}
```

### setVisible

Set the visibility of the layer.

```java
void setVisible(boolean visible){}
```

**Parameters**

A boolean value that indicates the visibility of the layer.

### isVisible

Get the visibility of the layer.

```java
boolean isVisible(){}
```

**Return Value**

A boolean value that indicates the visibility of the layer.

### addDrawingItems

Add a group of `DrawingItem` to the layer.

```java
void addDrawingItems(Arraylist<DrawingItem> items){} 
```

**Parameters**

`items`: An array of `DrawingItems` to be added to the layer.

### setDrawingItems

Set the `DrawingItems` to be displayed on the layer. The previously displayed DrawingItems are removed.

```java
void setDrawingItems(Arraylist<DrawingItem> items){}
```

**Parameters**

`items`: An array of `DrawingItems` to be set on the layer.

### getDrawingItems

Get all the `DrawingItems` on the layer.

```java
Arraylist<DrawingItem> getDrawingItems(){}
```

**Return Value**

An array of `DrawingItems`

### setDefaultStyle(style)

Set the default style of the layer. A `DrawingItem` on the layer will use the default style if it doesn't hold a style attribute.

```java
void setDefaultStyle(int styleId){}
```

**Parameters**

`styleId`: An ID of DrawingStyle.

### setDefaultStyle(style,state,mediaType)

Set the default style of the layer with filter options. A `DrawingItem` on the layer will use the default style if it doesn't hold a style attribute.

```java
void setDefaultStyle(int styleId, int state, int mediaTypes){}
```

**Parameters**

`drawingStyle`: An ID of DrawingStyle.  
`drawingItemState`: Specify a group of DrawingItem state. It filters which kinds of DrawingItems will use this default style.  
`drawingItemMediaType`: Specify a group of DrawingItem media type. It filters which kinds of DrawingItems will use this default style.

### clearDrawingItems

Remove all DrawingItems from the layer.

```java
void clearDrawingItems(){}
```
