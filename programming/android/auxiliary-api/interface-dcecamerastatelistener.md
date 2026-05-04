---
layout: default-layout
title: CameraStateListener - Dynamsoft Camera Enhancer Android Edition API Reference
description: "Understand the Dcecamerastatelistener interface in Dynamsoft Camera Enhancer Android API and learn how it supports capture, camera, or result workflows."
keywords: camera state, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraStateListener

The `CameraStateListener` interface includes methods for monitoring the camera state.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

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
