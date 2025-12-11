---
layout: default-layout
title: CameraEnhancer - Dynamsoft Camera Enhancer API Reference
description: The class CameraEnhancer of Dynamsoft Camera Enhancer defines the camera controlling APIs.
keywords: camera enhancer, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
permalink: /programming/android/primary-api/camera-enhancer.html
---

# CameraEnhancer

The `CameraEnhancer` class is the primary class of Dynamsoft Camera Enhancer that defines the camera controlling APIs. It is a subclass of `ImageSourceAdapter`.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class CameraEnhancer extends ImageSourceAdapter
```

## Methods

| Method | Description |
|------- |-------------|
| [`CameraEnhancer`](#cameraenhancer) | The constructor. |
| [`CameraEnhancer`](#cameraenhancer) | The constructor. |
| [`addListener`](#addlistener) | Add a VideoFrameListener to receive callback when video frames are output. |
| [`removeListener`](#removelistener) | Remove a VideoFrameListener. |
| [`takePhoto`](#takephoto) | Take a photo. |
| [`getCameraPosition`](#getcameraposition) | Get the camera position. |
| [`setZoomFactor`](#setzoomfactor) | Set the zoom factor of the camera. You can use getCapabilities to check the maximum available zoom factor. |
| [`getZoomFactor`](#getzoomfactor) | Get the zoom factor of the camera. |
| [`getFocusMode`](#getfocusmode) | Get the currently actived focus mode. |
| [`initSystemSettingsFromFile`](#initsystemsettingsfromfile) | Initialize system settings from a JSON file. The system settings contain more precise camera control parameters. |
| [`initSystemSettings`](#initsystemsettings) | Initialize system settings from a JSON string. The system settings contain more precise camera control parameters. |
| [`resetSystemSettings`](#resetsystemsettings) | Reset the system settings to default value. |
| [`initEnhancedSettingsFromFile`](#initenhancedsettingsfromfile) | Initialize enhanced settings from a JSON file. The enhanced settings contain auxiliary parameters of enhanced features. |
| [`initEnhancedSettings`](#initenhancedsettings) | Initialize enhanced settings from a JSON string. The enhanced settings contain auxiliary parameters of enhanced features. |
| [`outputEnhancedSettings`](#outputenhancedsettings) | Output the enhanced settings to a JSON string. The enhanced settings contain auxiliary parameters of enhanced features. |
| [`outputEnhancedSettingsToFile`](#outputenhancedsettingstofile) | Output the enhanced settings to a JSON file. The enhanced settings contain auxiliary parameters of enhanced features. |
| [`resetEnhancedSettings`](#resetenhancedsettings) | Reset the enhanced settings to default value. |
| [`getCapabilities`](#getcapabilities) | Get the device capabilities including zoom factor, ISO, exposure time, etc. |
| [`getCameraState`](#getcamerastate) | Get the device capabilities including zoom factor, ISO, exposure time, etc. |
| [`setCameraStateListener`](#setcamerastatelistener) | Set a CameraStateListener to receive callback when the camera state changed. |
| [`enableEnhancedFeatures`](#enableenhancedfeatures) | Enable the specified enhanced features. View EnumEnhancedFeatures for more details. |
| [`disableEnhancedFeatures`](#disableenhancedfeatures) | Disable the specified enhanced features. View EnumEnhancedFeatures for more details. |
| [`initWithView`](#cameraenhancerviewactivity) | Create an instance of CameraEnhancer. |
| [`init`](#cameraenhancer) | Create an instance of CameraEnhancer. |
| [`setScanRegion`](#setscanregion) | Set a scan region. The video frame is cropped based on the scan region. |
| [`getScanRegion`](#getscanregion) | Get a scan region. |
| [`open`](#open) | Open the camera. |
| [`close`](#close) | Close the camera. |
| [`setResolution`](#setresolution) | Set the resolution. If the targeting resolution is not available for your device, a closest available resolutionll be selected. |
| [`getResolution`](#getresolution) | Get the current resolution. |
| [`selectCamera(position)`](#selectcameraposition) | Select a camera with a camera position. |
| [`getFrameRate`](#getframerate) | Get the frame rate. |
| [`turnOnTorch`](#turnontorch) | Turn on the torch. |
| [`turnOffTorch`](#turnofftorch) | Turn off the torch. |
| [`setFocus`](#setfocus) | Set the focus point of interest and trigger an one-off auto-focus. |
| [`setFocus(subsequentFocusMode)`](#setfocussubsequentfocusmode) | Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode. |
| [`convertRectToViewCoordinates`](#convertrecttoviewcoordinates) | Convert the coordinates of a [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) under video coordinate system to a CGRect under camera view coordinate system. |
| [`convertPointToViewCoordinates`](#convertpointtoviewcoordinates) | Convert the coordinates of a CGPoint under video coordinate system to another CGPoint under camera view coordinate system. |
| [`setImageCaptureDistanceMode`](#setimagecapturedistancemode) | Set/get the capture distance property of the video frame. The capture distance property will be recorded by VideoFrameTag. |
| [`getImageCaptureDistanceMode`](#getimagecapturedistancemode) | Set/get the capture distance property of the video frame. The capture distance property will be recorded by VideoFrameTag. |
| [`setAutoZoomRange`](#setautozoomrange) | Set the range of auto zoom. |
| [`getAutoZoomRange`](#getautozoomrange) | Get the range of auto zoom. |
| [`cameraView`](#setcameraview) | Set/get the CameraView instance that bind with this CameraEnhancer instance. |
| [`getAllCameras`](#getallcameras) | Get the IDs of all available cameras. |
| [`selectCamera`](#selectcamera) | Select a camera with a camera ID. |
| [`getSelectedCamera`](#getselectedcamera) | Get the currently actived camera. |
| [`setZoomFactorChangeListener`](#setzoomfactorchangelistener) | Set a `ZoomFactorChangeListener` to receive callback when the zoom-factor changed. |

## Inherited Methods

The following methods are inherited from superclass [`ImageSourceAdapter`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html)

| Method | Description |
| ------ | ----------- |
| [`hasNextImageToFetch`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#hasnextimagetofetch) | Determines whether there are more images left to fetch. |
| [`setMaxImageCount`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#setmaximagecount) | Set the maximum capability of the Video Buffer. |
| [`getMaxImageCount`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#getmaximagecount) | Get the property defines the maximum capability of the Video Buffer. |
| [`setBufferOverflowProtectionMode`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#setbufferoverflowprotectionmode) | Sets a mode that determines the action to take when there is a new incoming image and the buffer is full. You can either block the Video Buffer or push out the oldest image and append a new one. |
| [`getBufferOverflowProtectionMode`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#getbufferoverflowprotectionmode) | Get the buffer overflow protection mode. |
| [`getImageCount`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#getimagecount) | Get the current image count in the Video Buffer. |
| [`isBufferEmpty`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#isbufferempty) | Check whether the Video Buffer is empty. |
| [`setColourChannelUsageType`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#setcolourchannelusagetype) | Set the usage type of a color channel in an image. |
| [`getColourChannelUsageType`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#getcolourchannelusagetype) | Get the usage type of a color channel in an image. |
| [`startFetching`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#startfetching) | Start fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`stopFetching`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#stopfetching) | Stop fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`getImage`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#getimage) | Get an image from the Video Buffer. |
| [`setNextImageToReturn(imageId)`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#setnextimagetoreturnimageid) | Specify the next image that is returned by method getImage. |
| [`setNextImageToReturn(imageId,keepInBuffer)`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#setnextimagetoreturnimageidkeepinbuffer) | Specify the next image that is returned by method getImage. |
| [`hasImage`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#hasimage) | Check the availability of the specified image. |
| [`addImageToBuffer`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#addimagetobuffer) | Adds an image to the buffer of the adapter. |
| [`clearBuffer`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#clearbuffer) | Clears the image buffer. |
| [`setErrorListener`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html#seterrorlistener) | Register an error listener to receive callback when error occurs in the [`ImageSourceAdapter`]({{ site.dcv_android_api }}core/basic-structures/image-source-adapter.html). |

### CameraEnhancer(lifecycleOwner)

The constructor.

```java
CameraEnhancer(@NonNull final LifecycleOwner lifecycleOwner)
```

**Parameters**

`lifecycleOwner`: An implementation of `LifecycleOwner` such as an `AppCompatActivity` object.

### CameraEnhancer(cameraView, lifecycleOwner)

The constructor.

```java
CameraEnhancer(@NonNull CameraView cameraView, @NonNull final LifecycleOwner lifecycleOwner)
```

**Parameters**

`cameraView`: An object of `CameraView`.

`lifecycleOwner`: An implementation of `LifecycleOwner` such as an `AppCompatActivity` object.

### addListener

Add a VideoFrameListener to receive callback when video frames are output.

```java
void addListener(VideoFrameListener listener){}
```

**Parameters**

`listener`: A delegate object of VideoFrameListener to receive video frame as a ImageData.

### removeListener

Remove a VideoFrameListener.

```java
void removeListener(VideoFrameListener listener){}
```

**Parameters**

`listener`: A delegate object of VideoFrameListener.

### takePhoto

Take a photo.

```java
void takePhoto(PhotoListener listener){}
```

**Parameters**

`photolistener`: A delegate object of PhotoListener to receive the captured photo.

### getCameraPosition

Get the camera position.

```java
EnumCameraPosition getCameraPosition(){}
```

**Return Value**

The camera position.

### setZoomFactor

Set the zoom factor of the camera. You can use getCapabilities to check the maximum available zoom factor.

```java
void setZoomFactor(float factor){}
```

**Parameters**

`factor`: The zoom factor.

### getZoomFactor

Get the zoom factor of the camera.

```java
float getZoomFactor(){}
```

**Return Value**

The zoom factor.

### getFocusMode

Get the currently actived focus mode.

```java
EnumFocusMode getFocusMode(){}
```

**Return Value**

The focus mode.

### initSystemSettingsFromFile

Initialize system settings from a JSON file. The system settings contain more precise camera control parameters.

```java
void initSystemSettingsFromFile(String filePath) throws CameraEnhancerException{}
```

**Parameters**

`filePath`: The path of the JSON file.  
`error`: A NSError pointer. An error occurs when the file path is not available or the JSON datacludes invalid keys or values.

**Return Value**

A bool value that indicates whether the system settings are initialized successfully.

### initSystemSettings

Initialize system settings from a JSON string. The system settings contain more precise camera control parameters.

```java
void initSystemSettings(String jsonString) throws CameraEnhancerException{}
```

**Parameters**

`JsonString`: The JSON string.
`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the system settings are initialized successfully.

