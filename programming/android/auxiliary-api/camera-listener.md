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

The `CameraListener` includes three interface methods for you to add your code on the previewed original, filtered and cropped frames.

```java
interface CameraListener
```

| Functions | Type |
| --------- | ---- |
| [`onPreviewOriginalFrame`](#onprevieworiginalframe) | [`Frame`]({{site.android-api-auxiliary}}frame.html) |
| [`onPreviewFilterFrame`](#onpreviewfilterframe) | [`Frame`]({{site.android-api-auxiliary}}frame.html) |
| [`onPreviewFastFrame`](#onpreviewfastframe) | [`Frame`]({{site.android-api-auxiliary}}frame.html) |

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
