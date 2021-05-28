---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Initialization
description: This is the documentation - Android API references - Initialization page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Initialization
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
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

## CameraEnhancer Methods

### [Frame preprocessing methods]({{site.android-cameraenhancer}}filter.html)

| Method | Description |
|--------|-------------|
| [`AcquireListFrame`]({{site.android-cameraenhancer}}basic-setting.html#acquirelistframe) | Get the latest frame from the frame queue when this API is activated. |
| [`enableFastMode`]({{site.android-cameraenhancer}}basic-setting.html#fast-mode) | Set true/false to turn on/off DCE fast mode. |
| [`getEnabledFastModeStatus`]({{site.android-cameraenhancer}}basic-setting.html#fast-mode) | Get the current status of fast mode (on/off). |
| [`enableFrameFilter`]({{site.android-cameraenhancer}}filter.html#enableframefilter) | Set true/false to turn on/off DCE frame filter. |
| [`getEnabledFrameFilterStatus`]({{site.android-cameraenhancer}}filter.html#enableframefilter) | Get the status (on/off) of DCE frame filter mode. |
| [`setMaxFrameRate`]({{site.android-cameraenhancer}}filter.html#setmaxframerate) | Set max frame rate. |
| [`enableSensorControl`]({{site.android-cameraenhancer}}filter.html#enablesensorcontrol) | Set true/false to turn on/off DCE sensor control. |
| [`getEnabledSensorControlStatus`]({{site.android-cameraenhancer}}filter.html#enablesensorcontrol) | Get the status (on/off) of DCE sensor control mode. |
| [`setSensorControlThreshold`]({{site.android-cameraenhancer}}filter.html#setsensorcontrolthreshold) | Enable user to change sensor sensitivity (default value is 50). |

### [Regular camera methods]({{site.android-cameraenhancer}}basic-setting.html)

| Method | Description |
|-----------------|---------------|
|[`getDeviceLevel`]({{site.android-cameraenhancer}}basic-setting.html#getdevicelevel)| Make an evaluation on the current device and define its level for further use. |
| [`setAutoModeLevelParam`]({{site.android-cameraenhancer}}filter.html#setautomodelevelparam) | Set auto mode level parameter. |
| [`updateCameraSetting`]({{site.android-cameraenhancer}}basic-setting.html#updatecamerasetting) | Update camera filter and focus settings from Json. |
| [`getVersion`]({{site.android-cameraenhancer}}basic-setting.html#getversion) | Check current DCE version |
| [`setCameraDesiredState`]({{site.android-cameraenhancer}}basic-setting.html#camera-state) | Set Camera on/off. |
| [`getCameraDesiredState`]({{site.android-cameraenhancer}}basic-setting.html#camera-state) | Get camera desired state. |
| [`getCameraCurrentState`]({{site.android-cameraenhancer}}basic-setting.html#camera-state) | Get camera current state. |
| [`pauseCamera`]({{site.android-cameraenhancer}}basic-setting.html#pausecamera-and-resumecamera) | Pause Camera. |
| [`resumeCamera`]({{site.android-cameraenhancer}}basic-setting.html#pausecamera-and-resumecamera) | Resume Camera. |
| [`startScanning`]({{site.android-cameraenhancer}}basic-setting.html#stopscanning-and-startscanning) | Start scanning. |
| [`stopScanning`]({{site.android-cameraenhancer}}basic-setting.html#stopscanning-and-startscanning) | Stop scanning. |
| [`addCameraListener`]({{site.android-cameraenhancer}}basic-setting.html#addcameralistener) | Add camera listener (on preview original, filtered or fast frames). |
| [`removeCameraListener`]({{site.android-cameraenhancer}}basic-setting.html#addcameralistener) | Remove camera listener. |
| [`setTorchDesiredState`]({{site.android-cameraenhancer}}basic-setting.html#torch-state) | Set torch state. |
| [`getTorchDesiredState`]({{site.android-cameraenhancer}}basic-setting.html#torch-state) | Get torch desired state. |
| [`getTorchCurrentState`]({{site.android-cameraenhancer}}basic-setting.html#torch-state) | Get torch current state. |
| [`addTorchListener`]({{site.android-cameraenhancer}}basic-setting.html#addtorchlistener) | Add torch listener. |
| [`getCameraPosition`]({{site.android-cameraenhancer}}basic-setting.html#camera-position) | Get current camera position. |
| [`switchCameraPosition`]({{site.android-cameraenhancer}}basic-setting.html#camera-position) | Switch camera position front/back. |
| [`setResolution`]({{site.android-cameraenhancer}}basic-setting.html#resolution-settings) | Set resolution. |
| [`getResolution`]({{site.android-cameraenhancer}}basic-setting.html#resolution-settings) | Get current resolution setting. |
| [`getResolutionList`]({{site.android-cameraenhancer}}basic-setting.html#resolution-settings) | Get all available resolutions |

### [Focus & zoom methods]({{site.android-cameraenhancer}}zoom-focus.html)

| Method | Description |
|-----------------|---------------|
| [`setAutoFocusPosition`]({{site.android-cameraenhancer}}zoom-focus.html#setautofocusposition) | Set auto focus position (Change the default auto focus position). |
| [`setManualFocusPosition`]({{site.android-cameraenhancer}}zoom-focus.html#setmanualfocusposition) | Set manual focus position (This focus position is only effected once for each time the API is called). |
| [`setFocalLength`]({{site.android-cameraenhancer}}zoom-focus.html#setfocallength) | Set focal length between 0 to 10 to enable fixed focal length mode. In fixed focal length mode, all focus parameters can't be changed until this mode is quit. To quit fixed focal length mode, please set focal length equals to -1. |
| [`enableDCEAutoFocus`]({{site.android-cameraenhancer}}zoom-focus.html#enabledceautofocus) | Set true/false to turn on/off DCE auto focus. |
| [`getEnabledDCEAutoFocusStatus`]({{site.android-cameraenhancer}}zoom-focus.html#enabledceautofocus) | Get the status (on/off) of DCE auto focus. |
| [`enableDefaultAutoFocus`]({{site.android-cameraenhancer}}zoom-focus.html#enabledefaultautofocus) | Set true/false to turn on/off default auto focus. |
| [`getEnabledDefaultAutoFocusStatus`]({{site.android-cameraenhancer}}zoom-focus.html#enabledefaultautofocus) | Get the status (on/off) of camera default auto focus. |
| [`enableRegularAutoFocus`]({{site.android-cameraenhancer}}zoom-focus.html#enableregularautofocus) | If this is true, camera will auto focus every 3 seconds. This focus mode will start automatically if DCE auto focus is enabled. Users can manually quit this focus mode when DCE auto focus is activated. |
| [`getEnabledRegularAutoFocusStatus`]({{site.android-cameraenhancer}}zoom-focus.html#enableregularautofocus) | Get the current status (on/off) of this auto focus mode. |
| [`setRegularAutoFocusParam`]({{site.android-cameraenhancer}}zoom-focus.html#setregularautofocusparam) | Set the time interval and terminate time for the regular auto focus |
| [`enableAutoFocusOnSharpnessChange`]({{site.android-cameraenhancer}}zoom-focus.html#enableautofocusonsharpnesschange) | If this is enabled, camera will autofocus when clarity change is detected. This focus mode will start automatically if DCE autofocus is enabled. Users can manually quit this focus mode when DCE autofocus is activated. |
| [`getEnabledAutoFocusOnSharpnessChangeStatus`]({{site.android-cameraenhancer}}zoom-focus.html#enableautofocusonsharpnesschange) | Get the current status (on/off) of this auto focus mode. |
| [`enableAutoZoom`]({{site.android-cameraenhancer}}zoom-focus.html#enableautozoom) | Set enableAutoZoom value true to enable auto zoom mode. |
| [`getEnabledAutoZoomStatus`]({{site.android-cameraenhancer}}zoom-focus.html#enableautozoom) | Get the status (on/off) of auto zoom mode. |
| [`setZoomFactor`]({{site.android-cameraenhancer}}zoom-focus.html#setzoomfactor) | Set zoom factor. |
