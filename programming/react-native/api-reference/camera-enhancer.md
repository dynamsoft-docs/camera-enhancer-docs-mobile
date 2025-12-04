---
layout: default-layout
title: CameraEnhancer Class - Dynamsoft Capture Vision React Native
description: CameraEnhancer class of Dynamsoft Capture Vision React Native edition manages camera operations and enhancements.
keywords: camera, enhancer, barcode reader, flutter, capture vision
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraEnhancer

The `CameraEnhancer` class provides camera-specific functionality including camera selection, focus control, zoom, and other enhanced features. The `CameraEnhancer` is also responsible for the basic UI of the camera view.

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
class CameraEnhancer extends ImageSourceAdapter
```

## Static Properties

| Property | Description |
| -------- | ----------- |
| [`instance`](#instance) | Returns the singleton instance of `CameraEnhancer`. |

### instance

```js
static CameraEnhancer get instance;
```

## Methods

| Method | Description |
| ------ | ----------- |
| [`close`](#close) | Closes the camera and releases the related resources. |
| [`destroy`](#destroy) | Destroys the camera enhancer instance and releases the related resources on the host side. |
| [`disableEnhancedFeatures`](#disableenhancedfeatures) | Disables the selected and activated enhanced features of the Camera Enhancer. |
| [`enableEnhancedFeatures`](#enableenhancedfeatures) | Activates the selected enhanced features provided by the Camera Enhancer library, including the auto-zoom and smart torch features. |
| [`getCameraPosition`](#getcameraposition) | Returns the current camera being used. |
| [`getFocusMode`](#getfocusmode) | Returns the current focus mode of the camera. |
| [`getScanRegion`](#getscanregion) | Returns the current scan region. |
| [`getZoomFactor`](#getzoomfactor) | Returns the current zoom factor of the camera. |
| [`open`](#open) | Opens the selected camera to begin the capture process. |
| [`selectCamera`](#selectcamera) | Selects the camera based on the specified camera position. |
| [`setFocus`](#setfocus) | Sets the focus point as well as the mode for the camera. |
| [`setResolution`](#setresolution) | Sets the resolution of the camera. |
| [`setScanRegion`](#setscanregion) | Sets the scan region of the camera and displays a bordered area on the UI. |
| [`setZoomFactor`](#setzoomfactor) | Sets the zoom factor of the camera. |
| [`turnOffTorch`](#turnofftorch) | Turns off the camera's flashlight (if available). |
| [`turnOnTorch`](#turnontorch) | Turns on the camera's flashlight (if available). |
| [`getInstance`](#getinstance) | Gets the singleton instance of `CameraEnhancer`. |
| [`requestCameraPermission`](#requestcamerapermission) | Request the camera permission. |

The following methods are inherited from superclass [`ImageSourceAdapter`]({{ site.dcv_react_native_api }}core/image-source-adapter.html)

| Method | Description |
| ------ | ----------- |
| [`addImageToBuffer`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#addimagetobuffer) | Adds an image to the internal buffer. |
| [`clearBuffer`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#clearbuffer) | Clears all images from the buffer, resetting the state for new image fetching. |
| [`getBufferOverflowProtectionMode`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#getbufferoverflowprotectionmode) | Get the current mode for handling buffer overflow. |
| [`getColourChannelUsageType`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#getcolourchannelusagetype) | Get the current usage type for color channels in images. |
| [`getImage`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#getimage) | Get a buffered image. Implementing classes should return a Promise that resolves with an instance of `ImageData`. |
| [`getMaximumImageCount`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#getmaximumimagecount) | Get the maximum number of images that can be buffered. |
| [`hasImage`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#hasimage) | Checks if an image with the specified ID is present in the buffer. |
| [`setBufferOverflowProtectionMode`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#setbufferoverflowprotectionmode) | Sets the behavior for handling new incoming images when the buffer is full. |
| [`setColourChannelUsageType`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#setcolourchannelusagetype) | Sets the usage type for color channels in images. |
| [`setMaximumImageCount`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#setmaximumimagecount) | Sets the maximum number of images that can be buffered at any time. |
| [`setNextImageToReturn`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#setnextimagetoreturn) | Sets the processing priority of a specific image. This can affect the order in which images are returned by getImage. |
| [`startFetching`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#startfetching) | Start fetching images from the source to the Video Buffer of `ImageSourceAdapter`. |
| [`stopFetching`]({{ site.dcv_react_native_api }}core/image-source-adapter.html#stopfetching) | Stop fetching images from the source to the Video Buffer of `ImageSourceAdapter`. |

### close

Closes the camera and releases the related resources. When the `CaptureVisionRouter` instance calls `stopCapturing`, please make sure to call this method as well to ensure that the resources are released properly.

```js
close()
```

### destroy

Destroys the camera enhancer instance and releases the related resources on the host side.

```js
destroy()
```

### disableEnhancedFeatures

Disables the selected and activated enhanced features of the Camera Enhancer.

```js
disableEnhancedFeatures(features: EnumEnhancedFeatures | number)
```

**Parameters**

`features`: An enum value or a combination of [`EnumEnhancedFeatures`](enum/enhanced-features-camera.md) indicating the features to be disabled.

### enableEnhancedFeatures

Activates the selected enhanced features (represented by [`EnumEnhancedFeatures`](enum/enhanced-features-camera.md)) provided by the Camera Enhancer library, including the auto-zoom and smart torch features.

```js
enableEnhancedFeatures(features: EnumEnhancedFeatures | number)
```

**Parameters**

`features`: An enum value or a combination of [`EnumEnhancedFeatures`](enum/enhanced-features-camera.md) indicating the features to be disabled.

### getCameraPosition

Returns the current camera being used, represented as a [`EnumCameraPosition`](enum/camera-position.md).

```js
getCameraPosition(): Promise<number>
```

**Returns**

A promise that resolves the current camera position, of type [`EnumCameraPosition`](enum/camera-position.md).

### getFocusMode

Returns the current focus mode of the camera, represented as a [`EnumFocusMode`](enum/focus-mode.md).

```js
getFocusMode(): Promise<number>
```

**Returns**

A promise that resolves the current focus mode, of type [`EnumFocusMode`](enum/focus-mode.md).

### getScanRegion

Returns the current scan region as a [`DSRect`]({{ site.dcv_react_native_api }}core/dsrect.html) object.

```js
getScanRegion(): Promise<undefined | null | DSRect>
```

**Returns**

A promise that resolves current scan region.

### getZoomFactor

Returns the current zoom factor of the camera.

```js
getZoomFactor(): Promise<number>
```

**Returns**

A promise that resolves current zoom factor.

### open

Opens the selected camera to begin the capture process.

```js
open()
```

### selectCamera

Selects the camera based on the specified [`EnumCameraPosition`](enum/camera-position.md).

```js
selectCamera(position: number)
```

**Parameters**

`position`: One of the [`EnumCameraPosition`](enum/camera-position.md).

**Remarks**

- **backUltraWide** & **backDualWideAuto**: iPhone only.

### setCameraView

Bind a CameraView instance with this CameraEnhancer instance.

```js
setCameraView(view: CameraView)
```

**Parameters**

`view`: A [`CameraView`](camera-view.md) element.

### setFocus

Sets the focus point as well as the mode (as a [`EnumFocusMode`](enum/focus-mode.md)) for the camera.

```js
setFocus(floatX: number, floatY: number, focusMode: number)
```

**Parameters**

`floatX`: The x of focus point of interest. The coordinate base of the point is "image".

`floatY`: The y of focus point of interest. The coordinate base of the point is "image".

`focusMode`: The subsequent focus mode.

### setResolution

Sets the resolution of the camera.

```js
setResolution(resolution: EnumResolution)
```

**Parameters**

`resolution`: One of the [`EnumResolution`](enum/resolution.md).

### setScanRegion

Sets the scan region of the camera and displays a bordered area on the UI to represent the scan region. To learn how to specify the scan region when using the Barcode Reader, please visit this [section of the foundational user guide]({{ site.dbr_react_native }}explore-features/ui-customization.html#specifying-a-scan-region).

```js
setScanRegion(region: undefined | null | DSRect)
```

**Parameters**

`region`: Specifies the scan region. If null or undefined, cancel the scan region.

**See also**

- [`DSRect`]({{ site.dcv_react_native_api }}core/dsrect.html).

### setZoomFactor

Sets the zoom factor of the camera.

```js
setZoomFactor(factor: number)
```

**Parameters**

`factor`: The zoom factor.

### turnOffTorch

Turns off the camera's flashlight (if available).

```js
turnOffTorch()
```

### turnOnTorch

Turns on the camera's flashlight (if available).

```js
turnOnTorch()
```

### getInstance

Get the singleton instance of `CameraEnhancer`.

```js
static getInstance(): CameraEnhancer
```

### requestCameraPermission

Request the camera permission.

```js
static async requestCameraPermission()
```
