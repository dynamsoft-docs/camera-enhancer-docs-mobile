---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android TextDrawingItem Class
description: This is the documentation - Android TextDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, TextDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android TextDrawingItem Class
---

# TextDrawingItem

`TextDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `TextDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

```java
class TextDrawingItem extends DrawingItem
```

## TextDrawingItem

The constructor of `TextDrawingItem`. Create an instance of `TextDrawingItem`.

```java
public TextDrawingItem(String text, android.graphics.Rect textRect);
```

**Parameters**

`text`: The text of the `TextDrawingItem`.
`textRect`: The `Rect` that indicates the location of the `TextDrawingItem`.

**Code Snippet**

```java
DrawingItem drawingItem = new TextDrawingItem(Text);
```

## getMediaType

Get the media type of the `TextDrawingItem`.

```java
public EnumDrawingItemMeidaType getMediaType();
```

**Return Value**

The media type of the `TextDrawingItem`.

**Code Snippet**

```java
EnumDrawingItemMediaType mediaType = drawingItem.getMediaType();
```

## getText

Get the `Text` of the `TextDrawingItem`.

```java
public String getText();
```

**Return Value**

The text content of the `TextDrawingItem`.

**Code Snippet**

```java
String text = drawingItem.getText();
```

## getTextRect

Get the `Rect` of the `TextDrawingItem`. It indicates the location of the `TextDrawingItem`.

```java
public android.graphics.Rect getTextRect();
```

**Return Value**

The Rect of the `TextDrawingItem`.

**Code Snippet**

```java
android.graphics.Rect rect = drawingItem.getTextRect();
```
