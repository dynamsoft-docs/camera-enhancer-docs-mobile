---
layout: default-layout
Title: TextDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSTextDrawingItem of Dynamsoft Camera Enhancer represents a text drawing item, which can be added to draw texts on the view.
Keywords: text drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSTextDrawingItem

The `DSTextDrawingItem` class is a subclass of `DSDrawingItem` and represents a text drawing item, which can be added to draw texts on the view.

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
