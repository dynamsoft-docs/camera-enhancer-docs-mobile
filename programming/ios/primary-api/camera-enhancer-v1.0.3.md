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

## License Activation Methods

### initLicenseFromDLS

Initialize the Camera Enhancer with a license.

```objc
- (instancetype)initLicenseFromDLS:(iDCEDLSConnectionParameters*)parameters
                              view:(DCECaptureView *)view
              verificationDelegate:(id)connectionDelegate;
```

**Parameters**

`iDCEDLSConnectionParameters`: The class [`DMDLSConnectionParameters`]({{site.android-api-auxiliary}}dlsconnection.html) parameters.  
`view`: The [`DCECaptureView`]({{ site.ios-api-auxiliary }}dcecameraview.html).

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
_decView = [DCECaptureView cameraWithFrame:self.view.bounds];
iDCEDLSConnectionParameters* dls = [[iDCEDLSConnectionParameters alloc] init];
dls.organizationID = @"200001";
_dce = [[DynamsoftCameraEnhancer alloc] initLicenseFromDLS:dls view:_dceView verificationDelegate:self];
```
2. 
```swift
dceView = DCECaptureView.init(view: self.view.bounds)
let dls = iDCEDLSConnectionParameters()
dls.organizationID = "200001"
dce = DynamsoftCameraEnhancer.init(licenseFromDLS: dls, view: dceView, verificationDelegate: self)
```

## Frame preprocessing methods

### AcquireListFrame

This API is designed for users to acquire a single frame. When this API is activated, it will fetch the latest frame from the DCE frame queue.

```objectivec
- (FramePackage*)AcquireListFrame;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
FramePackage *fg = [self.camera AcquireListFrame];
```
2. 
```swift
let fg = self.dce.acquireListFrame() 
```

### enableFastMode

This API is designed for users to setup DCE fast mode. DCE fast mode will cut frames into small images that contains barcode areas to improve decode efficiency. It is recommended to be enabled when decoding a single barcode.

```objc
@property (nonatomic, assign) BOOL enableFastMode;
```

**Parameters**

`true`: enable the fast mode.  
`false`: disable the fast mode.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableFastMode:true];
//To check the status of DCE fast mode
[dce getEnableFastMode];
```
2. 
```swift
dce.enableFastMode = true
```

### enableSensorControl

Turn on (off) sensor control

```objc
@property (nonatomic, assign) BOOL enableSensorControl;
```

**Parameters**

`true`: enable the sensor filter.  
`false`: disable the sensor filter.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableSensorControl:true];
//To check the status of the DCE sensor control
BOOL res= [dce enableSensorControl];
```
2. 
```swift
dce.enableSensorControl(true)
//To check the status of the DCE sensor control
let res = dce.enableSensorControl
```

### setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```objectivec
- (void)setSensorControlThreshold:(double)sensor NS_SWIFT_NAME(setSensorControlThreshold(_:));
```

**Parameters**

`int`: A int value that stands for the sensor filter threshold.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setSensorControlThreshold:55];
```
2. 
```swift
dce.setSensorControlThreshold(55)
```

### enableFrameFilter

Turn on(off) DCE filter (recommended to be true).

**Parameters**

`true`: enable the frame sharpness filter.  
`false`: disable the frame sharpness filter.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableFrameFilter:true];
//To check the status of the DCE frame filter
BOOL res= [dce enableFrameFilter];
```
2. 
```swift
dce.enableFrameFilter(true)
//To check the status of the DCE frame filter
let res = dce.enableFrameFilter
```

### setMaxFrameRate

Set max frame rate.

```objectivec
- (void)setMaxFrameRate:(int)maxFrameRate NS_SWIFT_NAME(setMaxFrameRate(_:));
```

**Parameters**

`int`: A int value that stands for the max frame rate.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setMaxFrameRate:24];
```
2. 
```swift
dce.setMaxFrameRate(24)
```

