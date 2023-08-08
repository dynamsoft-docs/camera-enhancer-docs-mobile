---
layout: default-layout
title: Android DrawingItem Class - Dynamsoft Camera Enhancer Documents
description: This is the documentation - Android DrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DrawingItem Class
permalink: /programming/android/auxiliary-api/drawingitem-v3.0.3.html
---

# DrawingItem

`DrawingItem` is the class for users to draw graphic items on the UI view.

```java
class com.dynamsoft.dce.DrawingItem
```

| Method Name | Description |
| ----------- | ----------- |
| [`getDrawingStyleId`](#getdrawingstyleid) | Get the drawing style of the current drawing item. |
| [`setDrawingStyleId`](#setdrawingstyleid) | Set the drawing style of the current drawing item. |
| [`getState`](#getstate) | Get the state of the current drawing item. |
| [`setState`](#setstate) | Set the state of the current drawing item. |
| [`getMediaType`](#getmediatype) | Get the media type of the current drawing item. |

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

## getMediaType

Get the media type of the `DrawingItem`.

```java
public abstract EnumDrawingItemMediaType getMediaType();
```

**Return Value**

One of the `EnumDrawingItemMediaType` that indicates the media type of the `DrawingItem`.

**Code Snippet**

```java
EnumDrawingItemMediaType type = drawingItem.getMediaType();
```
