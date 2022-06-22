---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DCECaptureView Class
description: This is the documentation - iOS DCECaptureView Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS DCECaptureView Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DCECaptureView Class
---

# DCECaptureView

`DCECaptureView` is the class that enable user to add elements on camera view conveniently.

```objc
@interface DCECaptureView: UIView<CALayerDelegate>
```

| Method Name | Description |
|------|------|
| [`addTorch`](#addtorch) | Add torch controlling icon |
| [`addOverlay`](#addoverlay) | Add overlay |
| [`addListener`](#addlistener) | Add view listener |
| [`removeListener`](#removelistener) | Remove view listener |

## addTorch

Add a torch controlling icon on the view.

```objc
- (void)addTorch;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, strong) DCECaptureView *dceView;
//Add a default torch icon
[_dceView addTorch];
//Or add a personalized torch icon
[_dceView addTorchWith:(nonnull UIImage *) TorchOffImg:(nonnull UIImage *) frame:(CGRect)];
```
2. 
```swift
var dceView:DCECaptureView! = nil
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

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, strong) DCECaptureView *dceView;
//Add a default overlay
[_dceView addOverlay];
//Add a personalized overlay
[_dceView addOverlay:(nonnull UIColor *) fill:(nonnull UIColor *)];
```
2. 
```swift
var dceView:DCECaptureView! = nil
//Add a default overlay
dceView.addOverlay()
//Add a personalized overlay
dceView.addOverlay(stroke: UIColor, fill: UIColor)
```

## addListener

Add view Listener.

```objc
- (void)addListener:(id<DCECaptureViewListener>)listener NS_SWIFT_NAME(addListener(_:));
```

**Parameters**

`Listener`: DCECaptureViewListener.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, strong) DCECaptureView *dceView;
[_dceView addListener:(nonnull id<DCECaptureViewListener>)];
```
2. 
```swift
var dceView:DCECaptureView! = nil
dceView.addListener(listener: DCECaptureViewListener)
```

## removeListener

Remove view listener.

```objc
- (void)removeListener;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, strong) DCECaptureView *dceView;
[_dceView removeListener];
```
2. 
```swift
var dceView:DCECaptureView! = nil
dceView.removeListener()
```