### resetSystemSettings

Reset the system settings to default value.

```java
void resetSystemSettings(){}
```

### initEnhancedSettingsFromFile

Initialize enhanced settings from a JSON file. The enhanced settings contain auxiliary parameters of enhanced features.

```java
void initEnhancedSettingsFromFile(String filePath) throws CameraEnhancerException{}
```

**Parameters**

`filePath`: The JSON string.
`error`: A NSError pointer. An error occurs when the file path is not available or the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the enhanced settings are initialized successfully.

### initEnhancedSettings

Initialize enhanced settings from a JSON string. The enhanced settings contain auxiliary parameters of enhanced features.

```java
void initEnhancedSettings(String jsonString) throws CameraEnhancerException{}
```

**Parameters**

`JsonString`: The JSON string.
`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the enhanced settings are initialized successfully.

### outputEnhancedSettings

Output the enhanced settings to a JSON string. The enhanced settings contain auxiliary parameters of enhanced features.

```java
String outputEnhancedSettings() throws CameraEnhancerException;
```

**Parameters**

`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

The enhanced settings in a JSON string.

### outputEnhancedSettingsToFile

Output the enhanced settings to a JSON file. The enhanced settings contain auxiliary parameters of enhanced features.

```java
void outputEnhancedSettingsToFile(String filePath) throws CameraEnhancerException;
```

