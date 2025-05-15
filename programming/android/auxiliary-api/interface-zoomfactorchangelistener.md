---
layout: default-layout
title: ZoomFactorChangeListener - Dynamsoft Camera Enhancer Android Edition API Reference
description: The interface ZoomFactorChangeListener of DynamsoftCameraEnhancer defines the methods for monitoring the change of the zoom-factor.
keywords: photo listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ZoomFactorChangeListener

The `ZoomFactorChangeListener` interface defines the methods for monitoring the change of the zoom-factor.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface ZoomFactorChangeListener
```

## Methods

| Method | Description |
|------- |-------------|
| [`onZoomFactorChanged`](#onphotooutput) | The method for monitoring the change of the zoom-factor. |

### onZoomFactorChanged

The method for monitoring the change of the zoom-factor.

```java
void onZoomFactorChanged(float currentZoomFactor);
```

**Parameters**

`currentZoomFactor`: The current zoom-factor.
