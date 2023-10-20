---
layout: default-layout
title: VideoFrameListener - Dynamsoft Camera Enhancer Module Android Edition API Reference
description: The protocol that defines methos for monitoring the video frame output.
keywords: Video frame listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# VideoFrameListener

The `VideoFrameListener` protocol includes methods for monitoring the camera state.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface VideoFrameListener
```

## Methods

### onFrameOutPut

The method for monitoring the camera state and receiving call.

```java
void onFrameOutput(ImageData frame, long timeStamp);
```

**Parameters**

`frame`: The output video frame in an [`ImageData`]({{ site.dcv_android_api }}core/basic-structures/image-data.html) object.  
`timeStamp`: The time stamp that the video frame is output.
