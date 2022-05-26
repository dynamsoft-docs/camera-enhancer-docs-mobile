---
layout: default-layout
title: Dynamsoft Camera Enhancer - Advanced Setting Parameters
description: This is the documentation - Advanced Setting Parameters Page of Dynamsoft Camera Enhancer.
keywords:  Advanced Setting Parameters
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Advanced Setting Parameters
---

# Parameter reference - Advanced Settings parameters

The following parameters are advanced parameters for special usages. These parameters can be uploaded via method [`updateAdvancedSettingsFromFile`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromfile) and [`updateAdvancedSettingsFromString`]({{site.android-api}}camera-enhancer.html#updateadvancedsettingsfromstring).

| Parameter Name | Type | Description |
| -------------- | ---- | ----------- |
| [`focalLength`](#focallength) | *float* | Set the fixed focal length. |
| [`autoFocusInterval`](#autofocusinterval) | *int* | Set the time interval of the auto focus. |
| [`autoFocusTerminateTime`](#autofocusterminatetime) | *int* | Set the minimum terminate time of auto focus. |
| [`sensorControlSensitivity`](#sensorcontrolsensitivity) | *int* | Set the sensitivity of the mobile sensor. |
| [`FastMode`](#fastmode) | *JSON data* | Set a group of crop regions. |

## focalLength

Set the fixed focal length with a float value. When this parameter is configured, the other focus methods and parameters will be disbaled and the focal length will be fixed. Users can reset the focalLength to -1 to disable the fixed focus settings. The closer to the 0, the further the focalLength will be.

**Default Value**

-1

**Range**

Android: -1 or float value between 0 and 10.  
iOS: -1 or float value between 0 and 1.

## autoFocusInterval

Set the time interval of the auto-focus with an int value.

**Default Value**

The default focus interval is 3000 milliseconds which means the camera will focus once for every 3 seconds.

**Range**

At least 0 and no maximum limit.

## autoFocusTerminateTime

The minimum termination time of the auto-focus with an int value.

**Default Value**

The default terminates time is 3000 milliseconds which means the camera will never focus for another time with in 500 miliseconds.

**Range**

At least 0 and no maximum limit.

## sensorControlSensitivity

Set the sensitivity of the mobile sensor with an int value. A lower input value results in a higher sensitivity.

**Default Value**

50

**Range**

At least 0 and no maximum limit.

## FastMode

The fast-mode parameters store four groups of frame cropping parameters. The cropping parameters will be implemented periodically when the fast mode is enabled. You can use the default cropping region settings or update your personalized crop regions via a JSON string or file.

**Default Value**

```json
"FastMode": {
    "cropRegions": [{
        "top": 0,
        "right": 100,
        "bottom": 100,
        "left": 0
    },
    {
        "top": 25,
        "right": 100,
        "bottom": 75,
        "left": 0
    },
    {
        "top": 25,
        "right": 75,
        "bottom": 75,
        "left": 25
    },
    {
        "top": 25,
        "right": 75,
        "bottom": 75,
        "left": 25
    }]
}
```

## ISO & ExposureTime

Set the ISO and exposure time of the camera.

For iOS users:

```json
{
    // The 'value' and 'timescale' will be generated to a CMTime object.
    'iOSExposureTime':{
        'value': 4,
        'timescale': 2,
    },
    'iso':30
}
```

For Android users:

```json
{
    'androidExposureTime': 2,
    'iso':30
}
```
