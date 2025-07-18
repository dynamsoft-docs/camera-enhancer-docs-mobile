---
layout: default-layout
title: DSCameraEnhancer - Dynamsoft Camera Enhancer API Reference
description: The class DSCameraEnhancer of Dynamsoft Camera Enhancer defines the camera controlling APIs.
keywords: camera enhancer, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraEnhancer

The `DSCameraEnhancer` class is the primary class of Dynamsoft Camera Enhancer that defines the camera controlling APIs. It is a subclass of `DSImageSourceAdapter`.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSCameraEnhancer: DSImageSourceAdapter
```
2. 
```swift
class CameraEnhancer : ImageSourceAdapter
```

## Methods

| Method | Description |
|------- |-------------|
| [`addListener`](#addlistener) | Add a DSVideoFrameListener to receive callback when video frames are output. |
| [`removeListener`](#removelistener) | Remove a DSVideoFrameListener. |
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
| [`getCameraState`](#getcamerastate) | Tells you whether the camera is open, opening, closing, or closed - each state being represented by a member of the [CameraState]({{ site.dce-enums }}camera-state.html?lang=objc,swift) enumeration. |
| [`setCameraStateListener`](#setcamerastatelistener) | Set a DSCameraStateListener to receive callback when the camera state changed. |
| [`enableEnhancedFeatures`](#enableenhancedfeatures) | Enable the specified enhanced features. View DSEnhancedFeatures for more details. |
| [`disableEnhancedFeatures`](#disableenhancedfeatures) | Disable the specified enhanced features. View DSEnhancedFeatures for more details. |
| [`initWithView`](#initwithview) | Create an instance of DSCameraEnhancer. |
| [`init`](#init) | Create an instance of DSCameraEnhancer. |
| [`setScanRegion`](#setscanregion) | Set a scan region. The video frame is cropped based on the scan region. |
| [`getScanRegion`](#getscanregion) | Get a scan region. |
| [`open`](#open) | Open the camera. |
| [`close`](#close) | Close the camera. |
| [`setResolution`](#setresolution) | Set the resolution. If the targeting resolution is not available for your device, a closest available resolutionll be selected. |
| [`getResolution`](#getresolution) | Get the current resolution. |
| [`selectCameraWithPosition`](#selectcamerawithposition) | Select a camera with a camera position. |
| [`getFrameRate`](#getframerate) | Get the frame rate. |
| [`turnOnTorch`](#turnontorch) | Turn on the torch. |
| [`turnOffTorch`](#turnofftorch) | Turn off the torch. |
| [`setFocus`](#setfocus) | Set the focus point of interest and trigger an one-off auto-focus. |
| [`setFocus(subsequentFocusMode)`](#setfocussubsequentfocusmode) | Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode. |
| [`convertRectToViewCoordinates`](#convertrecttoviewcoordinates) | Convert the coordinates of a [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) under video coordinate system to a CGRect under camera view coordinate system. |
| [`convertPointToViewCoordinates`](#convertpointtoviewcoordinates) | Convert the coordinates of a CGPoint under video coordinate system to another CGPoint under camera view coordinate system. |
| [`getAllCameras`](#getallcameras) | Get the IDs of all available cameras. |
| [`selectCamera`](#selectcamera) | Select a camera with a camera ID. |
| [`getSelectedCamera`](#getselectedcamera) | Get the currently actived camera. |
| [`setZoomFactorChangeListener`](#setzoomfactorchangelistener) | Set a `DSZoomFactorChangeListener` to receive callback when the zoom-factor changed. |

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`imageCaptureDistanceMode`](#imagecapturedistancemode) | Set/get the capture distance property of the video frame. The capture distance property will be recorded by DSVideoFrameTag. |
| [`autoZoomRange`](#autozoomrange) | Set/get the range of auto zoom. |
| [`cameraView`](#cameraview) | Set/get the DSCameraView instance that bind with this DSCameraEnhancer instance. |

## Inherited Methods

The following methods are inherited from base class [`ImageSourceAdapter`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html)

| Method | Description |
| ------ | ----------- |
| [`startFetching`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#startfetching) | Start fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`stopFetching`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#stopfetching) | Stop fetching images from the source to the Video Buffer of ImageSourceAdapter. |
| [`getImage`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#getimage) | Get an image from the Video Buffer. |
| [`setNextImageToReturn`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#setnextimagetoreturn) | Specify the next image that is returned by method getImage. |
| [`hasImage`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#hasimage) | Check the availability of the specified image. |
| [`addImageToBuffer`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#addimagetobuffer) | Adds an image to the buffer of the adapter. |
| [`clearBuffer`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#clearbuffer) | Clears the image buffer. |
| [`setErrorListener`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#seterrorlistener) | Registers a [`ImageSourceErrorListener`]({{ site.dcv_ios_api }}core/basic-structures/image-source-error-listener.html) to be used as a callback when an error occurs in the [`ImageSourceAdapter`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html). |

## Inherited Properties

The following properties are inherited from base class [`ImageSourceAdapter`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html)

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`hasNextImageToFetch`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#hasnextimagetofetch) | *BOOL* |Determines whether there are more images left to fetch. |
| [`maxImageCount`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#maximagecount) | *NSUInteger* | The property defines the maximum capability of the Video Buffer. |
| [`bufferOverflowProtectionMode`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#bufferoverflowprotectionmode) | *DSBufferOverflowProtectionMode* | Sets a mode that determines the action to take when there is a new incoming image and the buffer is full. You can either block the Video Buffer or push out the oldest image and append a new one. |
| [`imageCount`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#imagecount) | *NSUInteger* | The property defines current image count in the Video Buffer. |
| [`bufferEmpty`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#bufferempty) | *BOOL* | The read only property indicates whether the Video Buffer is empty. |
| [`colourChannelUsageType`]({{ site.dcv_ios_api }}core/basic-structures/image-source-adapter.html#colourchannelusagetype) | *colourChannelUsageType* | The usage type of a color channel in an image. |

### addListener

Add a DSVideoFrameListener to receive callback when video frames are output.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)addListener:(nonnull id<DSVideoFrameListener>)listener NS_SWIFT_NAME(addListener(_:));
```
2. 
```swift
func addListener(_ listener: DSVideoFrameListener)
```

