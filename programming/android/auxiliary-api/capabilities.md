---
layout: default-layout
Title: Capabilities - Dynamsoft Core Module Android Edition API Reference
Description: The class Capabilities of Dynamsoft Core Module represents the capability properties of the hardware, including the maximum zoom factor, focal length, exposure time, and ISO.
Keywords: capabilities, hardware, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# Capabilities

The `Capabilities` class represents the capability properties of the hardware, including the maximum zoom factor, focal length, exposure time, and ISO.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class Capabilities
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`maxZoomFactor`](#maxzoomfactor) | *CGFloat* | The maximum zoom factor. |
| [`minFocalLength`](#minfocallength) | *CGFloat* | The minimum focal length. |
| [`maxFocalLength`](#maxfocallength) | *CGFloat* | The maximum focal length. |
| [`minExposureTime`](#minexposuretime) | *CMTime* | The minimum exposure time. |
| [`maxExposureTime`](#maxexposuretime) | *CMTime* | The maximum exposure time. |
| [`minISO`](#miniso) | *CGFloat* | The minimum ISO. |
| [`maxISO`](#maxiso) | *CGFloat* | The maximum ISO. |

### maxZoomFactor

The maximum zoom factor.

```java
float maxZoomFactor;
```

### minFocalLength

The minimum focal length.

```java
float minFocalLength;
```

### maxFocalLength

The maximum focal length.

```java
float maxFocalLength;
```

### minExposureTime

The minimum exposure time.

```java
long minExposureTime;
```

### maxExposureTime

The maximum exposure time.

```java
long maxExposureTime;
```

### minISO

The minimum ISO.

```java
float minISO;
```

### maxISO

The maximum ISO.

```java
float maxISO;
```
