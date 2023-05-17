---
layout: default-layout
title: Guide on Objective-C & Swift - Dynamsoft Camera Enhancer
description: This is the documentation - Guide on Objective-C & Swift page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Guide on Objective-C & Swift
needAutoGenerateSidebar: true
noTitleIndex: true
breadcrumbText: iOS Guide
permalink: /programming/ios/guide/guide-v1.0.3.html
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

## Create a Camera Module

This section is the guide for users to create a camera module in Objective-C or Swift project. After the installation of DCE, please add the following code to the new project.

Objective-C code sample:

```objc
#import "ViewController.h"
#import <DynamsoftCameraEnhancer/DynamsoftCameraEnhancer.h>

@interface ViewController ()

@property(nonatomic, strong) DynamsoftCameraEnhancer *dce;
@property(nonatomic, strong) DCECameraView *dceView;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self configurationDCE];
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}

- (void)configurationDCE{
    _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
    [_dceView addOverlay];
    [self.view addSubview:_dceView];
    
    //Initialize License
    [DynamsoftCameraEnhancer initLicense:@"DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==" verificationDelegate:self];
    
    view:_dceView verificationDelegate:self];
    //Make camera settings, turn on the camera
    [_dce setDeiredCameraState:CAMERA_STATE_ON];
    _dce.isEnable = YES;
}

- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError *)error{
    NSLog(@"Verification: %@",error.userInfo);
}
```

Swift code sample:

```swift
import UIKit
import DynamsoftCameraEnhancer

class ViewController: UIViewController, DCELicenseVerificationDelegate, DBRTextResultDelegate {
    
    var dce:DynamsoftCameraEnhancer! = nil
    var dceView:DCECameraView! = nil
    override func viewDidLoad() {
        super.viewDidLoad()
        configurationDCE()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
    }
    
    func configurationDCE() {
        dceView = DCECameraView.init(view: self.view.bounds)
        dceView.addOverlay()
        self.view.addSubview(dceView)
        //Init DCE license
        DynamsoftCameraEnhancer.initLicense("DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==",verificationDelegate:self)
        //Turn on the camera
        dce.setDesiredCameraState(.CAMERA_STATE_ON)
        dce.isEnable = true
    }

    func DCELicenseVerificationCallback(_ isSuccess: Bool, error: Error?) {
        print("Verification: \(String(describing: error))")
    }    
}
```

## Extend the camera module with DCE functions

This section is displaying how to add DCE functions to the camera module we built just now.

For Objective-C users, please add the following code:

```objc
#import "ViewController.h"
#import <DynamsoftCameraEnhancer/DynamsoftCameraEnhancer.h>

@interface ViewController ()

@property(nonatomic, strong) DynamsoftCameraEnhancer *dce;
@property(nonatomic, strong) DCECameraView *dceView;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self configurationDCE];
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}

- (void)configurationDCE{
    _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
    [_dceView addOverlay];
    [self.view addSubview:_dceView];
    
    //Initialize License
    [DynamsoftCameraEnhancer initLicense:@"DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==" verificationDelegate:self];
    
    view:_dceView verificationDelegate:self];
    //Make camera settings, turn on the camera
    [_dce setDesiredCameraState:CAMERA_STATE_ON];
    _dce.isEnable = YES;
    
    //*********Newly added****************
    //*******Camera Settings**************
    [dce setEnableDefaultAutoFocus:true];
    [dce setEnableAutoZoom:true];
    [dce setEnableFastMode:true];
    [dce setEnableSensorControl:true];
    [dce setEnableFrameFilter:true];
}

- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError *)error{
    NSLog(@"Verification: %@",error.userInfo);
}
```

For Swift users, please add the following code:

