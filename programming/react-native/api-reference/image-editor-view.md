---
layout: default-layout
title: ImageEditorView Class - Dynamsoft Capture Vision React Native
description: ImageEditorView class of Dynamsoft Capture Vision React Native edition represents an image editor view, which allows users to add interactable UI elements on the view.
keywords: camera, enhancer, barcode reader, React Native, capture vision, view
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# ImageEditorView

`ImageEditorView` is a widget that allows users to add interactable UI elements on the view.

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
class ImageEditorView extends Component<ImageEditorViewNativeProps, any>
```

## Methods

| Method | Description |
| ------ | ----------- |
| [`setOriginalImage`](#setoriginalimage) | The initial image to display in the editor when created. |
| [`getSelectedQuad`](#getselectedquad) | Pre-populated drawing quadrilaterals organized by layer. |
| [`setQuads`](#setquads) | Callback invoked when the native platform view is successfully created. |

### getSelectedQuad

Retrieves the currently selected quadrilateral from the editor.

```js
getSelectedQuad(): Promise<null | Quadrilateral>
```

**Returns**

A promise that resolves the currently selected quadrilateral.

### setOriginalImage

Sets the original image in the native image editor.

```js
setOriginalImage(imageData: ImageData): void
```

**Parameters**

`imageData`: The `ImageData` Object to be set as the original image.

### setQuads

Updates the quadrilaterals in the editor for a specific drawing layer.

```js
setQuads(
    quads: undefined | null | Quadrilateral[],
    layerId: number,
): Promise<void>
```

**Parameters**

`quads`: The [`Quadrilaterals`]({{ site.dcv_react_native_api }}core/quadrilateral.html) to set, or null/undefined to clear them. The coordinate base of the point is "image".

`layerId`: The ID of the drawing layer to update.
