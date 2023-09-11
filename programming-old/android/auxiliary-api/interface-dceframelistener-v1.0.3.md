---
layout: default-layout
title: Android CameraListener - Dynamsoft Camera Enhancer
description: This is the documentation - CameraListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, CameraListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: CameraListener
permalink: /programming/android/auxiliary-api/interface-dceframelistener-v1.0.3.html
---

# CameraListener

The interface to handle callback when previewed frame callback is returned.

```java
interface com.dynamsoft.dce.CameraListener
```

| Methods | Description |
| --------- | ----------- |
| [`onPreviewOriginalFrame`](#onprevieworiginalframe) | The callback function where you can add code to use the previewed **original** frames. |
| [`onPreviewFilterFrame`](#onpreviewfilterframe) | The callback function where you can add code to use the previewed **filtered** frames. |
| [`onPreviewFastFrame`](#onpreviewfastframe) | The callback function where you can add code to use the previewed **cropped** frames. |

&nbsp;

## onPreviewOriginalFrame

The callback function where you can add code to use the previewed **original** frames.

```java
void onPreviewOriginalFrame(Frame originalFrame);
```

**Parameters**

`originalFrame`: The data of original frame(s). The Camera Enhancer can make preprocessing on video frames. In this callback function, the input parameters are the original frames that are captured by the camera.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame originalFrame) {
        // Add your code
    }
    @Override
    public void onPreviewFilterFrame(Frame filteredFrame) {}
    @Override
    public void onPreviewFastFrame(Frame fastFrame) {}
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}dceframe.html)

&nbsp;


## onPreviewFilterFrame

The callback function where you can add code to use the previewed **filtered** frames.

```java
void onPreviewFilterFrame(Frame filteredFrame);
```

**Parameters**

`filteredFrame`: The data of filtered frame(s). The Camera Enhancer can make preprocessing on video frames. If the frame filter processing is enabled, the input parameter of this function will be the filtered frames.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame originalFrame) {}
    @Override
    public void onPreviewFilterFrame(Frame filteredFrame) {
        // Add your code
    }
    @Override
    public void onPreviewFastFrame(Frame fastFrame) {}
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}dceframe.html)  
- [`enableFrameFilter`]({{site.android-api}}preprocess.html#enableframefilter)

&nbsp;

## onPreviewFastFrame

The callback function where you can add code to use the previewed **cropped** frames.

```java
void onPreviewFastFrame(Frame fastFrame);
```

**Parameters**

`fastFrame`: The data of cropped frame(s). The Camera Enhancer can make preprocessing on video frames. If the fast mode is enabled, the input parameter of this function will be the specially cropped frames.

**Code Snippet**

```java
cameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame originalFrame) {}
    @Override
    public void onPreviewFilterFrame(Frame filteredFrame) {}
    @Override
    public void onPreviewFastFrame(Frame fastFrame) {
        // Add your code
    }
});
```

**See also**

- [`class Frame`]({{site.android-api-auxiliary}}dceframe.html)
- [`enableFastMode`]({{site.android-api}}preprocess.html#enablefastmode)
