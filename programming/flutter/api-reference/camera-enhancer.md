---
layout: default-layout
title: CameraEnhancer Class - Dynamsoft Capture Vision Flutter
description: CameraEnhancer class of DCV Flutter edition manages camera operations and enhancements.
keywords: camera, enhancer, barcode reader, flutter, capture vision
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraEnhancer

The `CameraEnhancer` class provides camera-specific functionality including camera selection, focus control, zoom, and other enhanced features. The `CameraEnhancer` is also responsible for the basic UI of the camera view.

## Definition

*Assembly:* dynamsoft_capture_vision_flutter

```dart
class CameraEnhancer extends ImageSourceAdapter
```

## Static Properties

| Property | Description |
| -------- | ----------- |
| [`instance`](#instance) | Returns the singleton instance of `CameraEnhancer`. |

### instance

```dart
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

The following methods are inherited from superclass [`ImageSourceAdapter`]({{ site.dcv_flutter_api }}core/image-source-adapter.html)

| Method | Description |
| ------ | ----------- |
| [`addImageToBuffer`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#addimagetobuffer) | Adds an image to the internal buffer. |
| [`clearBuffer`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#clearbuffer) | Clears all images from the buffer, resetting the state for new image fetching. |
| [`getBufferOverflowProtectionMode`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#getbufferoverflowprotectionmode) | Get the current mode for handling buffer overflow. |
| [`getColourChannelUsageType`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#getcolourchannelusagetype) | Get the current usage type for color channels in images. |
| [`getImage`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#getimage) | Get a buffered image. Implementing classes should return a Promise that resolves with an instance of `ImageData`. |
| [`getMaximumImageCount`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#getmaximumimagecount) | Get the maximum number of images that can be buffered. |
| [`hasImage`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#hasimage) | Checks if an image with the specified ID is present in the buffer. |
| [`setBufferOverflowProtectionMode`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#setbufferoverflowprotectionmode) | Sets the behavior for handling new incoming images when the buffer is full. |
| [`setColourChannelUsageType`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#setcolourchannelusagetype) | Sets the usage type for color channels in images. |
| [`setMaximumImageCount`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#setmaximumimagecount) | Sets the maximum number of images that can be buffered at any time. |
| [`setNextImageToReturn`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#setnextimagetoreturn) | Sets the processing priority of a specific image. This can affect the order in which images are returned by getImage. |
| [`startFetching`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#startfetching) | Start fetching images from the source to the Video Buffer of `ImageSourceAdapter`. |
| [`stopFetching`]({{ site.dcv_flutter_api }}core/image-source-adapter.html#stopfetching) | Stop fetching images from the source to the Video Buffer of `ImageSourceAdapter`. |

### close

Closes the camera and releases the related resources. When the `CaptureVisionRouter` instance calls `stopCapturing`, please make sure to call this method as well to ensure that the resources are released properly.

```dart
Future<void> close();
```

### destroy

Destroys the camera enhancer instance and releases the related resources on the host side.

```dart
Future<void> destroy();
```

### disableEnhancedFeatures

Disables the selected and activated enhanced features (represented by [`EnumEnhancedFeatures`]({{ site.dcv_flutter_api }}core/enum/enhanced-features-camera.md)) of the Camera Enhancer.

```dart
Future<void> disableEnhancedFeatures(int features);
```

### enableEnhancedFeatures

Activates the selected enhanced features (represented by [`EnumEnhancedFeatures`]({{ site.dcv_flutter_api }}core/enum/enhanced-features-camera.md)) provided by the Camera Enhancer library, including the auto-zoom and smart torch features.

```dart
Future<void> enableEnhancedFeatures(int features);
```

**Remarks**

If you would like to activate multiple enhanced features, then they must be combined using the OR (`|`) operator.

```dart
await _cvr.setInput(_camera);
_camera.enableEnhancedFeatures(EnumEnhancedFeatures.autoZoom | EnumEnhancedFeatures.smartTorch);
_camera.open();
```

### getCameraPosition

Returns the current camera being used, represented as a [`EnumCameraPosition`]({{ site.dcv_flutter_api }}core/enum/enhanced-features-camera.md).

```dart
Future<EnumCameraPosition> getCameraPosition() async;
```

### getFocusMode

Returns the current focus mode of the camera, represented as a [`EnumFocusMode`]({{ site.dcv_flutter_api }}core/enum/focus-mode.md).

```dart
Future<EnumFocusMode> getFocusMode() async;
```

### getScanRegion

Returns the current scan region as a [`DSRect`]({{ site.dcv_flutter_api }}core/dsrect.html) object.

```dart
Future<DSRect?> getScanRegion() async;
```

### getZoomFactor

Returns the current zoom factor of the camera.

```dart
Future<double> getZoomFactor();
```

### open

Opens the selected camera to begin the capture process.

```dart
Future<void> open();
```

### selectCamera

Selects the camera based on the specified [`EnumCameraPosition`]({{ site.dcv_flutter_api }}core/enum/camera-position.md).

```dart
Future<void> selectCamera(EnumCameraPosition position);
```

**Remarks**

- **backUltraWide** & **backDualWideAuto**: iPhone only.

### setFocus

Sets the focus point as well as the mode (as a [`EnumFocusMode`]({{ site.dcv_flutter_api }}core/enum/focus-mode.md)) for the camera.

```dart
Future<void> setFocus(Point<double> point, EnumFocusMode focusMode);
```

### setResolution

Sets the resolution of the camera.

```dart
Future<void> setResolution(EnumResolution resolution);
```

### setScanRegion

Sets the scan region of the camera and displays a bordered area on the UI to represent the scan region. To learn how to specify the scan region when using the Barcode Reader, please visit this [section of the foundational user guide]({{ site.dbr_flutter }}explore-features/ui-customization.html#specifying-a-scan-region).

```dart
Future<void> setScanRegion(DSRect region) async;
```

**See also**

- [`DSRect`]({{ site.dcv_flutter_api }}core/dsrect.html).

### setZoomFactor

Sets the zoom factor of the camera.

```dart
Future<void> setZoomFactor(double zoom);
```

### turnOffTorch

Turns off the camera's flashlight (if available).

```dart
Future<void> turnOffTorch();
```

### turnOnTorch

Turns on the camera's flashlight (if available).

```dart
Future<void> turnOnTorch();
```