**Parameters**

`file` The path that you want to output the JSON file.
`error` A NSError pointer. An error occurs when the file path is not available.

**Return Value**

A bool value that indicates whether the enhanced settings are output successfully.

### resetEnhancedSettings

Reset the enhanced settings to default value.

```java
void resetEnhancedSettings(){}
```

### getCapabilities

Get the device capabilities including zoom factor, ISO, exposure time, etc.

```java
Capabilities getCapabilities(){}
```

**Return Value**

A [Capabilities](../auxiliary-api/capabilities.md) object.

### getCameraState

Tells you whether the camera is open, opening, closing, or closed - each state being represented by a member of the [CameraState]({{ site.android }}enum/camera-state.html) enumeration.

```java
EnumCameraState getCameraState(){}
```

**Return Value**

The camera state.

### setCameraStateListener

Set a [CameraStateListener](../auxiliary-api/interface-dcecamerastatelistener.md) to receive callback when the camera state changes.

```java
void setCameraStateListener (CameraStateListener listener){}
```

**Parameters**

`listener`: A delegate object of CameraStateListener to the camera state.

### enableEnhancedFeatures

Enable the specified enhanced features. View [EnumEnhancedFeatures]({{ site.android }}enum/enhanced-features.html?lang=android) to learn about these enhanced features. By default, these enhanced features are all disabled.

