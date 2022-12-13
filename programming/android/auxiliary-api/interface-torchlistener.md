---
layout: default-layout
title: Android TorchListener - Dynamsoft Camera Enhancer
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
void onTorchStateChanged(TorchState state);
```

**Parameters**

`state`: The torch status value. One of the parameters in [`TorchState`]({{site.parameter-reference}}index.html#torchstate)

**Code Snippet**

```java
cameraEnhancer.addTorchListener(new TorchListener() {
    @Override
    public void onTorchStateChanged(TorchState torchState) {
        // Add your code
    }
});
```
