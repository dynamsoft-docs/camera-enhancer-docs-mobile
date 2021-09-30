---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DCECameraView Class
description: This is the documentation - Android DCECameraView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DCECameraView
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DCECameraView Class
---

# DCECameraView

This page is for `DCECameraView` Class. `DCECameraView` is designed to Make basic settings on the overlay.

```Java
class com.dynamsoft.dce.DCECameraView
```

| Method Name | Description |
|------|------|
| [`setOverlayVisible`](#setOverlayVisible) | Display coloured and translucent overly on the interest areas. |
| [`getOverlayVisible`](#getOverlayVisible) | Get the visibility of the overlay. |
| [`setOverlayPosition`](#setOverlayPosition) | Set the position of the overlay. |
| [`setOverlayColour`](#setOverlayColour) | Set the colour of the overlay. |
| [`setViewfinderVisible`](#setViewfinderVisible) | Display a viewfinder on the UI. |
| [`getViewfinderVisible`](#getViewfinderVisible) | Get the visibility of the viewfinder. |
| [`setViewfinder`](#setViewfinder) | Set the attribute of the viewfinder. Currently only available for position and size setting. |

## setOverlayVisible

This method is controlling whether to display coloured and translucent overly on the interest areas.

```java
void setOverlayVisible(boolean isVisibile)
```

**Parameters**

`isVisibile`: If true, the camera enhancer will be able to draw and display overlays on the cameraView accroding to the position and colour settings. If false, the camera enhancer will never draw overlays evenif position and colour are set.

**Code Snippet**

```java
DCECameraView.setOverlayVisible(true);
```

## getOverlayVisible

Get the visibility (true/false) of overlays.

**Return Value**

`isVisible`: If true, the camera enhancer will be able to draw and display overlays on the cameraView accroding to the position and colour settings. If false, the camera enhancer will never draw overlays evenif position and colour are set.

**Code Snippet**

```java
Boolean isVisible = DCECameraView.getOverlayVisible()
```

## setOverlayPosition

## setOverlayColour

## setViewfinderVisible

## getViewfinderVisible

## setViewfinder