```swift
import UIKit
import DynamsoftCameraEnhancer

class ViewController: UIViewController, DCELicenseVerificationDelegate, DBRTextResultDelegate {

    var dce:DynamsoftCameraEnhancer! = nil
    var dceView:DCECameraView! = nil
    override func viewDidLoad() {
        super.viewDidLoad()
        configurationDCE()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
    }
    
    func configurationDCE() {
        dceView = DCECameraView.init(view: self.view.bounds)
        dceView.addOverlay()
        self.view.addSubview(dceView)
        //Init DCE license
        DynamsoftCameraEnhancer.initLicense("DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==",verificationDelegate:self)
        //Turn on the camera
        dce.setDesiredCameraState(.CAMERA_STATE_ON)
        dce.isEnable = true
        //*********************Newly added**********************
        //************Add Camera Enhancer functions*************
        dce.enableFastMode = true
        dce.enableFrameFilter = true
        dce.enableDefaultAutoFocus = true
        dce.enableAutoZoom = true
        dce.enableSensorControl = true
    }

    func DCELicenseVerificationCallback(_ isSuccess: Bool, error: Error?) {
        print("Verification: \(String(describing: error))")
    }
}
```

Run the project, now DCE functions have been added to the camera module.

## Add decoder to the camera module

This section is the guide for users to add a video stream decoder to the camera module. In this section, Dynamsoft Barcode Reader (DBR) will support decoding works. Before you start, please remember to add `DynamsoftBarcodeReader.framework` to your xcode project.

Add this code snippet to the Objective-C project.

```objc
#import "ViewController.h"
#import <DynamsoftCameraEnhancer/DynamsoftCameraEnhancer.h>
//import Dynamsoft Barcode Reader for decoding
#import <DynamsoftBarcodeReader/DynamsoftBarcodeReader.h>

@interface ViewController ()
//Barcode Reader initialize
@property(nonatomic, strong) DynamsoftBarcodeReader *barcodeReader;
@property(nonatomic, strong) DynamsoftCameraEnhancer *dce;
@property(nonatomic, strong) DCECameraView *dceView;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self initDBR];
    [self configurationDCE];
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}

- (void)configurationDCE{
    _dceView = [DCECameraView cameraWithFrame:self.view.bounds];
    [_dceView addOverlay];
    [self.view addSubview:_dceView];
    
    //Initialize License
    [DynamsoftCameraEnhancer initLicense:@"DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==" verificationDelegate:self];

    //Make camera settings, turn on the camera
    [_dce setDesiredCameraState:CAMERA_STATE_ON];
    _dce.isEnable = YES;
    
    //*********Newly added****************
    //*******Camera Settings**************
    [dce setEnableDefaultAutoFocus:true];
    [dce setEnableAutoZoom:true];
    [dce setEnableFastMode:true];
    [dce setEnableSensorControl:true];
    [dce setEnableFrameFilter:true];
}

//*************Newly added Barcode Reader Settings***************
//Dynamsoft Barcode Reader (DBR) initialization
- (void)initDBR{
    iDMDLSConnectionParameters* dbrPara = [[iDMDLSConnectionParameters alloc] init];
    //Initialize DBR License
    dbrPara.organizationID = @"Put your organizationID here";
    _barcodeReader = [[DynamsoftBarcodeReader alloc] initLicenseFromDLS:dbrPara verificationDelegate:self];
    [_barcodeReader setModeArgument:@"BinarizationModes" index:0 argumentName:@"EnableFillBinaryVacancy" argumentValue:@"0" error:nil];
    [_barcodeReader setModeArgument:@"BinarizationModes" index:0 argumentName:@"BlockSizeX" argumentValue:@"81" error:nil];
    [_barcodeReader setModeArgument:@"BinarizationModes" index:0 argumentName:@"BlockSizeY" argumentValue:@"81" error:nil];
}
//****************************************************************

- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError *)error{
    NSLog(@"Verification: %@",error.userInfo);
}

//***********************Newly added********************************
//******************Display text decode result**********************
- (void)textResultCallback:(NSInteger)frameId results:(NSArray<iTextResult *> *)results userData:(NSObject *)userData{
    if (results.count > 0) {
        _dce.isEnable = NO;
        __weak ViewController *weakSelf = self;
        [self showResult:results.firstObject.barcodeText
              completion:^{
                  weakSelf.dce.isEnable = YES;
              }];
    }else{
        return;
    }
}

- (void)showResult:(NSString *)result completion:(void (^)(void))completion {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:result message:nil preferredStyle:UIAlertControllerStyleAlert];
        [alert addAction:[UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault
                                                handler:^(UIAlertAction * action) {
                                                    completion();
                                                }]];
        [self presentViewController:alert animated:YES completion:nil];
    });
}
```

