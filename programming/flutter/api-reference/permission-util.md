---
layout: default-layout
title: PermissionUtil Class - Dynamsoft Capture Vision Flutter
description: PermissionUtil class of DCV Flutter handles the camera permissions on Android devices.
keywords: permission util, camera, capture vision, android, camera enhancer
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# PermissionUtil

The `PermissionUtil` class handles the camera permissions on Android devices. It provides static methods for requesting camera permissions specifically on Android devices.

> [!NOTE]
> For iOS, the camera permissions are granted via the Info.plist or the Info settings of the project.

## Definition

*Assembly:* dynamsoft_capture_vision_flutter

```dart
class PermissionUtil
```

## Methods

### requestCameraPermission

Requests camera permission from the Android user. On other platforms (iOS), this method does nothing and returns immediately. 

```dart
static Future<void> requestCameraPermission();
```
