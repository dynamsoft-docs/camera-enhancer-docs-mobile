---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - Initialization
description: This is the main page of Dynamsoft Camera Enhancer JavaScript SDK Initialization.
keywords: camera enhancer, initialization, javascript, js
needAutoGenerateSidebar: true
needGenerateH3Content: true
noTitleIndex: true
breadcrumbText: Initialization
---

# Initialization APIs

| API Name | Description |
|---|---|
| [createInstance()](#createinstance) | Creates a `CameraEnhancer` instance. |
| [defaultUIElementURL](#defaultuielementurl) | Returns or sets the URL of the .html file that defines the default UI Element. |
| [getUIElement()](#getuielement) | Returns the HTML element that is used by the `CameraEnhancer` instance. |
| [setUIElement()](#setuielement) | Specifies an HTML element for the `CameraEnhancer` instance to use as its UI element. |

## createInstance

Creates a `CameraEnhancer` instance.

```typescript
static createInstance(): Promise<CameraEnhancer>
```

**Parameters**

None.

**Return value**

A promise resolving to the created `CameraEnhancer` object.

**Code Snippet**

```js
let pEnhancer = null;
(async () => {
    let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
})();
```

## defaultUIElementURL

Returns or sets the URL of the *.html* file that defines the default UI Element. The URL can only be set before the API [createInstance](#createinstance) is called.

```typescript
static defaultUIElementURL: string
```

**Code Snippet**

```js
Dynamsoft.DCE.CameraEnhancer.defaultUIElementURL = "https://cdn.jsdelivr.net/npm/dynamsoft-camera-enhancer@2.0.0/dist/dce.ui.html";
let pEnhancer = null;
(async () => {
    let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
    await enhancer.open();
})();
```

## getUIElement

Returns the HTML element that is used by the [CameraEnhancer](#CameraEnhancer) instance.

```typescript
getUIElement(): HTMLElement
```

**Parameters**

None.

**Return value**

The HTML element used as the UI by the [CameraEnhancer](#CameraEnhancer) instance.

**Code Snippet**

```html
<!-- Define an element to hold the UI element -->
<div id="enhancerUIContainer"></div>
<script>
    let pEnhancer = null;
    (async () => {
        let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
        document.getElementById("enhancerUIContainer").appendChild(enhancer.getUIElement());
        await enhancer.open();
    })();
</script>
```

## setUIElement

Specifies an HTML element for the [CameraEnhancer](#CameraEnhancer) instance to use as its UI. The structure inside the element determines the appearance of the UI.

```typescript
setUIElement(elementOrURL: HTMLElement | string): Promise<void>
```

**Parameters**

`elementOrURL` : specifies an existing element on the page or the URL of an HTML file which contains an element.

**Return value**

A promise that resolves when the operation succeeds.

**Code Snippet**

```html
<!-- Define an element that shows only the video input -->
<video class="dce-video" playsinline="true"></video>
<script>
    let pEnhancer = null;
    (async () => {
        let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
        await enhancer.setUIElement(document.getElementsByClassName("dce-video")[0]);
        await enhancer.open();
    })();
</script>
```

```html
<!-- Use the default official UI element definition -->
<script>
    let pEnhancer = null;
    (async () => {
        let enhancer = await (pEnhancer = pEnhancer || Dynamsoft.DCE.CameraEnhancer.createInstance());
        await enhancer.setUIElement("https://cdn.jsdelivr.net/npm/dynamsoft-camera-enhancer@2.0.0/dist/dce.ui.html");
        await enhancer.open();
    })();
</script>
```
