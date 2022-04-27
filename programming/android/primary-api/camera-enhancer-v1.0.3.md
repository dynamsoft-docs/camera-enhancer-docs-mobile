---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - CameraEnhancer Class
description: This is the documentation - Android API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, CameraEnhancer Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraEnhancer Class
---

# Android CameraEnhancer Class

`CameraEnhancer` is the class that provides multifunctional APIs on frame preprocessing and camera controlling.

```java
class com.dynamsoft.dce.CameraEnhancer
```

## License Activation Methods

### initLicenseFromDLS

Initialize the `CameraEnhancer` from the license server.

```java
void initLicenseFromDLS(CameraDLSLicenseVerificationListener listener)
```

**Parameters**

`CameraDLSLicenseVerificationListener`: The interface [`CameraDLSLicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener-v1.0.3.html).

**Code Snippet**

```java
CameraEnhancer mCameraEnhancer = new CameraEnhancer(MainActivity.this);
mCameraEnhancer.addCameraView(cameraView);
com.dynamsoft.dce.DMDLSConnectionParameters info = new com.dynamsoft.dce.DMDLSConnectionParameters();
info.organizationID = "Put your organizationID here.";
mCameraEnhancer.initLicenseFromDLS(info,new CameraDLSLicenseVerificationListener() {
    @Override
    public void DLSLicenseVerificationCallback(boolean isSuccess, Exception error) {
        if(!isSuccess){ error.printStackTrace(); }
    }
});
```

## Frame Preprocessing methods

### AcquireListFrame

Fetch a single buffered frame from the video buffer.

```java
AcquireListFrame(boolean);
```

**Parameters**

`true`: If the video buffer is empty, the method will wait for the next added frame.
`false`: If the video buffer is empty, the method will return an empty value.

**Return Value**

[`DCEFrame`]({{site.android-api-auxiliary}}dceframe.html): This method returns the buffered frame data. The frame data includes the image data, width, height, strides and other frame information.

**Code Snippet**

```java
mCameraEnhancer.AcquireListFrame();
```

### enableFastMode

This API is designed for users to set up DCE fast mode. DCE fast mode will cut frames into small images that contain barcode areas to improve decoding efficiency. It is recommended to be enabled when decoding single barcodes.

```java
enableFastMode(boolean)
```

**Parameters**

`true`: Enable the fast-mode.  
`false`: Disable the fast-mode.

**Code Snippet**

```java
mCameraEnhancer.enableFastMode(true);
```

### getEnabledFastModeStatus

Get the status of the fast mode.

```java
getEnabledFastModeStatus()
```

**Return Value**

`true`: The fast-mode is enabled.  
`false`: The fast-mode is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledFastModeStatus();
```

### enableFrameFilter

Use `enableFrameFilter` to turn on/off frame filter.

```java
enableFrameFilter(boolean)
```

**Parameters**

`true`: Enable the frame filter.  
`false`: Disable the frame filter.

**Code Snippet**

```java
mCameraEnhancer.enableFrameFilter(true);
```

### getEnabledFrameFilterStatus

Get the frame filter status.

```java
getEnabledFrameFilterStatus()
```

**Return Value**

`true`: The frame filter is enabled.  
`false`: The frame filter is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledFrameFilterStatus();
```

### setMaxFrameRate

Set max frame rate.

```java
setMaxFrameRate(int)
```

**Parameters**

`int`: A int value that stands for the max frame rate.

**Code Snippet**

```java
mCameraEnhancer.setMaxFrameRate(24);
```

### enableSensorControl

Use `enableSensorControl` to turn on/off sensor control mode.

```java
enableSensorControl(boolean)
```

**Parameters**

`true`: Enable the sensor filter.  
`false`: Disable the sensor filter.

**Code Snippet**

```java
mCameraEnhancer.enableSensorControl(true);
```

### getEnabledSensorControlStatus

Get the status of sensor control mode.

```java
getEnabledSensorControlStatus()
```

**Return Value**

`true`: The sensor filter is enabled.  
`false`: The sensor filter is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledSensorControlStatus();
```

### setSensorControlThreshold

This API is designed for developers to apply different sensor sensitivity settings on different devices. The default value is 50.

```java
setSensorControlThreshold(int)
```

**Parameters**

`int`: A int value that stands for the sensor filter threshold.

**Code Snippet**

```java
mCameraEnhancer.setSensorControlThreshold(55);
```

## Regular Camera Methods

### getDeviceLevel

This API can help you make an evaluation on your mobile device. It will be helpful to automatically turn off DCE on high-level mobile devices.

```java
getDeviceLevel()
```

**Return Value**

`int`: Returns the device level. Read more in parameter reference [`HardwareUtil`]({{site.parameter-reference}}index.html#hardwareutil).

**Code Snippet**

```java
mCameraEnhancer.getDeviceLevel();
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

```java
mCameraEnhancer.setAutoModeLevelParam(cpuMHz1,cpuMHz2,ramMB1,ramMB2);
```

### updateCameraSetting

There are some detailed settings that can be updated from JSON.

#### Update Settings from JSON Object

```java
updateCameraSetting(JSONObject json) throws CameraEnhancerException
```

**Parameters**

`JSONObject`: The camera setting JSON object.

**Code Snippet**

```java
mJson = new JSONObject();
try {
    mJson.put("graydiffthreshold", 30);//auto zoom
    mJson.put("conversioncountthreshold", 30);//auto zoom
    mJson.put("sensorvalue", 5);//filter by sensor
    mJson.put("sharpnessthreshold", 0.2);//filter by sharpness
    mJson.put("sharpnessthresholdlarge", 0.4);//filter by sharpness
    mJson.put("abssharpnessthreshold", 200);//filter by sharpness
    mJson.put("absgraythreshold", 35);//filter by sharpness
    mJson.put("claritythreshold", 0.1);//focus by sharpness
    mJson.put("ternimatefocusbysharpness", 0.02);//focus by sharpness
} catch (JSONException e) {
    e.printStackTrace();
}
try {
    mCameraEnhancer.updateCameraSetting(mJson);
} catch (CameraEnhancerException e) {
    e.printStackTrace();
}
```

#### Update Settings from JSON file

```java
updateCameraSetting(String path) throws CameraEnhancerException
```

**Parameters**

`String`: A string that refers to the file path.

```java
mCameraEnhancer.updateCameraSetting("Your file path here.");
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

### getVersion

Users can check the current DCE version by using this API.

```java
getVersion()
```

**Return Value**

`String`: The version number.

**Code Snippet**

```java
mCameraEnhancer.getVersion();
```

### getCameraCurrentState

Get the current camera status.

```java
getCameraCurrentState()
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

```java
mCameraEnhancer.getCameraCurrentState();
```

### getCameraDesiredState

Get the camera desired status.

```java
getCameraDesiredState()
```

**Return Value**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

```java
mCameraEnhancer.getCameraDesiredState();
```

### setCameraDesiredState

Set the camera status.

```java
setCameraDesiredState(CameraState)
```

**Parameters**

`CameraState`: An argument that stands for the camera state. One of the [`CameraState`]({{site.parameter-reference}}index.html#camerastate) value.

**Code Snippet**

```java
mCameraEnhancer.setCameraDesireState(CameraState.CAMERA_STATE_OFF);
// Or
mCameraEnhancer.setCameraDesireState(CameraState.CAMERA_STATE_ON);
```

### pauseCamera and resumeCamera

Note: these APIs are created for pausing & resuming the camera but the camera module will still be working when paused. If you want to shut down the camera module please use `stopScanning`.

```java
void pauseCamera()
void resumeCamera()
```

**Code Snippet**

```java
mCameraEnhancer.pauseCamera();
mCameraEnhancer.resumeCamera();
```

### stopScanning and startScanning

Control the stopping & starting of the camera module.

```java
void stopScanning()
void startScanning()
```

**Code Snippet**

```java
mCameraEnhancer.startScanning();
mCameraEnhancer.stopScanning();
```

### addCameraListener

Add the Camera Listener. From the camera listener, you can get three different kinds of frames for further usage.

```java
addCameraListener(CameraListener)
```

**Parameters**

`CameraListener`: The interface [`CameraListener`]({{site.android-api-auxiliary}}interface-dceframelistener.html).

**Return Value**

`Frame`: The video frame captured by camera. View in class [`Frame`]({{site.android-api-auxiliary}}dceframe.html).

**Code Snippet**

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

### removeCameraListener

Remove the camera listener.

```java
removeCameraListener()
```

**Code Snippet**

```java
mCameraEnhancer.removeCameraListener();
```

### getTorchCurrentState

Get the current torch state.

```java
getTorchCurrentState()
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

```java
mCameraEnhancer.getTorchCurrentState();
```

### getTorchDesiredState

Get the desired torch state.

```java
getTorchDesiredState()
```

**Return Value**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

```java
mCameraEnhancer.getTorchDesiredState();
```

### setTorchDesiredState

Set the desired torch state.

```java
setTorchDesiredState(TorchState)
```

**Parameters**

`TorchState`: An argument that stands for the torch state. One of the [`TorchState`]({{site.parameter-reference}}index.html#torchstate) value.

**Code Snippet**

```java
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_AUTO);
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_ON);
mCameraEnhancer.setTorchDesiredState(TorchState.TORCH_STATE_OFF);
```

### addTorchListener

Add the torch listener.

```java
addTorchListener(TorchListener)
```

**Parameters**

`TorchListener`: The interface [`TorchListener`]({{site.android-api-auxiliary}}interface-torchlistener.html)

**Code Snippet**

```java
mCameraEnhancer.addTorchListener(new TorchListener() {
    @Override
    public void onTorchStateChanged(TorchState torchState) {
                
    }
});
```

### getCameraPosition

DCE will use the back camera of your mobile device by default. You can use `getCameraPosition` to check which camera is activated and use `switchCameraPosition` to change the setting.

```java
getCameraPosition()
```

**Return Value**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

**Code Snippet**

```java
mCameraEnhancer.getCameraPosition();
```

### switchCameraPosition

Change the camera position. Switch between the front or back camera.

```java
switchCameraPosition(CameraPosition)
```

**Parameters**

`CameraPosition`: An argument that stands for which camera is selected. One of the [`CameraPosition`]({{site.parameter-reference}}index.html#cameraposition) value.

**Code Snippet**

```java
mCameraEnhancer.switchCameraPosition(CameraPosition.CAMERA_POSITION_USER);
mCameraEnhancer.switchCameraPosition(CameraPosition.CAMERA_POSITION_WORLD);
```

### getResolution

Get the current resolution settings.

```java
getResolution()
```

**Return Value**

`Resolution`: One of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value.

**Code Snippet**

```java
mCameraEnhancer.getResolution();
```

### setResolution

Set the resolution.

```java
setResolution(Resolution)
```

**Parameters**

`Resolution`: One of the [`Resolution`]({{site.parameter-reference}}index.html#resolution) value.

**Code Snippet**

```java
mCameraEnhancer.setResolution(Resolution.RESOLUTION_1080P);
```

### getResolutionList

Get all the available resolution value of the device.

```java
getResolutionList()
```

**Return Value**

`List<Size>`: The device available Resolution: The device available resolution list. This resolution list might be different from the value of parameter `Resolution`.

**Code Snippet**

```java
mCameraEnhancer.getResolutionList();
```

**Remarks**

If the pre-set resolution is unavailable for the current device, the SDK will select the highest available resolution below the pre-set value.

## Focus & Zoom Methods

### setAutoFocusPosition

Set the position that you want to auto focus at. This setting will replace the default focus value and always focus on the set point.

```java
setAutoFocusPosition(float, float)
```

**Parameters**

`X`: A float value that stands for the X coordinate of the focus position.  
`Y`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

```java
mCameraEnhancer.setAutoFocusPosition(0.5f,0.6f);
```

### setManualFocusPosition

Set the manual focus position. This position only takes effect once when this API is called.

```java
setAutoFocusPosition(int, int)
```

**Parameters**

`X`: The int pixel value that stands for the X coordinate of the focus position.  
`Y`: The int pixel value that stands for the Y coordinate of the focus position.

**Code Snippet**

```java
//The focus position will be 200 pixel from left and 300 pixel from top.
mCameraEnhancer.setManualFocusPosition(200, 300);
```

### setFocalLength

Set the focal length (float). The range of focal length is from 0 to 10. The value is a precentage. If user sets `setFocalLength(5);` it means the focal length will be 50% of the maxium focal length of the camera. Please note, If this API is called to set a focal length, the focal length will be fixed and all other auto focus mode will be disabled. To quit this fixed focal length mode, please set the focal length into -1.

```java
setFocalLength(float)
```

**Parameters**

`float`: A float value between 0 to 10 that stands for the focal length. You can input -1 to quit the fixed focal length mode.

**Code Snippet**

```java
mCameraEnhancer.setFocalLength(8.5);
```

To quit:

```java
mCameraEnhancer.setFocalLength(-1);
```

### enableDCEAutoFocus

This API is designed to turn on DCE auto focus mode which is specially designed and is separate from the systems default auto focus mode. DCE auto focus and the default auto focus can work together at the same time without any conflict. The above focus settings are also available for controlling system default auto focus.

```java
enableDCEAutoFocus(boolean)
```

**Parameters**

`true`: Enable the DCE auto focus.  
`false`: Disable the DCE auto focus.

**Code Snippet**

```java
mCameraEnhancer.enableDCEAutoFocus(true);
```

### getEnabledDCEAutoFocusStatus

Get the status (on/off) of DCE autofocus mode:

```java
getEnabledDCEAutoFocusStatus()
```

**Return Value**

`true`: The DCE auto focus is enabled.  
`false`: The DCE auto focus is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledDCEAutoFocusStatus();
```

### enableDefaultAutoFocus

This API is designed for controlling the system default autofocus.

```java
enableDefaultAutoFocus(boolean)
```

**Parameters**

`true`: Enable the default auto focus.  
`false`: Disable the default auto focus.

**Code Snippet**

```java
mCameraEnhancer.enableDefaultAutoFocus(false);
```

### getEnabledDefaultAutoFocusStatus

To get status (on/off) of Default autofocus mode:

```java
getEnabledDefaultAutoFocusStatus()
```

**Return Value**

`true`: The default auto focus is enabled.  
`false`: The default auto focus is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledDefaultAutoFocusStatus();
```

### enableRegularAutoFocus

Regular auto focus is an advanced setting that enables the camera to auto focus every 3 seconds. It is contained in DCE auto focus. When DCE auto focus is enabled, regular auto focus is enabled as well. To turn off regular auto focus mode:

```java
enableRegularAutoFocus(boolean)
```

**Parameters**

`true`: Enable the regular auto focus.  
`false`: Disable the regular auto focus.

**Code Snippet**

```java
mCameraEnhancer.enableRegularAutoFocus(false);
```

### getEnabledRegularAutoFocusStatus

Get status (on/off) of regular autofocus mode:

```java
getEnabledRegularAutoFocusStatus()
```

**Parameters**

`true`: The regular auto focus is enabled.  
`false`: The regular auto focus is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledRegularAutoFocusStatus();
```

### setRegularAutoFocusParam

You can set the focus interval time and focus terminate time in regular auto focus mode. Please use `setregularautofocusparam` to make these settings.

```java
setRegularAutoFocusParam(int, int)
```

**Parameters**

`int`: Focus interval, Default value is 3000 (millisecond), which means the camera will auto focus for every 3000 milliseconds.  
`int`: Terminate time, Default value is 500 (millisecond), which means the camera will not focus once again within 500 milliseconds.

**Code Snippet**

```java
// Set focus interval = 3000 and focus terminate time = 500.
mCameraEnhancer.setRegularAutoFocusParam(3000, 500);
```

### enableAutoFocusOnSharpnessChange

This API is another advanced setting that enabled the camera to autofocus when sharpness change is detected between contiguous frames. The same with regular autofocus, this focus mode is also enabled by default when DCE autofocus is enabled. To turn off camera autofocus when sharpness changes:

```java
enableAutoFocusOnSharpnessChange(boolean)
```

**Parameters**

`true`: Enable the sharpness auto focus.  
`false`: Disable the sharpness auto focus.

**Code Snippet**

```java
mCameraEnhancer.enableAutoFocusOnSharpnessChange(false);
```

### getEnabledAutoFocusOnSharpnessChangeStatus

Get the status (on/off) of the sharpness autofocus mode:

```java
getEnabledAutoFocusOnSharpnessChangeStatus()
```

**Return Value**

`true`: The sharpness auto focus is enabled.  
`false`: The sharpness auto focus is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledAutoFocusOnSharpnessChangeStatus();
```

### enableAutoZoom

This auto zoom mode is specially designed for Dynamsoft Barcode Reader users. The barcode reader can always get a localization result even if it fails on decoding. DCE auto zoom will enable the camera to approach the localized barcode area if the barcode reader got a localization result but failed to get a barcode result.

```java
enableAutoZoom(boolean)
```

**Parameters**

`true`: Enable the auto zoom.  
`false`: Disable the auto zoom.

**Code Snippet**

```java
mCameraEnhancer.enableAutoZoom(true);
```

### getEnabledAutoZoomStatus

Get the status (on/off) of autozoom mode:

```java
getEnabledAutoZoomStatus()
```

**Return Value**

`true`: The auto zoom is enabled.  
`false`: The auto zoom is disabled.

**Code Snippet**

```java
boolean x = mCameraEnhancer.getEnabledAutoZoomStatus();
```

### setZoomFactor

Set the zoom factor (float).

```java
setZoomFactor(float)
```

**Parameters**

`float`: A float value that stands for the zoom factor.

**Code Snippet**

```java
mCameraEnhancer.setZoomFactor(1.5f);
```
