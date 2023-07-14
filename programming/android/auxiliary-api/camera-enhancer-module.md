---
layout: default-layout
Title: CameraEnhancerModule - Dynamsoft Core Module Android Edition API Reference
Description: The class DSCameraEnhancerModule of Dynamsoft Core Module represents the camera enhancer module, which provides general functions for the camera enhancer.
Keywords: camera enhancer, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSCameraEnhancerModule

The `DSCameraEnhancerModule` class defines general functions of the camera enhancer module.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class CameraEnhancerModule
```

## Methods

| Method | Description |
|------- |-------------|
| [`getVersion`](#getversion) | Get the version of Dynamsoft Camera Enhancer. |

### getVersion

Get the version of Dynamsoft Camera Enhancer.

```java
+ (NSString *)getVersion;
```
2. 
```kotlin
class func getVersion() -> String
```

**Return Value**

The version of Dynamsoft Camera Enhancer.

**Code Snippet**

```java
NSString *version = [DSCameraEnhancerModule getVersion];
```
2. 
```kotlin
let version = CameraEnhancerModule.getVersion()
```
