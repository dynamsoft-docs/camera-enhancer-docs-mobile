---
layout: default-layout
Title: Note - Dynamsoft Core Module Android Edition API Reference
Description: The class DSNote of Dynamsoft Core Module represents a note, which contains a key and content.
Keywords: note, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSNote

The `DSNote` class represents a note, which contains a key and content.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class Note
```
2. 
```kotlin
class Note
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`name`](#name) | *NSString \** | Set/get the name of the Note. |
| [`content`](#content) | *NSString \** | Set/get the content of the Note. |

### name

Set/get the name of the Note.

```java
@property(nonatomic, copy) NSString *name;
```
2. 
```kotlin
var name: String? { get set }
```

### content

Set/get the content of the Note.

```java
@property(nonatomic, copy) NSString *content;
```
2. 
```kotlin
var content: String? { get set }
```
