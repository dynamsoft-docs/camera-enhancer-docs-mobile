---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - CameraEnhancer Class
description: This is the documentation - Android API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, CameraEnhancer Class
needAutoGenerateSidebar: true
breadcrumbText: Android CameraEnhancer Class
---

# CameraEnhancer

## CameraEnhancer Initialization

```java
CameraEnhancer mCameraEnhancer;
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    mCameraEnhancer = new CameraEnhancer(MainActivity.this);
}
```

## CameraEnhancer Settings

- [Basic camera settings]({{site.android-cameraenhancer}}basic-setting.html)
- [Filter settings]({{site.android-cameraenhancer}}filter.html)
- [Focus & zoom settings]({{site.android-cameraenhancer}}zoom-focus.html)
