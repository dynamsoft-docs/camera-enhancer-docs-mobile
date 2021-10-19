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

If you don’t have SDK yet, please download Dynamsoft Camera Enhancer (DCE) SDK from<a href="https://www.dynamsoft.com/camera-enhancer/downloads/1000021-confirmation/" target="_blank">Dynamsoft website</a> and unzip the package. After decompression, the root directory of the DCE installation package is `DynamsoftCameraEnhancer`, which is represented by `INSTALLATION FOLDER`.

## Build Your First Application with Dynamsoft Camera Enhancer

The following sample will demonstrate how to acquire a frame from video streaming by DCE.

> Note:
> - You can download the similar complete source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/master/android/HelloWorld).
> - For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/master/android/).

### Create a New Project and Include Dynamsoft Camera Enhancer

1. Create a new Objective-C or Swift project.

2. Drag and drop the `DynamsoftCameraEnhancer.framework` into your Xcode project. Make sure to `check Copy items if needed` and `Create groups` to copy the framework into your project’s folder.

3. Click on the project. Go to the `General --> Frameworks --> Libraries and Embedded Content`. Set the `embed type` to `Embed & Sign`.

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

### Initialize the Camera View and Control the Camera

1. Delcare the DCE & DCECameraView property.

Objective-C:

```objc
@property (nonatomic, strong) DynamsoftCameraEnhancer *dce;
@property (nonatomic, strong) DCECameraView *dceView;
```

Swift:

```swift
var dce:DynamsoftCameraEnhancer! = nil
var dceView:DCECameraView! = nil
```

2. Initialize the DCE & DCECameraView in a method.

Objective-C:

```objc
- (void)configurationDCE{
  _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
  [self.view.addSubView:_dceView];
  /*The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here will grant you a public trial license good for 7 days. After that, please visit: https://www.dynamsoft.com/customer/license/trialLicense?product=dce&utm_source=installer&package=ios to request for 30 days extension.*/
  [DynamsoftCameraEnhancer initLicense:@"DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" verificationDelegate:self];
  _dce = [[DynamsoftCameraEnhancer alloc] initWithView:_dceView];
  [_dce open];
  [_dce addListener:self];
  [_dce setFrameRate:30];
}
```

Swift:

```swift
func configurationDCE() {
  dceView = DCECameraView.init(frame: self.view.bounds)
  self.view.addSubview(dceView)
  // The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here will grant you a public trial license good for 7 days. After that, please visit: https://www.dynamsoft.com/customer/license/trialLicense?product=dce&utm_source=installer&package=ios to request for 30 days extension.
  DynamsoftCameraEnhancer.initLicense("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9", verificationDelegate: self)
  dce = DynamsoftCameraEnhancer.init(view: dceView)
  dce.open()
  dce.setFrameRate(30)
  dce.addListener(self)
}
```

Now, DCE and CameraView instance are created. You can control the and add elements on the view via DCE high-level APIs.

### Capture Frame(s)

Dynamsoft Camera Enhancer provides two solutions on fetching the video frames:

