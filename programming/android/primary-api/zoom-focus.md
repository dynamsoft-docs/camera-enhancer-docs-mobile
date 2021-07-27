---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android API references - Focus & Zoom Methods
description: This is the documentation - Android API references - Focus & Zoom Methods page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Focus, Zoom, Android API Reference
needAutoGenerateSidebar: true
breadcrumbText: Android Zoom and Focus
---

# Android API Reference - Focus & Zoom Methods

## setAutoFocusPosition

Set the position that you want to auto focus at. This setting will replace the default focus value and always focus on the set point.

```java
com.dynamsoft.dce.CameraEnhancer.setAutoFocusPosition(float, float)
```

**Parameters**

- `X`: A float value that stands for the X coordinate of the focus position.
- `Y`: A float value that stands for the Y coordinate of the focus position.

**Code Snippet**

Java:

```java
mCameraEnhancer.setAutoFocusPosition(0.5f,0.6f);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setAutoFocusPosition(0.5f,0.6f)
```

## setManualFocusPosition

Set the manual focus position. This position only takes effect once when this API is called.

```java
com.dynamsoft.dce.CameraEnhancer.setAutoFocusPosition(int, int)
```

**Parameters**

- `X`: The int pixel value that stands for the X coordinate of the focus position.
- `Y`: The int pixel value that stands for the Y coordinate of the focus position.

**Code Snippet**

Java:

```java
//The focus position will be 200 pixel from left and 300 pixel from top.
mCameraEnhancer.setManualFocusPosition(200, 300);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setManualFocusPosition(200,300)
```

## setFocalLength

Set the focal length (float). The range of focal length is from 0 to 10. The value is a precentage. If user sets `setFocalLength(5);` it means the focal length will be 50% of the maxium focal length of the camera. Please note, If this API is called to set a focal length, the focal length will be fixed and all other auto focus mode will be disabled. To quit this fixed focal length mode, please set the focal length into -1.

```java
com.dynamsoft.dce.CameraEnhancer.setFocalLength(float)
```

**Parameters**

- `FocalLength`: A float value between 0 to 10 that stands for the focal length. You can input -1 to quit the fixed focal length mode.

**Code Snippet**

Java:

```java
    mCameraEnhancer.setFocalLength(8.5);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.setFocalLength(8.5)
```

To quit:

Java:

```java
    mCameraEnhancer.setFocalLength(-1);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.setFocalLength(-1)
```

## enableDCEAutoFocus

This API is designed to turn on DCE auto focus mode which is specially designed and is separate from the systems default auto focus mode. DCE auto focus and the default auto focus can work together at the same time without any conflict. The above focus settings are also available for controlling system default auto focus.

```java
com.dynamsoft.dce.CameraEnhancer.enableDCEAutoFocus(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    mCameraEnhancer.enableDCEAutoFocus(true);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.enableDCEAutoFocus(true)
```

## getEnabledDCEAutoFocusStatus

Get the status (on/off) of DCE autofocus mode:

```java
com.dynamsoft.dce.CameraEnhancer.getEnabledDCEAutoFocusStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    boolean x = mCameraEnhancer.getEnabledDCEAutoFocusStatus();
```

Kotlin:

```kotlin
    var x:Boolean? = mCameraEnhancer!!.enabledDCEAutoFocusStatus
```

## enableDefaultAutoFocus

This API is designed for controlling the system default autofocus.

```java
com.dynamsoft.dce.CameraEnhancer.enableDefaultAutoFocus(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    mCameraEnhancer.enableDefaultAutoFocus(false);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.enableDefaultAutoFocus(false)
```

## getEnabledDefaultAutoFocusStatus

To get status (on/off) of Default autofocus mode:

```java
com.dynamsoft.dce.CameraEnhancer.getEnabledDefaultAutoFocusStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    boolean x = mCameraEnhancer.getEnabledDefaultAutoFocusStatus();
```

Kotlin:

```kotlin
    var x:Boolean? = mCameraEnhancer!!.enabledDefaultAutoFocusStatus
```

## enableRegularAutoFocus

