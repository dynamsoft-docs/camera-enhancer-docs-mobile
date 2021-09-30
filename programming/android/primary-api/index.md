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

# CameraEnhancer Class

```java
class com.dynamsoft.dce.CameraEnhancer
```

## Initialization

| Method | Description |
| ------ | ----------- |
| [`CameraEnhancer`](#cameraenhancer) | Initialize the `CameraEnhancer` object. |
| [`initLicense`](#initlicense) | Initialize Dynamsoft Camera Enhancer with a valid license. |
| [`getVersion`](#getversion) | Get the SDK version. |

&nbsp;

### CameraEnhancer

Initialize the `CameraEnhancer` Object.

```java
CameraEnhancer()
```

**Code Snippet**

```java
CameraEnhancer cameraEnhancer = new CameraEnhancer();
```

&nbsp;

### initLicense

Initialize the camera enhancer with a valid license.

```java
static void initLicense(String license, DCELicenseVerificationListener listener)
```

**Parameters**

`license`: The product key.  
`DCELicenseVerificationListener`: The listener that handle callback when license server returns.

**Code Snippet**

```java
CameraEnhancer.initLicense("", new DCELicenseVerificationListener(){
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

`DCEVersion`: A string value that stands for the camera enhancer SDK version.

**Code Snippet**

```java
String DCEVersion = CameraEnhancer.getVersion();
```

&nbsp;

## Video Streaming Controlling & Frame Acquiring Methods

| [`getFrameFromBuffer`](#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`](#addlistener) | Add [`DCEFrameListener`](). |
| [`removeListener`](#removelistener) | Remove [`DCEFrameListener`](). |
| [`enableFeatures`](#enablefeature) | Enable DCE features with Enumeration value. |
| [`disableFeatures`](#disablefeature) | Disable DCE features with Enumeration value. |
| [`isFeatureEnabled`](#isfeatureenabled) | Returns a boolean value that means whether the feature(s) you input is (are) enabled. |

&nbsp;

### getFrameFromBuffer

Get the latest frame from the video buffer.

**Parameters**

`true`: The frame will be kept in the video buffer.  
`false`: The frame will be removed from the video buffer.

```java
getFrameFromBuffer(boolean keepOrRemove)
```

&nbsp;

### addListener

Add a `DCEFrameListener` to the `CameraEnhancer` instance. This method will have no effect if the same listener is already added.

```java
void addListener(DCEFrameListener listener)
```

**Parameters**

`listener`: Add an object of `DCEFrameListener`. Callback method, `frameOutputCallback`, will be available for users to make further operations on the video streaming.

**Code Snippet**

```java
DCEFrameListener listener = new DCEFrameListener(){
    @Override
    public void frameOutputCallback(DCEFrame frame, long timeStamp)
};
CameraEnhancer.addListener(listener);
```

&nbsp;

### removeListener

Remove a preciously added `DCEFrameListener` from the `CameraEnhancer` instance. This method will have no effect if there is no listener exists in `CameraEnhancer` instance.

```java
void removeListener(DCEFrameListener listener)
```

**Parameters**

`listener`: The input listener will be removed from CameraEnhancer instance.

**Code Snippet**

```java
//Suppose we have added "listener" via CameraEnhancer.addListener(listener);
// You can remove it via removeListener
CameraEnhancer.removeListener(listener);
```

&nbsp;

### enableFeatures

Enable camera enhancer features by inputting `EnumEnhancerFeatures` value.

```java
void enableFeatures(int enhancerFeatures) throws CameraEnhancerException
```

**Parameters**

`enhancerFeatures`: The combined value of `EnumEnhancerFeatures`.  

**Code Snippet**

```java
CameraEnhancer.enableFeatures(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

The `EnumEnhancerFeatures` members:

|  Members | Value |
| ------------------------------ | ----- |
| `FRAME_FILTER` | 0x01 |
| `SENSOR_CONTROL` | 0x02 |
| `ENHANCED_FOCUS` | 0x04 |
| `FAST_MODE` | 0x08 |
| `AUTO_ZOOM` | 0x10 |

The enable action will not be approved if the license is invalid. If your input values include the features that already enabled, these features will keep the enabled status.

&nbsp;

### disableFeatures

Disable camera enhancer features by inputting `EnumEnhancerFeatures` values.

```java
void disableFeatures(int enhancerFeatures)
```

**Parameters**

`enhancerFeatures`: The combined value of `EnumEnhancerFeatures`.  

**Code Snippet**

```java
CameraEnhancer.disableFeatures(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

You can still disable the features evenif the license is invalid. If your input values include the features that are not enabled, these features will keep the disabled status.

&nbsp;

### isFeatureEnabled

Returns a boolean value that means whether the feature(s) you input is (are) enabled.

```java
boolean isFeatureEnabled(int enhancerFeatures)
```

**Parameters**

`enhancerFeatures`: The combined value of `EnumEnhancerFeatures`.

**Return Value**

`True`: All the features you input are enabled.  
`False`: There is at least one feature is not enabled among your input values.

**Code Snippet**

```java
boolean isEnabled = CameraEnhancer.isFeatureEnabled(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

If the features you input are all enabled but don't cover all the enabled features, this method will still return `true`.

&nbsp;

## Regular Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`getAllCameras`](#getallcameras) | Get all available cameras. This method returns a list of available camera IDs. |
| [`selectCamera`](#selectcamera) | Select and active a camera from the camera list with the camera ID. |
| [`getSelectedCamera`](#getselectedcamera) | Get the camera ID of the current actived camera. |
| [`open`](#open) | Turn on the current actived camera. |
| [`close`](#close) | Turn off the current actived camera. |
| [`pause`](#pause) | Pause the current actived  camera. |
| [`resume`](#resume) | Resume the current actived camera. |
| [`turnOnTorch`](#turnontorch) | Turn on the torch. |
| [`turnOffTorch`](#turnofftorch) | Turn off the torch. |

&nbsp;

### getAllCameras

Get the IDs of all available cameras.

```java
String[] getAllCameras()
```

**Return Value**

`cameraIDList`: An array list that inclueds all available cameras. User can clearly read whether the camera is front-facing, back-facing or external from the cameraID.

**Code Snippet**

```java
CameraEnhancer.getAllCameras();
```

&nbsp;

### selectCamera

Select camera by `cameraID`. The selected camera will be activated and further camera control settings will be applied to this camera. When the activated camera is changed by selecting another camera via this method, the settings that applied to this camera will be inherited by the newly selected camera.

```java
void selectCamera(String cameraID) throws CameraEnhancerException
```

**Parameters**

`cameraID`: A `String` value that listed in the `cameraIDList` returned by `getAllCamera`. The method will have no effects if the input value does not exist in the `cameraIDList`.

**Code Snippet**

```java
CameraEnhancer.selectCamera("BACK_FACING_CAMERA_0");
```

**Remarks**

There is always a back-facing camera be defined as a default camera. If user don't select any camera via `selectCamera`, the default camera will be considered as the selected camera.

&nbsp;

### getSelectedCamera

Get the ID of the current actived camera.

```java
String getSelectedCamera();
```

**Return Value**

`cameraID`: The ID of the current actived camera.

**CodeSnippet**

```java
String selectedCameraID = CameraEnhancer.getSelectedCamera();
```

&nbsp;

### open

- Turn on the selected camera if a camera has been selected via `selectCamera`.
- Turn on the default camera if no camera is selected via `selectCamera`.

```java
void open() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.open();
```

&nbsp;

### close

- Turn off the selected camera if a camera has been selected via `selectCamera`.
- Turn off the default camera if no camera is selected via `selectCamera`.

```java
void close() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.close();
```

&nbsp;

### pause

- Pause the selected camera if a camera has been selected via `selectCamera`.
- Pause the default camera if no camera is selected via `selectCamera`.

```java
void pause() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.pause();
```

**Remarks**

If the `pause` method is triggered:

- The camera UI will be stopped on the last frame that captured before you `pause` the camera.
- The camera is still opened.
- The video streaming input is not stopped.
- DCE video buffer will continue appending frames.

&nbsp;

### resume

- Resume the selected camera if a camera has been selected via `selectCamera`.
- Resume the default camera if no camera is selected via `selectCamera`.

```java
void resume() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.resume();
```

&nbsp;

### turnOnTorch

Turn on the torch (if the torch of the mobile device is available).

```java
void turnOnTorch() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.turnOnTorch();
```

&nbsp;

### turnOffTorch

Turn off the torch.

```java
void turnOffTorch() throws CameraEnhancerException
```

**Code Snippet**

```java
CameraEnhancer.turnOffTorch();
```

&nbsp;

## Advanced Camera Control Methods

| Method | Description |
| ------ | ----------- |
| [`setFrameRate`](#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`](#getframerate) | Get the current frame rate. |
| [`getResolutionList`](#getresolutionlist) | Get all available resolutions. |
| [`setResolution`](#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolution`](#getresolution) | Get the current resolution. |
| [`setZoom`](#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`setFocus`](#setfocusposition) | Focus once at the input position. |
| [`updateAdvancedSettings`](#updateadvancedsetting) | Update advanced parameter settings including filter, sensor and focus settings from a JSON Object. |

### setFrameRate

Camera Enhancer will try to set the frame rate around the input value.

```java
void setFrameRate(int frameRate) throws CameraEnhancerException
```

**Parameters**

`frameRate`: An int value that refers to the target frame rate.  

**Code Snippet**

```java
CameraEnhancer.setFrameRate(25);
```

**Remarks**

The available frame rate setting threshold is alway intermittent, which means the input value might not match any available frame rate threshold. If the input value is below the lowest available threshold, the frame rate will be set to the lowest available threshold. If the input value is above the lowest available threshold but still not match any threshold, the frame rate will be set to the highest available threshold that belows the input value.

&nbsp;

### getFrameRate

Get the current frame rate.

```java
int getFrameRate()
```

**Return Value**

`frameRate`: the current frame rate.

**Code Snippet**

```java
int frameRate = CameraEnhancer.getFrameRate();
```

&nbsp;

### getResolutionList

Check the available resolutions of the current device.

```java
List<Size> getResolutionList()
```

**Return Value**

`resolutionList`: A list that contains all available resolutions.

**Code Snippet**

```java
List<Size> resolutionList = mCameraEnhancer.getResolutionList();
```

&nbsp;

### setResolution

Input a target resolution value that preset in Enumeration `Resolution`. The camera enhancer will try to set the resolution to the target value or the closest available value below the target value.

```java
void setResolution(Resolution resolution) throws CameraEnhancerException
```

**Parameters**

`resolution`: One of the int value that preset in Enumeration `Resolution`.

**Code Snippet**

```java
CameraEnhancer.setResolution(Resolution.RESOLUTION_2K);
```

&nbsp;

### getResolution

```java
Size getResolution()
```

**Return Value**

`resolution`: The size of the current resolution.

**Code Snippet**

```java
Size currentResolution = CameraEnhancer.getResolution();
```

&nbsp;

### setZoom

Set the zoom factor. The camera will zoom in/out immediately after this method is triggered.

```java
void setZoom(float factor) throws CameraEnhancerException
```

**Parameters**

`factor`: The target zoom factor.

**Code Snippet**

```java
CameraEnhancer.setZoom(2.5)
```

&nbsp;

### setFocus

Set the focus position and trigger a focus at the configured position.

```java
void setFocus(float x, float y) throws CameraEnhancerException
```

**Parameters**

`x`: The x-coordinate of the targeting focus position.  
`y`: The y-coordinate of the targeting focus position.

**Code Snippet**

```java
CameraEnhancer.setFocus(0.5,0.4);
```

&nbsp;

### updateAdvancedSettingsFromFile

Update the advanced camera controlling and video streaming processing parameters. This method enable you to update the JSON data via a JSON file from the storage.

```java
void updateAdvancedSettings(String filePath) throws CameraEnhancerException
```

**Parameters**

`filePath`: The file path of the JSON file.

**Code Snippet**

```java
// Replace the filePath with your target filePath
CameraEnhancer.updateAdvancedSettingsFromFile("/storage/emulated/0/")
```

**Remarks**

You might need permission authority to enable the Camera Enhancer to read the file in your mobile storage.

&nbsp;

### updateAdvancedSettingsFromString

Update the advanced camera controlling and video streaming processing parameters. This method enable you to update the JSON data via a JSON string.

```java
void updateAdvancedSettings(String jsonString) throws CameraEnhancerException
```

**Parameters**

`jsonString`: A stringified JSON data.

**Code Snippet**

```java
CameraEnhancer.updateAdvancedSettingsFromFile("")
```

&nbsp;

## Camera UI Methods

| Method | Description |
| ------ | ----------- |
| [`setCameraView`](#setcameraview) | Set the object of [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) |
| [`getCameraView`](#getcameraview) | Get the object of [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) |

&nbsp;

### setCameraView

Set a [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) object as the camera UI.

```java
void setCameraView(DCECameraView cameraView)
```

**Parameters**

`cameraView`: [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) Object.

**Code Snippet**

```java
CameraView cameraView = findViewById(R.id.cameraView);
CameraEnhancer.setCameraView(cameraView);
```

&nbsp;

### getCameraView

Get the [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) object of the current UI.

```java
DCECameraView getCameraView()
```

**Return Value**

`cameraView`: The [`DCECameraView`]({{ site.android-api-auxiliary }}cameraview.html) object of the currently displayed UI.

**Code Snippet**

```java
DCECameraView cameraView =  CameraEnhancer.getCameraView();
```
