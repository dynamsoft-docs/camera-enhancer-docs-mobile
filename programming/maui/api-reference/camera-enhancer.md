---
layout: default-layout
title: CameraEnhancer Class - Dynamsoft Capture Vision MAUI Edition
description: CameraEnhancer Class of DCV MAUI edition is the class that defines camera controlling APIs.
keywords: Camera, scan region, focus mode, zoom factor
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraEnhancer

The `CameraEnhancer` class is the primary class of Dynamsoft Camera Enhancer that defines the camera controlling APIs. It is a subclass of `ImageSourceAdapter`.

## Definition

*Namespace:* Dynamsoft.CameraEnhancer.Maui

*Assembly:* Dynamsoft.CaptureVisionRouter.Maui

```java
class CameraEnhancer : ImageSourceAdapter
```

## Methods

| Method | Description |
|------- |-------------|
| [`CameraEnhancer(CameraView cameraView)`](#cameraenhancercameraview-cameraview) | The constructor. Initialize the `CameraEnhancer` with a `CameraView` instance. |
| [`CameraEnhancer`](#cameraenhancer-1) | The constructor. |
| [`SetCameraView`](#setcameraview) | Set/get the `CameraView` instance that bind with this `CameraEnhancer` instance. |
| [`GetCameraView`](#getcameraview) | Set/get the `CameraView` instance that bind with this `CameraEnhancer` instance. |
| [`Open`](#open) | Open the camera. |
| [`Close`](#close) | Close the camera. |
| [`SetScanRegion`](#setscanregion) | Set a scan region. The video frame is cropped based on the scan region. |
| [`GetScanRegion`](#getscanregion) | Get a scan region. |
| [`EnableEnhancedFeatures`](#enableenhancedfeatures) | Enable the specified enhanced features. View EnumEnhancedFeatures for more details. |
| [`DisableEnhancedFeatures`](#disableenhancedfeatures) | Disable the specified enhanced features. View EnumEnhancedFeatures for more details. |
| [`SelectCamera`](#selectcamera) | Select a camera with a camera position. |
| [`GetCameraPosition`](#getcameraposition) | Select a camera with a camera position. |
| [`SetZoomFactor`](#setzoomfactor) | Set the zoom factor of the camera. |
| [`GetZoomFactor`](#getzoomfactor) | Get the zoom factor of the camera. |
| [`SetFocus`](#setfocus) | Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode. |
| [`GetFocusMode`](#getfocusmode) | Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode. |

The following methods are inherited from superclass [`ImageSourceAdapter`]({{ site.dcv_android_api }}core/image-source-adapter.html)

| Method | Description |
| ------ | ----------- |
| [`StartFetching`]({{ site.dcv_maui_api }}core/image-source-adapter.html#startfetching) | Start fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`StopFetching`]({{ site.dcv_maui_api }}core/image-source-adapter.html#stopfetching) | Stop fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`SetMaximumImageCount`]({{ site.dcv_maui_api }}core/image-source-adapter.html#setmaximumimagecount) | Sets the maximum number of images that can be buffered at any time. |
| [`GetMaximumImageCount`]({{ site.dcv_maui_api }}core/image-source-adapter.html#getmaximumimagecount) | Returns the maximum number of images that can be buffered. |
| [`GetImageCount`]({{ site.dcv_maui_api }}core/image-source-adapter.html#getimagecount) | Returns the current number of images in the buffer. |
| [`IsBufferEmpty`]({{ site.dcv_maui_api }}core/image-source-adapter.html#isbufferempty) | Determines whether the buffer is currently empty. |
| [`ClearBuffer`]({{ site.dcv_maui_api }}core/image-source-adapter.html#clearbuffer) | Clears all images from the buffer, resetting the state for new image fetching. |
| [`SetColourChannelUsageType`]({{ site.dcv_maui_api }}core/image-source-adapter.html#setcolourchannelusagetype) | Sets the usage type for color channels in images. |
| [`GetColourChannelUsageType`]({{ site.dcv_maui_api }}core/image-source-adapter.html#getcolourchannelusagetype) | Returns the current usage type for color channels in images. |

### CameraEnhancer(CameraView cameraView)

The constructor. Initialize the `CameraEnhancer` with a `CameraView` instance.

```csharp
CameraEnhancer(CameraView cameraView);
```

**Parameters**

`cameraView`: A [`CameraView`](camera-view.md) instance.

### CameraEnhancer

The constructor.

```csharp
CameraEnhancer();
```

### SetCameraView

Bind a `CameraView` instance with this `CameraEnhancer` instance.

```csharp
void SetCameraView(CameraView view);
```

### GetCameraView

Get the `CameraView` object that bind to this `CameraEnhancer`.

```csharp
CameraView GetCameraView();
```

### Open

Open the camera.

```csharp
void Open();
```

### Close

Close the camera.

```csharp
void Close();
```

### SetScanRegion

Set a scan region. The video frame is cropped based on the scan region.

```csharp
void SetScanRegion(DMRect scanRegion);
```

**Parameters**

`scanRegion`: A [`DMRect`]({{ site.dcv_maui_api }}core/rect.html) object.

### GetScanRegion

Get the scan region if one has been set.

```csharp
DMRect GetScanRegion();
```

**Return Value**

A [`DMRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html) object that represent the scan region area.

### EnableEnhancedFeatures

Enable the specified enhanced features. View [EnumEnhancedFeatures]({{ site.dce_maui_api }}enum/enhanced-features.html) to learn about these enhanced features. By default, these enhanced features are all disabled.

```csharp
void EnableEnhancedFeatures(EnumEnhancedFeatures features);
```

**Parameters**

`enhancedFeatures`: A combined value of `EnumEnhancedFeatures` which indicates a series of enhanced features.

**Return Value**

A bool value that indicates whether the enhanced features are enabled successfully.

### DisableEnhancedFeatures

Disable any enhanced features that have been previously enabled. View [EnumEnhancedFeatures]({{ site.dce_maui_api }}enum/enhanced-features.html) to learn about these enhanced features.

```csharp
void DisableEnhancedFeatures(EnumEnhancedFeatures features);
```

**Parameters**

`enhancedFeatures`: A combined value of `EnhancedFeatures` which indicates a series of enhanced features.

### SelectCamera

Select a camera with a camera position.

```csharp
void SelectCamera(EnumCameraPosition cameraPosition);
```

**Parameters**

`cameraPosition`: One of the [`EnumCameraPosition`]({{ site.dce_maui_api }}enum/camera-position.html) value.

### GetCameraPosition

Get the current camera position.

```csharp
EnumCameraPosition GetCameraPosition();
```

**Return Value**

A `EnumCameraPosition` value that represents the current camera position.

### SetZoomFactor

Set the zoom factor of the camera.

```csharp
void SetZoomFactor(float zoomFactor);
```

**Parameters**

`zoomFactor`: The zoom factor.

### GetZoomFactor

Get the zoom factor of the camera.

```csharp
float GetZoomFactor();
```

**Return Value**

The zoom factor.

### SetFocus

Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode.

```csharp
void SetFocus(Point focusPoint, EnumFocusMode subsequentFocusMode);
```

**Parameters**

`focusPoint`: The focus point of interest. The coordinate base of the point is "image".  
`subsequentFocusMode`: The subsequent focus mode of type [`EnumFocusMode`]({{ site.dce_maui_api }}enum/focus-mode.html).

### GetFocusMode

Get the current focus mode.

```csharp
EnumFocusMode GetFocusMode();
```

**Return Value**

A [`EnumFocusMode`]({{ site.dce_maui_api }}enum/focus-mode.html) value that represents the current focus mode.
