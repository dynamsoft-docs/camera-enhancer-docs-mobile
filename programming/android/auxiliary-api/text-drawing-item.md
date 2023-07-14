---
layout: default-layout
Title: TextDrawingItem - Dynamsoft Camera Enhancer Android Edition API Reference
Description: The class DSTextDrawingItem of Dynamsoft Camera Enhancer represents a text drawing item, which can be added to draw texts on the view.
Keywords: text drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSTextDrawingItem

The `DSTextDrawingItem` class is a subclass of `DSDrawingItem` and represents a text drawing item, which can be added to draw texts on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class TextDrawingItem extends DrawingItem
```
2. 
```kotlin
class TextDrawingItem : DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`text`](#text) | *NSString \** |Get the text content of the DSTextDrawingItem. |
| [`topLeftPoint`](#topleftpoint) | *CGPoint* |Get the top-left point of the DSTextDrawingItem. |
| [`width`](#width) | *NSInteger* |Get the width of the DSTextDrawingItem. |
| [`height`](#height) | *NSInteger* |Get the height of the DSTextDrawingItem. |

## Methods
| Method | Description |
|------- |-------------|
| [`initWithText`](#initwithtext) | Create an instance of DSTextDrawingItem. |
| [`initWithText:coordinateBase:`](#initwithtextcoordinatebase) | Create an instance of DSTextDrawingItem with coordinate base. |

### text

Get the text content of the DSTextDrawingItem.

```java
@property (nonatomic, copy, readonly) NSString *text;
```
2. 
```kotlin
var text: String { get }
```

### topLeftPoint

Get the top-left point of the DSTextDrawingItem.

```java
@property (nonatomic, readonly) CGPoint topLeftPoint;
```
2. 
```kotlin
var topLeftPoint: CGPoint { get }
```

### width

Get the width of the DSTextDrawingItem.

```java
@property (nonatomic, readonly) NSInteger width;
```
2. 
```kotlin
var width: Int { get }
```

### height

Get the height of the DSTextDrawingItem.

```java
@property (nonatomic, readonly) NSInteger height;
```
2. 
```kotlin
var height: Int { get }
```

### initWithText

Create an instance of DSTextDrawingItem.

```java
- (instancetype)initWithText:(NSString *)text
                topLeftPoint:(CGPoint)topLeftPoint
                       width:(NSInteger)width
                      height:(NSInteger)height;
```
2. 
```kotlin
init(text: String, topLeftPoint: CGPoint, width: Int, height: Int)
```
**Parameters**

`text`: The text content of the DSTextDrawingItem.  
`topLeftPoint`: The top-left point of the DSTextDrawingItem.  
`width`: The width of the DSTextDrawingItem.  
`height`: The height of the DSTextDrawingItem.  

**Return Value**

An instance of DSTextDrawingItem.

**Code Snippet**

```java
DSTextDrawingItem *item = [[DSTextDrawingItem alloc] initWithText:@"Hello, World!" topLeftPoint:CGPointMake(0, 0) width:100 height:50];
```
2. 
```kotlin
let item = TextDrawingItem(text: "Hello, World!", topLeftPoint: CGPoint(x: 0, y: 0), width: 100, height: 50)
```

### initWithText:coordinateBase:

Create an instance of DSTextDrawingItem with coordinate base.

```java
- (instancetype)initWithText:(NSString *)text
                topLeftPoint:(CGPoint)topLeftPoint
                       width:(NSInteger)width
                      height:(NSInteger)height
              coordinateBase:(DSCoordinateBase)coordinateBase;
```
2. 
```kotlin
init(text: String, topLeftPoint: CGPoint, width: Int, height: Int, coordinateBase: CoordinateBase)
```

**Parameters**

`text`: The text content of the DSTextDrawingItem.  
`topLeftPoint`: The top-left point of the DSTextDrawingItem.  
`width`: The width of the DSTextDrawingItem.  
`height`: The height of the DSTextDrawingItem.  
`coordinateBase`: The coordinate base of the DrawingItem.  

**Return Value**

An instance of `DSTextDrawingItem`.

**Code Snippet**

```java
DSTextDrawingItem *item = [[DSTextDrawingItem alloc] initWithText:@"Hello, World!" topLeftPoint:CGPointMake(0, 0) width:100 height:50 coordinateBase:DSCoordinateBase_View];
```
2. 
```kotlin
let item = TextDrawingItem(text: "Hello, World!", topLeftPoint: CGPoint(x: 0, y: 0), width: 100, height: 50, coordinateBase: .view)
```
