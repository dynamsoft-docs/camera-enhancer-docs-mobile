---
layout: default-layout
title: CameraEnhancer Class - Dynamsoft Camera Enhancer Android API references
description: This is the documentation - Android API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android API references, CameraEnhancer Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraEnhancer Class
permalink: /programming-old/android/primary-api/camera-enhancer-v2.0.0.html
---

# CameraEnhancer Class

The main class of `CameraEnhancer` library. It contains APIs that enable user to:

- Implement basic camera control like open, close, change resolution, etc.
- Get frames from the video streaming.
- Enable advanced features including:
  - Frame filtering by sharpness
  - Frame filtering by sensor
  - Enhanced focus
  - Frame cropping
  - Auto zoom

```java
class com.dynamsoft.dce.CameraEnhancer
```

## Initialization Methods Summary

| Method | Description |
| ------ | ----------- |
| [`CameraEnhancer`](#cameraenhancer) | Initialize the `CameraEnhancer` object. |
| [`initLicense`](#initlicense) | Sets product key and activate the SDK. |
| [`getVersion`](#getversion) | Get the SDK version. |

## Basic Camera Control Methods Summary

| Method | Description |
| ------ | ----------- |
| [`getAllCameras`](#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera(String)`](#selectcamerastring) | Select a camera from the camera list with the camera ID. |
| [`getSelectedCamera`](#getselectedcamera) | Get the camera ID of the current selected camera. |
| [`getCameraState`](#getcamerastate) | Get the state of the currently selected camera. |
| [`open`](#open) | Turn on the current selected camera. |
| [`close`](#close) | Turn off the current selected camera. |
| [`pause`](#pause) | Pause the current selected  camera. |
| [`resume`](#resume) | Resume the current selected camera. |
| [`turnOnTorch`](#turnontorch) | Turn on the torch. |
| [`turnOffTorch`](#turnofftorch) | Turn off the torch. |
| [`getFrameRate`](#getframerate) | Get the current frame rate. |
| [`getResolutionList`](#getresolutionlist) | Get all available resolutions. |
| [`setResolution`](#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`](#getresolution) | Get the current resolution. |
| [`setZoom`](#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`setFocus`](#setfocus) | Focus once at the input position. |
| [`setFrameRate`](#setframerate) | **Deprecated, will be removed in v3.0**. Set the frame rate to the input value (if the input value is available for the device). |

## Frame Acquiring Methods Summary

| Method | Description |
| ------ | ----------- |
| [`getFrameFromBuffer`](#getframefrombuffer) | Get the latest frame from the buffer. The boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`](#addlistener) | Add a listener to the camera enhancer instance. |
| [`removeListener`](#removelistener) | Remove a previously added listener from the camera enhancer instance. |

## Enhanced Features Methods Summary

| Method | Description |
| ------ | ----------- |
| [`enableFeatures`](#enablefeatures) | Enable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android) values. |
| [`disableFeatures`](#disablefeatures) | Disable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android) values. |
| [`isFeatureEnabled`](#isfeatureenabled) | Check whether the input features are enabled. |

## Camera UI Methods Summary

| Method | Description |
| ------ | ----------- |
| [`setCameraView`](#setcameraview) | Set the object of [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html) |
| [`getCameraView`](#getcameraview) | Get the object of [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html) |

## Advanced Camera Control Methods Summary

| Method | Description |
| ------ | ----------- |
| [`updateAdvancedSettingsFromFile`](#updateadvancedsettingsfromfile) | Update advanced parameter settings including filter, sensor and focus settings from a JSON file. |
| [`updateAdvancedSettingsFromString`](#updateadvancedsettingsfromstring) | Update advanced parameter settings including filter, sensor and focus settings from a JSON string. |

&nbsp;

## Initialization Methods Details

### CameraEnhancer

Initialize the `CameraEnhancer` Object.

```java
CameraEnhancer(Activity activity)
```

**Parameters**

`activity`: An instance of `android.app.Activity`.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
```

&nbsp;

### initLicense

Set product key and activate the SDK.

```java
static void initLicense(String license, DCELicenseVerificationListener listener)
```

**Parameters**

`license`: The product key.  
`listener`: The listener that handles callback when the license server returns.  See also [`DCELicenseVerificationListener`]({{ site.android-api-auxiliary }}interface-licenselistener.html).

**Code Snippet**

```java
CameraEnhancer.initLicense("Put your license here", new DCELicenseVerificationListener(){
    @Override
    public void DCELicenseVerificationCallback(boolean b, Exception e) {
        if (!b && e != null) {
            e.printStackTrace();
        }
    }
});
```

&nbsp;

### getVersion

Get the SDK version of Dynamsoft Camera Enhancer.

```java
String getVersion()
```

**Return Value**

A string value that stands for the camera enhancer SDK version.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
String DCEVersion = cameraEnhancer.getVersion();
```

&nbsp;

## Basic Camera Control Methods Details

### getAllCameras

Get the IDs of all available cameras.

```java
String[] getAllCameras()
```

**Return Value**

An array list that inclueds all available cameras. Users can clearly read whether the camera is front-facing, back-facing or external from the cameraID.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
String[] cameraIds = cameraEnhancer.getAllCameras();
```

&nbsp;

### selectCamera(String)

Select camera by `cameraID`. The camera will be selected and further camera control settings will be applied to this camera. When the selected camera is changed by selecting another camera via this method, the settings applied to this camera will be inherited by the newly selected camera.

```java
void selectCamera(String cameraID) throws CameraEnhancerException
```

**Parameters**

`cameraID`: A `String` value that listed in the `cameraIDList` returned by `getAllCameras`. The method will have no effects if the input value does not exist in the `cameraIDList`.

**Exception**

An exception thrown to indicate an error has occurred when switching the camera.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.selectCamera("BACK_FACING_CAMERA_0");
```

**Remarks**

- There is always a back-facing camera be defined as a default camera. If the user doesn't select any camera via `selectCamera`, the default camera will be considered as the selected camera.
- If there is no opened camera, the method `selectCamera` will not open any camera.
- If there is an opened camera and the opened camera's ID exactly equals the input ID, the method `selectCamera` will make no changes.
- If there is an opened camera and the opened camera's ID is different from the input ID, the method `selectCamera` will close the currently opened camera and then open a new camera by the input ID.

&nbsp;

### getSelectedCamera

Get the ID of the currently selected camera.

```java
String getSelectedCamera()
```

**Return Value**

The ID of the current selected camera.

**CodeSnippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
String selectedCameraID = cameraEnhancer.getSelectedCamera();
```

&nbsp;

### getCameraState

Get the state of the currently selected camera.

```java
EnumCameraState getCameraState()
```

**Return Value**

One of the preset camera state in Enumeration [`EnumCameraState`]({{site.mobile-enum}}enum-camera-state.html).

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this);
int cameraState = cameraEnhancer.getCameraState();
```

&nbsp;

### open

- Turn on the selected camera if a camera has been selected via `selectCamera`.
- Turn on the default camera if no camera is selected via `selectCamera`.

```java
void open() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is opening the camera.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.open();
```

&nbsp;

### close

- Turn off the selected camera if a camera has been selected via `selectCamera`.
- Turn off the default camera if no camera is selected via `selectCamera`.

```java
void close() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is closing the camera.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.close();
```

&nbsp;

### pause

- Pause the selected camera if a camera has been selected via `selectCamera`.
- Pause the default camera if no camera is selected via `selectCamera`.

```java
void pause() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is pausing the camera.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.pause();
```

**Remarks**

If the `pause` method is triggered:

- The camera UI will be stopped on the last captured frame before you `pause` the camera.
- The camera is still open.
- The video streaming input is not stopped.
- DCE video buffer will continue appending frames.

&nbsp;

### resume

- Resume the selected camera if a camera has been selected via `selectCamera`.
- Resume the default camera if no camera is selected via `selectCamera`.

```java
void resume() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is resuming the camera.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.resume();
```

&nbsp;

### turnOnTorch

Turn on the torch (if the torch of the mobile device is available).

```java
void turnOnTorch() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is turning on the torch.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.turnOnTorch();
```

&nbsp;

### turnOffTorch

Turn off the torch.

```java
void turnOffTorch() throws CameraEnhancerException
```

**Exception**

An exception thrown to indicate an error has occurred when the device is turning off the torch.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
cameraEnhancer.turnOffTorch();
```

&nbsp;

### getFrameRate

Get the current frame rate.

```java
int getFrameRate()
```

**Return Value**

The current frame rate.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

int frameRate = cameraEnhancer.getFrameRate();
```

&nbsp;

### getResolutionList

Check the available resolutions of the current device.

```java
List<Size> getResolutionList()
```

**Return Value**

A list that contains all available resolutions.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

List<Size> resolutionList = cameraEnhancer.getResolutionList();
```

&nbsp;

### setResolution

Input a preset resolution value in Enumeration `Resolution`. The camera enhancer will try to set the resolution to the target value or the closest available value below the target value.

```java
void setResolution(EnumResolution resolution) throws CameraEnhancerException
```

**Parameters**

`resolution`: One of the int value that preset in Enumeration [`EnumResolution`]({{site.mobile-enum}}enum-resolution.html?lang=android).

**Exception**

An exception thrown to indicate an error has occurred when trying to change the resolution.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.setResolution(EnumResolution.RESOLUTION_2K);
```

&nbsp;

### getResolution

Get the current resolution.

```java
Size getResolution()
```

**Return Value**

The size of the current resolution.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

Size currentResolution = cameraEnhancer.getResolution();
```

&nbsp;

### setZoom

Set the zoom factor. The camera will zoom in/out immediately after this method is triggered.

```java
void setZoom(float factor) throws CameraEnhancerException
```

**Parameters**

`factor`: The target zoom factor.

**Exception**

An exception thrown to indicate an error has occurred when trying to zoom-in or zoom-out.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.setZoom(2.5)
```

&nbsp;

### setFocus

Set the focus position (value range from 0.0f to 1.0f) and trigger a focus at the configured position.

```java
void setFocus(float x, float y) throws CameraEnhancerException
```

**Parameters**

`x`: The x-coordinate of the targeting focus position.  
`y`: The y-coordinate of the targeting focus position.

**Exception**

An exception thrown to indicate an error has occurred when trying to trigger a focus.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.setFocus(0.5,0.4);
```

&nbsp;

### setFrameRate

> Note:
> The method is deprecated in v9.0.2 and will be removed in v10.0 release.

Camera Enhancer will try to set the frame rate around the input value.

```java
void setFrameRate(int frameRate) throws CameraEnhancerException
```

**Parameters**

`frameRate`: An int value that refers to the target frame rate.  

**Exception**

An exception thrown to indicate the an error has occurred when trying to change the frame rate.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.setFrameRate(25);
```

**Remarks**

The available frame rate setting threshold is always intermittent, which means the input value might not match any available frame rate threshold. If the input value is below the lowest available threshold, the frame rate will be set to the lowest available threshold. If the input value is above the lowest available threshold but still does not match any threshold, the frame rate will be set to the highest available threshold below the input value.

&nbsp;

## Frame Acquiring Methods Details

### getFrameFromBuffer

Get the latest frame from the video buffer.

```java
DCEFrame getFrameFromBuffer(boolean isKeep)
```

**Parameters**

`isKeep`: If set to `true`, the frame will be kept in the video buffer. Otherwise, it will be removed from the video buffer.

**Return Value**

The latest frame in the video buffer.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
DCEFrame frame = cameraEnhancer.getFrameFromBuffer(false);
```

&nbsp;

### addListener

Add a listener to the `CameraEnhancer` instance. This method will have no effect if the same listener is already added.

```java
void addListener(DCEFrameListener listener)
```

**Parameters**

`listener`: An object of `DCEFrameListener`. Its callback method `frameOutputCallback` will be available for users to make further operations on the captured video frame.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

DCEFrameListener listener = new DCEFrameListener(){
    @Override
    public void frameOutputCallback(DCEFrame frame, long timeStamp) {
        //perform custom action on generated frame
    }
};
cameraEnhancer.addListener(listener);
```

&nbsp;

### removeListener

Remove a previously added listener from the `CameraEnhancer` instance. This method will have no effect if there is no listener exists in `CameraEnhancer` instance.

```java
void removeListener(DCEFrameListener listener)
```

**Parameters**

`listener`: The input listener will be removed from the Camera Enhancer instance.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

DCEFrameListener listener = new DCEFrameListener(){
    @Override
    public void frameOutputCallback(DCEFrame frame, long timeStamp) {
        //perform custom action on generated frame
    }
};
cameraEnhancer.addListener(listener);
// ......
cameraEnhancer.removeListener(listener);
```

&nbsp;

## Enhanced Features Methods Details

### enableFeatures

Enable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android) value.

```java
void enableFeatures(int enhancerFeatures) throws CameraEnhancerException
```

**Parameters**

`enhancerFeatures`: The combined value of [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android).  

**Exception**

An exception thrown to indicate an error has occurred when trying to access the sensor.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.enableFeatures(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

The `EnumEnhancerFeatures` members:

| Members | Value |
| -------- | ----- |
| `EF_FRAME_FILTER` | 0x01 |
| `EF_SENSOR_CONTROL` | 0x02 |
| `EF_ENHANCED_FOCUS` | 0x04 |
| `EF_FAST_MODE` | 0x08 |
| `EF_AUTO_ZOOM` | 0x10 |

The enable action will not be approved if the license is invalid. If your input values include the features that have been already enabled, these features will keep the enabled status.

&nbsp;

### disableFeatures

Disable camera enhancer features by inputting [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android) values.

```java
void disableFeatures(int enhancerFeatures)
```

**Parameters**

`enhancerFeatures`: The combined value of [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android).  

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.disableFeatures(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

You can still disable the features even if the license is invalid. If your input values include the features that are not enabled, these features will keep the disabled status.

&nbsp;

### isFeatureEnabled

Returns a boolean value that means whether the feature(s) you input is (are) enabled.

```java
boolean isFeatureEnabled(int enhancerFeatures)
```

**Parameters**

`enhancerFeatures`: The combined value of [`EnumEnhancerFeatures`]({{site.mobile-enum}}enum-enhancer-features.html?lang=android).

**Return Value**

`True`: All the features you input are enabled.  
`False`: There is at least one feature that is not enabled among your input values.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

boolean isEnabled = cameraEnhancer.isFeatureEnabled(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

If the features you input are all enabled but don't cover all the enabled features, this method will still return `true`.

&nbsp;

## Camera UI Methods Details

### setCameraView

Set a [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html) object as the main UI view.

```java
void setCameraView(DCECameraView cameraView)
```

**Parameters**

`cameraView`: The main UI view. See also [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html).

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

DCECameraView cameraView = findViewById(R.id.cameraView);
cameraEnhancer.setCameraView(cameraView);
```

&nbsp;

### getCameraView

Get the [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html) object of the current UI view.

```java
DCECameraView getCameraView()
```

**Return Value**

The current UI view. See also [`DCECameraView`]({{ site.android-api-auxiliary }}dcecameraview.html).

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

DCECameraView cameraView =  cameraEnhancer.getCameraView();
```

&nbsp;

## Advanced Camera Control Methods Details

### updateAdvancedSettingsFromFile

Update the advanced camera controlling and video streaming processing parameters. This method enable you to update settings via a JSON file from the storage.

```java
void updateAdvancedSettingsFromFile(String filePath) throws CameraEnhancerException
```

**Parameters**

`filePath`: The file path of the JSON file.

**Exception**

An exception thrown to indicate the JSON data is invalid.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 
// Replace the filePath with your target filePath
cameraEnhancer.updateAdvancedSettingsFromFile("/storage/emulated/0/1.json")
```

**Remarks**

You might need permission authority to enable the Camera Enhancer to read the file in your mobile storage.

&nbsp;

### updateAdvancedSettingsFromString

Update the advanced camera controlling and video streaming processing parameters. This method enables you to update settings via a JSON string.

```java
void updateAdvancedSettingsFromString(String jsonString) throws CameraEnhancerException
```

**Parameters**

`jsonString`: A stringified JSON data.

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer(MainActivity.this); 

cameraEnhancer.updateAdvancedSettingsFromString("{'sensorvalue':3,'graydiffthreshold':30,'conversioncountthreshold':30,'sharpnessthreshold':0.2,'sharpnessthresholdlarge':0.4,'abssharpnessthreshold':200,'absgraythreshold':35,'claritythreshold':0.1}");
```

The advanced settings are as follow:

| Parameter Name | Type | Description |
| -------------- | ---- | ----------- |
| [`focalLength`](#focallength) | *float* | Set the fixed focal length. |
| [`autoFocusInterval`](#autofocusinterval) | *int* | Set the time interval of the auto focus. |
| [`autoFocusTerminateTime`](#autofocusterminatetime) | *int* | Set the minimum terminate time of auto focus. |
| [`sensorControlSensitivity`](#sensorcontrolsensitivity) | *int* | Set the sensitivity of the mobile sensor. |

#### focalLength

Set the fixed focal length with a float value. When this parameter is configured, the other focus methods and parameters will be disbaled and the focal length will be fixed. Users can reset the focalLength to -1 to disable the fixed focus settings. The closer to the 0, the further the focalLength will be.

| Value Type | Value Range | Default Value |
| ---------- | ----------- | ------------- |
| *int* | [0,10] | -1 |

#### autoFocusInterval

Set the time interval of the auto-focus with an int value.

| Value Type | Value Range | Default Value |
| ---------- | ----------- | ------------- |
| *int* | [0,0x7fffffff] | 3000(ms) |

#### autoFocusTerminateTime

The minimum termination time of the auto-focus with an int value.

| Value Type | Value Range | Default Value |
| ---------- | ----------- | ------------- |
| *int* | [0,0x7fffffff] | 500(ms) |

#### sensorControlSensitivity

Set the sensitivity of the mobile sensor with an int value. A lower input value results in a higher sensitivity.

| Value Type | Value Range | Default Value |
| ---------- | ----------- | ------------- |
| *int* | [0,0x7fffffff] | 50 |
