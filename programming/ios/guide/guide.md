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
- (void)configuration{
  _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
  [self.view.addSubView:_dceView];
  // The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here will grant you a public trial license good for 7 days. After that, please visit: https://www.dynamsoft.com/customer/license/trialLicense?product=dce&utm_source=installer&package=ios to request for 30 days extension.
  [DynamsoftCameraEnhancer initLicense:@"DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" verificationDelegate:self];
  _dce = [[DynamsoftCameraEnhancer alloc] initWithView:_dceView];
  [_dce open];
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
  self.addbutton()
}
```

Now, DCE and CameraView instance are created. You can control the and add elements on the view via DCE high-level APIs.

### Capture Frame(s)

Dynamsoft Camera Enhancer provides 2 solutions for you to get the frames from the video streaming. `FrameOutputCallback` is a callback method in `DCEFrameListener`, from which you can get continuous video frames that captured by the camera. In addition, there is a method `getFrameFromBuffer` for you to get a single frame from the video buffer when the method is triggered.

On this page, you will be guide on how to use the `getFrameFromBuffer` to acquire a single frame and save it as an image when using Dynamsoft Camera Enhancer.

1. Add a button on the UI to trigger the image capture.

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

2. Fetch the frames and convert them to visible images.

Objective-C:

```objc
- (void)takePictures{
  [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleOrientationDidChange) name:UIDeviceOrientationDidChangeNotification object:nil];
  /*Get Frame*/
  DCEFrame *dceframe = [_dce getFrameFromBuffer:false];
  UIImage *image = dceframe.toUIImage;
}
```

Swift:

```swift
@objc func takePictures() {
  NotificationCenter.default.addObserver(self, selector: #selector(handleOrientationDidChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)
  /*Get Frame*/
  let dceframe:DCEFrame = dce.getFrameFromBuffer(false)
  image = dceframe.toUIImage()
}
```

3. Display the image on the view and add an additional button.

Objective-C:

```objc
- (void)takePictures{
  /*
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleOrientationDidChange) name:UIDeviceOrientationDidChangeNotification object:nil];
    [photoButton setEnabled:false];
    
    DCEFrame *dceframe = [_dce getFrameFromBuffer:false];
    UIImage *image = dceframe.toUIImage;
  */

  CGFloat w = [[UIScreen mainScreen] bounds].size.width;
  CGFloat h = [[UIScreen mainScreen] bounds].size.height;
  resImageview = [[UIImageView alloc] initWithFrame:CGRectMake(0, 0, w, h)];    
  [resImageview setImage:image];
  [self.view addSubview:resImageview];
  [self addBack];
}

- (void)addBack{
  self.navigationItem.leftBarButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemReply target:self action:@selector(BackToHome)];
}

- (void)BackToHome{
  [resImageview removeFromSuperview];
  self.navigationItem.leftBarButtonItem = nil;
  [photoButton setEnabled:true];
}
```

Swift:

```swift
@objc func takePictures() {
  /*
  NotificationCenter.default.addObserver(self, selector: #selector(handleOrientationDidChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)
  self.photoButton?.isEnabled = false
        
  let dceframe:DCEFrame = dce.getFrameFromBuffer(false)
  var image:UIImage!
  image = dceframe.toUIImage()
  */
  let w = UIScreen.main.bounds.size.width
  let h = UIScreen.main.bounds.size.height
  resImageview = UIImageView(frame: CGRect(x: 0, y: 0, width: w, height: h))       
  resImageview.image = image
  self.view.addSubview(resImageview)
  self.addBack()
}
    
func addBack(){
  self.navigationItem.leftBarButtonItem = UIBarButtonItem.init(barButtonSystemItem: .reply, target: self, action: #selector(backToHome))
}
    
@objc func backToHome(){
  self.resImageview.removeFromSuperview()
  self.photoButton?.isEnabled = true
  self.navigationItem.leftBarButtonItem = nil
}
```

Run the project. Now, you first app with Dynamsoft Camera Enhancer is completed.
