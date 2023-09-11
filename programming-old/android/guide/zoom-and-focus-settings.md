---
layout: default-layout
title: Configure Zoom & Focus Settings - Exploring Features of Dynamsoft Camera Enhancer Android Edition.
description: This page introduce how to configure zoom & focus settings with Dynamsoft Camera Enhancer Android Edition.
keywords:  Camera Enhancer, Zoom, Focus
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: Zoom & Focus
permalink: /programming/android/guide/zoom-and-focus-settings.html
---

# How to Config Zoom & Focus Settings with DynamsoftCameraEnhancer

## Zoom

### Set Zoom Factor

### Auto Zoom

## Focus

- Auto Focus: Trigger a focus with an interest point. Your device will calculate the focal length autometically.
- Continuous Auto Focus: Trigger an "auto-focus". After that, enable the device to trigger the "auto-focus" continuously.
- Tap to Focus: Tap the screen to trigger an "auto-focus". This feature is enabled by default.
- Enhanced Focus: Continuous "auto-focus" that controlled by DCE algorithm.
- Set Focal Length: Directly set the focal length. Much faster than the "auto-focus".

### Trigger an "Auto-Focus"

`setFocus` is a method for you to trigger an auto-focus at a point of interest.

To trigger a one-off "auto-focus", you have to set the focus mode to locked after the focus.

```java
mCameraEnhancer.setFocus(new PointF(0.5f,0.5f), EnumFocusMode.FM_LOCKED);
```

Also, you can trigger a auto-focus and keep the "continuous auto focus" enabled:

```java
mCameraEnhancer.setFocus(new PointF(0.5f,0.5f), EnumFocusMode.FM_CONTINUOUS_AUTO);
```

### Enable Enhanced Focus

```java
```

> Note: A valid license is required to enable the enhanced focus feature.

### Set the Focal Length
