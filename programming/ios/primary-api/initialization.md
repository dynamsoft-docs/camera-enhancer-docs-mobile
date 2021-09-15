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
| [`initLicense`](#initLicense) | Initialize the Camera Enhancer from the license server with a license. |

---

## initLicense

Initialize the Camera Enhancer with a license.

```objc
+ (void)initLicense:(NSString*)license verificationDelegate:(id)connectionDelegate;
```

**Parameters**

`license`: You have to input a valid license to access the full feature of `Dynamsoft Camera Enhancer`.

**Code Snippet**

Objective-C:

```objc
//Replace the string with your own license
[DynamsoftCameraEnhancer initLicense:@"DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==" verificationDelegate:self];

- (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError *)error{
    NSLog(@"Verification: %@",error.userInfo);
}
```

Swift:

```swift
//Replace the string with your own license
DynamsoftCameraEnhancer.initLicense("DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==",verificationDelegate:self)

func DCELicenseVerificationCallback(_ isSuccess: Bool, error: Error?) {
    print("Verification: \(String(describing: error))")
}
```
