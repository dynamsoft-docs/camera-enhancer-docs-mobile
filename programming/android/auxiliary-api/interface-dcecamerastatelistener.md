---
layout: default-layout
title: CameraStateListener - Dynamsoft Core Module Android Edition API Reference
description: The protocol that includes methods for monitoring the camera state.
keywords: camera state, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraStateListener

The `CameraStateListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface CameraStateListener
```

## Methods

### onCameraStateChanged

The method for monitoring the camera state and receiving call.

```java
void onCameraStateChanged(EnumCameraState state);
```

**Parameters**

`currentState`: The current camera state.