**Parameters**

`listener`: A delegate object of DSVideoFrameListener to receive video frame as a DSImageData.

### removeListener

Remove a DSVideoFrameListener.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)removeListener:(nonnull id<DSVideoFrameListener>)listener NS_SWIFT_NAME(removeListener(_:));
```
2. 
```swift
func removeListener(_ listener: DSVideoFrameListener)
```

**Parameters**

`listener`: A delegate object of VideoFrameListener.

### takePhoto

Take a photo.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)takePhoto:(DSPhotoListener)photoListener;
```
2. 
```swift
func takePhoto(_ photoListener: PhotoListener)
```

**Parameters**

`photolistener`: A delegate object of DSPhotoListener to receive the captured photo.

### getCameraPosition

Get the camera position.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSCameraPosition)getCameraPosition;
```
2. 
```swift
func getCameraPosition() -> CameraPosition
```

**Return Value**

The camera position.

### setZoomFactor

Set the zoom factor of the camera. You can use getCapabilities to check the maximum available zoom factor.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setZoomFactor:(CGFloat)factor;
```
2. 
```swift
func setZoomFactor(_ factor: CGFloat)
```

**Parameters**

`factor`: The zoom factor.

### getZoomFactor

Get the zoom factor of the camera.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (CGFloat)getZoomFactor;
```
2. 
```swift
func getZoomFactor() -> CGFloat
```

**Return Value**

The zoom factor.

### getFocusMode

Get the currently actived focus mode.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSFocusMode)getFocusMode;
```
2. 
```swift
func getFocusMode() -> FocusMode
```

**Return Value**

The focus mode.

### initSystemSettingsFromFile