For Swift users, please add the following code to the Swift project.

```swift
import UIKit
//Import Dynamsoft Barcode Reader
import DynamsoftBarcodeReader
import DynamsoftCameraEnhancer

class ViewController: UIViewController, DCELicenseVerificationDelegate, DBRTextResultDelegate {
    
    var dce:DynamsoftCameraEnhancer! = nil
    var dceView:DCECameraView! = nil
    //*********************Newly added**********************
    //************init Dynamsoft Barcode Reader*************
    var barcodeReader:DynamsoftBarcodeReader! = nil
    override func viewDidLoad() {
        super.viewDidLoad()

        //*********************Newly added**********************
        //************init Dynamsoft Barcode Reader*************
        initDBR()
        configurationDCE()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
    }
    
    //********************Newly added***********************
    //**********Initialize Dynamsoft Barcode Reader*********
    func initDBR() {
        let dls = iDMDLSConnectionParameters()
        dls.organizationID = "Put your organizationID here"
        barcodeReader = DynamsoftBarcodeReader(licenseFromDLS: dls, verificationDelegate: self)
        barcodeReader.setModeArgument("BinarizationModes", index: 0, argumentName: "EnableFillBinaryVacancy", argumentValue: "0", error: nil)
        barcodeReader.setModeArgument("BinarizationModes", index: 0, argumentName: "BlockSizeX", argumentValue: "81", error: nil)
        barcodeReader.setModeArgument("BinarizationModes", index: 0, argumentName: "BlockSizeY", argumentValue: "81", error: nil)
    }
    
    func configurationDCE() {
        dceView = DCECameraView.init(view: self.view.bounds)
        dceView.addOverlay()
        self.view.addSubview(dceView)
        //Init DCE license
        DynamsoftCameraEnhancer.initLicense("DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==",verificationDelegate:self)
        //Turn on the camera
        dce.setDesiredCameraState(.CAMERA_STATE_ON)
        dce.isEnable = true
        //*********************Newly added**********************
        //************Add Camera Enhancer functions*************
        dce.enableFastMode = true
        dce.enableFrameFilter = true
        dce.enableDefaultAutoFocus = true
        dce.enableAutoZoom = true
        dce.enableSensorControl = true
        //*********************Newly added**********************
        //Instantiate DCE, send result and immediate result call back to Dynamsoft Barcode Reader
        let para = DCESettingParameters.init()
        para.cameraInstance = dce
        para.textResultDelegate = self
        barcodeReader.setCameraEnhancerPara(para)
    }

    func DCELicenseVerificationCallback(_ isSuccess: Bool, error: Error?) {
        print("Verification: \(String(describing: error))")
    }
    
    //*********************Newly added**********************
    //******Get and display barcode decoding text result****
    func textResultCallback(_ frameId: Int, results: [iTextResult]?, userData: NSObject?) {
        if results!.count > 0 {
            dce.isEnable = false
            showResult(results!.first!.barcodeText!) { [weak self] in
                self?.dce.isEnable = true
            }
        }else{
            return
        }
    }
    
    private func showResult(_ result: String, completion: @escaping () -> Void) {
        DispatchQueue.main.async {
            let alert = UIAlertController(title: result, message: nil, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default, handler: { _ in completion() }))
            self.present(alert, animated: true, completion: nil)
        }
    }
}
```

Run the project. Now a simple decode app has been built via Dynamsoft Camera Enhancer and Dynamsoft Barcode Reader.
