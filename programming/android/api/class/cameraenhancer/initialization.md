---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Initialization
description: This is the documentation - Android API references - Initialization page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Initialization
needAutoGenerateSidebar: true
breadcrumbText: Android Initialization
---

# Android API Reference - Initialization

## Initialize CameraEnhancer

Use the following code to initialize Dynamsoft Camera Enhancer.

```java
CameraEnhancer mCameraEnhancer;
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    mCameraEnhancer = new CameraEnhancer(MainActivity.this);
}
```

## CameraEnhancer Settings

For more APIs, please click the following links:

- [Basic camera settings]({{site.android-cameraenhancer}}basic-setting.html)
- [Filter settings]({{site.android-cameraenhancer}}filter.html)
- [Focus & zoom settings]({{site.android-cameraenhancer}}zoom-focus.html)
