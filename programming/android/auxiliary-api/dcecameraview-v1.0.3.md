---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android CameraView Class
description: This is the documentation - Android CameraView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, CameraView
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraView Class
---

# CameraView

This page is for `CameraView` Class. `CameraView` is designed to Make basic settings on the overlay.

```Java
class com.dynamsoft.dce.CameraView
```

| Method Name | Description |
|------|------|
| [`addOverlay`](#addoverlay) | Add overlay |
| [`removeOverlay`](#removeoverlay) | Remove overlay |
| [`setBrushColor`](#setbrushcolor) | Set the brush color |

## addOverlay

Add overlay on located barcode.

```java
void addOverlay()
```

**Code Snippet**

Java:

```java
cameraView.addOverlay();
```

Kotlin:

```kotlin
cameraView!!.addOverlay()
```

## removeOverlay

Remove the overlay.

```java
void removeOverlay()
```

**Code Snippet**

Java:

```java
cameraView.removeOverlay();
```

Kotlin:

```kotlin
cameraView!!.removeOverlay()
```

## setBrushColor

```java
void setBrushColor(String color)
```

**Parameters**

`String`: A string value that refers to a color.

**Code Snippet**

Java:

```java
cameraView.setBrushColor("Put your color string here");
```

Kotlin:

```kotlin
cameraView!!.setBrushColor("Put your color string here")
```
