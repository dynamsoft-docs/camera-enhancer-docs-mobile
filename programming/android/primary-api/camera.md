---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Regular Camera Methods
description: This is the documentation - Android API references - Basic Settings page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, Regular Camera Methods
needAutoGenerateSidebar: true
breadcrumbText: Android Regular Camera Methods
---

# Android API Reference - Regular Camera Methods

## getDeviceLevel

This API can help you make an evaluation on your mobile device. It will be helpful to automatically turn off DCE on high-level mobile devices.

```java
getDeviceLevel()
```

**Return Value**

`int`: Returns the device level. Read more in parameter reference [`HardwareUtil`]({{site.parameter-reference}}index.html#hardwareutil).

**Code Snippet**

Java:

```java
mCameraEnhancer.getDeviceLevel();
```

Kotlin:

```kotlin
mCameraEnhancer!!.deviceLevel
```

## setAutoModeLevelParam

Set auto mode level parameter - cpuMHz1, cpuMHz2, ramMB1, ramMB2. These are settings for device-level.

```java
setAutoModeLevelParam(int, int, int, int)
```

**Parameters**

We are defining the devices level by their CPU and RAM performance. You can define the ranges for CPU and RAM performance throw this API.

`int (cpuMHz1)`: The smallest value for CPU processing speed.  
`int (cpuMHz2)`: The greatest value for CPU processing speed.  
`int (ramMB1)`: The smallest value for RAM size.  
`int (ramMB2)`: The greatest value for RAM size.

| CPU & RAM | If device CPUMHz > cpuMHz2 | If device CPUMHz1 < CPUMHz < cpuMHz2 | If device CPUMHz < CPUMHz1 |
|--|--|--|--|
| If device ramMB > ramMB2 | Device-level is high | Device-level is mid | Device-level is mid |
| If ramMB1 < device ramMB < ramMB2 | Device-level is mid | Device-level is mid | Device-level is mid |
| If device ramMB < ramMB1 | Device-level is mid | Device-level is mid | Device-level is low |

**Code Snippet**

Java:

```java
mCameraEnhancer.setAutoModeLevelParam(cpuMHz1,cpuMHz2,ramMB1,ramMB2);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setAutoModeLevelParam(cpuMHz1,cpuMHz2,ramMB1,ramMB2)
```

## updateCameraSetting

There are some detailed settings that can be updated from JSON.

### Update Settings from JSON Object

```java
updateCameraSetting(JSONObject json) throws CameraEnhancerException
```

**Parameters**

`JSONObject`: The camera setting JSON object.

**Code Snippet**

Java:

```java
mCameraEnhancer.updateCameraSetting("{"sensorvalue":3,"graydiffthreshold":30,"conversioncountthreshold":30,"sharpnessthreshold":0.2,"sharpnessthresholdlarge":0.4,"abssharpnessthreshold":200,"absgraythreshold":35,"claritythreshold":0.1}");
```

Kotlin:

```kotlin
mCameraEnhancer!!.updateCameraSetting("{'sensorvalue':3,'graydiffthreshold':30,'conversioncountthreshold':30,'sharpnessthreshold':0.2,'sharpnessthresholdlarge':0.4,'abssharpnessthreshold':200,'absgraythreshold':35,'claritythreshold':0.1}")
```

### Update Settings from JSON file

```java
updateCameraSetting(String path) throws CameraEnhancerException
```

**Parameters**

`String`: A string that refers to the file path.

Java:

```java
mCameraEnhancer.updateCameraSetting("Your file path here.");
```

Kotlin:

```kotlin
mCameraEnhancer!!.updateCameraSetting("Your file path here.")
```

JSON file template:

```json
{
    //Absolute sharpness value, A threshold value for controlling filter
    "abssharpnessthreshold":200,
    //Sensor value, A threshold value for controlling filter
    "sensorvalue":3,        
    //A threshold value for gray scale analysis
    "graydiffthreshold":30,
    //A threshold for judging whether the device is shaking
    "sharpnessthreshold":0.2,
    //A threshold for judging whether the device is shaking violently
    "sharpnessthresholdlarge":0.4,
    //A threshold value for calculating sharpness
    "absgraythreshold":35,
    //A threshold value for controlling auto zoom
    "conversioncountthreshold":30,
    //A threshold value that controlling auto focus
    "claritythreshold":0.1
}
```

## getVersion

Users can check the current DCE version by using this API.

```java
getVersion()
```

**Return Value**

`String`: The version number.

**Code Snippet**

Java:

```java
    mCameraEnhancer.getVersion();
```

Kotlin:

```kotlin
    mCameraEnhancer!!.version
```

## getCameraCurrentState

Get the current camera status.

```java
getCameraCurrentState()
```

**Return Value**

[`CameraState`]({{site.parameter-reference}}index.html#camerastate): The camera status.

**Code Snippet**

```java
mCameraEnhancer.getCameraCurrentState();
```

Kotlin:

```kotlin
mCameraEnhancer!!.cameraCurrentState
```

## getCameraDesiredState

Get the camera desired status.

```java
getCameraDesiredState()
```

**Return Value**

[`CameraState`]({{site.parameter-reference}}index.html#camerastate): The camera status.

**Code Snippet**

Java:

```java
mCameraEnhancer.getCameraDesiredState();
```

Kotlin:

```kotlin
mCameraEnhancer!!.cameraDesiredState
```

## setCameraDesiredState

Set the camera status.

```java
setCameraDesiredState(CameraState)
```

**Parameters**

[`CameraState`]({{site.parameter-reference}}index.html#camerastate): The camera status.

**Code Snippet**

Java:

```java
mCameraEnhancer.setCameraDesireState(CameraState.CAMERA_STATE_OFF);
// Or
mCameraEnhancer.setCameraDesireState(CameraState.CAMERA_STATE_ON);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setCameraDesiredState(CameraState.CAMERA_STATE_ON)
// Or
mCameraEnhancer!!.setCameraDesiredState(CameraState.CAMERA_STATE_OFF)
```

## pauseCamera and resumeCamera

Note: these APIs are created for pausing & resuming the camera but the camera module will still be working when paused. If you want to shut down the camera module please use `stopScanning`.

```java
void pauseCamera()
void resumeCamera()
```

**Code Snippet**

Java:

```java
mCameraEnhancer.pauseCamera();
mCameraEnhancer.resumeCamera();
```

Kotlin:

```kotlin
mCameraEnhancer!!.pauseCamera()
mCameraEnhancer!!.resumeCamera()
```

## stopScanning and startScanning

Control the stopping & starting of the camera module.

```java
void stopScanning()
void startScanning()
```

**Code Snippet**

Java:

```java
mCameraEnhancer.startScanning();
mCameraEnhancer.stopScanning();
```

Kotlin:

```kotlin
mCameraEnhancer!!.startScanning()
mCameraEnhancer!!.stopScanning()
```

## addCameraListener

Add the Camera Listener. From the camera listener, you can get three different kinds of frames for further usage.

```java
addCameraListener(CameraListener)
```

**Parameters**

[`CameraListener`]({{site.android-api-auxiliary}}interface.html#cameralistener): interface `CameraListener`.

**Return Value**

`Frame`: The video frame captured by camera. View in class [`Frame`]({{site.android-api-auxiliary}}frame.html).

**Code Snippet**

Java:

```java
mCameraEnhancer.addCameraListener(new CameraListener() {
    @Override
    public void onPreviewOriginalFrame(Frame frame) {}
    @Override
    public void onPreviewFilterFrame(Frame frame) {}
    @Override
    public void onPreviewFastFrame(Frame frame) {}
});
```

Kotlin:

```kotlin
mCameraEnhancer!!.addCameraListener(object : CameraListener {
    override fun onPreviewOriginalFrame(frame: Frame) {}
    override fun onPreviewFilterFrame(frame: Frame) {}
    override fun onPreviewFastFrame(frame: Frame) {}
})
```

## removeCameraListener

Remove the camera listener.

```java
removeCameraListener()
```

**Code Snippet**

Java:

```java
mCameraEnhancer.removeCameraListener();
```

Kotlin:

```kotlin
mCameraEnhancer!!.removeCameraListener()
```

## getTorchCurrentState

Get the current torch state.

```java
getTorchCurrentState()
```

**Return Value**

`TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Java:

```java
mCameraEnhancer.getTorchCurrentState();
```

Kotlin:

```kotlin
mCameraEnhancer!!.torchCurrentState()
```

## getTorchDesiredState

Get the desired torch state.

```java
getTorchDesiredState()
```

**Return Value**

`TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Java:

```java
mCameraEnhancer.getTorchDesiredState();
```

Kotlin:

```kotlin
mCameraEnhancer!!.torchDesiredState
```

## setTorchDesiredState

Set the desired torch state.

```java
setTorchDesiredState(TorchState)
```

**Parameters**

`TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Java:

```java
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_AUTO);
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_ON);
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_OFF);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setTorchDesiredState(TorchState.TORCH_STATE_AUTO)
mCameraEnhancer!!.setTorchDesiredState(TorchState.TORCH_STATE_ON)
mCameraEnhancer!!.setTorchDesiredState(TorchState.TORCH_STATE_OFF)
```

## addTorchListener

Add the torch listener.

```java
addTorchListener(TorchListener)
```

**Parameters**

[`TorchListener`]({{site.android-api-auxiliary}}interface.html#torchlistener): interface `TorchListener`

**Code Snippet**

Java:

```java
mCameraEnhancer.addTorchListener(new TorchListener() {
    @Override
    public void onTorchStateChanged(TorchState torchState) {
                
    }
});
```

Kotlin:

```kotlin
mCameraEnhancer!!.addTorchListener(object : TorchListener {
    override fun onTorchStateChanged(TorchState: torchState) {}
})
```

## getCameraPosition

DCE will use the back camera of your mobile device by default. You can use `getCameraPosition` to check which camera is activated and use `switchCameraPosition` to change the setting.

```java
getCameraPosition()
```

**Return Value**

[`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition): View in parameter `CameraPosition`.

**Code Snippet**

Java:

```java
mCameraEnhancer.getCameraPosition();
```

Kotlin:

```kotlin
mCameraEnhancer!!.cameraPosition
```

## switchCameraPosition

Change the camera position. Switch between the front or back camera.

```java
switchCameraPosition(CameraPosition)
```

**Parameters**

[`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition): View in parameter `CameraPosition`.

**Code Snippet**

Java:

```java
mCameraEnhancer.switchCameraPosition(CameraPosition.CAMERA_POSITION_USER);
mCameraEnhancer.switchCameraPosition(CameraPosition.CAMERA_POSITION_WORLD);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.switchCameraPosition(CameraPosition.CAMERA_POSITION_USER)
    mCameraEnhancer!!.switchCameraPosition(CameraPosition.CAMERA_POSITION_WORLD)
```

## getResolution

Get the current resolution settings.

```java
getResolution()
```

**Return Value**

[`Resolution`]({{site.parameter-reference}}index.html#resolution): View the parameter `Resolution`.

**Code Snippet**

Java:

```java
    mCameraEnhancer.getResolution();
```

Kotlin:

```kotlin
    mCameraEnhancer!!.resolution
```

## setResolution

Set the resolution.

```java
setResolution(Resolution)
```

**Parameters**

[`Resolution`]({{site.parameter-reference}}index.html#resolution): View the parameter `Resolution`.

**Code Snippet**

Java:

```java
mCameraEnhancer.setResolution(Resolution.RESOLUTION_1080P);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setResolution(Resolution.RESOLUTION_1080P)
```

## getResolutionList

Get all the available resolution value of the device.

```java
getResolutionList()
```

**Return Value**

`List<Size>`: The device available Resolution: The device available resolution list. This resolution list might be different from the value of parameter `Resolution`.

**Code Snippet**

Java:

```java
mCameraEnhancer.getResolutionList();
```

Kotlin:

```kotlin
mCameraEnhancer!!.resolutionList
```
