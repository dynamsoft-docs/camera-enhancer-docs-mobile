---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS RectDrawingItem Class
description: This is the documentation - iOS RectDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, RectDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS RectDrawingItem Class
---

# RectDrawingItem

`RectDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `RectDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

```objc
@interface RectDrawingItem (DrawingItem)
```

## initWithRect

The constructor of `RectDrawingItem`. Initialize the instance of `RectDrawingItem`.

```objc
- (instancetype) initWithRect:(CGRect)rect;
```

**Parameters**

`rect`: A `Rect` that indicates the location of the `RectDrawingItem`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

## rect

The property that indicates the `Rect` of the `RectDrawingItem`.

```objc
@property (assign, nonatomic, readonly) CGRect rect;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```
