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
| [`onPreviewOriginalFrame`](#onprevieworiginalframe) | The function for user to add code on the previewed original frames. |
| [`onPreviewFilterFrame`](#onpreviewfilterframe) |  The function for user to add code on the previewed filtered frames. |
| [`onPreviewFastFrame`](#onpreviewfastframe) |  The function for user to add code on the previewed cropped frames. |

## onPreviewOriginalFrame

Add your code on the previewed original frames.

```java
void onPreviewOriginalFrame(Frame var1);
```

**Parameters**

[`Frame`]({{site.android-api-auxiliary}}frame.html): The original frame(s).

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

## onPreviewFilterFrame

Add your code on the previewed filtered frames.

```java
void onPreviewFilterFrame(Frame var1);
```

**Parameters**

[`Frame`]({{site.android-api-auxiliary}}frame.html): The filtered frame(s).

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

## onPreviewFastFrame

Add your code on the previewed cropped frames.

```java
void onPreviewFastFrame(Frame var1);
```

**Parameters**

[`Frame`]({{site.android-api-auxiliary}}frame.html): The filtered and cropped frame(s).

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
