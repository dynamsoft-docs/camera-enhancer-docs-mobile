---
layout: default-layout
title: DSTipConfig - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSTipConfig of DynamsoftCameraEnhancer represents the configurations of tip, including the top left point, width, duration, and coordinate base.
keywords: tip config, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSTipConfig

The `DSTipConfig` class defines the configurations of tip, including the top left point, width, duration, and coordinate base.

## Definition

*Assembly:* DynamsoftCore.xcframework

```objc
@interface DSTipConfig : NSObject
```

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSTipConfig : NSObject
```
2. 
```swift
class TipConfig : NSObject
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`topLeftPoint`](#topleftpoint) | *CGPoint* | The top left point of the tip area. |
| [`width`](#width) | *NSInteger* | The width of the tip area. |
| [`duration`](#duration) | *NSInteger* | The duration of each tip message will be displayed. |
| [`coordinateBase`](#coordinatebase) | *DSCoordinateBase* | The coordinate base of the tip message. |

## Methods

| Method | Description |
|------- |-------------|
| [`init`](#init) | Create an instance of TipConfig with default configurations. |
| [`initWithCoordinates`](#initwithcoordinates) | Create an instance of TipConfig. |

### topLeftPoint

The top left point of the tip area.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, assign) CGPoint topLeftPoint;
```
2. 
```swift
var topLeftPoint: CGPoint { get set }
```

## width

The width of the tip area.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, assign) NSInteger width;
```
2. 
```swift
var width: Int { get set }
```

## duration

The duration of each tip message will be displayed.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, assign) NSInteger duration;
```
2. 
```swift
var duration: Int { get set }
```

## coordinateBase

The coordinate base of the tip message.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, assign) EnumCoordinateBase coordinateBase;
```
2. 
```swift
var coordinateBase: EnumCoordinateBase { get set }
```

## init

Create an instance of TipConfig with default configurations.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)init;
```
2. 
```swift
init()
```

**Return Value**

An instance of `TipConfig`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
TipConfig *config = [[TipConfig alloc] init];
```
2. 
```swift
let config = TipConfig()
```

## initWithCoordinates

Create an instance of TipConfig.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (instancetype)initWithCoordinates:(CGPoint)topLeftPoint
                             width:(NSInteger)width
                          duration:(NSInteger)duration
                  coordinateBase:(EnumCoordinateBase)coordinateBase;
```
2. 
```swift
init(topLeftPoint: CGPoint, width: Int, duration: Int, coordinateBase: EnumCoordinateBase)
```

**Parameters**

`topLeftPoint`: The top left point of the tip area.

`width`: The width of the tip area.

`duration`: The duration of each tip message will be displayed.

`coordinateBase`: The coordinate base of the tip message.

**Return Value**

An instance of `TipConfig`.

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
TipConfig *config = [[TipConfig alloc] initWithCoordinates:CGPointMake(0, 0) width:100 duration:5 coordinateBase:BaseTopLeft];
```
2. 
```swift
let config = TipConfig(topLeftPoint: CGPoint(x: 0, y: 0), width: 100, duration: 5, coordinateBase: .topLeft)
```
