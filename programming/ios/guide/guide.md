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

1. Add a Button to Save the Image.

Objective-C:

```objc
- (void)addbutton{
    CGFloat w = [[UIScreen mainScreen] bounds].size.width;
    CGFloat h = [[UIScreen mainScreen] bounds].size.height;
    CGFloat SafeAreaBottomHeight = [[UIApplication sharedApplication] statusBarFrame].size.height > 20 ? 34 : 0;
    photoButton = [[UIButton alloc] initWithFrame:CGRectMake(w / 2 - 60, h - 170 - SafeAreaBottomHeight, 120, 120)];
    photoButton.adjustsImageWhenDisabled = NO;
    [photoButton setImage:[UIImage imageNamed:@"icon_capture"] forState:UIControlStateNormal];
    [photoButton addTarget:self action:@selector(takePictures) forControlEvents:UIControlEventTouchUpInside];
    dispatch_async(dispatch_get_main_queue(), ^{
        [self.view addSubview:self->photoButton];
    });
}
```

Swift:

```swift
func addbutton() {
  let w = UIScreen.main.bounds.size.width
  let h = UIScreen.main.bounds.size.height
  let safeAreaBottomHeight:CGFloat = UIApplication.shared.statusBarFrame.size.height > 20 ? 34 : 0
  photoButton = UIButton(frame: CGRect(x:w / 2 - 60, y: h - 170 - safeAreaBottomHeight, width: 120, height: 120))
  photoButton.adjustsImageWhenDisabled = false
  photoButton.setImage(UIImage(named: "icon_capture"), for: .normal)
  photoButton.addTarget(self, action: #selector(takePictures), for: .touchUpInside)
  DispatchQueue.main.async {
    self.view.addSubview(self.photoButton)
  }
}
```

2. Add Code to Fetch and Save the Frame.

Objective-C:

```objc
- (void)takePictures{
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleOrientationDidChange) name:UIDeviceOrientationDidChangeNotification object:nil];
    /*Get Frame*/
    DCEFrame *dceframe = [_dce getFrameFromBuffer:false];
}
```

Swift:

```swift
@objc func takePictures() {
  NotificationCenter.default.addObserver(self, selector: #selector(handleOrientationDidChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)
  /*Get Frame*/
  let dceframe:DCEFrame = dce.getFrameFromBuffer(false)
}
```

3. Add Code to Convert the Frame to visible image.

Objective-C:

```objc

```

Swift:

```swift
/*
@objc func takePictures() {
  NotificationCenter.default.addObserver(self, selector: #selector(handleOrientationDidChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)

  let dceframe:DCEFrame = dce.getFrameFromBuffer(false)
  var image:UIImage!
*/
  image = dceframe.toUIImage()
/*
}
*/
```

4. Display the Saved Image on the View

Objective-C:

```objc

```

Swift:

```swift

```
