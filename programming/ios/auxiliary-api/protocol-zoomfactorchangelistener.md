---
layout: default-layout
title: DSZoomFactorChangeListener - DynamsoftCameraEnhancer iOS Edition API Reference
description: The protocol DSZoomFactorChangeListener of DynamsoftCameraEnhancer defines the methods for monitoring the change of the zoom-factor.
keywords: photo listener, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSZoomFactorChangeListener

The `DSZoomFactorChangeListener` protocol defines the methods for monitoring the change of the zoom-factor.

## Definition

*Assembly:* DynamsoftCameraEnhancer
.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSZoomFactorChangeListener <NSObject>
```
2. 
```swift
protocol ZoomFactorChangeListener : NSObjectProtocol
```

## Methods

| Method | Description |
|------- |-------------|
| [`onZoomFactorChanged`](#onzoomfactorchanged) | The method for monitoring the change of the zoom-factor. |

### onZoomFactorChanged

The method for monitoring the change of the zoom-factor.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onZoomFactorChanged:(CGFloat)currentZoomFactor;
```
2. 
```swift
func onZoomFactorChanged(currentZoomFactor: CGFloat)
```

**Parameters**

`currentZoomFactor`: The current zoom-factor.