Regular auto focus is an advanced setting that enables the camera to auto focus every 3 seconds. It is contained in DCE auto focus. When DCE auto focus is enabled, regular auto focus is enabled as well. To turn off regular auto focus mode:

```java
com.dynamsoft.dce.CameraEnhancer.enableRegularAutoFocus(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    mCameraEnhancer.enableRegularAutoFocus(false);
```

Kotlin:

```kotlin
    mCameraEnhancer!!.enableRegularAutoFocus(false)
```

## getEnabledRegularAutoFocusStatus

Get status (on/off) of regular autofocus mode:

```java
com.dynamsoft.dce.CameraEnhancer.getEnabledRegularAutoFocusStatus()
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
    boolean x = mCameraEnhancer.getEnabledRegularAutoFocusStatus();
```

Kotlin:

```kotlin
    var x:Boolean? = mCameraEnhancer!!.enabledRegularAutoFocusStatus
```

## setRegularAutoFocusParam

You can set the focus interval time and focus terminate time in regular auto focus mode. Please use `setregularautofocusparam` to make these settings.

```java
com.dynamsoft.dce.CameraEnhancer.setRegularAutoFocusParam(int, int)
```

**Parameters**

- Focus interval: Default value is 3000 (millisecond), which means the camera will auto focus for every 3000 milliseconds.
- Terminate time: Default value is 500 (millisecond), which means the camera will not focus once again within 500 milliseconds.

**Code Snippet**

Java:

```java
// Set focus interval = 3000 and focus terminate time = 500.
mCameraEnhancer.setRegularAutoFocusParam(3000, 500);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setRegularAutoFocusParam(3000,500)
```

## enableAutoFocusOnSharpnessChange

This API is another advanced setting that enabled the camera to autofocus when sharpness change is detected between contiguous frames. The same with regular autofocus, this focus mode is also enabled by default when DCE autofocus is enabled. To turn off camera autofocus when sharpness changes:

```java
com.dynamsoft.dce.CameraEnhancer.enableAutoFocusOnSharpnessChange(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
mCameraEnhancer.enableAutoFocusOnSharpnessChange(false);
```

Kotlin:

```kotlin
mCameraEnhancer!!.enableAutoFocusOnSharpnessChange(false)
```

## getEnabledAutoFocusOnSharpnessChangeStatus

Get the status (on/off) of the sharpness autofocus mode:

```java
com.dynamsoft.dce.CameraEnhancer.getEnabledAutoFocusOnSharpnessChangeStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledAutoFocusOnSharpnessChangeStatus();
```

Kotlin:

```kotlin
var x:Boolean? = mCameraEnhancer!!.enabledAutoFocusOnSharpnessChangeStatus
```

## enableAutoZoom

This auto zoom mode is specially designed for Dynamsoft Barcode Reader users. The barcode reader can always get a localization result even if it fails on decoding. DCE auto zoom will enable the camera to approach the localized barcode area if the barcode reader got a localization result but failed to get a barcode result.

```java
com.dynamsoft.dce.CameraEnhancer.enableAutoZoom(boolean)
```

**Parameters**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
mCameraEnhancer.enableAutoZoom(true);
```

Kotlin:

```kotlin
mCameraEnhancer!!.enableAutoZoom(true)
```

## getEnabledAutoZoomStatus

Get the status (on/off) of autozoom mode:

```java
com.dynamsoft.dce.CameraEnhancer.getEnabledAutoZoomStatus()
```

**Return Value**

- `Boolean`: True/false value that stands for enabled/disabled status.

**Code Snippet**

Java:

```java
boolean x = mCameraEnhancer.getEnabledAutoZoomStatus();
```

Kotlin:

```kotlin
var x:Boolean? = mCameraEnhancer!!.enabledAutoZoomStatus
```

## setZoomFactor

Set the zoom factor (float).

```java
com.dynamsoft.dce.CameraEnhancer.setZoomFactor(float)
```

**Parameters**

- `Zoom Factor`: A float value that stands for the zoom factor.

**Code Snippet**

Java:

```java
mCameraEnhancer.setZoomFactor(1.5f);
```

Kotlin:

```kotlin
mCameraEnhancer!!.setZoomFactor(1.5f)
```
