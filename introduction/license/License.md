---
layout: default-layout
title: Dynamsoft Camera Enhancer - License initialization
description: This is the documentation - License initialization page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, License initialization
needAutoGenerateSidebar: true
breadcrumbText: License Initialization
---

# License initialization

> NOTE
>
> The JavaScript edition doesn't require a license as of version 2.0.0.

## Get a trial key

- A 7-day public trial key is available for every new device for first use of Dynamsoft Camera Enhancer.
- If your free key is expired, please visit <a href="https://www.dynamsoft.com/customer/license/trialLicense?product=dce&utm_source=docs&package=android" target="_blank">Private Trial License Page</a> to get a 30-day extension.

## Get a full key license

- [Please contact us to purchase for full key license]({{site.contact-us}})

## Set up the license from Dynamsoft License Server

Once you have a license you can use following code to set up your license from `Dynamsoft License Server`:

For Android users:

Android sample

Java:

```java
    mCamera.initLicense("", new DCELicenseVerificationListener() {
        @Override
        public void DCELicenseVerificationCallback(boolean b, Exception e) {
            if(!b && e != null){
                e.printStackTrace();
            }
        }
    });
```

Kotlin:

```kotlin
    mCameraEnhancer!!.initLicense("") { isSuccess, error ->
        if (!isSuccess) {
            error.printStackTrace()
        }
    }
```

For iOS users:

Objective-C sample

```objectivec
    [DynamsoftCameraEnhancer initLicense:@"DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==" verificationDelegate:self];

    - (void)DCELicenseVerificationCallback:(bool)isSuccess error:(NSError *)error{
        NSLog(@"Verification: %@",error.userInfo);
    }
```

Swift sample

```swift
    DynamsoftCameraEnhancer.initLicense("DCE2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInByb2R1Y3RzIjoyfQ==",verificationDelegate:self)

    func DCELicenseVerificationCallback(_ isSuccess: Bool, error: Error?) {
        print("Verification: \(String(describing: error))")
    }
```
