---
layout: default-layout
Title: PhotoListener - Dynamsoft Core Module Android Edition API Reference
Description: The interface PhotoListener of Dynamsoft Core Module defines the methods for monitoring the photo output.
Keywords: photo listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# PhotoListener

The `PhotoListener` interface defines the methods for monitoring the photo output.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface PhotoListener
```

## Methods
| Method | Description |
|------- |-------------|
| [`onPhotoOutput`](#onphotooutput) | The method for monitoring the photo output. |

### onPhotoOutput

The method for monitoring the photo output.

```java
void onPhotoOutput(byte[] bytes);
```

**Parameters**

`bytes`: The captured photo as JPEG bytes.