- Use the method [`getFrameFromBuffer`]({{site.ios-api}}index.html#getframefrombuffer) to fetch a single frame from the video buffer.
- Use callback method [`FrameOutputCallback`]({{ site.ios-api-auxiliary }}protocol-dceframelistener.html) to continuously fetching the video frames.

On this page, you will be guide on how to get a raw frame from the video streaming and convert it into a visible image so that you can display it on the UI.

1. Add a capture button on the UI.

Objective-C:

```objc
- (void)configurationUI{
  CGFloat w = [[UIScreen mainScreen] bounds].size.width;
  CGFloat h = [[UIScreen mainScreen] bounds].size.height;
  CGFloat SafeAreaBottomHeight = [[UIApplication sharedApplication] statusBarFrame].size.height > 20 ? 34 : 0;
  photoButton = [[UIButton alloc] initWithFrame:CGRectMake(w / 2 - 60, h - 170 - SafeAreaBottomHeight, 120, 120)];
  photoButton.adjustsImageWhenDisabled = NO;
  [photoButton setImage:[UIImage imageNamed:@"icon_capture"] forState:UIControlStateNormal];
  self->imageView = [[UIImageView alloc] initWithFrame:CGRectMake(0, 0, w, h)];
  [photoButton addTarget:self action:@selector(takePictures) forControlEvents:UIControlEventTouchUpInside];
  dispatch_async(dispatch_get_main_queue(), ^{
    [self.view addSubview:self->photoButton];
  });
}
```

Swift:

```swift
func configurationUI() {
  let w = UIScreen.main.bounds.size.width
  let h = UIScreen.main.bounds.size.height
  let safeAreaBottomHeight:CGFloat = UIApplication.shared.statusBarFrame.size.height > 20 ? 34 : 0
  photoButton = UIButton(frame: CGRect(x:w / 2 - 60, y: h - 170 - safeAreaBottomHeight, width: 120, height: 120))
  photoButton.adjustsImageWhenDisabled = false
  photoButton.setImage(UIImage(named: "icon_capture"), for: .normal)
  self.imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: w, height: h))
  photoButton.addTarget(self, action: #selector(takePictures), for: .touchUpInside)
  DispatchQueue.main.async {
    self.view.addSubview(self.photoButton)
  }
}
```

2. Add the trigger of the capture button.

Objective-C:

```objc
/*Declare a BOOL value to control the capture*/
bool isview;
/*Add a method to trigger the capture*/
- (void)takePictures{
  isview = true;
}
```

Swift:

```swift
/*Declare a BOOL value to control the capture*/
var isview:Bool = false
/*Add a method to trigger the capture*/
func takePictures() {
  isview = true;
}
```

3. Fetch the frames from the callback. Convert the frame to a visible image and display it on the view if the capture button is triggered.

Objective-C:

```objc
- (void)frameOutPutCallback:(nonnull DCEFrame *)frame timeStamp:(NSTimeInterval)timeStamp {
  if (isview) {
    isview = false;
    dispatch_async(dispatch_get_main_queue(), ^{
      [self->photoButton setEnabled:false];
      UIImage *image = [[UIImage alloc] initWithCGImage: frame.toUIImage.CGImage
                                                  scale: 1.0
                                            orientation: UIImageOrientationRight];
      [self->imageView setImage:image];
      [self.view addSubview:self->imageView];
      [self addBack];
    });
  }
}
```

Swift:

```swift
func frameOutPutCallback(_ frame: DCEFrame, timeStamp: TimeInterval) {
  if isview {
    isview = false
    DispatchQueue.main.async {
      self.photoButton?.isEnabled = false
      var image:UIImage!
      image = frame.toUIImage()
      image = UIImage.init(cgImage: image.cgImage!, scale: 1.0, orientation: UIImageOrientation.right)
      self.imageView.image = image
      self.view.addSubview(self.imageView)
      self.addBack()
    }
  }
}
```

4. Configure a BackToHome button.

Objective-C:

```objc
- (void)addBack{
  self.navigationItem.leftBarButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemReply target:self action:@selector(BackToHome)];
}

- (void)BackToHome{
  [imageView removeFromSuperview];
  self.navigationItem.leftBarButtonItem = nil;
  [photoButton setEnabled:true];
}
```

Swift:

```swift
func addBack(){
  self.navigationItem.leftBarButtonItem = UIBarButtonItem.init(barButtonSystemItem: .reply, target: self, action: #selector(backToHome))
}
    
@objc func backToHome(){
  self.imageView.removeFromSuperview()
  self.photoButton?.isEnabled = true
  self.navigationItem.leftBarButtonItem = nil
}
```

Run the project. Now, you first app with Dynamsoft Camera Enhancer is completed.

## What's Next?

### How to integration with barcode reader

<a href="https://www.dynamsoft.com/barcode-reader/programming/objectivec-swift/user-guide.html?utm_source=docs" target="_blank">This article</a> guides you to integrate the barcode reader function into your app.
