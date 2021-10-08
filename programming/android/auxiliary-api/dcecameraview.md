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

This method controls whether to display coloured and translucent overly on the interest areas.

```java
void setOverlayVisible(boolean overlayVisibile)
```

**Parameters**

`overlayVisibile`: If true, the camera enhancer will be able to draw and display overlays on the `DCECameraView` according to the position and colour settings. If false, the camera enhancer will never draw overlays even if position and colour are set.

**Code Snippet**

```java
DCECameraView.setOverlayVisible(true);
```

## getOverlayVisible

Get the visibility (true: visible/ false: invisible) of overlays.

```java
boolean getOverlayVisible()
```

**Return Value**

If the return value is true, the camera enhancer will be able to draw and display overlays on the `DCECameraView` according to the position and colour settings. Otherwise, the camera enhancer will never draw overlays even if position and colour are set.

**Code Snippet**

```java
Boolean isVisible = DCECameraView.getOverlayVisible();
```

## setOverlayPosition

Set the position of the interest area so that the camera enhancer can draw overlay(s) on the interest area.

```java
void setOverlayPosition(ArrayList<Quadrilateral> overlayPosition)
```

**Parameters**

`overlayPosition`: The position that you want to draw the overlay.

**Code Snippet**

```java
ArrayList<Quadrilateral> overlayPosition = new ArrayList<>();
Point[] points = new Point[4];
points[0].x = 800;
points[0].y = 600;
points[1].x = 800;
points[1].y = 250;
points[2].x = 850;
points[2].y = 250;
points[3].x = 850;
points[3].y = 600;
Quadrilateral quadrilateral_0 = new Quadrilateral();
quadrilateral_0.points = points;
overlayPosition.add(quadrilateral_0);
DCECameraView.setOverlayPosition(overlayPosition);
```

**Remarks**

The method `setOverlayPosition` applies the same coordinate system with the class `DCEFrame`. The origin of the coordinate is the left-top point of the image and the unit of the horizontal and vertical positions is the pixel length.

## setOverlayColour

Set the stroke and fill in colour of the overlay(s).

```java
void setOverlayColour(int strokeARGB, int fillARGB)
```

**Parameters**

`strokeARGB`: The colour code of the overlay stroke.
`fillARGB`: The colour code of the overlay stroke.

**Code Snippet**

```java
DCECameraView.setOverlayColour(0xff00ff00, 0x00000000);
```

## setViewfinderVisible

This method controls whether to display a viewfinder on the `DCECameraView`.

```java
void setViewfinderVisible(boolean viewfinderVisible)
```

**Parameters**

`viewfinderVisible`: A boolean value that means whether the viewfinder is visible. If the input value is true, the camera enhancer will try to create a viewfinder on the `DCECameraView`. Users can define the position and size of the viewfinder via method [`setViewfinder`](#setviewfinder). The viewfinder will be created based on the default value if the `setViewfinder` has never been triggered.

**Code Snippet**

```java
DCECameraView.setViewfinderVisible(true);
```

## getViewfinderVisible

Get the visibility (true: visible/ false: invisible) of the viewfinder.

**Return Value**

A boolean value that means whether the viewfinder is visible.

## setViewfinder

Set the position and the size of the viewfinder.

```java
void setViewfinder(float left, float top, float right, float bottom) throws CameraEnhancerException
```

**Parameters**

`left`: The distance (by percentage) between the left border of the viewfinder and the left side of the screen. The default value is 0.15.  
`top`: The distance (by percentage) between the top border of the viewfinder and the top side of the screen. The default value is 0.3.  
`right`: The distance (by percentage) between the right border of the viewfinder and the left side of the screen. The default value is 0.85.  
`bottom`: The distance (by percentage) between the bottom border of the viewfinder and the top side of the screen. The default value is 0.7.

**Code Snippet**

```java
DCECameraView.setViewfinder(0.2, 0.3, 0.8, 0.7);
```

**Remarks**

The viewfinder is built based on the screen coordinate system. The origin of the coordinate is the left-top point of the mobile device. The `left border` of the viewfinder always means the closest border that parallels to the left side of the mobile device no matter how the mobile device is rotated.