```java
void enableEnhancedFeatures(int enhancedFeatures) throws CameraEnhancerException{}
```

**Parameters**

`enhancedFeatures`: A combined value of `EnumEnhancedFeatures` which indicates a series of enhanced features.

**Return Value**

A bool value that indicates whether the enhanced features are enabled successfully.

### disableEnhancedFeatures

Disable any enhanced features that have been previously enabled. View [EnumEnhancedFeatures]({{ site.android }}enum/enhanced-features.html?lang=android) to learn about these enhanced features.

```java
void disableEnhancedFeatures(int enhancerFeatures){}
```

**Parameters**

`enhancedFeatures`: A combined value of `EnhancedFeatures` which indicates a series of enhanced features.

### CameraEnhancer(view,activity)

Create an instance of CameraEnhancer with a [CameraView](../auxiliary-api/dcecameraview.md) object.

```java
CameraEnhancer(CameraView view, Activity activity){}
```

**Parameters**

`view`: A CameraView instance.
`activity`: An activity object.

**Return Value**

An instance of CameraEnhancer.

### CameraEnhancer

Create an instance of CameraEnhancer.

```java
CameraEnhancer(Activity activity){}
```

**Return Value**

An instance of CameraEnhancer.

### setScanRegion

Set a scan region. The video frame is cropped based on the scan region. To learn the full code to setting a scan region, please refer to the [scan region](../guide/scan-region.md) article.

```java
void setScanRegion(DSRect scanRegion) throws CameraEnhancerException{}
```

**Parameters**

`scanRegion`: A [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) object.
`error`: A NSError pointer. An error occurs when the [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) data is invalid.

**Return Value**

A bool value that indicates whether the scan region has been successfully set or not.

**Code Snippet**

### getScanRegion

Get the scan region if one has been set.

```java
DSRect getScanRegion(){}
```

**Return Value**

A [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) object that represent the scan region area.

### open

Open the camera.

```java
void open(){}
```

### close

Close the camera.

```java
void close(){}
```

### setResolution

Set the resolution. If the targeted resolution is not available for your device, the closest available resolution will be selected.

```java
void setResolution(EnumResolution resolution){}
```

**Parameters**

`resolution` One of the EnumResolution value.

### getResolution

Get the current resolution.

```java
Size getResolution(){}
```

**Return Value**

The current resolution.

### getAvailableResolutions

Get all available resolutions.

```java
List<Size> getAvailableResolutions(){}
```

**Return Value**

All available resolutions in a list.

### selectCamera(position)

Select a camera with a camera position.

