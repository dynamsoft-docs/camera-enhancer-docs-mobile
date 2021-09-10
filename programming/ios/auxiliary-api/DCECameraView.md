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

| Method Name | Description |
| ----------- | ----------- |
| [`initWithView`](#initwithview) |  |
| [`captureWithFrame`](#capturewithframe) |  |
| [`addTorch`](#addtorch) | Add torch controlling icon |
| [`addOverlay`](#addoverlay) | Add overlay |

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

Init the DCECameraView.

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

## addTorch

Add a torch controlling icon on the view.

```objc
- (void)addTorch;
```

**Code Snippet**

Objective-C:

```objectivec
@property(nonatomic, strong) DCECameraView *dceView;
//Add a default torch icon
[_dceView addTorch];
//Or add a personalized torch icon
[_dceView addTorchWith:(nonnull UIImage *) TorchOffImg:(nonnull UIImage *) frame:(CGRect)];
```

Swift:

```swift
var dceView:DCECameraView! = nil
//Add a default torch icon
dceView.addTorch()
//Or add a personalized torch icon
dceView.addTorch(with: UIImage, torchOffImg: UIImage, frame: CGRect)
```

## addOverlay

Add overlay on the view.

```objc
- (void)addOverlay;
```

**Code Snippet**

Objective-C:

```objectivec
@property(nonatomic, strong) DCECameraView *dceView;
//Add a default overlay
[_dceView addOverlay];
//Add a personalized overlay
[_dceView addOverlay:(nonnull UIColor *) fill:(nonnull UIColor *)];
```

Swift:

```swift
var dceView:DCECameraView! = nil
//Add a default overlay
dceView.addOverlay()
//Add a personalized overlay
dceView.addOverlay(stroke: UIColor, fill: UIColor)
```
