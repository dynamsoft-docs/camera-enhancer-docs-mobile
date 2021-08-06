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

```objc
- (void)updateCameraSettingFromJson:(NSString*)params;
```

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

```objc
- (void)updateCameraSettingFromFile:(NSString*)filePath;
```

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

```objectivec
- (NSString*)getVersion;
```

**Return Value**

`NSString`: The version number.

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

```objectivec
- (CameraState)getCameraCurrentState NS_SWIFT_NAME(getCameraCurrentState());
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

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

```objc
- (CameraState)getCameraDesiredState NS_SWIFT_NAME(getCameraDesiredState());
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

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

```objc
- (void)setCameraDesiredState:(CameraState)state;
```

**Parameters**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

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

```objc
- (void)resumeCamera NS_SWIFT_NAME(resumeCamera());
- (void)pauseCamera NS_SWIFT_NAME(pauseCamera());
```

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

```objc
- (void)startScanning;
- (void)stopScanning;
```

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

```objc
- (void)addCameraListener:(id)listener NS_SWIFT_NAME(addCameraListener(_:));
```

**Parameters**

`Listener`: The camera listener.

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

```objc
- (TorchState)getTorchCurrentState;
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

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

```objc
- (TorchState)getTorchDesiredState;
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

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

```objc
- (void)setTorchDesiredState:(TorchState)state NS_SWIFT_NAME(setTorchDesiredState(_:));
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

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

```objc
- (void)addTorchListener:(id)listener NS_SWIFT_NAME(addTorchListener(_:));
```

**Parameters**

`Listener`: The torch listener.

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

```objc
- (CameraPosition)getCameraPosition;
```

**Return Value**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

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

```objc
- (void)switchCameraPosition;
```

**Parameters**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

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

```objc
- (NSString*)getResolution;
```

**Return Value**

`NSString`: One of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value.

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

```objc
- (void)setResolution:(Resolution)resolution;
```

**Parameters**

`Resolution`: Input one of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value to set the resolution.

**Code Snippet**

Objective-C:

```objectivec
[dce setResolution:RESOLUTION_1080P];
```

Swift:

```swift
dce.setResolution(Resolution.RESOLUTION_1080P)
```

**Remarks**

If the pre-set resolution is unavailable for the current device, the SDK will select the highest available resolution below the pre-set value.
