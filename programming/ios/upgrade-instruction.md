---
layout: default-layout
title: iOS Upgrade Instructions- Dynamsoft Camera Enhancer
description: This is the documentation of iOS upgrade instructionspage of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS upgrade instructions
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS API references
permalink: /programming/ios/upgrade-instruction.html
---

# How to Upgrade

## From v2.x/v3.x to v4.x

### Update License Activation Code

License activation API are removed from `DynamsoftCameraEnhancer` library. Please use the `LicenseManager` of `DynamsoftLicense` instead.

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

## Re-write your Code Based on the API References

The APIs of `DynamsoftCameraEnhancer` are refactored. Please follow the [API reference](api-reference.md) to update your code.

### CameraEnhancer API changes

The following APIs are changed on parameters and return values:

* [`CameraEnhancer`](primary-api/camera-enhancer.html#cameraenhancer): Added parameter `CameraView cameraView`.
* [`setScanRegion`](primary-api/camera-enhancer.html#setscanregion): Changed the type of `region` from `iRegionDefinition` to [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html).
* [`getScanRegion`](primary-api/camera-enhancer.html#getscanregion): Changed the type of return value from `iRegionDefinition` to [`DSRect`]({{ site.dcv_android_api }}core/basic-structures/rect.html).
  * `set/getScanRegionVisible`: Replaced by a series of methods in `CameraView` class.
    * `scanRegionMaskVisible`
    * `scanLaserVisible`

### UI Configuring API changes

* `DCECameraView` is renamed to `CameraView`.
* Added a new view class `ImageEditorView`.

Read [How to configure UI](guide/ui-configurations.html) for more details about the API changes.
