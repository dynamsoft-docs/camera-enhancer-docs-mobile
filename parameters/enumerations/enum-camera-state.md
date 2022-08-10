---
layout: default-layout
title: Dynamsoft Camera Enhancer - Enumerations Camera State
description: This is the documentation - Enumerations Camera State page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Enumerations Camera State
needAutoGenerateSidebar: true
breadcrumbText: Enumerations Camera State
---

# EnumCameraState

## Declarations

| Language | Declaration |
|----------|-------------|
| Java(Android) | `class EnumCameraState` |
| Objective-C & Swift | `enum EnumCameraState` |

## Members

| Member (Android) | Member (Objective-C) | Member (Swift) | Value | Description |
| ---------------- | -------------------- | -------------- | ----- | ----------- |
| `CAMERA_STATE_OPENED` | `EnumCAMERA_STATE_OPENED` | `EnumCAMERA_STATE_OPENED` | 1 | The selected camera is opened. |
| `CAMERA_STATE_CLOSED` | `EnumCAMERA_STATE_CLOSED` | `EnumCAMERA_STATE_CLOSED` | 2 | The selected camera is closed. |
| `CAMERA_STATE_OPENING` | `EnumCAMERA_STATE_OPENING` | `EnumCAMERA_STATE_OPENING` | 0 | The selected camera is currently closed but will be opened soon. |
| `CAMERA_STATE_CLOSING` | `EnumCAMERA_STATE_CLOSING` | `EnumCAMERA_STATE_CLOSING` | 3 | The selected camera is currently closed but will be closed soon. |
