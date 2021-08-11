---
layout: default-layout
title: Dynamsoft Camera Enhancer - TorchListener
description: This is the documentation - TorchListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, TorchListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: TorchListener
---

# TorchListener

The interface to handle callback when torch state callback is returned.

```java
interface com.dynamsoft.dce.TorchListener
```

| Functions | Description |
| --------- | ----------- |
| [`onTorchStateChanged`](#onTorchStateChanged) | The method for user to add code when torch state is changed. |

## onTorchStateChanged

The method for user to add code when torch state is changed.

```java
void onTorchStateChanged(TorchState var1);
```

**Parameters**

[`TorchState`]({{site.parameter-reference}}index.html#torchstate): The torch status.

**Code Snippet**

```java
cameraEnhancer.addTorchListener(new TorchListener() {
    @Override
    public void onTorchStateChanged(TorchState torchState) {
        // Add your code
    }
});
```
