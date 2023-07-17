---
layout: default-layout
Title: CameraStateListener - Dynamsoft Core Module Android Edition API Reference
Description: The protocol that includes methods for monitoring the camera state.
Keywords: camera state, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraStateListener

The `DSCameraStateListener` protocol includes methods for monitoring the camera state.

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
