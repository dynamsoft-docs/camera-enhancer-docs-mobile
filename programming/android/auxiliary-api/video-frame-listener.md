---
layout: default-layout
Title: VideoFrameListener - Dynamsoft Camera Enhancer Module Android Edition API Reference
Description: The protocol that defines methos for monitoring the video frame output.
Keywords: Video frame listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSVideoFrameListener

The `DSVideoFrameListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface VideoFrameListener
```
2. 
```kotlin
protocol VideoFrameListenerProtocol
```

## Methods

### onFrameOutPut

The method for monitoring the camera state and receiving call.

```java
- (void)onFrameOutPut:(DSImageData*)frame
            timeStamp:(NSTimeInterval)timeStamp;
```
2. 
```kotlin
func onFrameOutPut(_ frameextends ImageData, timeStamp: NSTimeInterval)
```

**Parameters**

`frame`: The output video frame.  
`timeStamp`: The time stamp that the video frame is output.
