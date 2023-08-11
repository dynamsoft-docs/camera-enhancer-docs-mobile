---
layout: default-layout
title: Android PermissionUtil Class - Dynamsoft Camera Enhancer Documents
description: PermissionUtil Class page of Dynamsoft Camera Enhancer Android edition defines methods for getting the camera permission.
keywords:  Camera Enhancer, Android, PermissionUtil
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android PermissionUtil Class
permalink: /programming/android/auxiliary-api/permission-util.html
---

# PermissionUtil

The `PermissionUtil` class defines the methods for requesting the camera permission.

```java
final class PermissionUtil
```

| Functions | Description |
| --------- | ----------- |
| [`requestCameraPermission`](#requestcamerapermission) | Trigger to request the camera permission. |

## requestCameraPermission

Trigger to request the camera permission.

```java
static void requestCameraPermission(@NonNull Activity activity)
```

**Parameters**

`activity`: The activity that you want to request the camera permission