## Regular Camera Methods

### updateCameraSettingFromJson

There are Some detailed settings that can be updated from JSON string or file. [View JSON data template and explanation](#updatecamerasettingfromfile)

```objc
- (void)updateCameraSettingFromJson:(NSString*)params;
```

**Parameters**

The camera setting JSON Strings.

**Code Snippet**

To update from JSON string:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce updateCameraSettingFromJson:@"json string"];
```
2. 
```swift
dce.updateCameraSetting(fromJson: "Your json string")
```

### updateCameraSettingFromFile

There are some detailed settings that can be updated from JSON string or file.

```objc
- (void)updateCameraSettingFromFile:(NSString*)filePath;
```

**Parameters**

The camera setting JSON Strings.

**Code Snippet**

To update from JSON file:

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce updateCameraSettingFromFile:@"your json file path"];
```
2. 
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

### getVersion

Users can check the current DCE version by using this API.

```objectivec
- (NSString*)getVersion;
```

**Return Value**

`NSString`: The version number.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getVersion];
```
2. 
```swift
dce.getVersion()
```

### getCameraCurrentState

Get the current status (on/off) of the camera.

```objectivec
- (CameraState)getCameraCurrentState NS_SWIFT_NAME(getCameraCurrentState());
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getCameraCurrentState];
```
2. 
```swift
dce.getCameraCurrentState()
```

### getCameraDesiredState

Get the desired status (on/off)of the camera.

```objc
- (CameraState)getCameraDesiredState NS_SWIFT_NAME(getCameraDesiredState());
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getCameraDesiredState];
```
2. 
```swift
dce.getCameraDesiredState()
```

### setCameraDesiredState

Set the camera state.

```objc
- (void)setCameraDesiredState:(CameraState)state;
```

**Parameters**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setCameraDesiredState:CAMERA_STATE_ON];
```
2. 
```swift
dce.setCameraDesiredState(CAMERA_STATE_ON)
```

### pauseCamera and resumeCamera

Note: these APIs are created for pausing & resuming the camera but the camera module is still working when paused. if you want to shut down camera module please use `stopScanning`.

```objc
- (void)resumeCamera NS_SWIFT_NAME(resumeCamera());
- (void)pauseCamera NS_SWIFT_NAME(pauseCamera());
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce pauseCamera];
[dce resumeCamera];
```
2. 
```swift
dce.pauseCamera()
dce.resumeCamera()
```

### stopScanning and startScanning

Control the stopping & starting of the camera module.

```objc
- (void)startScanning;
- (void)stopScanning;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce startScanning];
[dce stopScanning];
```
2. 
```swift
dce.startScanning()
dce.stopScanning()
```

### addCameraListener

Add Camera Listener

```objc
- (void)addCameraListener:(id)listener NS_SWIFT_NAME(addCameraListener(_:));
```

**Parameters**

`Listener`: The camera listener.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce addCameraListener:self];
```
2. 
```swift
dce.addCameraListener(self)
```

### getTorchCurrentState

Get the current torch state.

```objc
- (TorchState)getTorchCurrentState;
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getTorchCurrentState];
```
2. 
```swift
dce.getTorchCurrentState()
```

### getTorchDesiredState

Get desired torch state (on/off)

```objc
- (TorchState)getTorchDesiredState;
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getTorchDesiredState];
```
2. 
```swift
dce.getTorchDesiredState()
```

### setTorchDesiredState

Set the torch on/off.

```objc
- (void)setTorchDesiredState:(TorchState)state NS_SWIFT_NAME(setTorchDesiredState(_:));
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setTorchDesiredState:TorchState.on];
```
2. 
```swift
dce.setTorchDesiredState(TorchState.on)
```

### addTorchListener

Add the torch listener.

```objc
- (void)addTorchListener:(id)listener NS_SWIFT_NAME(addTorchListener(_:));
```

**Parameters**

`Listener`: The torch listener.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce addTorchListener:self];
```
2. 
```swift
dce.addTorchListener(self)
```

