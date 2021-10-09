---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DCECameraView Class
description: This is the documentation - iOS DCECameraView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS DCECameraView Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DCECameraView Class
---

# DCECameraView

`DCECameraView` is the class that enables users to add elements on camera view conveniently.

```objc
@interface DCECameraView: UIView<CALayerDelegate>
```

| Method/Property Name | Description |
| ----------- | ----------- |
| [`initWithView`](#initwithview) | Init the `DCECameraView`. |
| [`captureWithFrame`](#capturewithframe) | Init the `DCECameraView` with a static method. |
| [`overlayVisible`](#overlayvisible) | The property stores the BOOL value that controls the visibility of the overlays. |
| [`setOverlayColour`](#setoverlaycolour) | Set the stroke and fill in colour of the overlay(s). |
| [`viewfinderVisible`](#setoverlaycolour) | The property stores the BOOL value that controls the visibility of the viewfinder. |
| [`setViewfinder`](#setoverlaycolour) | Set the attribute of the viewfinder. Currently only available for position and size setting. |

## initWithView

Init the DCECameraView.

```objc
- (instancetype)initWithView:(CGRect)frame;
```

**Code Snippet**

Objective-C:

```objc
_dceView = [[DCECameraView alloc] initWithView:<#(CGRect)#>]
```

Swift:

```swift
dceView = DCECameraView.init(view: self.view.bounds)
```

## captureWithFrame

Statically init the DCECameraView.

```objc
+ (instancetype)captureWithFrame:(CGRect)frame NS_SWIFT_NAME(init(frame:));
```

**Code Snippet**

Objective-C:

```objc
_dceView = [DCECameraView captureWithFrame:self.view.bounds];
```

Swift:

```swift
dceView = DCECameraView.init(frame:self.view.bounds)
```

## overlayVisible

The property stores the BOOL value that controls the visibility of the overlays.

```objc
BOOL overlayVisible
```

**Remarks**

If the property value is `true`, the `cameraView` will try to draw and display overlays on the interest areas. Otherwise, the `cameraView` will not draw overlays.

## setOverlayColour

Set the stroke and fill in colour of the overlay(s).

```objc
- (void)setOverlayColour:(UIColor*)stroke fill:(UIColor*)fill;
```

**Parameters**

`stroke`: The stroke colour of the overlay.  
`fill`: The fill in colour of the overlay.

## viewfinderVisible

The property stores the BOOL value that controls the visibility of the viewfinder.

```objc
BOOL viewfinderVisible
```

**Remarks**

If the property value is `true`, the `cameraView` will try to create and display a viewfinder. Otherwise, the `cameraView` will not create the viewfinder.

## setViewfinder

Set the attribute of the viewfinder. Currently only available for position and size setting.

```objc
- (void)setViewfinder:(CGFloat)left top:(CGFloat)top right:(CGFloat)right bottom:(CGFloat)bottom;
```

**Parameters**

`left`: The distance (by percentage) between the left border of the viewfinder and the left side of the screen. The default value is 0.15.  
`top`: The distance (by percentage) between the top border of the viewfinder and the top side of the screen. The default value is 0.3.  
`right`: The distance (by percentage) between the right border of the viewfinder and the left side of the screen. The default value is 0.85.  
`bottom`: The distance (by percentage) between the bottom border of the viewfinder and the top side of the screen. The default value is 0.7.

**Remarks**

The viewfinder is built based on the screen coordinate system. The origin of the coordinate is the left-top point of the mobile device. The `left border` of the viewfinder always means the closest border that parallels to the left side of the mobile device no matter how the mobile device is rotated.
