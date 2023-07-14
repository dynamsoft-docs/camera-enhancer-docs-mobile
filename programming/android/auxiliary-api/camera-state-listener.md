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
2. 
```kotlin
interface CameraStateListener
```

## Methods

### onCameraStateChanged

The method for monitoring the camera state and receiving call.

```java
- (void)onCameraStateChanged:(DSCameraState)currentState;
```
2. 
```kotlin
func onCameraStateChanged(_ currentStateextends CameraState)
```

**Parameters**

`currentState`: The current camera state.

**Code Snippet**

```java
[listener onCameraStateChanged:currentState];
```
2. 
```kotlin
listener.onCameraStateChanged(currentState)
```