Initialize system settings from a JSON file. The system settings contain more precise camera control parameters.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)initSystemSettingsFromFile:(NSString*)filePath error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(initSettingsFromFile(_:));
```
2. 
```swift
func initSystemSettingsFromFile(_ filePath: String) throws -> BOOL
```

**Parameters**

`filePath`: The path of the JSON file.

`error`: A NSError pointer. An error occurs when the file path is not available or the JSON datacludes invalid keys or values.

**Return Value**

A bool value that indicates whether the system settings are initialized successfully.

### initSystemSettings

Initialize system settings from a JSON string. The system settings contain more precise camera control parameters.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)initSystemSettings:(NSString*)JsonString error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(initSettings(_:));
```
2. 
```swift
func initSystemSettings(_ filePath: String) throws -> BOOL
```

**Parameters**

`JsonString`: The JSON string.

`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the system settings are initialized successfully.

### resetSystemSettings

Reset the system settings to default value.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)resetSystemSettings;
```
2. 
```swift
func resetSystemSettings()
```

### initEnhancedSettingsFromFile

Initialize enhanced settings from a JSON file. The enhanced settings contain auxiliary parameters of enhanced features.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)initEnhancedSettingsFromFile:(NSString*)filePath error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(initSettingsFromFile(_:));
```
2. 
```swift
func initEnhancedSettingsFromFile(_ filePath: String) throws -> BOOL
```

**Parameters**

`filePath`: The JSON string.

`error`: A NSError pointer. An error occurs when the file path is not available or the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the enhanced settings are initialized successfully.

### initEnhancedSettings

Initialize enhanced settings from a JSON string. The enhanced settings contain auxiliary parameters of enhanced features.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)initEnhancedSettings:(NSString*)JsonString error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(initSettings(_:));
```
2. 
```swift
func initEnhancedSettings(_ JsonString: String) throws -> BOOL
```

**Parameters**

`JsonString`: The JSON string.

`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

A bool value that indicates whether the enhanced settings are initialized successfully.

### outputEnhancedSettings

Output the enhanced settings to a JSON string. The enhanced settings contain auxiliary parameters of enhanced features.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (nullable NSString *)outputEnhancedSettings:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(outputSettings());
```
2. 
```swift
func outputEnhancedSettings() throws -> String
```

**Parameters**

`error`: A NSError pointer. An error occurs when the JSON data includes invalid keys or values.

**Return Value**

The enhanced settings in a JSON string.

### outputEnhancedSettingsToFile

Output the enhanced settings to a JSON file. The enhanced settings contain auxiliary parameters of enhanced features.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)outputEnhancedSettingsToFile:(NSString *)file error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(outputSettingsToFile(_:templateName:));
```
2. 
```swift
func outputEnhancedSettingsToFile(_ file: String) throws -> String
```

**Parameters**

`file` The path that you want to output the JSON file.

`error` A NSError pointer. An error occurs when the file path is not available.

**Return Value**

A bool value that indicates whether the enhanced settings are output successfully.

### resetEnhancedSettings

Reset the enhanced settings to default value.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)resetEnhancedSettings;
```
2. 
```swift
func resetEnhancedSettings()
```

### getCapabilities

Get the device capabilities including zoom factor, ISO, exposure time, etc.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSCapabilities *)getCapabilities;
```
2. 
```swift
func getCapabilities() -> Capabilities
```

**Return Value**

A [DSCapabilities](../auxiliary-api/capabilities.md) object.

### getCameraState

Tells you whether the camera is open, opening, closing, or closed - each state being represented by a member of the [CameraState]({{ site.dce-enums }}camera-state.html?lang=objc,swift) enumeration.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSCameraState)getCameraState;
```
2. 
```swift
func getCameraState() -> CameraState
```

**Return Value**

The camera state.

### setCameraStateListener

Set a [DSCameraStateListener](../auxiliary-api/protocol-dcecamerastatelistener.md) to receive callback when the camera state changes.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setCameraStateListener:(nullable id<DSCameraStateListener>)listener;
```
2. 
```swift
func setCameraStateListener(_ listener: CameraStateListener)
```

**Parameters**

`listener`: A delegate object of DSCameraStateListener to the camera state.

### enableEnhancedFeatures

Enable the specified enhanced features. View [DSEnhancedFeatures]({{ site.dce-enums }}enhanced-features.html?lang=objc,swift) to learn about these enhanced features. By default, these enhanced features are all disabled.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (bool)enableEnhancedFeatures:(NSInteger)enhancedFeatures;
```
2. 
```swift
func enableEnhancedFeatures(_ enhancedFeatures: Int) -> BOOL
```

