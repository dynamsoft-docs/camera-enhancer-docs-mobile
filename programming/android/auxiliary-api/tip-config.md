---
layout: default-layout
Title: TipConfig - Dynamsoft Core Module Android Edition API Reference
Description: The class DSTipConfig of Dynamsoft Core Module represents the configurations of tip, including the top left point, width, duration, and coordinate base.
Keywords: tip config, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSTipConfig

The `DSTipConfig` class defines the configurations of tip, including the top left point, width, duration, and coordinate base.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class TipConfig
```

```java
class TipConfig
```
2. 
```kotlin
class TipConfig
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

```java
@property(nonatomic, assign) CGPoint topLeftPoint;
```
2. 
```kotlin
var topLeftPoint: CGPoint { get set }
```

## width

The width of the tip area.

```java
@property(nonatomic, assign) NSInteger width;
```
2. 
```kotlin
var width: Int { get set }
```

## duration

The duration of each tip message will be displayed.

```java
@property(nonatomic, assign) NSInteger duration;
```
2. 
```kotlin
var duration: Int { get set }
```

## coordinateBase

The coordinate base of the tip message.

```java
@property(nonatomic, assign) EnumCoordinateBase coordinateBase;
```
2. 
```kotlin
var coordinateBase: EnumCoordinateBase { get set }
```

## init

Create an instance of TipConfig with default configurations.

```java
- (instancetype)init;
```
2. 
```kotlin
init()
```

**Return Value**

An instance of `TipConfig`.

**Code Snippet**

```java
TipConfig *config = [[TipConfig alloc] init];
```
2. 
```kotlin
let config = TipConfig()
```

## initWithCoordinates

Create an instance of TipConfig.

```java
- (instancetype)initWithCoordinates:(CGPoint)topLeftPoint
                             width:(NSInteger)width
                          duration:(NSInteger)duration
                  coordinateBase:(EnumCoordinateBase)coordinateBase;
```
2. 
```kotlin
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

```java
TipConfig *config = [[TipConfig alloc] initWithCoordinates:CGPointMake(0, 0) width:100 duration:5 coordinateBase:BaseTopLeft];
```
2. 
```kotlin
let config = TipConfig(topLeftPoint: CGPoint(x: 0, y: 0), width: 100, duration: 5, coordinateBase: .topLeft)
```