### getCameraPosition

Get the camera position. DCE will use the back camera as default.

```objc
- (CameraPosition)getCameraPosition;
```

**Return Value**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getCameraPosition];
```
2. 
```swift
dce.getCameraPosition()
```

### switchCameraPosition

Change the camera (front/back).

```objc
- (void)switchCameraPosition;
```

**Parameters**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce switchCameraPosition];
```
2. 
```swift
dce.switchCameraPosition()
```

### getResolution

Get the current resolution setting.

```objc
- (NSString*)getResolution;
```

**Return Value**

`NSString`: One of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce getResolution];
```
2. 
```swift
dce.getResolution()
```

### setResolution

Set the resolution.

```objc
- (void)setResolution:(Resolution)resolution;
```

**Parameters**

`Resolution`: Input one of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value to set the resolution.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setResolution:RESOLUTION_1080P];
```
2. 
```swift
dce.setResolution(EnumResolution.EnumRESOLUTION_1080P)
```

**Remarks**

If the pre-set resolution is unavailable for the current device, the SDK will select the highest available resolution below the pre-set value.

## Focus & Zoom Methods

### setDefaultAutoFocusPosition

Set the position you want to auto focus at. This setting will replace the default focus value and always focus on the set point.

```objc
- (void)setDefaultAutoFocusPosition:(CGPoint)point NS_SWIFT_NAME(setDefaultAutoFocusPosition(_:));
```

**Parameters**

`float`: A float value that stands for the X coordinate of the focus position.  
`float`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setAutoFocusPosition:CGPointMake(0.5, 0.5)];
```
2. 
```swift
dce.setAutoFocusPosition(CGPoint(x: 0.5, y: 0.5))
```

### setManualFocusPosition

Set the position you want to manually focus at. This focus position only takes effect once each time this code is called.

```objc
- (void)setManualFocusPosition:(CGPoint)point NS_SWIFT_NAME(setManualFocusPosition(_:));
```

**Parameters**

`float`: A float value that stands for the X coordinate of the focus position.  
`float`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setManualFocusPosition:CGPointMake(0.5, 0.5)];
```
2. 
```swift
dce.setManualFocusPosition(CGPoint(x: 0.5, y: 0.5))
```

### setFocalLength

Set focal length (float). The range of focal length is from 0 to 1. The value is a precentage. If user sets `setFocalLength(0.5);` it means the focal length will be 50% of the maxium focal length of the camera. Please note, If this API is called to set a focal length, the focal length will be fixed and all other auto focus mode will be disabled. To quit this fixed focal length mode, please set the focal length into -1.

```objc
- (void)setFocalLength:(float)len NS_SWIFT_NAME(setFocalLength(_:));
```

**Parameters**

`float`: A float value between 0 to 10 that stands for the focal length. You can input -1 to quit the fixed focal length mode.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setFocalLength:0.8];
```
2. 
```swift
dce.setFocalLength = 0.8
```

### enableDCEAutoFocus

This API is designed to turn on DCE autofocus mode which is specially designed and is separate from the systems default autofocus mode. DCE autofocus and the default autofocus can work together at the same time without any conflict. The above focus settings are also available for controlling system default autofocus. To turn on DCE autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableDCEAutoFocus;
```

**Parameters**

`true`: Enable the DCE autofocus.  
`false`: Disable the DCE autofocus.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableDCEAutoFocus:true];
//To check the status of DCE autofocus.
bool res = [dce enableDCEAutoFocus];
```
2. 
```swift
dce.enableDCEAutoFocus = true
//To check the status of DCE autofocus.
let res = dce.enableDCEAutoFocus
```

### enableDefaultAutoFocus

This API is designed for controlling the system default autofocus. To turn off default autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableDefaultAutoFocus;
```

