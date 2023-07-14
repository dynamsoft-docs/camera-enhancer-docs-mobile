---
layout: default-layout
Title: DrawingStyleManager - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSDrawingStyleManager of Dynamsoft Camera Enhancer provides methods to manage drawing styles.
Keywords: drawing style, manager, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingStyleManager

The `DSDrawingStyleManager` class is the manager of DrawingStyles in Dynamsoft Camera Enhancer.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class DrawingStyleManager
```

## Methods

| Method | Description |
|------- |-------------|
| [`getDrawingStyle`](#getdrawingstyle) | Get the specified DrawingStyle. |
| [`createDrawingStyle`](#createdrawingstyle) | Create an instance of the DrawingStyle and get the style ID. |
| [`getAllDrawingStyles`](#getalldrawingstyles) | Get all available DrawingStyles. |

### getDrawingStyle

Get the specified DrawingStyle.

```java
static DrawingStyle getDrawingStyle(int styleId){}
```

**Parameters**

`styleId`: Specify a style ID.

**Return Value**

The DrawingStyle with the specified ID.

### createDrawingStyle

Create an instance of the DrawingStyle and get the style ID.

```java
static int createDrawingStyle(int strokeColor, float strokeWidth, int fillColor, int textColor){}
```

**Parameters**

`strokeColor`: Set the stroke colour.  
`strokeWidth`: Set the stroke width.  
`fillColor`: Set the fill colour.  
`textColor`: Set the text colour.  

**Return Value**

The style ID of the created DrawingStyle.

### getAllDrawingStyles

Get all available DrawingStyles.

```java
static DrawingStyle[] getAllDrawingStyles(){}
```

**Return Value**

An array that contains all available DrawingStyles.
