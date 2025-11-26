---
layout: default-layout
title: CameraToggleButton Class - Dynamsoft Capture Vision Flutter
description: CameraToggleButton class of DCV Flutter edition displays a camera preview with customizable UI elements.
keywords: camera, enhancer, barcode reader, flutter, capture vision, view
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraToggleButton

`CameraToggleButton` is a widget that represents a camera toggle button with customizable appearance and location. The camera toggle button allows the user to switch between the front and back cameras.

## Definition

*Assembly:* dynamsoft_capture_vision_flutter

```dart
class CameraToggleButton
```

## Constructors

```dart
CameraToggleButton({
  required this.location,
  this.imageBase64,
});
```

## Properties

| Properties | Type | Description |
| ---------- | ---- | ----------- |
| [`location`](#location) | *Rect* | Defines the location of the camera button. This rectangle specifies the button's position and size on the screen. Coordinates are in logical pixels. |
| [`imageBase64`](#imagebase64) | *String* | A base 64 string that specifies the camera toggle image. |

### location

Defines the location of the camera button. This rectangle specifies the button's position and size on the screen. Coordinates are in logical pixels.

```dart
Rect location;
```

### imageBase64

A base 64 string that specifies the camera toggle image.

```dart
String? imageBase64;
```

**Remarks**

When setting the imageBase64 string, please note that the string should not include the `data:image/png;base64,` portion of the base64 string.

