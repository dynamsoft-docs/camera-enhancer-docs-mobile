---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS TextDrawingItem Class
description: This is the documentation - iOS TextDrawingItem Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS, TextDrawingItem
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS TextDrawingItem Class
---

# TextDrawingItem

`TextDrawingItem` is a subclass of `DrawingItem`. Dynamsoft Camera Enhancer will draw the `TextDrawingItem` on the UI if it is created and added to the `DCECameraView` or `DCEImageEditorView`.

```objc
@interface TextDrawingItem (DrawingItem)
```

&nbsp;

## initWithText

The constructor of `TextDrawingItem`. Initialize the instance of `TextDrawingItem`.

```objc
- (instancetype) initWithText:(NSString*)text textRect(CGRect)textRect;
```

**Parameters**

`text`: The text of the `TextDrawingItem`.
`textRect`: The `CGRect` that indicates the location of the `TextDrawingItem`.

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

## text

The property that indicates the text of the `TextDrawingItem`.

```objc
@property (assign, nonatomic, readonly) NSString* text;
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

## textRect

The `CGRect` property that indicates the location of the `TextDrawingItem`.

```objc
@property (assign, nonatomic, readonly) CGRect textRect;
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
