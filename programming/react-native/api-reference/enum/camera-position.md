---
layout: default-layout
title: EnumCameraPosition - Dynamsoft Capture Vision React Native
description: Enumeration EnumCameraPosition of Dynamsoft Capture Vision React Native Edition defines the possible camera(s) to choose from.
keywords: camera enhancer, position, react native, barcode
needAutoGenerateSidebar: true
needGenerateH3Content: true
breadcrumbText: EnumCameraPosition
---

# EnumCameraPosition

`EnumCameraPosition` is an enumeration that defines the possible camera positions that are available to a device. The majority of modern mobile devices have a front and a rear camera. The more recent iPhones also come with multiple rear cameras, each being suited to different scenarios.

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
enum EnumCameraPosition {
    CP_BACK,
    CP_FRONT,
    CP_BACK_ULTRA_WIDE,
    CP_BACK_DUAL_WIDE_AUTO
}
```

## Members

| Member | Description |
| ------ | ----------- |
| `CP_BACK` | The default, back-facing camera. It is a wide-angle camera for general usage. |
| `CP_FRONT` | The front-facing camera. |
| `CP_BACK_ULTRA_WIDE` | (iOS ONLY) The back-facing ultra-wide-angle camera - which should be used for macro-distance scenarios. |
| `CP_BACK_DUAL_WIDE_AUTO` | (iOS ONLY) The back-facing virtual camera that can automatically switch between the default wide-angle and the ultra-wide-angle cameras. (Supported devices: Pro or Pro Max iPhones) |
