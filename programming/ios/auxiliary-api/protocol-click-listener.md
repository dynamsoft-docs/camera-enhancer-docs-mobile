---
layout: default-layout
title: DSDrawingItemClickListener - DynamsoftCameraEnhancer iOS Edition API Reference
description: The protocol that includes methods for monitoring the click events of the DrawingItems.
keywords: click events, drawingItems, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingItemClickListener

The `DSDrawingItemClickListener` protocol includes methods for monitoring the click events of the [`DrawingItems`](drawingitem.md).

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@protocol DSDrawingItemClickListener <NSObject>
```
2. 
```swift
protocol DrawingItemClickListener : NSObjectProtocol
```

## Methods

| Method | Description |
|------- |-------------|
| [`onClicked`](#onclicked) | The method for monitoring the click events of the [`DrawingItems`](drawingitem.md) and receiving call. |

### onClicked

The method for monitoring the click events of the [`DrawingItems`](drawingitem.md) and receiving call.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)onClicked:(DSDrawingItem *)clickedItem;
```
2. 
```swift
func onClicked(_ clickedItem: DrawingItem)
```

**Parameters**

`clickedItem`: The clicked DrawingItems.