**Parameters**

`true`: Enable the default autofocus.  
`false`: Disable the default autofocus.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableDefaultAutoFocus:false];
//To check the status of system default autofocus.
bool res = [dce enableDefaultAutoFocus];
```
2. 
```swift
dce.enableDefaultAutoFocus = false
//To check the status of system default autofocus.
let res = dce.enableDefaultAutoFocus
```

### enableRegularAutoFocus

Regular autofocus is an advanced setting that enables the camera to autofocus for every 3 seconds. It is contained in DCE autofocus. When DCE autofocus is enabled, regular autofocus is enabled as well. To turn off regular autofocus mode:

```objc
@property (nonatomic, assign) BOOL enableRegularAutoFocus;
```

**Parameters**

`true`: Enable the regular autofocus.  
`false`: Disable the regular autofocus.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableRegularAutoFocus:false];
//To check the status of DCE autofocus.
bool res = [dce enableRegularAutoFocus];
```
2. 
```swift
dce.enableRegularAutoFocus = false
//To check the status of DCE regular autofocus.
let res = dce.enableRegularAutoFocus
```

### setRegularAutoFocusParam

Set the focus interval and termination time for the regular autofocus.

```objc
- (void)setRegularAutoFocusParam:(int)focusTimems
            terminateFocusByTime:(int)terminateFocusByTime
            NS_SWIFT_NAME(setRegularAutoFocusParam(_:terminateFocusByTime:));
```

**Parameters**

`int`: Default value is 3000 (millisecond), which means the camera will auto focus for every 3000 milliseconds.  
`int`: Default value is 500 (millisecond), which means the camera will not focus once again within 500 milliseconds.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
//The camera will autofocus for every 3s. It won't focus for a second time within 500ms.
[_dce setRegularAutoFocusParam:3000 terminateFocusByTime:500];
```
2. 
```swift
dce.setRegularAutoFocusParam(3000, terminateFocusByTime: 500)
```

### enableAutoFocusOnSharpnessChange

This API is another advanced setting that enables the camera to autofocus when a change in sharpness is detected between contiguous frames. The same happens with regular autofocus, this focus mode is also enabled by default when DCE auto focus is enabled. To turn off camera autofocus when sharpness changes:

```objc
@property (nonatomic, assign) BOOL enableAutoFocusOnSharpnessChange;
```

**Parameters**

`true`: Enable the sharpness autofocus.  
`false`: Disable the sharpness autofocus.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableAutoFocusOnSharpnessChange:false];
//To check the status of DCE sharpness focus.
bool res = [dce enableAutoFocusOnSharpnessChange];
```
2. 
```swift
dce.enableAutoFocusOnSharpnessChange = false
//To check the status of DCE sharpness focus.
let res = dce.enableAutoFocusOnSharpnessChange
```

### enableAutoZoom

DCE auto zoom mode can be enabled if user is using DCE to enhance decode performance. The auto zoom mode is based on decode region predicted algorithm. In DCE auto zoom mode, If the lastest decoded frame is predicted to contain a barcode but failing to decode, DCE will control the camera to zoom in to approach the barcode region. To enable auto zoom mode:

```objc
@property (nonatomic, assign) BOOL enableAutoZoom;
```

**Parameters**

`true`: Enable the autozoom.  
`false`: Disable the autozoom.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce enableAutoZoom:true];
//To check the status of DCE autozoom.
bool res = [dce enableAutoZoom];
```
2. 
```swift
dce.enableAutoZoom = true
//To check the status of DCE autozoom.
let res = dce.enableAutoZoom
```

### setZoomFactor

To set the zoom factor (float).

```objc
- (void)setZoomFactor:(CGFloat)zoomFactor;
```

**Parameters**

`float`: A float value that stands for the zoom factor.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[dce setZoomFactor:1.5];
```
2. 
```swift
dce.setZoomFactor = 1.5
```
