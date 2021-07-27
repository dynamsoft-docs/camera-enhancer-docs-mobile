---
layout: default-layout
title: Dynamsoft Camera Enhancer - Objective-C & Swift API references - Regular Camera Methods
description: This is the documentation - Objective-C & Swift API references - Regular Camera Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Objective-C & Swift API references, Regular Camera Methods
needAutoGenerateSidebar: true
breadcrumbText: iOS Regular Camera Methods
---

# iOS API Reference - Regular Camera Methods

## updateCameraSettingFromJson

There are Some detailed settings that can be updated from JSON string or file. [View JSON data template and explanation](#updatecamerasettingfromfile)

**Parameters**

The camera setting JSON Strings.

**Code Snippet**

To update from JSON string:

Objective-C:

```objectivec
[dce updateCameraSettingFromJson:@"json string"];
```

Swift:

```swift
dce.updateCameraSetting(fromJson: "Your json string")
```

## updateCameraSettingFromFile

There are some detailed settings that can be updated from JSON string or file.

**Parameters**

The camera setting JSON Strings.

**Code Snippet**

To update from JSON file:

Objective-C:

```objectivec
[dce updateCameraSettingFromFile:@"your json file path"];
```

Swift:

```swift
dce.updateCameraSettingFromFile(fromFile: "Your file path")
```

This is the template for `updateCameraSettingFromJson` and `updateCameraSettingFromFile`:

```Json
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

**Return Value**

The version number.

**Code Snippet**

Objective-C:

```objectivec
[dce getVersion];
```

Swift:

```swift
dce.getVersion()
```

## getCameraCurrentState

Get the current status (on/off) of the camera.

**Return Value**

The [`CameraState`]({{site.parameter-reference}}index.html#camerastate).

**Code Snippet**

Objective-C:

```objectivec
[dce getCameraCurrentState];
```

Swift:

```swift
dce.getCameraCurrentState()
```

## getCameraDesiredState

Get the desired status (on/off)of the camera.

**Return Value**

The [`CameraState`]({{site.parameter-reference}}index.html#camerastate).

**Code Snippet**

Objective-C:

```objectivec
[dce getCameraDesiredState];
```

Swift:

```swift
dce.getCameraDesiredState()
```

## setCameraDesiredState

Set the camera state.

**Parameters**

The [`CameraState`]({{site.parameter-reference}}index.html#camerastate).

**Code Snippet**

Objective-C:

```objectivec
[dce setCameraDesiredState:CAMERA_STATE_ON];
```

Swift:

```swift
dce.setCameraDesiredState(CAMERA_STATE_ON)
```

## pauseCamera and resumeCamera

Note: these APIs are created for pausing & resuming the camera but the camera module is still working when paused. if you want to shut down camera module please use `stopScanning`.

**Code Snippet**

Objective-C:

```objectivec
[dce pauseCamera];
[dce resumeCamera];
```

Swift:

```swift
dce.pauseCamera()
dce.resumeCamera()
```

## stopScanning and startScanning

Control the stopping & starting of the camera module.

**Code Snippet**

Objective-C:

```objectivec
[dce startScanning];
[dce stopScanning];
```

Swift:

```swift
dce.startScanning()
dce.stopScanning()
```

## addCameraListener

Add Camera Listener

**Parameters**

- `CameraEnhancerListener`

**Code Snippet**

Objective-C:

```objectivec
[dce addCameraListener:self];
```

Swift:

```swift
dce.addCameraListener(self)
```

## getTorchCurrentState

Get the current torch state.

**Return Value**

- `TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Objective-C:

```objectivec
[dce getTorchCurrentState];
```

Swift:

```swift
dce.getTorchCurrentState()
```

## getTorchDesiredState

Get desired torch state (on/off)

**Return Value**

- `TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Objective-C:

```objectivec
[dce getTorchDesiredState];
```

Swift:

```swift
dce.getTorchDesiredState()
```

## setTorchDesiredState

Set the torch on/off.

**Return Value**

- `TorchState`: The parameter that stands for the torch state. View in parameter [`TorchState`]({{site.parameter-reference}}index.html#torchstate).

**Code Snippet**

Objective-C:

```objectivec
[dce setTorchDesiredState:TorchState.on];
```

Swift:

```swift
dce.setTorchDesiredState(TorchState.on)
```

## addTorchListener

Add the torch listener.

**Parameters**

- `CameraTorchListener`

**Code Snippet**

Objective-C:

```objectivec
[dce addTorchListener:self];
```

Swift:

```swift
dce.addTorchListener(self)
```

## getCameraPosition

Get the camera position. DCE will use the back camera as default.

**Return Value**

- `CameraPosition`: View in parameter [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition).

**Code Snippet**

Objective-C:

```objectivec
[dce getCameraPosition];
```

Swift:

```swift
dce.getCameraPosition()
```

## switchCameraPosition

Change the camera (front/back).

**Parameters**

- `CameraPosition`: View in parameter [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition).

**Code Snippet**

Objective-C:

```objectivec
[dce switchCameraPosition];
```

Swift:

```swift
dce.switchCameraPosition()
```

## getResolution

Get the current resolution setting.

**Return Value**

- Resolution: A resolution value. View in [`Resolution`]({{site.parameter-reference}}index.html#resolution).

**Code Snippet**

Objective-C:

```objectivec
[dce getResolution];
```

Swift:

```swift
dce.getResolution()
```

## setResolution

Set the resolution.

**Parameters**

- Resolution: Input a resolution value. View in [`Resolution`]({{site.parameter-reference}}index.html#resolution).

**Code Snippet**

Objective-C:

```objectivec
[dce setResolution:RESOLUTION_1080P];
```

Swift:

```swift
dce.setResolution(Resolution.RESOLUTION_1080P)
```

## getResolutionList

Get the available resolutions of the current device.

**Return Value**

- Resolution(s): The available resolutions of the current device. This resolution list might be different from the DCE preset resolution list.

**Code Snippet**

Objective-C:

```objectivec
[dce getResolutionList];
```

Swift:

```swift
dce.getResolutionList()
```
