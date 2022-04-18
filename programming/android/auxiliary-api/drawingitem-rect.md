---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android RectDrawingItem Class
description: This is the documentation - Android RectDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, RectDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android RectDrawingItem Class
---

# RectDrawingItem

`RectDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `RectDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

```java
class RectDrawingItem extends DrawingItem
```

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
