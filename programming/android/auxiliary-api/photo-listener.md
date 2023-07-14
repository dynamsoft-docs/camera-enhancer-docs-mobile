---
layout: default-layout
Title: PhotoListener - Dynamsoft Core Module Android Edition API Reference
Description: The protocol DSPhotoListener of Dynamsoft Core Module defines the methods for monitoring the photo output.
Keywords: photo listener, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSPhotoListener

The `DSPhotoListener` protocol defines the methods for monitoring the photo output.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
interface PhotoListener
```
2. 
```kotlin
protocol PhotoListenerProtocol
```

## Methods
| Method | Description |
|------- |-------------|
| [`onPhotoOutput`](#onphotooutput) | The method for monitoring the photo output. |

### onPhotoOutput

The method for monitoring the photo output.

```java
- (void)onPhotoOutput:(NSData *)jpegBytes;
```
2. 
```kotlin
func onPhotoOutput(_ jpegBytes: Data)
```

**Parameters**

`jpegBytes`: The captured photo as JPEG bytes.

**Code Snippet**

```java
[listener onPhotoOutput:jpegData];
```
2. 
```kotlin
listener.onPhotoOutput(jpegData)
```
