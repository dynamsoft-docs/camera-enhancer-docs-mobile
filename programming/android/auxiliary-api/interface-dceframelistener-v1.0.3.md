---
layout: default-layout
title: Dynamsoft Camera Enhancer - CameraListener
description: This is the documentation - CameraListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, CameraListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: CameraListener
---

# CameraListener

The interface to handle callback when previewed frame callback is returned.

```java
interface com.dynamsoft.dce.CameraListener
```

| Functions | Description |
| --------- | ----------- |
| [`onPreviewOriginalFrame`](#onprevieworiginalframe) | The callback function where you can add code to use the previewed **original** frames. |
| [`onPreviewFilterFrame`](#onpreviewfilterframe) | The callback function where you can add code to use the previewed **filtered** frames. |
| [`onPreviewFastFrame`](#onpreviewfastframe) | The callback function where you can add code to use the previewed **cropped** frames. |

## onPreviewOriginalFrame

Add your code to use the previewed `original frames`.

```java
void onPreviewOriginalFrame(Frame var1);
```

**Parameters**

`Original frames`: The data of original frame(s). The Camera Enhancer can make preprocessing on video frames. In this callback function, the input parameters are the original frames that are captured by the camera.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame frame) {
        // Add your code
    }
    @Override
    public void onPreviewFilterFrame(Frame frame) {}
    @Override
    public void onPreviewFastFrame(Frame frame) {}
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}frame.html)

## onPreviewFilterFrame

Add your code to use the previewed `filtered` frames.

```java
void onPreviewFilterFrame(Frame var1);
```

**Parameters**

`Filtered frames`: The data of filtered frame(s). The Camera Enhancer can make preprocessing on video frames. If the frame filter processing is enabled, the input parameter of this function will be the filtered frames.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame frame) {}
    @Override
    public void onPreviewFilterFrame(Frame frame) {
        // Add your code
    }
    @Override
    public void onPreviewFastFrame(Frame frame) {}
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}frame.html)  
- [`enableFrameFilter`]({{site.android-api}}preprocess.html#enableframefilter)

## onPreviewFastFrame

Add your code to use the previewed cropped frames.

```java
void onPreviewFastFrame(Frame var1);
```

**Parameters**

`Fast frames`: The data of cropped frame(s). The Camera Enhancer can make preprocessing on video frames. If the fast mode is enabled, the input parameter of this function will be the specially cropped frames.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame frame) {}
    @Override
    public void onPreviewFilterFrame(Frame frame) {}
    @Override
    public void onPreviewFastFrame(Frame frame) {
        // Add your code
    }
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}frame.html)
- [`enableFastMode`]({{site.android-api}}preprocess.html#enablefastmode)
