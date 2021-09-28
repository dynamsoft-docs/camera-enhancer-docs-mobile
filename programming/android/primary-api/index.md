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

## Video Streaming Controlling & Frame Acquiring Methods

| [`getFrameFromBuffer`](#getframefrombuffer) | Get the latest frame from the buffer. The input boolean value determines whether the fetched frame will be removed from the buffer. |
| [`addListener`](#addlistener) | Add [`DCEFrameListener`](). |
| [`removeListener`](#removelistener) | Remove [`DCEFrameListener`](). |

| [`enableFeatures`](#enablefeature) | Enable DCE features with Enumeration value. |
| [`disableFeatures`](#disablefeature) | Disable DCE features with Enumeration value. |
| [`isFeatureEnabled`](#isfeatureenabled) | Returns a boolean value that means whether the feature(s) you input is (are) enabled. |
| [`setFrameRate`](#setframerate) | Set the frame rate to the input value (if the input value is available for the device). |
| [`getFrameRate`](#getframerate) | Get the current frame rate. |

### getFrameFromBuffer

Get the latest frame from the video buffer.

**Parameters**

`true`: The frame will be kept in the video buffer.  
`false`: The frame will be removed from the video buffer.

```java
getFrameFromBuffer(boolean keepOrRemove)
```

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

| `EnumEnhancerFeatures` Members | Value |
| ------------------------------ | ----- |
| `FRAME_FILTER` | 0x01 |
| `SENSOR_CONTROL` | 0x02 |
| `ENHANCED_FOCUS` | 0x04 |
| `FAST_MODE` | 0x08 |
| `AUTO_ZOOM` | 0x10 |

The enable action will not be approved if the license is invalid. If your input values include the features that already enabled, these features will keep the enabled status.

For example:

```java
// The following code equals to CameraEnhancer.enableFeatures(0x01|0x02|00x4);
CameraEnhancer.enableFeatures(0x01|0x02);
CameraEnhancer.enableFeatures(0x02|0x04);
```

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

For example:

```java
CameraEnhancer.enableFeatures(0x01|0x02);
CameraEnhancer.disableFeatures(0x02|0x04);
// Finally, feature 0x01 is enabled, 0x02 and 0x04 are not enabled;
```

### isFeatureEnabled

Returns a boolean value that means whether the feature(s) you input is (are) enabled.

```java
boolean isFeatureEnabled(int enhancerFeatures)
```

**Parameters**

`True`: All the features you input are enabled.
`False`: There is at least one feature is not enabled among your input values.

**Code Snippet**

```java
boolean isEnabled = CameraEnhancer.isFeatureEnabled(EnumEnhancerFeatures.FRAME_FILTER | EnumEnhancerFeatures.SENSOR_CONTROL);
```

**Remarks**

If the features you input are all enabled but don't cover all the enabled features, this method will still return `true`.

For example:

```java
CameraEnhancer.enableFeatures(0x01|0x02);
boolean isEnabled_0 = CameraEnhancer.isFeatureEnabled(0x01);
boolean isEnabled_1 = CameraEnhancer.isFeatureEnabled(0x01|0x02);
boolean isEnabled_2 = CameraEnhancer.isFeatureEnabled(0x01|0x04);
// The value isEnabled_0 = true
// The value isEnabled_1 = true
// The value isEnabled_2 = false
```

### setFrameRate

Camera Enhancer will try to set the frame rate around the input value.

```java
void setFrameRate(int frameRate) throws CameraEnhancerException
```

**Parameters**

`frameRate`: An int value that refers to the target frame rate. The available frame rate setting threshold is alway intermittent, which means the input value might not match any available frame rate threshold. If the input value is below the lowest available threshold, the frame rate will be set to the lowest available threshold. If the input value is above the lowest available threshold but still not match any threshold, the frame rate will be set to the highest available threshold that belows the input value.

**Code Snippet**

```java
CameraEnhancer.setFrameRate(25);
```

### getFrameRate

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

## Advanced Camera Control Methods

| [`getResolution`](#getresolution) | Get the current resolution. |
| [`setResolution`](#setresolution) | Set the resolution to the input value (if the input value is available for the device). |
| [`getResolutionList`](#getresolutionlist) | Get all available resolutions. |
| [`setZoomRegion`](#setzoomregion) | Set `Rect` value of the interest region. The Camera Enhancer will try to zoom in to maximize the interest area on the screen. |
| [`setZoom`](#setzoom) | Set the zoom factor. Once `setZoom` is triggered and approved, the zoom factor of the actived camera will immediately become the input value. |
| [`setFocusPosition`](#setfocusposition) | Focus once at the input position. |
| [`updateAdvancedSettings`](#updateadvancedsetting) | Update advanced parameter settings including filter, sensor and focus settings from a JSON Object. |

## Camera UI Methods

| Method | Description |
| ------ | ----------- |
| [`addCameraView`](#addcameraview) | Add camera video streaming UI. Read more from [`DCECameraView`](). |
