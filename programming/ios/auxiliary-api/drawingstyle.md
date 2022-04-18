---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS DrawingStyle Class
description: This is the documentation - iOS DrawingStyle Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, DrawingStyle
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS DrawingStyle Class
---

# DrawingStyle

The class of `DrawingStyle`. It stores the detailed styles of the drawing item.

```objc
class DrawingStyle 
```

| Method | Description |
| ------ | ----------- |
| `initWithId` | The constructor of the `initWithId`. |
| `id` | The id of the drawing style. |
| `strokeColor` | The stroke color of the drawing style. |
| `fillColor` | The fill color of the drawing style. |
| `textColor` | The text color of the drawing style. |
| `strokeWidth` | The stroke width of the drawing style. |
| `fontSize` | The font size of the drawing style. |
| `fontFamily` | The font-Family of the drawing style. |

&nbsp;

## initWithId

The constructor of the `DrawingStyle`.

```objc
- (instancetype)initWithId:(NSInteger)id
               strokeColor:(UIColor)strokeColor
               strokeWidth:(CGFloat)strokeWidth
                 fillColor:(UIColor)fillColor
                 textColor:(UIColor)textColor
                  fontSize:(NSInteger)fontSize
                fontFamily:(NSString*)fontFamily
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

&nbsp;

## id

The id of the drawing style.

```objc
@property (assign, nonatomic, readonly) NSInteger id;
```

&nbsp;

## strokeColor

The stroke color of the drawing style.

```objc
@property (assign, nonatomic) UIColor strokeColor;
```

&nbsp;

## fillColor

The fill color of the drawing style.

```objc
@property (assign, nonatomic) UIColor fillColor;
```

&nbsp;

## textColor

The text color of the drawing style.

```objc
@property (assign, nonatomic) UIColor textColor;
```

&nbsp;

## strokeWidth

The stroke width of the drawing style.

```objc
@property (assign, nonatomic) CGFloat strokeWidth;
```

&nbsp;

## fontSize

The font size of the drawing style.

```objc
@property (assign, nonatomic) NSInteger fontSize;
```

&nbsp;

## fontFamily

The font-Family of the drawing style.

```objc
@property (assign, nonatomic) NSString* fontFamily;
```