**Parameters**

`enhancedFeatures`: A combined value of `DSEnhancedFeatures` which indicates a series of enhanced features.

**Return Value**

A bool value that indicates whether the enhanced features are enabled successfully.

### disableEnhancedFeatures

Disable any enhanced features that have been previously enabled. View [DSEnhancedFeatures]({{ site.dce-enums }}enhanced-features.html?lang=objc,swift) to learn about these enhanced features.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)disableEnhancedFeatures:(NSInteger)enhancedFeatures;
```
2. 
```swift
func disableEnhancedFeatures(_ enhancedFeatures: Int)
```

**Parameters**

`enhancedFeatures`: A combined value of `DSEnhancedFeatures` which indicates a series of enhanced features.

### initWithView

Create an instance of DSCameraEnhancer with a [DSCameraView](../auxiliary-api/dcecameraview.md) object.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithView:(DSCameraView *)view NS_SWIFT_NAME(init(view:));
```
2. 
```swift
init(view: CameraView)
```

**Parameters**

`view` A DSCameraView instance.

**Return Value**

An instance of DSCameraEnhancer.

### init

Create an instance of DSCameraEnhancer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)init;
```
2. 
```swift
init()
```

**Return Value**

An instance of DSCameraEnhancer.

### setScanRegion

Set a scan region. The video frame is cropped based on the scan region. To learn the full code to setting a scan region, please refer to the [scan region](../guide/scan-region.md) article.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)setScanRegion:(DSRect* _Nullable)scanRegion error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(setScanRegion(_:));
```
2. 
```swift
func setScanRegion(_ scanRegion: DSRect) -> BOOL
```

**Parameters**

`scanRegion`: A  [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) object.

`error`: A NSError pointer. An error occurs when the [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) data is invalid.

**Return Value**

A bool value that indicates whether the scan region has been successfully set or not.

### getScanRegion

Get the scan region if one has been set.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (nullable DSRect*)getScanRegion;
```
2. 
```swift
func getScanRegion() -> DSRect
```

**Return Value**

A [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) object that represent the scan region area.

### open

Open the camera.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)open;
```
2. 
```swift
func open()
```

### close

Close the camera.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)close;
```
2. 
```swift
func close()
```

### setResolution

Set the resolution. If the targeted resolution is not available for your device, the closest available resolution will be selected.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setResolution:(DSResolution)resolution;
```
2. 
```swift
func setResolution(_ resolution: Resolution)
```

**Parameters**

`resolution` One of the DSResolution value.

### getResolution

Get the current resolution.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSString*)getResolution;
```
2. 
```swift
func getResolution() -> Resolution
```

**Return Value**

The current resolution.

### selectCameraWithPosition

Select a camera with a camera position.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)selectCameraWithPosition:(DSCameraPosition)position error:(NSError * _Nullable * _Nullable)error;
```
2. 
```swift
func selectCamera(with position: CameraPosition) throws
```

**Parameters**

`position`: One of the DSCameraPosition value.

`error`: A NSError pointer. An error occurs when failed to switch the camera.

**Return Value**

A bool value that indicates whether the camera selection is successful.

### getFrameRate

Get the frame rate.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSInteger)getFrameRate;
```
2. 
```swift
func getFrameRate() -> Int
```

**Return Value**

The current frame rate.

### turnOnTorch

Turn on the torch.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)turnOnTorch;
```
2. 
```swift
func turnOnTorch()
```

### turnOffTorch

Turn off the torch.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)turnOffTorch;
```
2. 
```swift
func turnOffTorch()
```

### setFocus

Set the focus point of interest and trigger an one-off auto-focus.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setFocus:(CGPoint)focusPoint;
```
2. 
```swift
func setFocus(_ focusPoint: CGPoint)
```

**Parameters**

`focusPoint`: The focus point of interest. The coordinate base of the point is "image".

### setFocus(subsequentFocusMode)

