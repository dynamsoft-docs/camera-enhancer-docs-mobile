---
layout: default-layout
title: TextDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
description: The class TextDrawingItem of Dynamsoft Camera Enhancer represents a text drawing item, which can be added to draw texts on the view.
keywords: text drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# TextDrawingItem

The `TextDrawingItem` class is a subclass of `DrawingItem` and represents a text drawing item, which can be added to draw texts on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class TextDrawingItem extends DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`getText`](#gettext) | Get the text information of the `TextDrawingItem`. |
| [`getTopLeftPoint`](#gettopleftpoint) | Get the top-left point of the `TextDrawingItem`. |
| [`getWidth`](#getwidth) | Get the width of the `TextDrawingItem`. |
| [`getHeight`](#getheight) | Get the height of the `TextDrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`TextDrawingItem(text)`](#textdrawingitemtext) | Create an instance of `TextDrawingItem`. |
| [`TextDrawingItem(text,coordinateBase)`](#textdrawingitemtextcoordinatebase) | Create an instance of `TextDrawingItem`. |

## Interited Methods

The following methods are inherited from the superclass [`DrawingItem`](drawingitem.html).

| Method | Description |
|------- |-------------|
| [`setDrawingStyleId`](drawingitem.html#setdrawingstyleid) | Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer. |
| [`getDrawingStyleId`](drawingitem.html#getdrawingstyleid) | Get the DrawingStyle of the `DrawingItem`. |
| [`setState`](drawingitem.html#setstate) | Set the state of the `DrawingItem`. |
| [`getState`](drawingitem.html#getstate) | Get the state of the `DrawingItem`. |
| [`getCoordinateBase`](drawingitem.html#getcoordinatebase) | Get the coordinate base of the `DrawingItem`. The coordinate base is image by default. |
| [`getMediaType`](drawingitem.html#getmediatype) | Get the media type of the `DrawingItem`. |
| [`addNote`](drawingitem.html#addnote) | Add a note to the `DrawingItem`. |
| [`getNote`](drawingitem.html#getnote) | Get the specified `Note`. |
| [`hasNote`](drawingitem.html#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](drawingitem.html#updatenote) | Update the content of the specified `Note`. |
| [`deleteNote`](drawingitem.html#deletenote) | Remove the specified `Note` with the specified name. |
| [`getAllNotes`](drawingitem.html#getallnotes) | Get all `Notes` of this DrawingItem. |
| [`clearNotes`](drawingitem.html#clearnotes) | Remove all `Notes` of this DrawingItem. |

### getText

Get the text information of the `TextDrawingItem`.

```java
String getText(){}
```

### getTopLeftPoint

Get the top-left point of the `TextDrawingItem`.

```java
Point getTopLeftPoint(){}
```

### getWidth

Get the width of the `TextDrawingItem`.

```java
int getWidth(){}
```

### getHeight

Get the height of the `TextDrawingItem`.

```java
int getHeight(){}
```

### getMediaType

Get the media type of the `DrawingItem`.

```java
EnumDrawingItemMeidaType getMediaType;
```

### TextDrawingItem(text)

Create an instance of `TextDrawingItem`.

```java
TextDrawingItem(String text, Point topLeftPoint, int width, int height){}
```

**Parameters**

`text`: A string that stores the text coordinates information.  
`topLeftPoint`: The top-left point of the `TextDrawingItem`.  
`width`: The width of the `TextDrawingItem`.  
`height`: The height of the `TextDrawingItem`.  

**Return Value**

An instance of `TextDrawingItem`.

## TextDrawingItem(text,coordinateBase)

Create an instance of `TextDrawingItem`.

```java
TextDrawingItem(String text, Point topLeftPoint, int width, int height, EnumCoordinateBase coordinateBase){}
```

**Parameters**

`text`: A string that stores the text coordinates information.  
`topLeftPoint`: The top-left point of the `TextDrawingItem`.  
`width`: The width of the `TextDrawingItem`.  
`height`: The height of the `TextDrawingItem`.  
`coordinateBase`: The coordinate base of the `DrawingItem`.

**Return Value**

An instance of `TextDrawingItem`.
