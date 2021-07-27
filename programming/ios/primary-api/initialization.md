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

# iOS CameraEnhancer Class

`CameraEnhancer` is the class that provides multifunctional APIs on frame preprocessing and camera controlling.

For Objective-C users:

```objectivec
@property(nonatomic, strong) DynamsoftCameraEnhancer *dce;
```

For Swift users:

```swift
var dce:DynamsoftCameraEnhancer! = nil
```

## CameraEnhancer Methods

### [Frame preprocessing methods]({{site.ios-api}}preprocess.html)

| Method | Description |
|-----------------|---------------|
| [`acquireListFrame`]({{site.ios-api}}preprocess.html#acquirelistframe) | Get the latest frame from the frame queue when this API is activated. |
| [`enableFastMode`]({{site.ios-api}}preprocess.html#enablefastmode) | Set the value true/false to turn on/off DCE fast mode |
| [`enableSensorControl`]({{site.ios-api}}preprocess.html#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
|[`setSensorControlThreshold`]({{site.ios-api}}preprocess.html#setsensorcontrolthreshold)| Make settings on sensor control threshold |
| [`enableFrameFilter`]({{site.ios-api}}preprocess.html#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`setMaxFrameRate`]({{site.ios-api}}preprocess.html#setmaxframerate) | Set max frame rate |

### [Regular camera methods]({{site.ios-api}}camera.html)

| Method | Description |
|-----------------|---------------|
| [`updateCameraSettingFromJson`]({{site.ios-api}}camera.html#updatecamerasettingfromjson) | Update camera filter and focus settings from Json |
| [`updateCameraSettingFromFile`]({{site.ios-api}}camera.html#updatecamerasettingfromfile) | Update camera filter and focus settings from file |
| [`getVersion`]({{site.ios-api}}camera.html#getversion) | Check current DCE version |
| [`getCameraCurrentState`]({{site.ios-api}}camera.html#getcameracurrentstate) | Get camera current state |
| [`getCameraDesiredState`]({{site.ios-api}}camera.html#getcameradesiredstate) | Get camera desired state |
| [`setCameraDesiredState`]({{site.ios-api}}camera.html#setcameradesiredstate) | Set Camera on/off |
| [`pauseCamera`]({{site.ios-api}}camera.html#pausecamera-and-resumecamera) | Pause Camera |
| [`resumeCamera`]({{site.ios-api}}camera.html#pausecamera-and-resumecamera) | Resume Camera |
| [`startScanning`]({{site.ios-api}}camera.html#stopscanning-and-startscanning) | Start scanning |
| [`stopScanning`]({{site.ios-api}}camera.html#stopscanning-and-startscanning) | Stop scanning |
| [`addCameraListener`]({{site.ios-api}}camera.html#addcameralistener) | Add camera listener (on preview original, filtered or fast frames) |
| [`getTorchCurrentState`]({{site.ios-api}}camera.html#gettorchcurrentstate) | Get torch current state |
| [`getTorchDesiredState`]({{site.ios-api}}camera.html#gettorchdesiredstate) | Get torch desired state |
| [`setTorchDesiredState`]({{site.ios-api}}camera.html#settorchdesiredstate) | Set torch state |
| [`addTorchListener`]({{site.ios-api}}camera.html#addtorchlistener) | Add torch listener |
| [`getCameraPosition`]({{site.ios-api}}camera.html#getcameraposition) | Get current camera position |
| [`switchCameraPosition`]({{site.ios-api}}camera.html#switchcameraposition) | Switch camera position front/back |
| [`getResolution`]({{site.ios-api}}camera.html#getresolution) | Get current resolution setting |
| [`setResolution`]({{site.ios-api}}camera.html#setresolution) | Set resolution |
| [`getResolutionList`]({{site.ios-api}}camera.html#getresolutionlist) | Get all available resolutions |

### [Focus & zoom methods]({{site.ios-api}}zoom-focus.html)

| Method | Description |
|-----------------|---------------|
| [`setAutoFocusPosition`]({{site.ios-api}}zoom-focus.html#setautofocusposition) | Set auto focus position (Change the default auto focus position). |
| [`setManualFocusPosition`]({{site.ios-api}}zoom-focus.html#setmanualfocusposition) | Set manual focus position (This focus position only takes effect once for each time the API is called). |
| [`setFocalLength`]({{site.ios-api}}zoom-focus.html#setfocallength) | Set focal length between 0 to 10 to enable fixed focal length mode. In fixed focal length mode, all focus parameters can't be changed until this mode is quit. To quit fixed focal length mode, please set focal length equals to -1. |
| [`enableDCEAutoFocus`]({{site.ios-api}}zoom-focus.html#enabledceautofocus) | Set true/false to turn on/off DCE auto focus. |
| [`enableDefaultAutoFocus`]({{site.ios-api}}zoom-focus.html#enabledefaultautofocus) | Set true/false to turn on/off default auto focus. |
| [`enableRegularAutoFocus`]({{site.ios-api}}zoom-focus.html#enableregularautofocus) | If this is true, camera will auto focus for every 3 seconds. |
| [`setRegularAutoFocusParam`]({{site.ios-api}}zoom-focus.html#setregularautofocusparam) | Set the focus interval and termination time for the regular autofocus. |
| [`enableAutoFocusOnSharpnessChange`]({{site.ios-api}}zoom-focus.html#enableautofocusonsharpnesschange) | If this is enabled, camera will autofocus when clarity change is detected. |
| [`enableAutoZoom`]({{site.ios-api}}zoom-focus.html#enableautozoom) | Set enableAutoZoom value true to enable auto zoom mode. |
| [`setZoomFactor`]({{site.ios-api}}zoom-focus.html#setzoomfactor) | Set zoom factor |
