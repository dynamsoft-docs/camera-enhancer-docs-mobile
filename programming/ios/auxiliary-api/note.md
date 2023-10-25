---
layout: default-layout
title: DSNote - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSNote of DynamsoftCameraEnhancer represents a note, which contains a key and content.
keywords: note, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSNote

The `DSNote` class represents a note, which contains a key and content.

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSNote : NSObject
```
2. 
```swift
class Note : NSObject
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`name`](#name) | *NSString \** | Set/get the name of the Note. |
| [`content`](#content) | *NSString \** | Set/get the content of the Note. |

### name

Set/get the name of the Note.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, copy) NSString *name;
```
2. 
```swift
var name: String? { get set }
```

### content

Set/get the content of the Note.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property(nonatomic, copy) NSString *content;
```
2. 
```swift
var content: String? { get set }
```
