---
layout: default-layout
Title: DSDrawingStyle - Dynamsoft Core Module iOS Edition API Reference
Description: The class DSDrawingStyle of Dynamsoft Core Module represents the style attributes of the drawing items, including stroke color, fill color, text color, stroke width, and font.
Keywords: drawing style, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingStyle

The `DSDrawingStyle` class represents the style attributes of the drawing items, including stroke color, fill color, text color, stroke width, and font.

## Definition

*Assembly:* DynamsoftCore.framework

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

## Methods

| Method | Description |
|------- |-------------|
| [`initWithId:strokeColor:strokeWidth:fillColor:textColor:`](#initwithidstrokecolorstrokewidthfillcolortextcolor) | Create an instance of the DrawingStyle. |

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

### initWithId:strokeColor:strokeWidth:fillColor:textColor:

Create an instance of the DrawingStyle.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithId:(NSInteger)styleId strokeColor:(UIColor *)strokeColor strokeWidth:(CGFloat)strokeWidth fillColor:(UIColor *)fillColor textColor:(UIColor *)textColor;
```
2. 
```swift
init(styleId: Int, strokeColor: UIColor?, strokeWidth: CGFloat, fillColor: UIColor?, textColor: UIColor?)
```
**Parameters**

`styleId`: Set the style ID.  
`strokeColor`: Set the stroke color.  
`strokeWidth`: Set the stroke width.  
`fillColor`: Set the fill color.  
`textColor`: Set the text color.  

**Return Value**

An instance of the `DSDrawingStyle` class.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingStyle *style = [[DSDrawingStyle alloc] initWithId:1 strokeColor:[UIColor blackColor] strokeWidth:2.0 fillColor:[UIColor redColor] textColor:[UIColor whiteColor]];
```
2. 
```swift
let style = DrawingStyle(styleId: 1, strokeColor: UIColor.black, strokeWidth: 2.0, fillColor: UIColor.red, textColor: UIColor.white)
```