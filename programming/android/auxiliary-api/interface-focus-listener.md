---
layout: default-layout
title: FocusListener - Dynamsoft Camera Enhancer Android Edition API Reference
description: The interface that includes methods for monitoring the focus status.
keywords: Focus listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# FocusListener

The `FocusListener` interface includes methods for monitoring the focus status and receiving focus completion events.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
interface FocusListener
```

## Methods

### onFocusFinished

The method for receiving notifications when a focus operation is completed.

```java
void onFocusFinished(PointF focusPoint);
```

**Parameters**

`focusPoint`: A `PointF` object that represents the coordinates of the focus point.

**Remarks**

This callback is triggered under the following conditions:

- Always triggered when calling `setFocus(Point, FocusModeLocked)`
- Might be triggered when performing tap-to-focus
- Never triggered when calling `setFocus(Point, FocusModeContinuousAuto)`
