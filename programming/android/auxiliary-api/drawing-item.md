---
layout: default-layout
Title: DrawingItem - Dynamsoft Core Module Android Edition API Reference
Description: The class DSDrawingItem of Dynamsoft Core Module represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.
Keywords: drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DSDrawingItem

The `DSDrawingItem` class represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.

## Definition

*Assembly:* package com.dynamsoft.dce

```java
class DrawingItem
```

## Attributes

| Attributes | Type | Description |
| ---------- | ---- | ----------- |
| [`drawingStyleId`](#drawingstyleid) | *NSInteger* | The DrawingStyle of the `DrawingItem`. If a `DrawingItem` holds a drawingStyleId, it will not use the default style of its layer. |
| [`state`](#state) | *DSDrawingItemState* | The state of the `DrawingItem`. |
| [`CoordinateBase`](#coordinatebase) | *DSCoordinateBase* | The coordinate base of the `DrawingItem`. The coordinate base is image by default. |

## Methods

| Method | Description |
|------- |-------------|
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`addNote`](#addnote) | Add a note to the `DrawingItem`. |
| [`getNote`](#getnote) | Get the specified DSNote. |
| [`hasNote`](#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](#updatenote) | Update the content of the specified DSNote. |
| [`deleteNote`](#deletenote) | Remove the specified DSNote with the specified name. |
| [`getAllNotes`](#getallnotes) | Get all DSNotes of this DrawingItem. |
| [`clearNotes`](#clearnotes) | Remove all DSNotes of this DrawingItem. |

### setDrawingStyleId

Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer.

```java
void setDrawingStyleId(int style){}
```

### getDrawingStyleId

Get the `DrawingStyle` of the `DrawingItem`.

```java
int getDrawingStyleId(){}
```

### getState

The state of the `DrawingItem`.

```java
@EnumDrawingItemState int getState(){}
```

### CoordinateBase

The coordinate base of the `DrawingItem`. The coordinate base is image by default.

```java
@EnumCoordinateBase int getCoordinateBase(){}
```

### getMediaType

Get the media type of the `DrawingItem`.

```java
abstract int getMediaType(){}
```

### addNote

Add a note to the `DrawingItem`.

```java
void addNote(Note note, boolean replace){}
```

**Parameters**

`note`: The DSNote object to add.  
`replace`: Whether to replace the previous one when there already exists a DSNote with the same name.

### getNote

Get the specified DSNote.

```java
Note getNote(String noteName){}
```

**Parameters**

`noteName`: The name of the DSNote.

**Return Value**

The specified DSNote object.

### hasNote

Check whether the specified Note exists.

```java
boolean hasNote(String noteName){}
```

**Parameters**

`noteName`: The name of the DSNote.

**Return Value**

Whether the specified Note exists.

### updateNote

Update the content of the specified DSNote.

```java
boolean updateNote(String noteName, String content, boolean mergeContent){}
```

**Parameters**

`name`: The name of the DSNote.  
`content`: The content to add or replace with.  
`mergeContent`: If true, merge the new content to the previous content. Otherwise, replace it.

### deleteNote

Remove the specified DSNote with the specified name.

```java
void deleteNote(String noteName){}
```

**Parameters**

`name`: The name of the DSNote.

### getAllNotes

Get all DSNotes of this DrawingItem.

```java
Note[] getAllNotes(){}
```

**Return Value**

An array of DSNote.

### clearNotes

Remove all DSNotes of this DrawingItem.

```java
void clearNotes(){}
```
