---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DrawingItem Class
description: This is the documentation - Android DrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DrawingItem Class
---

# DrawingItem

| Method Name | Description |
| ----------- | ----------- |
| [`getDrawingStyle`](#getdrawingstyle) | Get the drawing style of the current drawing item. |
| [`setDrawingStyle`](#setdrawingstyle) | Set the drawing style of the current drawing item. |
| [`getState`](#getstate) | Get the state of the current drawing item. |
| [`setState`](#setstate) | Set the state of the current drawing item. |
| [`getCoordinateSystem`](#getcoordinatesystem) | Get the coordinate system of the current drawing item. |
| [`setCoordinateSystem`](#setcoordinatesystem) | Set the coordinate system of the current drawing item. |
| [`getMediaType`](#getmediatype) | Get the media type of the current drawing item. |

&nbsp;

## getDrawingStyle

```java
public int getDrawingStyleId();
```

**Return Value**

An int value that representing the style ID.

**Code Snippet**

```java
int styleId = drawingItem.getDrawingStyleId();
```

&nbsp;

## setDrawingStyle

```java
public void setDrawingStyleId(int style);
```

**Parameters**

`style`: An int value that representing the style ID.

**Code Snippet**

```java
drawingItem.setDrawingStyle(0);
```

&nbsp;

## getState

```java
public EnumDrawingItemState getState();
```

**Return Value**

The state of the drawing item. View all available drawing item states in [`EnumDrawingItemState`]().

**Code Snippet**

```java
EnumDrawingItemState state = drawingItem.getState();
```

&nbsp;

## setState

```java
public void setState(EnumDrawingItemState state);
```

**Parameters**

`state`: The state of the drawing item. View all available drawing item states in [`EnumDrawingItemState`]().

**Code Snippet**

```java
drawingItem.setState(EnumDrawingItemState.DIS_SELECTED)
```

&nbsp;

## getCoordinateSystem

```java
public EnumCoordinateSystem getCoordinateSystem();
```

**Return Value**

The coordinate system of the drawing item. It can be the image coordinate or the view coordinate.

**Code Snippet**

```java
EnumCoordinateSystem coordinateSystem = drawingItem.getCoordinateSystem();
```

&nbsp;

## setCoordinateSystem

```java
public void setCoordinateSystem(EnumCoordinateSystem coordinateSystem);
```

**Parameters**

`coordinateSystem`: the coordinate system of the drawing item. It can be the image coordinate or the view coordinate.

**Code Snippet**

```java
drawingItem.setCoordinateSystem(EnumCoordinateSystem.CS_IMAGE);
```

&nbsp;

## getMediaType

```java
public EnumDrawingItemMeidaType getMediaType();
```

**Return Value**

The media type of the drawing item.

**Code Snippet**

```java
EnumDrawingItemMeidaType mediaType = drawingItem.getMediaType();
```
