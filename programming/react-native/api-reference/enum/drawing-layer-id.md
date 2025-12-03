---
layout: default-layout
title: EnumDrawingLayerId - Dynamsoft Capture Vision React Native
description: Enumeration EnumDrawingLayerId of Dynamsoft Capture Vision React Native Edition defines the different drawing layers that the CameraView provides.
keywords: drawing layer, React Native, camera enhancer, UI
needAutoGenerateSidebar: true
needGenerateH3Content: true
breadcrumbText: EnumDrawingLayerId
---

# EnumDrawingLayerId

`EnumDrawingLayerId` is an enumeration that defines the different drawing layers that the CameraView provides. The drawing layer is responsible for creating the highlight boxes around detected barcodes and other captured results. By default, there is a drawing layer assigned to each functional product under Capture Vision. 

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
enum EnumDrawingLayerId {
    DDN_LAYER_ID = 1,
    DBR_LAYER_ID = 2,
    DLR_LAYER_ID = 3,
    TIP_LAYER_ID = 999
}
```

## Members

| Member | Description |
| ------ | ----------- |
| `DDN_LAYER_ID` | The preset DrawingLayer for the Dynamsoft Document Normalizer. |
| `DBR_LAYER_ID` | The preset DrawingLayer for the Dynamsoft Barcode Reader. |
| `DLR_LAYER_ID` | The preset DrawingLayer for the Dynamsoft Label Recognizer. |
| `TIP_LAYER_ID` | A custom DrawingLayer for tips. |