Set the focus point of interest and trigger an one-off auto-focus. After the focus, you can either lock the focalngth or keep the continuous auto focus enabled by configuring the subsequent focus mode.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setFocus:(CGPoint)focusPoint focusMode:(DSFocusMode)subsequentFocusMode;
```
2. 
```swift
func setFocus(_ focusPoint: CGPoint, subsequentFocusMode: FocusMode)
```

**Parameters**

`focusPoint`: The focus point of interest. The coordinate base of the point is "image".

`subsequentFocusMode`: The subsequent focus mode.

### convertRectToViewCoordinates

Convert the coordinates of a [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) under video coordinate system to a CGRect under camera view coordinate system.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (CGRect)convertRectToViewCoordinates:(DSRect)videoRect;
```
2. 
```swift
func convertRectToViewCoordinates(_ videoRect: DSRect) -> CGRect
```

**Parameters**

`videoRect`: The [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) that you want to convert.

**Return Value**

A CGRect (coordinate measured in PT) converted from the [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html).

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
CGRect rect = [cameraView convertRectToViewCoordinates:videoRect];
```
2. 
```swift
let rect = cameraView.convertRectToViewCoordinates(videoRect)
```

### convertPointToViewCoordinates

Convert the coordinates of a CGPoint under video coordinate system to another CGPoint under camera view coordinate system.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (CGPoint)convertPointToViewCoordinates:(CGPoint)point;
```
2. 
```swift
func convertPointToViewCoordinates(_ point: CGPoint) -> CGPoint
```

**Parameters**

`point`: The CGPoint that you want to convert.

**Return Value**

A CGPoint (coordinate measured in PT) converted from the video CGPoint measured in PT.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
CGPoint convertedPoint = [cameraView convertPointToViewCoordinates:videoPoint];
```
2. 
```swift
let convertedPoint = cameraView.convertPointToViewCoordinates(point)
```

### imageCaptureDistanceMode

Set/get the capture distance property of the video frame. The capture distance property will be recorded by DSVideoFrameTag.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign) DSImageCaptureDistanceMode imageCaptureDistanceMode;
```
2. 
```swift
var imageCaptureDistanceMode: CGPoint { get set }
```

### autoZoomRange

Set/get the range of auto zoom.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign) UIFloatRange autoZoomRange;
```
2. 
```swift
var autoZoomRange: UIFloatRange { get set }
```

### cameraView

Set/get the DSCameraView instance that bind with this DSCameraEnhancer instance.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign) DSCameraView * cameraView;
```
2. 
```swift
var cameraView: CameraView { get set }
```

### getAllCameras

> This method is deprecated.

Get the IDs of all available cameras.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSArray<NSString*>*)getAllCameras;
```
2. 
```swift
func getAllCameras() -> [String]
```

**Return Value**

An array of camera IDs.

### selectCamera

> This method is deprecated.

Select a camera with a camera ID.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (BOOL)selectCamera:(NSString*)cameraId error:(NSError * _Nullable * _Nullable)error NS_SWIFT_NAME(selectCamera(_:));
```
2. 
```swift
func selectCamera(_ cameraId: String) -> BOOL
```

**Parameters**

`position`: One of the Camera IDs.

`error`: A NSError pointer. An error occurs when failed to switch the camera.

**Return Value**

A bool value that indicates whether the camera selection is successful.

### getSelectedCamera

> This method is deprecated.

Get the currently actived camera.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSString*)getSelectedCamera;
```
2. 
```swift
func getSelectedCamera() -> String
```

**Return Value**

The ID of the currently actived camera.

### setZoomFactorChangeListener

Set a [`DSZoomFactorChangeListener`](../auxiliary-api/protocol-zoomfactorchangelistener.md) to receive callback when the zoom-factor changed.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setZoomFactorChangeListener:(nullable id<DSZoomFactorChangeListener>)listener;
```
2. 
```swift
func setZoomFactorChangeListener(_ listener: DSZoomFactorChangeListener?)
```

**Parameters**

`listener`: A delegate object of [`DSZoomFactorChangeListener`](../auxiliary-api/protocol-zoomfactorchangelistener.md) to receive zoom-factor changed notification.
