---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS Protocol CameraTorchListener
description: This is the documentation - iOS Protocol CameraTorchListener page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS Protocol CameraTorchListener
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: false
breadcrumbText: iOS Protocol CameraTorchListener
---

# CameraTorchListener

The protocol that handles the torch state when the torch state changes.

```objc
@protocol CameraTorchListener <NSObject>
```

| Method | Type | Description |
| ------ | ---- | ----------- |
| `didChangeTorchState` | *required* | The method for user to add code when torch state is changed. |

## didChangeTorchState

The method for user to add code when torch state is changed.

```objc
- (void)didChangeTorchState:(TorchState)torchState NS_SWIFT_NAME(didChangeTorchState(torchState:));
```

**Parameters**

[`TorchState`]({{site.parameter-reference}}index.html#torchstate): The torch status.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
[_dce addTorchListener:self];
// Add protocol requirements
- (void)didChangeTorchState:(TorchState) torchState{
    // TODO add your code for torch listener
}
```
2. 
```swift
dce.addTorchListener(self)
// Add protocol requirements
func didChangeTorchState(torchState: TorchState){
    // TODO add your code for torch listener
}
```
