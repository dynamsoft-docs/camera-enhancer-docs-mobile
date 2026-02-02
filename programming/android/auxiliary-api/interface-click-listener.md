---
layout: default-layout
title: DrawingItemClickListener - Dynamsoft Camera Enhancer Android Edition API Reference
description: The interface that includes methods for monitoring the click events.
keywords: Click listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DrawingItemClickListener

The `DrawingItemClickListener` interface includes methods for monitoring the click events of the [`DrawingItems`](drawingitem.md).

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
interface DrawingItemClickListener
```

## Methods

### onClicked

The method for monitoring the click events of the [`DrawingItems`](drawingitem.md).

```java
void onClicked(DrawingItem clickedItem);
```

**Parameters**

`clickedItem`: The clicked `DrawingItem`.
