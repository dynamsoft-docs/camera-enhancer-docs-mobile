---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - Interface DrawingStyle
description: This page shows the DrawingStyle Interface of Dynamsoft Camera Enhancer JavaScript SDK.
keywords: DrawingStyle, CameraEnhancer, api reference, javascript, js
needAutoGenerateSidebar: false
noTitleIndex: true
breadcrumbText: DrawingStyle
---

# DrawingStyle

`interface` DrawingStyle

* id: `number`

  The ID of the current `DrawingStyle` .

* lineWidth: `number`

  The line width (in pixels) of the current `DrawingStyle` . Default: `2`.

* fillStyle: `string`

  The fill color of the current `DrawingStyle` . Default: `rgba(245, 236, 73, 0.3)`.

* strokeStyle: `string`

  The stroke color of the current `DrawingStyle` . Default: `rgba(245, 236, 73, 1)`.

* paintMode: "fill" | "stroke" | "strokeAndFill"

  Three paint modes provided. Default: `stroke`.

* fontSize: `number`

  The fontSize of the current `DrawingStyle` . Default: `10`.

* fontFamily: `string`

  The fontFamily of the current `DrawingStyle` . Default: `sans-serif`.

## Built-in DrawingStyles

  The SDK comes with 8 default Drawing styles. Their style definition are listed below

  //TODO: add a picture to demonstrate the 8 styles

  ```js
  // DrawingStyle 1
  // Used by Dynamsoft Document Normalizer
  {
      fillStyle: "rgba(73, 173, 245, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 1,
      lineWidth: 2,
      paintMode: "stroke",
      strokeStyle: "rgba(73, 173, 245, 1)"
  }
  // DrawingStyle 2
  // Used by Dynamsoft Label Recognizer
  {
      fillStyle: "rgba(73, 245, 73, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 2,
      lineWidth: 2,
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(73, 245, 73, 0.9)"
  }
  // DrawingStyle 3
  // Used by Dynamsoft Barcode Reader
  {
      fillStyle: "rgba(254, 180, 32, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 3,
      lineWidth: 2,
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(254, 180, 32, 0.9)"
  }
  // DrawingStyle 4
  // One of two default styles for custom DrawingLayers
  {
      fillStyle: "rgba(245, 236, 73, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 4,
      lineWidth: 2,
      paintMode: "stroke",
      strokeStyle: "rgba(245, 236, 73, 1)"
  }
  // DrawingStyle 5
  // Used by Dynamsoft Document Normalizer
  {
      fillStyle: "rgba(73, 173, 245, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 5,
      lineWidth: 1
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(73, 173, 245, 1)"
  }
  // DrawingStyle 6
  // Used by Dynamsoft Label Recognizer
  {
      fillStyle: "rgba(73, 245, 73, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 6,
      lineWidth: 2,
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(73, 245, 73, 0.9)"
  }
  // DrawingStyle 7
  // Used by Dynamsoft Barcode Reader
  {
      fillStyle: "rgba(254, 180, 32, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 7,
      lineWidth: 2,
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(254, 180, 32, 1)"
  }
  // DrawingStyle 8
  // One of two default styles for custom DrawingLayers
  {
      fillStyle: "rgba(245, 236, 73, 0.3)",
      fontFamily: "sans-serif",
      fontSize: 10,
      id: 8,
      lineWidth: 2,
      paintMode: "strokeAndFill",
      strokeStyle: "rgba(245, 236, 73, 1)"
  }
  ```
