---
layout: default-layout
title: Guide on iOS - Dynamsoft Camera Enhancer
description: This is the documentation - Guide on Objective-C & Swift page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Guide on Objective-C & Swift
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS Guide
permalink: /programming/ios/guide/guide.html
---

# User Guide on iOS

The Dynamsoft Camera Enhancer iOS SDK enables you to easily control cameras from your iOS applications to stream live video and acquire realtime frames. 

> **Example Usage**
> 
> See how Dynamsoft Camera Enhancer helps in camera control and video recognition:
> - **Barcode scanning from video stream**: check [Dynamsoft Barcode Reader iOS User Guide](https://www.dynamsoft.com/barcode-reader/docs/mobile/programming/objectivec-swift/user-guide.html?ver=latest)

Step-by-step guide on how to integrate Dynamsoft Camera Enhancer SDK to your iOS app:

## App Prerequisites

- System Requirements:
  - macOS 10.11 and above.
  - iOS 9.0 and above.
- Environment: Xcode 7.1 - 11.5 and above.
- Recommended: macOS 10.15.4+, Xcode 11.5+, iOS 11+

## Installation

If you don't have SDK yet, please download Dynamsoft Camera Enhancer (DCE) SDK from <a href="https://www.dynamsoft.com/camera-enhancer/downloads/1000021-confirmation/" target="_blank">Dynamsoft website</a> and unzip the package. After decompression, the root directory of the DCE installation package is `DynamsoftCameraEnhancer`, which is represented by `INSTALLATION FOLDER`.

## Build Your First Application with Dynamsoft Camera Enhancer

The following sample will demonstrate how to acquire a frame from video streaming by DCE.

> Note:
> - You can download the similar complete Objective-C source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/ios/HelloWorldObjc).
> - You can download the similar complete Swift source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/ios/HelloWorldSwift).
> - For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/ios/).

### Create a New Project and Include Dynamsoft Camera Enhancer

1. Create a new Objective-C or Swift project.

2. Drag and drop the **DynamsoftCameraEnhancer.xcframework** into your Xcode project. Make sure to **check Copy items if needed** and **Create groups** to copy the framework into your project's folder.

3. Click on the project. Go to the **General --> Frameworks --> Libraries and Embedded Content**. Set the **Embed type** to **Embed & Sign**.

4. Go to the **Build Settings --> Build Options --> Validate Workspace**. Set the **Validate Workspace** to **yes**.

5. In the `ViewController.m` or `ViewController.swift` Import Dynamsoft Camera Enhancer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
#import <DynamsoftCameraEnhancer/DynamsoftCameraEnhancer.h>
```
2. 
```swift
import DynamsoftCameraEnhancer
```

Now Dynamsoft Camera Enhancer is added to your project.

&nbsp;

### License Activation (Optional)

A valid license is required when using the following features:

- Frame Sharpness Filter
- Sensor Filter
- Auto Zoom
- Enhanced Focus
- Fast Mode
- Smart torch

The above features are enabled by triggering method [`enableFeatures`](../primary-api/camera-enhancer.md#enablefeatures). If you are not using these features, you can skip the license activation step.

To activate the license:

1. Add **DynamsoftLicense.xcframework** to your project and include `DynamsoftLicense` in your `AppDelegate`

   <div class="sample-code-prefix"></div>
   >- Objective-C
   >- Swift
   >
   >1. 
   ```objc
   #import <DynamsoftLicense/DynamsoftLicense.h>
   ```
   2. 
   ```swift
   import DynamsoftLicense
   ```

2. Initialize the license in your code.

   <div class="sample-code-prefix"></div>
   >- Objective-C
   >- Swift
   >
   >1. 
   ```objc
   @interface AppDelegate ()<DBRLicenseVerificationListener>
   ...
   - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      [DSLicenseManager initLicense:@"DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" verificationDelegate:self];
      ...
   }
   - (void)onLicenseVerified:(BOOL)isSuccess error:(NSError *)error {
       [self verificationCallback:error];
   }
   ```
   2. 
   ```swift
   class AppDelegate: UIResponder, UIApplicationDelegate, DBRLicenseVerificationListener {
      ...
      func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
             ...
             LicenseManager.initLicense("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9", verificationDelegate: self)
             ...
      }
      func onLicenseVerified(_ isSuccess: Bool, error: Error?) {
             if !isSuccess {
                if let error = error {
                       print("\(error.localizedDescription)")
                }
             }
      }
   }
   ```

### Initialize the Camera View and Control the Camera

In this section, we continue working on the `ViewController` file in the project. You will learn how to create a simple camera app.

#### Step 1.1

Delcare the DCE & DCECameraView property.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface ViewController ()<DSVideoFrameListener>
@property (nonatomic, strong) DSCameraView *cameraView;
@property (nonatomic, strong) DSCameraEnhancer *dce;
@end
```
2. 
```swift
var cameraView:CameraView!
let dce:CameraEnhancer = .init()
```

#### Step 1.2

