---
layout: default-layout
title: Dynamsoft Camera Enhancer - Guide on Objective-C & Swift
description: This is the documentation - Guide on Objective-C & Swift page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Guide on Objective-C & Swift
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS Guide
---

# User Guide on Objective-C & Swift

- System Requirements:
  - macOS 10.11 and above.
  - iOS 9.0 and above.
- Environment: Xcode 7.1 - 11.5 and above.
- Recommended: macOS 10.15.4+, Xcode 11.5+, iOS 11+

## Installation

1. <a href="https://www.dynamsoft.com/camera-enhancer/downloads/1000021-confirmation/" target="_blank">Download Dynamsoft Camera Enhancer</a> from Dynamsoft website to get `dce-ios-{version-number}.zip`. Unzip the package and find DynamsoftCameraEnhancer.framework.

2. Create a new Objective-C or Swift project.

3. Add DynamsoftCameraEnhancer.framework in your Xcode project.

4. Import Dynamsoft Camera Enhancer

Objective-C:

```objectivec
#import <DynamsoftCameraEnhancer/DynamsoftCameraEnhancer.h>
```

Swift:

```Swift
import DynamsoftCameraEnhancer
```

Now Dynamsoft Camera Enhancer is added to your project.

## Initialize DCE and Add the Camera View

1. Delcare the DCE & DCECameraView property.

Objective-C:

```objc
@property (nonatomic, strong) DynamsoftCameraEnhancer *dce;
@property (nonatomic, strong) DCECameraView *dceView;
```

Swift:

```swift

```

2. Initialize the DCE & DCECameraView.

Objective-C:

```objc
- (void)configuration{
    _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
    [self.view.addSubView:_dceView];
    [DynamsoftCameraEnhancer initLicense:@"DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" verificationDelegate:self];
    _dce = [[DynamsoftCameraEnhancer alloc] initWithView:_dceView];
    [_dce open];
}
```

Swift:

```swift

```

Now, DCE and CameraView instance are created. You can control the and add elements on the view via DCE high-level APIs.

## Get Video Frame(s)

Dynamsoft Camera Enhancer provides 2 solutions for you to get the frames from the video streaming. `FrameOutputCallback` is a callback method in `DCEFrameListener`, from which you can get continuous video frames that captured by the camera. In addition, there is a method `getFrameFromBuffer` for you to get a single frame from the video buffer when the method is triggered.

On this page, you will be guide on how to use the `getFrameFromBuffer` to acquire a single frame and save it as an image when using Dynamsoft Camera Enhancer.

1. Add a Capture Button:

Objective-C:

```objc

```

Swift:

```swift

```

2. Add Method for the Button

Objective-C:

```objc

```

Swift:

```swift

```
