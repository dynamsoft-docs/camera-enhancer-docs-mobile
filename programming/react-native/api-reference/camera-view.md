---
layout: default-layout
title: CameraView Class - Dynamsoft Capture Vision React Native
description: CameraView class of Dynamsoft Capture Vision React Native edition displays a camera preview with customizable UI elements.
keywords: camera, enhancer, barcode reader, React Native, capture vision, view
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# CameraView

`CameraView` is a widget that integrates with the [`CameraEnhancer`](camera-enhancer.md) - providing a camera interface with configurable and customizable UI components like torch control, scan region visualization, and custom drawing layers.

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
class CameraView extends Component<CameraViewNativeProps, any>
```

## Properties

| Property | Type | Description |
| -------- | ---- | ----------- |
| [`cameraToggleButton`](#cameratogglebutton) | *Object* | Defines a custom widget to replace the default camera toggle button. |
| [`cameraToggleButtonVisible`](#cameratogglebuttonvisible) | *boolean* | Determines whether the camera toggle button is visible. |
| [`scanLaserVisible`](#scanlaservisible) | *boolean* | Determines whether the scan laser will be visible in the scan region. |
| [`scanRegionMaskVisible`](#scanregionmaskvisible) | *boolean* | Determines whether the scan region mask will be visible. (Scan region mask is a mask covered outside the scan region.) |
| [`torchButton`](#torchbutton) | *Object* | Defines a custom `TorchButton` instead of the default torch icon. |
| [`torchButtonVisible`](#torchbuttonvisible) | *boolean* | Controls the visibility of the torch/flash button. |
| [`visibleLayerIds`](#visiblelayerids) | *number[]* | Defines which drawing layer(s) to display on the camera view. |

### cameraToggleButton

Defines a custom widget (as a [`CameraToggleButton`](camera-toggle-button.md) object) to replace the default camera toggle button (to switch between the front and back cameras).

```js
cameraToggleButton?: {
    location?: {
        x?: Int32;
        y?: Int32;
        width?: Int32;
        height?: Int32;
    }
    cameraToggleImageBase64?: string;
};
```

### cameraToggleButtonVisible

Determines whether the camera toggle button (to switch between the front and back cameras) is visible.

```js
cameraToggleButtonVisible?: boolean
```

**Default Value**

`false`.

### scanLaserVisible

Determines whether the scan laser will be visible in the scan region or not.

```js
scanLaserVisible?: boolean
```

**Default Value**

`false`

### scanRegionMaskVisible

Determines whether the scan region mask will be visible. Scan region mask is a mask covered outside the scan region.

```js
scanRegionMaskVisible?: boolean
```

**Default Value**

`false`

### torchButtonVisible

Controls the visibility of the torch/flash button that allows the user to activate the flash in low brightness scenarios.

```js
torchButtonVisible?: boolean
```

**Default Value**

`false`

### torchButton

Defines a custom [`TorchButton`](torch-button.md) instead of the default torch icon that comes with the camera view. This property allows you to customize the size, position, and icon images of the torch button.

```js
torchButton?: {
    location?: {
        x?: Int32;
        y?: Int32;
        width?: Int32;
        height?: Int32;
    };
    visible?: boolean;
    torchOnImageBase64?: string;
    torchOffImageBase64?: string;
};
```

### visibleLayerIds

Defines which drawing layer(s) (see [`EnumDrawingLayerId`]({{site.dcv_react_native_api}}core/enum/drawing-layer-id.html)) to display on the camera view. The drawing layer is responsible for highlighting the captured result, so in the case of the Barcode Reader, the drawing layer would highlight any recognized barcodes.

```js
visibleLayerIds?: number[]
```

**Remarks**

The Capture Vision library can work with multiple functional products, including the Barcode Reader, Label Recognizer, and the Document Normalizer. If you would like to disable the feature to highlight any found barcodes, then the `visibleLayerIds` must not include `EnumDrawingLayerId.dbr`.
