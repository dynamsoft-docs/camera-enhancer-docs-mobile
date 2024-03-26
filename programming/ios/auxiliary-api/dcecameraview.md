---
layout: default-layout
title: DSCameraView - Dynamsoft Camera SDK API Reference
description: The class DSCameraView of Dynamsoft Camera SDK represents a camera view that displays the camera preview and provides UI controlling APIs.
keywords: camera view, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraView

The `DSCameraView` class is used to display the camera preview and provides UI controlling APIs. Users can add interactable UI elements on the view.

## Definition

*Assembly:* DynamsoftCameraSDK.xcframework

```objc
@interface DSCameraView: UIView<CALayerDelegate>
```

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSCameraView: UIView<CALayerDelegate>
```
2. 
```swift
class CameraView: UIView {}
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`torchButtonVisible`](#torchbuttonvisible) | *BOOL* | Set/get the visibility of the torch button. |
| [`scanRegionMaskVisible`](#scanregionmaskvisible) | *BOOL* | Set/get the visibility of the scan region mask. |
| [`scanLaserVisible`](#scanlaservisible) | *BOOL* | Set/get the visibility of the scan laser. |
| [`tipConfig`](#tipconfig) | *DSTipConfig* | Set/get the tip configurations. |
| [`tipVisible`](#tipvisible) | *BOOL* | Set/get the visibility of tip. |

## Methods

| Method | Description |
|------- |-------------|
| [`initWithFrame`](#initwithframe) | Create an instance of DSCameraView. |
| [`getDrawingLayer`](#getdrawinglayer) | Get the specified DrawingLayer. |
| [`createDrawingLayer`](#createdrawinglayer) | Create a new DrawingLayer. |
| [`getVisibleRegionOfVideo`](#getvisibleregionofvideo) | Get the visible region of the video streaming. |
| [`setTorchButtonWithFrame`](#settorchbuttonwithframe) | Add a torch button on your view. |
| [`deleteUserDefinedDrawingLayer`](#deleteuserdefineddrawinglayer) | Delete the specified drawing layer. |
| [`clearUserDefinedDrawingLayers`](#clearuserdefineddrawinglayers) | Clear all the user-defined drawing layers. |
| [`getAllDrawingLayers`](#getalldrawinglayers) | Get all the drawing layers on the view. |
| [`setScanRegionMaskStyle`](#setscanregionmaskstyle) | Set the style of the scan region mask. |
| [`updateTipMessage`](#updatetipmessage) | Update the tip message. |
| [`setDrawingItemClickListener`](#setdrawingitemclicklistener) | Set a [`DrawingItemClickListener`](protocol-click-listener.md) to receive callback when [`DrawingItems`](drawingitem.md) on the view are clicked. |

### torchButtonVisible

Set/get the visibility of the torch button.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) BOOL torchButtonVisible;
```
2. 
```swift
var torchButtonVisible: BOOL { get set }
```

### scanRegionMaskVisible

Set/get the visibility of the scan region mask.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign) BOOL scanRegionMaskVisible;
```
2. 
```swift
var scanRegionMaskVisible: BOOL { get set }
```

### scanLaserVisible

Set/get the visibility of the scan laser.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, assign) BOOL scanLaserVisible;
```
2. 
```swift
var scanLaserVisible: BOOL { get set }
```

### tipConfig

Set/get the tip configurations.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) DSTipConfig * tipConfig;
```
2. 
```swift
var tipConfig: DSTipConfig { get set }
```

### tipVisible

Set/get the visibility of tip.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) BOOL tipVisible;
```
2. 
```swift
var tipConfig: BOOL { get set }
```

### initWithFrame

Create an instance of DSCameraView.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithFrame:(CGRect)frame;
```
2. 
```swift
init(frame: CGRect)
```
**Parameters**

`frame`: A CGRect value that defines the position of the view.

**Return Value**

An instance of DSCameraView.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSCameraView *cameraView = [[DSCameraView alloc] initWithFrame:frame];
```
2. 
```swift
let cameraView = CameraView(frame: frame)
```

### getDrawingLayer

Get the specified DrawingLayer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (nullable DSDrawingLayer *)getDrawingLayer:(NSUInteger)layerId;
```
2. 
```swift
func getDrawingLayer(_ layerId: UInt) -> DSDrawingLayer?
```

**Parameters**

`layerId`: The ID of the layer that you want to get.

**Return Value**

The object of the targeting layer.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingLayer *drawingLayer = [cameraView getDrawingLayer:layerId];
```
2. 
```swift
let drawingLayer = cameraView.getDrawingLayer(layerId)
```

### createDrawingLayer

Create a new DrawingLayer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSDrawingLayer *)createDrawingLayer;
```
2. 
```swift
func createDrawingLayer() -> DSDrawingLayer
```
**Return Value**

The object of the layer you created.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingLayer *drawingLayer = [cameraView createDrawingLayer];
```
2. 
```swift
let drawingLayer = cameraView.createDrawingLayer()
```

### getVisibleRegionOfVideo

Get the visible region of the video streaming.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSRect *)getVisibleRegionOfVideo;
```
2. 
```swift
func getVisibleRegionOfVideo() -> DSRect
```
**Return Value**

A [`DSRect`]({{ site.dcv_ios_api }}core/basic-structures/rect.html) object (measuredInPercentage = true) that defines the visible region of the video.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSRect *visibleRegion = [cameraView getVisibleRegionOfVideo];
```
2. 
```swift
let visibleRegion = cameraView.getVisibleRegionOfVideo()
```

### setTorchButtonWithFrame

Add a torch button on your view. If you are using enhanced feature - smart torch, the style of this torch button will be applied to the smart torch as well.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setTorchButtonWithFrame:(CGRect)frame
                   torchOnImage:(UIImage* _Nullable)torchOnImage
                  torchOffImage:(UIImage* _Nullable)torchOffImage
NS_SWIFT_NAME(setTorchButton(frame:torchOnImage:torchOffImage:));
```
2. 
```swift
func setTorchButton(_ frame: CGRect, torchOnImage: UIImage, torchOffImage: UIImage)
```

**Parameters**

`frame`: The place that you want to locate the torch button.  
`torchOnImage`: The torch button image that you want to display when the torch is on.  
`torchOffImage`: The torch button image that you want to display when the torch is off.  

### deleteUserDefinedDrawingLayer

Delete the specified drawing layer.

**Parameters**

`frame`: The ID of the layer that you want to delete.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)deleteUserDefinedDrawingLayer:(NSUInteger)layerId;
```
2. 
```swift
func deleteUserDefinedDrawingLayer(_ layerId:UInt)
```

### clearUserDefinedDrawingLayers

Clear all the user-defined drawing layers.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)clearUserDefinedDrawingLayers;
```
2. 
```swift
func deleteUserDefinedDrawingLayer()
```

### getAllDrawingLayers

Get all the drawing layers on the view.

**Return Value**

All the drawing layers. The return value includes both system drawing layers and user defined drawing layers.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSArray<DSDrawingLayer *>*)getAllDrawingLayers;
```
2. 
```swift
func getAllDrawingLayers() -> [DrawingLayer]
```

### setScanRegionMaskStyle

Set the style of the scan region mask.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setScanRegionMaskStyle:(UIColor)strokeColour
                   strokeWidth:(CGFloat)strokeWidth
             surroundingColour:(UIColor)surroundingColour;
```
2. 
```swift
func setScanRegionMaskStyle(_ strokeColour: UIColor, strokeWidth: CGFloat, surroundingColour: UIColor)
```

**Parameters**

`strokeColour` The stroke colour of the scan region box.  
`strokeWidth` The width of the stroke.  
`surroundingColour` The colour of the mask around the scan region.  

### updateTipMessage

Update the tip message. The new tip message will be immediately displayed on the view. Generally, tip messages are uploaded internally.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)updateTipMessage:(NSString*)message;
```
2. 
```swift
func updateTipMessage(_ message: String)
```

**Parameters**

`tipMessage` The new message that you want to display.

### setDrawingItemClickListener

Set a [`DrawingItemClickListener`](protocol-click-listener.md) to receive callback when [`DrawingItems`](drawingitem.md) on the view are clicked.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setDrawingItemClickListener:(nullable id<DSDrawingItemClickListener>)clickListener;
```
2. 
```swift
func setDrawingItemClickListener(_ clickListener: DrawingItemClickListener?)
```

**Parameters**

`clickListener`: A protocol instance of [`DrawingItemClickListener`](protocol-click-listener.md).
