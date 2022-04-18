---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DrawingStyleManager Class
description: This is the documentation - iOS DrawingStyleManager Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, DrawingStyleManager
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DrawingStyleManager Class
---

# DrawingStyleManager

&nbsp;

## getDrawingStyle

Get the `DrawingStyle` instance with the style ID.

```objc
+(DrawingStyle*)getDrawingStyle:(NSInteger)styleId;
```

**Parameters**

`styleId`: The ID of the target `DrawingStyle`.

**Return Value**

An instance of `DrawingStyle`.

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

**Remarks**

There are 5 preset types of drawing styles.

| ID | Style Name |
| -- | ---------- |
| 0 | `DEFAULT_STYLE_ID_0` |
| 1 | `DEFAULT_STYLE_ID_1` |
| 2 | `DEFAULT_STYLE_ID_2` |
| 3 | `DEFAULT_STYLE_ID_3` |
| 4 | `DEFAULT_STYLE_ID_4` |

&nbsp;

## createDrawingStyle

Create a user-defined `DrawingStyle` instance.

```objc
+(NSInteger)createDrawingStyle:(UIColor*)strokeColor strokeWidth:(CGFloat)strokeWidth 
fillColor:(UIColor*) fillColor
```

**Parameters**

`strokeColor`: The stroke colour.
`strokeWidth`: The width of the stroke.
`fillColor`: The fill colour.
`textColor`: The text colour.
`fontSize`: The font size.
`fontFamily`: The font family.

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
