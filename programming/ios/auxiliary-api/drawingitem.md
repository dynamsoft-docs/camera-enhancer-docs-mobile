---
layout: default-layout
title: DSDrawingItem - DynamsoftCameraEnhancer iOS Edition API Reference
description: The class DSDrawingItem of DynamsoftCameraEnhancer represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.
keywords: drawing item, objective-c, swift
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingItem

The `DSDrawingItem` class represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.

## Definition

*Assembly:* DynamsoftCore.framework

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@interface DSDrawingItem : NSObject
```
2. 
```swift
class DrawingItem : NSObject
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`drawingStyleId`](#drawingstyleid) | *NSInteger* | The DrawingStyle of the DrawingItem. If a DrawingItem holds a drawingStyleId, it will not use the default style of its layer. |
| [`state`](#state) | *DSDrawingItemState* | The state of the DrawingItem. |
| [`CoordinateBase`](#coordinatebase) | *DSCoordinateBase* | The coordinate base of the DrawingItem. The coordinate base is image by default. |

## Methods

| Method | Description |
|------- |-------------|
| [`getMediaType`](#getmediatype) | Get the media type of the DrawingItem. |
| [`addNote`](#addnote) | Add a note to the DrawingItem. |
| [`getNote`](#getnote) | Get the specified DSNote. |
| [`hasNote`](#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](#updatenote) | Update the content of the specified DSNote. |
| [`deleteNote`](#deletenote) | Remove the specified DSNote with the specified name. |
| [`getAllNotes`](#getallnotes) | Get all DSNotes of this DrawingItem. |
| [`clearNotes`](#clearnotes) | Remove all DSNotes of this DrawingItem. |

### drawingStyleId

The DrawingStyle of the DrawingItem. If a DrawingItem holds a drawingStyleId, it will not use the default style of its layer.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) NSInteger drawingStyleId
```
2. 
```swift
var drawingStyleId: Int { get set }
```

### state

The state of the DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic) DSDrawingItemState state
```
2. 
```swift
var state: DSDrawingItemState { get set }
```

### CoordinateBase

The coordinate base of the DrawingItem. The coordinate base is image by default.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
@property (assign, nonatomic, readonly) DSCoordinateBase CoordinateBase
```
2. 
```swift
var CoordinateBase: DSCoordinateBase { get }
```

### getMediaType

Get the media type of the DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSDrawingItemMediaType)getMediaType;
```
2. 
```swift
func getMediaType() -> DSDrawingItemMediaType
```

### addNote

Add a note to the DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)addNote:(DSNote *)note
        replace:(bool)replace;
```
2. 
```swift
func addNote(_ note: DSNote, replace: Bool)
```
**Parameters**

`note`: The DSNote object to add.

`replace`: Whether to replace the previous one when there already exists a DSNote with the same name.

### getNote

Get the specified DSNote.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (DSNote *)getNote:(NSString *)noteName;
```
2. 
```swift
func getNote(_ noteName: String) -> DSNote?
```
**Parameters**

`noteName`: The name of the DSNote.

**Return Value**

The specified DSNote object.

### hasNote

Check whether the specified Note exists.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (bool)hasNote:(NSString *)noteName;
```
2. 
```swift
func hasNote(_ noteName: String) -> Bool
```
**Parameters**

`noteName`: The name of the DSNote.

**Return Value**

Whether the specified Note exists.

### updateNote

Update the content of the specified DSNote.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)updateNote:(NSString *)name
           content:(NSString *)content
      mergeContent:(bool)mergeContent;
```
2. 
```swift
func updateNote(_ name: String, content: String, mergeContent: Bool)
```

**Parameters**

`name`: The name of the DSNote.  
`content`: The content to add or replace with.  
`mergeContent`: If true, merge the new content to the previous content. Otherwise, replace it.

### deleteNote

Remove the specified DSNote with the specified name.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)deleteNote:(NSString *)name;
```
2. 
```swift
func deleteNote(_ name: String)
```

**Parameters**

`name`: The name of the DSNote.

### getAllNotes

Get all DSNotes of this DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (NSArray<DSNote *> *)getAllNotes;
```
2. 
```swift
func getAllNotes() -> [Note]
```

**Return Value**

An array of DSNote.

### clearNotes

Remove all DSNotes of this DrawingItem.

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc
- (void)clearNotes;
```
2. 
```swift
func clearNotes()
```
