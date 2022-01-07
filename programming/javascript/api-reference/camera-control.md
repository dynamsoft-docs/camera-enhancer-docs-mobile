---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - Camera Control
description: This is the main page of Dynamsoft Camera Enhancer JavaScript SDK Camera Control.
keywords: camera enhancer, camera control, javascript, js
needAutoGenerateSidebar: true
needGenerateH3Content: true
noTitleIndex: true
breadcrumbText: Camera Control
---

# Camera Control

## Basic Control

| API Name | Description |
|---|---|
| [getAllCameras()](#getallcameras) | Returns infomation of all available cameras on the device. |
| [selectCamera()](#selectcamera) | Chooses a camera as the video source. |
| [getSelectedCamera()](#getselectedcamera) | Returns information about the selected / current camera. |
| [open()](#open) | Turns on the camera to start streaming live video. |
| [close()](#close) | Stops video streaming and releases the camera. |
| [isOpen()](#isopen) | Returns whether the selected camera is turned on / occupied. |
| [pause()](#pause) | Pauses video streaming without releasing the camera. |
| [resume()](#resume) | Resumes video streaming. |
| [setResolution()](#setresolution) | Sets the resolution of the current video input. |
| [getResolution()](#getresolution) | Returns the resolution of the current video input. |

### Advanced Control

| API Name | Description |
|---|---|
| [setFrameRate()](#setframerate) | Adjusts the frame rate. |
| [getFrameRate()](#getframerate) | Returns the real-time frame rate. |
| [turnOnTorch()](#turnontorch) | Turns on the torch/flashlight. |
| [turnOffTorch()](#turnofftorch) | Turns off the torch/flashlight. |
| [setZoom()](#setzoom) | Sets the zoom level of the video. |
| [setFocus()](#setfocus) | Sets the focus mode and focus distance of the camera. |
| [getFocus()](#getfocus) | Gets the focus mode and focus distance of the camera. |
| [getCapabilities()](#getcapabilities) | Inspects and returns the capabilities of the selected camera. |
| [setColorTemperature()](#setcolortemperature) | Adjusts the color temperature of the selected camera. |
| [setExposureCompensation()](#setexposurecompensation) | Sets the exposure compensation index of the selected camera. |

<!--| [getCameraSettings()](#getcamerasettings) | Returns the current values for each constrainable property of the selected camera. |-->

## getAllCameras

Returns infomation of all available cameras on the device.

```typescript
getAllCameras(): Promise<VideoDeviceInfo[]>
```

**Parameters**

None.

**Return value**

A promise resolving to an array of `VideoDeviceInfo` objects.

**Code Snippet**

```js
let cameras = await enhancer.getAllCameras();
if (cameras.length) {
    await enhancer.selectCamera(cameras[0]);
}
```

**See also**

* [VideoDeviceInfo](interface/videodeviceinfo.md)

## selectCamera

Chooses a camera as the video source.

```typescript
selectCamera(cameraObjectOrDeviceID: videodeviceinfo | string): Promise<PlayCallbackInfo>
```

**Parameters**

`cameraObjectOrDeviceID` : specifies the camera.

**Return value**

A promise resolving to a `PlayCallbackInfo` object.

**Code Snippet**

```js
let cameras = await enhancer.getAllCameras();
if (cameras.length) {
    await enhancer.selectCamera(cameras[0]);
}
```

**See also**

* [PlayCallbackInfo](interface/playcallbackinfo.md)

## getSelectedCamera

Returns information about the selected / current camera.

```typescript
getSelectedCamera(): Promise<VideoDeviceInfo | null>
```

**Parameters**

None.

**Return value**

A promise resolving to a `VideoDeviceInfo` object.

**Code Snippet**

```js
let camera = await enhancer.getSelectedCamera();
```

**See also**

* [VideoDeviceInfo](interface/videodeviceinfo.md)

## open

Turns on the camera to start streaming live video.

```typescript
open(appendOrShowUI?: boolean): void
```

**Parameters**

`appendOrShowUI` : this parameter specifies how to handle the UI. When set to true, if the UI doesn't exist in the DOM tree, the CameraEnhancer instance will append it in the DOM and show it; if the UI already exists in the DOM tree but is hidden, it'll be displayed. When not set or set to false, it means not to change the original state of that UI: if it doesn't exist in the DOM tree, nothing shows up on the page; if it exists in the DOM tree, it may or may not show up depending on its original state.

**Return value**

None.

## close

Stops video streaming and releases the camera.

```typescript
close(hideUI?: boolean): void
```

**Parameters**

`hideUI` : this parameter specifies how to handle the UI. When set to true, if the UI doesn't exist in the DOM tree or it exists but is hidden, nothing is done; if the UI already exists in the DOM tree and is shown, it'll be hidden. When not set or set to false, it means not to change the original state of that UI: if it doesn't exist in the DOM tree, nothing happens; if it exists in the DOM tree, it may or may not be hidden depending on its original state.

**Return value**

None.

## isOpen

Returns whether the selected camera is turned on / occupied.

```typescript
isOpen(): boolean
```

**Parameters**

None.

**Return value**

`true` means the camera is turned on and `false` the opposite.

## onPlayed

Defines a callback which is triggered when the video streaming first starts or restarts when its source (camera) or resolution changes.

```typescript
onPlayed: (playCallBackInfo:PlayCallBackInfo) => {}
```

**Arguments**

playCallBackInfo: returns the resolution of the video input.

**Code Snippet**

```js
let pEnhancer = null;
(async () => {
    let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
    enhancer.onPlayed = playCallBackInfo => {
        console.log(playCallBackInfo.width);
    };
    await enhancer.open();
})();
```

**See also**

* [PlayCallbackInfo](interface/playcallbackinfo.md)

## pause

Pauses video streaming without releasing the camera.

```typescript
pause(): void
```

**Parameters**

None.

**Return value**

None.

## resume

Resumes video streaming.

```typescript
resume(): void
```

**Parameters**

None.

**Return value**

None.

## setResolution

Sets the resolution of the current video input. If the specified resolution is not exactly supported, the closest resolution will be applied.

```typescript
setResolution(width: number, height: number): Promise<PlayCallbackInfo>
```

**Parameters**

`width` : specifies the horizontal resolution.
`height` : specifies the vertical resolution.

**Return value**

A promise resolving to a `PlayCallbackInfo` object.

**Code Snippet**

```js
await enhancer.setResolution(width, height);
```

**See also**

* [PlayCallbackInfo](interface/playcallbackinfo.md)

## getResolution

Returns the resolution of the current video input.

```typescript
getResolution(): number[]
```

**Parameters**

None.

**Return value**

An array of two numbers representing the resolution in the sequence of [width, height].

**Code Snippet**

```js
let resolution = await enhancer.getResolution();
console.log(resolution.width + " x " + resolution.height);
```

## setFrameRate

Adjusts the frame rate.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
setFrameRate(rate: number): Promise<void>
```

**Parameters**

`rate` : specifies the new frame rate.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.setFrameRate(10);
```

**See also**

* [getCapabilities](#getcapabilities)

## getFrameRate

Returns the real-time frame rate.

```typescript
getFrameRate(): number;
```

**Parameters**

None.

**Return value**

The calculated real-time frame rate.

**Code Snippet**

```js
await enhancer.getFrameRate();
```

## turnOnTorch

Turns on the torch/flashlight.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
turnOnTorch(): Promise<void>
```

**Parameters**

None.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.turnOnTorch();
```

**See also**

* [turnOffTorch](#turnofftorch)
* [getCapabilities](#getcapabilities)

## turnOffTorch

Turns off the torch/flashlight.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
turnOffTorch(): Promise<void>
```

**Parameters**

None.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.turnOffTorch();
```

**See also**

* [turnOnTorch](#turnontorch)
* [getCapabilities](#getcapabilities)

## setZoom

Sets the focus mode and focus distance of the camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
setZoom(zoomValue: number): Promise<void>
```

**Parameters**

`zoomValue` : specifies the zoom level.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.setZoom(400);
```

**See also**

* [getCapabilities](#getcapabilities)

## setFocus

Sets the focus mode and focus distance of the camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
setFocus(mode: string, distance?: number): Promise<void>;
```

**Parameters**

`mode` : specifies the focus mode, the available values include `continuous` and `manual` .
`distance` : specifies the focus distance, only required when the `mode` is set to `manual` . Use [getCapabilities](#getcapabilities) to get the allowed value range.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.setFocus("manual", 400);
```

**See also**

* [getCapabilities](#getcapabilities)

## getFocus

Gets the focus mode and the focus distance.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
getFocus(): {mode: string, distance?: number}
```

**Parameters**

None.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.getFocus();
```

**See also**

* [getCapabilities](#getcapabilities)

## getCapabilities

Inspects and returns the capabilities of the selected camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
getCapabilities(): MediaTrackCapabilities
```

**Parameters**

None.

**Return value**

A `MediaTrackCapabilities` object which specifies the values or range of values for each constrainable property of the current camera.

**Code Snippet**

```js
enhancer.getCapabilities();
/* Result sample
{
  aspectRatio: {max: 1280, min: 0.001388888888888889},
  brightness: {max: 64, min: -64, step: 1},
  colorTemperature: {max: 6500, min: 2800, step: 10},
  contrast: {max: 95, min: 0, step: 1},
  deviceId: "3a505c29a3312600ea0afd79f8e2b4ba4fba3e539257801ff1de8718c27f2bed",
  exposureMode: ["continuous", "manual"],
  exposureTime: {max: 10000, min: 39.0625, step: 39.0625},
  facingMode: [],
  focusDistance: {max: 1024, min: 0, step: 10},
  focusMode: ["continuous", "manual"],
  frameRate: {max: 30, min: 0},
  groupId: "35a82dcb7d5b0ef5bda550718d194f04a812c976175e926ccb81fb9d235d010f",
  height: {max: 720, min: 1},
  resizeMode: ["none", "crop-and-scale"],
  saturation: {max: 100, min: 0, step: 1},
  sharpness: {max: 7, min: 1, step: 1},
  whiteBalanceMode: ["continuous", "manual"],
  width: {max: 1280, min: 1}
}
*/
```

**See also**

* [MediaTrackCapabilities](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack/getCapabilities)

## getCameraSettings

Returns the current values for each constrainable property of the selected camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
getCameraSettings(): any
```

**Parameters**

None.

**Return value**

The current values for each constrainable property of the current camera

**Code Snippet**

```js
enhancer.getCameraSettings();
/* Result sample
{
  aspectRatio: 1.3333333333333333,
  brightness: 0,
  colorTemperature: 4600,
  contrast: 0,
  deviceId: "3a505c29a3312600ea0afd79f8e2b4ba4fba3e539257801ff1de8718c27f2bed",
  exposureMode: "continuous",
  exposureTime: 156.25,
  focusDistance: 120,
  focusMode: "continuous",
  frameRate: 30,
  groupId: "35a82dcb7d5b0ef5bda550718d194f04a812c976175e926ccb81fb9d235d010f",
  height: 480,
  resizeMode: "none",
  saturation: 73,
  sharpness: 2,
  whiteBalanceMode: "continuous",
  width: 640
}
*/
```

**See also**

* [getCapabilities](#getcapabilities)

## setColorTemperature

Adjusts the color temperature of the selected camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
setColorTemperature(colorTemperatur: number): Promise<void>
```

**Parameters**

`colorTemperatur` : specifies the new color temperature.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.setColorTemperature(5000);
```

**See also**

* [getCapabilities](#getcapabilities)

## setExposureCompensation

Sets the exposure compensation index of the selected camera.

> Right now, this method only works in Chrome or other Chromium-based browsers and should be called when a camera is open.

```typescript
setExposureCompensation(exposureCompensation: number): Promise<void>
```

**Parameters**

`exposureCompensation` : specifies the new exposure compensation index.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```js
await enhancer.setExposureCompensation(-0.7);
```

**See also**

* [getCapabilities](#getcapabilities)