```java
selectCamera(EnumCameraPosition position){}
```

**Parameters**

`position`: One of the `EnumCameraPosition` value.
`error`: A NSError pointer. An error occurs when failed to switch the camera.

**Return Value**

A bool value that indicates whether the camera selection is successful.

### getFrameRate

Get the frame rate.

```java
int getFrameRate(){}
```

**Return Value**

The current frame rate.

### turnOnTorch

Turn on the torch.

```java
void turnOnTorch(){}
```

### turnOffTorch

Turn off the torch.

```java
void turnOffTorch(){}
```

### setFocus

Set the focus point of interest and trigger an one-off auto-focus.

```java
void setFocus(android.graphics.PointF focusPoint){}
```

**Parameters**

`focusPoint`: The focus point of interest. The coordinate base of the point is "image".

### setFocus(subsequentFocusMode)

Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode.

```java
void setFocus(android.graphics.PointF focusPoint, EnumFocusMode subsequentFocusMode){}
```

**Parameters**

`focusPoint`: The focus point of interest. The coordinate base of the point is "image".  
`subsequentFocusMode`: The subsequent focus mode.

### convertRectToViewCoordinates

Convert the coordinates of a [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) under video coordinate system to a CGRect under camera view coordinate system.

```java
android.graphics.Rect convertRectToViewCoordinates(com.dynamsoft.core.basic_structure.DSRect videoRect){}
```

**Parameters**

`videoRect`: The [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) that you want to convert.

**Return Value**

A CGRect (coordinate measured in PT) converted from the [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html).

### convertPointToViewCoordinates

Convert the coordinates of a CGPoint under video coordinate system to another CGPoint under camera view coordinate system.

```java
Point convertPointToViewCoordinates(Point point){}
```

**Parameters**

`point`: The CGPoint that you want to convert.

**Return Value**

A CGPoint (coordinate measured in PT) converted from the video CGPoint measured in PT.

### setImageCaptureDistanceMode

Set the capture distance property of the video frame. The capture distance property will be recorded by VideoFrameTag.

```java
void setImageCaptureDistanceMode(EnumImageCaptureDistanceMode mode){}
```

### getImageCaptureDistanceMode

Get the capture distance property of the video frame. The capture distance property will be recorded by VideoFrameTag.

```java
EnumImageCaptureDistanceMode getImageCaptureDistanceMode(){}
```

### setAutoZoomRange

Set the range of auto zoom.

```java
void setAutoZoomRange(android.util.Range ){}
```

**Parameters**

`zoomRange`: The zoom range of the auto zoom feature.

### getAutoZoomRange

Get the range of auto zoom.

```java
Range getAutoZoomRange(){}
```

**Return Value**

The zoom range of the auto zoom feature.

### setCameraView

Bind a `CameraView` instance with this `CameraEnhancer` instance.

```java
void setCameraView(CameraView view){}
```

### setZoomFactorChangeListener

Set a [`ZoomFactorChangeListener`](../auxiliary-api/interface-zoomfactorchangelistener.md) to receive callback when the zoom-factor changed.

```java
void setZoomFactorChangeListener(ZoomFactorChangeListener listener);
```

**Parameters**

`listener`: A [`ZoomFactorChangeListener`](../auxiliary-api/interface-zoomfactorchangelistener.md) to receive callback when the zoom-factor changed.

### getAllCameras

> This method is deprecated.

Get the IDs of all available cameras.

```java
String[] getAllCameras(){}
```

**Return Value**

An array of camera IDs.

### selectCamera

> This method is deprecated.

Select a camera with a camera ID.

```java
void selectCamera(String cameraID) throws CameraEnhancerException{}
```

**Parameters**

`position`: One of the Camera IDs.
`error`: A NSError pointer. An error occurs when failed to switch the camera.

**Return Value**

A bool value that indicates whether the camera selection is successful.

### getSelectedCamera

> This method is deprecated.

Get the currently actived camera.

```java
String getSelectedCamera(){}
```

**Return Value**

The ID of the currently actived camera.
