---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS API references - CameraEnhancer Class
description: This is the documentation - iOS API references - CameraEnhancer Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS API references, CameraEnhancer Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS CameraEnhancer Class
---

# Initialization Methods

| Method | Description |
| ------ | ----------- |
| [`initLicenseFromDLS`](#initLicensefromdls) | Initialize the Camera Enhancer from the license server with a license. |

---

## initLicenseFromDLS

Initialize the Camera Enhancer with a license.

```objc
- (instancetype)initLicenseFromDLS:(iDCEDLSConnectionParameters*)parameters
                              view:(DCECaptureView *)view
              verificationDelegate:(id)connectionDelegate;
```

**Parameters**

`iDCEDLSConnectionParameters`: The class [`DMDLSConnectionParameters`]({{site.android-api-auxiliary}}dlsconnection.html) parameters.  
`view`: The [`DCECaptureView`]({{ site.ios-api-auxiliary }}dcecameraview.html).

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
_decView = [DCECaptureView cameraWithFrame:self.view.bounds];
iDCEDLSConnectionParameters* dls = [[iDCEDLSConnectionParameters alloc] init];
dls.organizationID = @"200001";
_dce = [[DynamsoftCameraEnhancer alloc] initLicenseFromDLS:dls view:_dceView verificationDelegate:self];
```
2. 
```swift
dceView = DCECaptureView.init(view: self.view.bounds)
let dls = iDCEDLSConnectionParameters()
dls.organizationID = "200001"
dce = DynamsoftCameraEnhancer.init(licenseFromDLS: dls, view: dceView, verificationDelegate: self)
```
