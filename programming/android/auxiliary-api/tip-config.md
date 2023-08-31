---
layout: default-layout
title: TipConfig - Dynamsoft Core Module Android Edition API Reference
description: The class TipConfig of Dynamsoft Core Module represents the configurations of tip, including the top left point, width, duration, and coordinate base.
keywords: tip config, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# TipConfig

The `TipConfig` class defines the configurations of tip, including the top left point, width, duration, and coordinate base.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class TipConfig
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`topLeftPoint`](#topleftpoint) | *CGPoint* | The top left point of the tip area. |
| [`width`](#width) | *NSInteger* | The width of the tip area. |
| [`duration`](#duration) | *NSInteger* | The duration of each tip message will be displayed. |
| [`coordinateBase`](#coordinatebase) | *EnumCoordinateBase* | The coordinate base of the tip message. |

## Methods

| Method | Description |
|------- |-------------|
| [`TipConfig`](#tipconfig) | Create an instance of `TipConfig` with default configurations. |
| [`TipConfig(topLeftPoint,width,duration,CoordinateBase)`](#tipconfigtopleftpointwidthdurationcoordinatebase) | Create an instance of `TipConfig`. |

### topLeftPoint

The top left point of the tip area.

```java
Point topLeftPoint;
```

### width

The width of the tip area.

```java
int width;
```

### duration

The duration of each tip message will be displayed.

```java
int duration;
```

### coordinateBase

The coordinate base of the tip message.

```java
EnumCoordinateBase CoordinateBase;
```

### TipConfig

Create an instance of TipConfig with default configurations.

```java
void TipConfig();
```

**Return Value**

An instance of `TipConfig`.

### TipConfig(topLeftPoint,width,duration,CoordinateBase)

Create an instance of TipConfig.

```java
void TipConfig(Point topLeftPoint, int width, int duration, EnumCoordinateBase CoordinateBase);
```

**Parameters**

`topLeftPoint`: The top left point of the tip area.  
`width`: The width of the tip area.  
`duration`: The duration of each tip message will be displayed.  
`coordinateBase`: The coordinate base of the tip message.

**Return Value**

An instance of `TipConfig`.
