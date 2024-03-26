---
layout: default-layout
title: DSDrawingStyleManager - Dynamsoft Camera Enhancer iOS Edition API Reference
description: The class DSDrawingStyleManager of Dynamsoft Camera Enhancer provides methods to manage drawing styles.
keywords: drawing style, manager, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingStyleManager

The `DSDrawingStyleManager` class is the manager of DrawingStyles in Dynamsoft Camera Enhancer.

## Definition

*Assembly:* DynamsoftCameraEnhancer.xcframework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NS_ASSUME_NONNULL_BEGIN
NS_SWIFT_NAME(DrawingStyleManager)
@interface DSDrawingStyleManager : NSObject
```
2. 
```swift
class DrawingStyleManager : NSObject
```

## Methods

| Method | Description |
|------- |-------------|
| [`getDrawingStyle`](#getdrawingstyle) | Get the specified DrawingStyle. |
| [`createDrawingStyle`](#createdrawingstyle) | Create an instance of the DrawingStyle and get the style ID. |
| [`getAllDrawingStyles`](#getalldrawingstyles) | Get all available DrawingStyles. |

### getDrawingStyle

Get the specified DrawingStyle.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (DSDrawingStyle *)getDrawingStyle:(NSInteger)styleId;
```
2. 
```swift
class func getDrawingStyle(_ styleId: Int) -> DSDrawingStyle?
```

**Parameters**

`styleId`: Specify a style ID.

**Return Value**

The DrawingStyle with the specified ID.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
DSDrawingStyle *style = [DSDrawingStyleManager getDrawingStyle:STYLE_BLUE_STROKE];
```
2. 
```swift
if let style = DrawingStyleManager.getDrawingStyle(STYLE_BLUE_STROKE) {
    // Use the style
}
```

### createDrawingStyle

Create an instance of the DrawingStyle and get the style ID.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (NSInteger)createDrawingStyle:(UIColor *)strokeColor strokeWidth:(CGFloat)strokeWidth fillColor:(UIColor *)fillColor textColor:(UIColor *)textColor font:(UIFont *)font;
```
2. 
```swift
class func createDrawingStyle(strokeColor: UIColor, strokeWidth: CGFloat, fillColor: UIColor, textColor: UIColor, font: UIFont) -> Int
```

**Parameters**

`strokeColor`: Set the stroke colour.  
`strokeWidth`: Set the stroke width.  
`fillColor`: Set the fill colour.  
`textColor`: Set the text colour.  
`font`: Set the font.  

**Return Value**

The style ID of the created DrawingStyle.

### getAllDrawingStyles

Get all available DrawingStyles.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
+ (nullable NSArray<DSDrawingStyle*> *)getAllDrawingStyles;
```
2. 
```swift
class func getAllDrawingStyles() -> [DSDrawingStyle]
```

**Return Value**

An array that contains all available DrawingStyles.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
NSArray<DSDrawingStyle*> *styles = [DSDrawingStyleManager getAllDrawingStyles];
```
2. 
```swift
let styles = DrawingStyleManager.getAllDrawingStyles()
```
