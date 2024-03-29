---
layout: default-layout
title: Android RectDrawingItem Class - Dynamsoft Camera Enhancer Documents
description: This is the documentation - Android RectDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, RectDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android RectDrawingItem Class
permalink: /programming/android/auxiliary-api/drawingitem-rect-v3.0.3.html
---

# RectDrawingItem Class

`RectDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `RectDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

```java
class com.dynamsoft.dce.RectDrawingItem extends DrawingItem
```

| Method | Descriptions |
| ------ | ------------ |
| [`RectDrawingItem`](#rectdrawingitem) | The constructor of `RectDrawingItem`. Create an instance of `RectDrawingItem`. |
| [`getMediaType`](#getmediatype) | Get the media type of the `RectDrawingItem`. |
| [`getRect`](#getrect) | Get the `Rect` of the `RectDrawingItem`. |
| [`getDrawingStyleId`](#getdrawingstyleid) | Get the drawing style of the current drawing item. |
| [`setDrawingStyleId`](#setdrawingstyleid) | Set the drawing style of the current drawing item. |
| [`getState`](#getstate) | Get the state of the current drawing item. |
| [`setState`](#setstate) | Set the state of the current drawing item. |

&nbsp;

## RectDrawingItem

The constructor of `RectDrawingItem`. Create an instance of `RectDrawingItem`.

```java
public RectDrawingItem(android.graphics.Rect rect);
```

**Parameters**

`rect`: The `Rect` that indicates the location of the `RectDrawingItem`.

**Code Snippet**

```java
DrawingItem drawingItem = new RectDrawingItem(rect);
```

&nbsp;

## getMediaType

Get the media type of the `RectDrawingItem`.

```java
public EnumDrawingItemMeidaType getMediaType();
```

**Return Value**

The media type of the `RectDrawingItem`.

**Code Snippet**

```java
EnumDrawingItemMediaType mediaType = drawingItem.getMediaType();
```

&nbsp;

## getRect

Get the `Rect` of the `RectDrawingItem`.

```java
public android.graphics.Rect getRect();
```

**Return Value**

The `Rect` that indicates the location of the `RectDrawingItem`.

**Code Snippet**

```java
android.graphics.Rect rect = drawingItem.getRect();
```

&nbsp;

## getDrawingStyleId

Get the ID of the `DrawingStyle` that is applied on this `DrawingItem`.

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

## setDrawingStyleId

Set a `DrawingStyle` by ID for the `DrawingItem`.

```java
public void setDrawingStyleId(int style);
```

**Parameters**

`style`: An int value that representing the style ID.

**Code Snippet**

```java
drawingItem.setDrawingStyleId(0);
```

&nbsp;

## getState

Get the status of the `DrawingItem`.

```java
public EnumDrawingItemState getState();
```

**Return Value**

The value that indicates the state of the `DrawingItem`. View all available `DrawingItem` states in [`EnumDrawingItemState`]({{ site.android_camera_enhancer }}enum-drawing-item-state.html).

**Code Snippet**

```java
EnumDrawingItemState state = drawingItem.getState();
```

&nbsp;

## setState

Set the status of the `DrawingItem`.

```java
public void setState(EnumDrawingItemState state);
```

**Parameters**

`state`: The value that indicates the state of the `DrawingItem`. View all available `DrawingItem` states in [`EnumDrawingItemState`]({{ site.android_camera_enhancer }}enum-drawing-item-state.html).

**Code Snippet**

```java
drawingItem.setState(EnumDrawingItemState.DIS_SELECTED)
```

&nbsp;
