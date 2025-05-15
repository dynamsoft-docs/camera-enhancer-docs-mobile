---
layout: default-layout
title: DSDrawingStyle - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSDrawingStyle of DynamsoftCameraEnhancer represents the style attributes of the drawing items, including stroke color, fill color, text color, stroke width, and font.
keywords: drawing style, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingStyle

The `DSDrawingStyle` class represents the style attributes of the drawing items, including stroke color, fill color, text color, stroke width, and font.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSDrawingStyle : NSObject
```
2. 
```swift
class DrawingStyle : NSObject
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`styleId`](#styleid) | *NSInteger* |Get the style ID. |
| [`strokeColor`](#strokecolor) | *UIColor \** | Set/get the stroke color. |
| [`fillColor`](#fillcolor) | *UIColor \** | Set/get the fill color. |
| [`textColor`](#textcolor) | *UIColor \** | Set/get the text color. |
| [`strokeWidth`](#strokewidth) | *CGFloat* | Set/get the stroke width (in pixel). |
| [`font`](#font) | *UIFont \** | Set/get the font. |

### styleId

Get the style ID.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic, readonly) NSInteger styleId;
```
2. 
```swift
var styleId: Int { get }
```

### strokeColor

Set/get the stroke color.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, copy) UIColor *strokeColor;
```
2. 
```swift
var strokeColor: UIColor? { get set }
```

### fillColor

Set/get the fill color.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, copy) UIColor *fillColor;
```
2. 
```swift
var fillColor: UIColor? { get set }
```

### textColor

Set/get the text color.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, copy) UIColor *textColor;
```
2. 
```swift
var textColor: UIColor? { get set }
```

### strokeWidth

Set/get the stroke width (in pixel).

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) CGFloat strokeWidth;
```
2. 
```swift
var strokeWidth: CGFloat { get set }
```

### font

Set/get the font.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (nonatomic, copy) UIFont *font;
```
2. 
```swift
var font: UIFont? { get set }
```