Initialize the DCE & DCECameraView in a method.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)setUpCamera {
   self.cameraView = [[DSCameraView alloc] initWithFrame:self.view.bounds];
   self.cameraView.autoresizingMask = UIViewAutoresizingFlexibleWidth |UIViewAutoresizingFlexibleHeight;
   [self.view insertSubview:self.cameraView atIndex:0];
   self.dce = [[DSCameraEnhancer alloc] init];
   self.dce.cameraView = self.cameraView;
   [self.dce addListener:self];
}
```
2. 
```swift
func setUpCamera() {
   cameraView = .init(frame: view.bounds)
   cameraView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
   view.insertSubview(cameraView, at: 0)
   dce.cameraView = cameraView
   dce.addListener(self)
}
```

Add the `setUpCamera` to the `viewDidLoad` method and open the camera when the view appear.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)viewDidLoad {
   [super viewDidLoad];
   // Do any additional setup after loading the view.
   [self setUpCamera];
}
- (void)viewWillAppear:(BOOL)animated {
   [super viewWillAppear:animated];
   [self.dce open];
}
```
2. 
```swift
override func viewDidLoad() {
   super.viewDidLoad()
   // Do any additional setup after loading the view.
   setUpCamera()
}
override func viewWillAppear(_ animated: Bool) {
   super.viewWillAppear(animated)
   dce.open()
}
```

#### Step 1.3

Go to the file **info.plist** under your project folder. Under **Information Property List**, add **Privacy - Camera Usage Description**.

Build the app. Now, a simple camera app is created. After permitting the camera usage, you will see the camera view on the app.

&nbsp;

### Capture Frames From the Video Streaming

In this section, you will learn how to capture video frames with `DynamsoftCameraEnhancer`.

Dynamsoft Camera Enhancer provides two solutions for fetching the video frames:

- Use the method [`getFrameFromBuffer`]({{site.ios-api}}camera-enhancer.html#getframefrombuffer) to fetch a single frame from the video buffer.
- Use callback method [`FrameOutputCallback`]({{ site.ios-api-auxiliary }}protocol-dceframelistener.html) to continuously fetching the video frames.

> Note:
> - All the following code will be added to the `ViewController` file in your project.

#### Step 2.1

Add `DCEFrameListener` to your `ViewController` so that you can use `FrameOutputCallback` to get video frames.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface ViewController ()<DSVideoFrameListener>
```
2. 
```swift
class ViewController: UIViewController,VideoFrameListener{
   //...
}
```

Add `FrameOutputCallback` to your project to get frames from camera output. DCEFrame is the class that stores frame data. You can use Image processing tools to parse the image information from a DCEFrame object or use `DCEFrame.toUIImage` to convert it into a UIImage for other usages.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onFrameOutPut:(nonnull DSImageData *)frame {
   if (self.isClicked) {
          self.isClicked = false;
          dispatch_async(dispatch_get_main_queue(), ^{
             self.button.enabled = false;
             self.imageView.image = [frame toUIImage:nil];
             self.imageView.hidden = false;
             [self addBack];
          });
   }
}
```
2. 
```swift
func onFrameOutPut(_ frame: ImageData) {
   if isClicked {
          isClicked = false
          DispatchQueue.main.async { [self] in
             button.isEnabled = false
             imageView.image = try? frame.toUIImage()
             imageView.isHidden = false
             addBack()
          }
   }
}
```

#### Step 2.2

Add the trigger of the capture button.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@implementation ViewController{
   // Add these varibles to capture and display images.
   UIButton *photoButton;
   UIImageView* imageView;
   bool isview;
}
// The UI for displaying the captured image.
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
// Method for capturing image
- (void)takePictures{
   isview = true;
}
// The captured image will be displayed on another view. Add back button to get back to the camera.
- (void)addBack{
   self.navigationItem.leftBarButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemReply target:self action:@selector(BackToHome)];
}
- (void)BackToHome{
   [imageView removeFromSuperview];
   self.navigationItem.leftBarButtonItem = nil;
   [photoButton setEnabled:true];
}
```
2. 
```swift
// Add these varibles to capture and display images.
var photoButton:UIButton! = UIButton()
var imageView:UIImageView!
var isview:Bool = false
// The UI for displaying the captured image.
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
// Method for capturing image
@objc func takePictures() {
   isview  = true
}
// The captured image will be displayed on another view. Add back button to get back to the camera.
func addBack(){
   self.navigationItem.leftBarButtonItem = UIBarButtonItem.init(barButtonSystemItem: .reply, target: self, action: #selector(backToHome))
}
@objc func backToHome(){
   self.imageView.removeFromSuperview()
   self.photoButton?.isEnabled = true
   self.navigationItem.leftBarButtonItem = nil
}
```

Run the project. Now, you can try to capture video frames with Dynamsoft Camera Enhancer.

&nbsp;

> Note:
> - You can download the similar complete Objective-C source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/ios/HelloWorldObjc).
> - You can download the similar complete Swift source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/ios/HelloWorldSwift).
> - For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/ios/).

## What's Next?

### How to integration with barcode reader

<a href="https://www.dynamsoft.com/barcode-reader/programming/objectivec-swift/user-guide.html?utm_source=docs" target="_blank">This article</a> guides you to integrate the barcode reader function into your app.
