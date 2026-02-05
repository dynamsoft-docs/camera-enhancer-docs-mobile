---
layout: default-layout
title: DrawingItem - DynamsoftCameraEnhancer Android Edition API Reference
description: The class DrawingItem of DynamsoftCameraEnhancer represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.
keywords: drawing item, Java, Kotlin
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# DrawingItem

The `DrawingItem` class represents a base class for drawing items, which can be added to drawing layers to draw basic graphics on the view.

## Definition

*Assembly:* DynamsoftCaptureVisionBundle.aar

*Namespace:* com.dynamsoft.dce

```java
class DrawingItem
```

## Methods

| Method | Description |
|------- |-------------|
| [`setDrawingStyleId`](#setdrawingstyleid) | Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer. |
| [`getDrawingStyleId`](#getdrawingstyleid) | Get the DrawingStyle of the `DrawingItem`. |
| [`setState`](#setstate) | Set the state of the `DrawingItem`. |
| [`getState`](#getstate) | Get the state of the `DrawingItem`. |
| [`getCoordinateBase`](#getcoordinatebase) | Get the coordinate base of the `DrawingItem`. The coordinate base is image by default. |
| [`getMediaType`](#getmediatype) | Get the media type of the `DrawingItem`. |
| [`addNote`](#addnote) | Add a note to the `DrawingItem`. |
| [`getNote`](#getnote) | Get the specified `Note`. |
| [`hasNote`](#hasnote) | Check whether the specified Note exists. |
| [`updateNote`](#updatenote) | Update the content of the specified `Note`. |
| [`deleteNote`](#deletenote) | Remove the specified `Note` with the specified name. |
| [`getAllNotes`](#getallnotes) | Get all `Notes` of this DrawingItem. |
| [`clearNotes`](#clearnotes) | Remove all `Notes` of this DrawingItem. |

### setDrawingStyleId

Set the `DrawingStyle` of the `DrawingItem`. If a `DrawingItem` holds a drawing style ID, it will not use the default style of its layer.

```java
void setDrawingStyleId(int style){}
```

**Parameters**

`style`: Specifiy a style ID for the `DrawingItem`.

### getDrawingStyleId

Get the `DrawingStyle` of the `DrawingItem`.

```java
int getDrawingStyleId(){}
```

**Return Value**

The style ID of the `DrawingItem`.

### setState

Set the state of the `DrawingItem`.

```java
void setState(@EnumDrawingItemState int state){}
```

**Parameters**

`state`: The state of the `DrawingItem`.

### getState

The state of the `DrawingItem`.

```java
@EnumDrawingItemState int getState(){}
```

**Return Value**

The state of the `DrawingItem`.

### getCoordinateBase

Get the coordinate base of the `DrawingItem`. The coordinate base is image by default.

```java
@EnumCoordinateBase int getCoordinateBase(){}
```

**Return Value**

The coordinate base of the `DrawingItem`.

### getMediaType

An abstract method to get the media type of the `DrawingItem`.

```java
abstract int getMediaType(){}
```

**Return Value**

The media type of the `DrawingItem`.

### addNote

Add a note to the `DrawingItem`.

```java
void addNote(Note note, boolean replace){}
```

**Parameters**

`note`: The `Note` object to add.  
`replace`: Whether to replace the previous one when there already exists a `Note` with the same name.

### getNote

Get the specified `Note`.

```java
Note getNote(String noteName){}
```

**Parameters**

`noteName`: The name of the `Note`.

**Return Value**

The specified `Note` object.

### hasNote

Check whether the specified `Note` exists.

```java
boolean hasNote(String noteName){}
```

**Parameters**

`noteName`: The name of the `Note`.

**Return Value**

Whether the specified `Note` exists.

### updateNote

Update the content of the specified `Note`.

```java
boolean updateNote(String noteName, String content, boolean mergeContent){}
```

**Parameters**

`name`: The name of the `Note`.  
`content`: The content to add or replace with.  
`mergeContent`: If true, merge the new content to the previous content. Otherwise, replace it.

### deleteNote

Remove the specified `Note` with the specified name.

```java
void deleteNote(String noteName){}
```

**Parameters**

`name`: The name of the `Note`.

### getAllNotes

Get all `Notes` of this DrawingItem.

```java
Note[] getAllNotes(){}
```

**Return Value**

An array of `Note`.

### clearNotes

Remove all `Notes` of this DrawingItem.

```java
void clearNotes(){}
```
