---
layout: default-layout
title: Android CameraView Class - Dynamsoft Camera Enhancer
description: This is the documentation - Android CameraView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, CameraView
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraView Class
permalink: /programming-old/android/auxiliary-api/dcecameraview-v1.0.3.html
---

# CameraView

This page is for `CameraView` Class. `CameraView` is designed to Make basic settings on the overlay.

```java
class com.dynamsoft.dce.CameraView
```

| Method Name | Description |
|------|------|
| [`addOverlay`](#addoverlay) | Add overlay |
| [`removeOverlay`](#removeoverlay) | Remove overlay |
| [`setBrushColor`](#setbrushcolor) | Set the brush color |

&nbsp;

## addOverlay

Add overlay on located barcode.

```java
void addOverlay()
```

**Code Snippet**

```java
cameraView.addOverlay();
```

&nbsp;

## removeOverlay

Remove the overlay.

```java
void removeOverlay()
```

**Code Snippet**

```java
cameraView.removeOverlay();
```

&nbsp;

## setBrushColor

```java
void setBrushColor(String color)
```

**Parameters**

`String`: A string value that refers to a color.

**Code Snippet**

```java
cameraView.setBrushColor("Put your color string here");
```
