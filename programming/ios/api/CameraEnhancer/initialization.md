---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS API references - CameraEnhancer Class
description: This is the documentation - iOS API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS API references, CameraEnhancer Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS CameraEnhancer Class
---

# CameraEnhancer Class

`CameraEnhancer` is the class that provides multifunctional APIs on frame preprocessing and camera controlling.

## CameraEnhancer Methods

### [Frame preprocessing methods]({{site.ios-cameraenhancer}}preprocess.html)

| Method | Description |
|-----------------|---------------|
| [`enableFastMode`]({{site.ios-cameraenhancer}}preprocess.html#enablefastmode) | Set the value true/false to turn on/off DCE fast mode |
| [`acquireListFrame`]({{site.ios-cameraenhancer}}preprocess.html#acquirelistframe) | Get the latest frame from the frame queue when this API is activated. |
| [`enableSensorControl`]({{site.ios-cameraenhancer}}preprocess.html#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
|[`setSensorControlThreshold`]({{site.ios-cameraenhancer}}preprocess.html#setsensorcontrolthreshold)| Make settings on sensor control threshold |
| [`enableFrameFilter`]({{site.ios-cameraenhancer}}preprocess.html#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`setMaxFrameRate`]({{site.ios-cameraenhancer}}preprocess.html#setmaxframerate) | Set max frame rate |

### [Regular camera methods]({{site.ios-cameraenhancer}}camera.html)

| Method | Description |
|-----------------|---------------|
| [`updateCameraSettingFromJson`]({{site.ios-cameraenhancer}}camera.html#updatecamerasettingfromjson) | Update camera filter and focus settings from Json |
| [`updateCameraSettingFromFile`]({{site.ios-cameraenhancer}}camera.html#updatecamerasettingfromfile) | Update camera filter and focus settings from file |
| [`getVersion`]({{site.ios-cameraenhancer}}camera.html#getversion) | Check current DCE version |
| [`setCameraDesiredState`]({{site.ios-cameraenhancer}}camera.html#camera-state) | Set Camera on/off |
| [`getCameraDesiredState`]({{site.ios-cameraenhancer}}camera.html#camera-state) | Get camera desired state |
| [`getCameraCurrentState`]({{site.ios-cameraenhancer}}camera.html#camera-state) | Get camera current state |
| [`pauseCamera`]({{site.ios-cameraenhancer}}camera.html#pausecamera-and-resumecamera) | Pause Camera |
| [`resumeCamera`]({{site.ios-cameraenhancer}}camera.html#pausecamera-and-resumecamera) | Resume Camera |
| [`startScanning`]({{site.ios-cameraenhancer}}camera.html#stopscanning-and-startscanning) | Start scanning |
| [`stopScanning`]({{site.ios-cameraenhancer}}camera.html#stopscanning-and-startscanning) | Stop scanning |
| [`addCameraListener`]({{site.ios-cameraenhancer}}camera.html#addcameralistener) | Add camera listener (on preview original, filtered or fast frames) |
| [`removeCameraListener`]({{site.ios-cameraenhancer}}camera.html#addcameralistener) | Remove camera listener |
| [`setTorchDesiredState`]({{site.ios-cameraenhancer}}camera.html#torch-state) | Set torch state |
| [`getTorchDesiredState`]({{site.ios-cameraenhancer}}camera.html#torch-state) | Get torch desired state |
| [`getTorchCurrentState`]({{site.ios-cameraenhancer}}camera.html#torch-state) | Get torch current state |
| [`addTorchListener`]({{site.ios-cameraenhancer}}camera.html#addtorchlistener) | Add torch listener |
| [`removeTorchListener`]({{site.ios-cameraenhancer}}camera.html#addtorchlistener) | Remove Torch Listener |
| [`getCameraPosition`]({{site.ios-cameraenhancer}}camera.html#camera-position) | Get current camera position |
| [`switchCameraPosition`]({{site.ios-cameraenhancer}}camera.html#camera-position) | Switch camera position front/back |
| [`setResolution`]({{site.ios-cameraenhancer}}camera.html#resolution-settings) | Set resolution |
| [`getResolution`]({{site.ios-cameraenhancer}}camera.html#resolution-settings) | Get current resolution setting |
| [`getResolutionList`]({{site.ios-cameraenhancer}}camera.html#resolution-settings) | Get all available resolutions |

### [Focus & zoom methods]({{site.ios-cameraenhancer}}zoom-focus.html)

| Method | Description |
|-----------------|---------------|
| [`setAutoFocusPosition`]({{site.ios-cameraenhancer}}zoom-focus.html#setautofocusposition) | Set auto focus position (Change the default auto focus position). |
| [`setManualFocusPosition`]({{site.ios-cameraenhancer}}zoom-focus.html#setmanualfocusposition) | Set manual focus position (This focus position only takes effect once for each time the API is called). |
| [`setFocalLength`]({{site.ios-cameraenhancer}}zoom-focus.html#setfocallength) | Set focal length between 0 to 10 to enable fixed focal length mode. In fixed focal length mode, all focus parameters can't be changed until this mode is quit. To quit fixed focal length mode, please set focal length equals to -1. |
| [`enableDefaultAutoFocus`]({{site.ios-cameraenhancer}}zoom-focus.html#enabledefaultautofocus) | Set true/false to turn on/off default auto focus. |
| [`enableRegularAutoFocus`]({{site.ios-cameraenhancer}}zoom-focus.html#enableregularautofocus) | If this is true, camera will auto focus for every 3 seconds. |
| [`setRegularAutoFocusParam`]({{site.ios-cameraenhancer}}zoom-focus.html#setregularautofocusparam) | Set the focus interval and termination time for the regular autofocus. |
| [`enableAutoFocusOnSharpnessChange`]({{site.ios-cameraenhancer}}zoom-focus.html#enableautofocusonsharpnesschange) | If this is enabled, camera will autofocus when clarity change is detected. |
| [`enableAutoZoom`]({{site.ios-cameraenhancer}}zoom-focus.html#enableautozoom) | Set enableAutoZoom value true to enable auto zoom mode. |
| [`setZoomFactor`]({{site.ios-cameraenhancer}}zoom-focus.html#setzoomfactor) | Set zoom factor |
