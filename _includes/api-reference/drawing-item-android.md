


&nbsp;

## getDrawingStyleId

```java
public int getDrawingStyleId();
```

**Return Value**

An int value that representing the style ID.

**Code Snippet**

```java
int styleId = drawingItem.getDrawingStyleId();
```

&nbsp;

## setDrawingStyleId

```java
public void setDrawingStyleId(int style);
```

**Parameters**

`style`: An int value that representing the style ID.

**Code Snippet**

```java
drawingItem.setDrawingStyleId(0);
```

&nbsp;

## getState

```java
public EnumDrawingItemState getState();
```

**Return Value**

The state of the drawing item. View all available drawing item states in [`EnumDrawingItemState`]().

**Code Snippet**

```java
EnumDrawingItemState state = drawingItem.getState();
```

&nbsp;

## setState

```java
public void setState(EnumDrawingItemState state);
```

**Parameters**

`state`: The state of the drawing item. View all available drawing item states in [`EnumDrawingItemState`]().

**Code Snippet**

```java
drawingItem.setState(EnumDrawingItemState.DIS_SELECTED)
```

&nbsp;

## getCoordinateSystem

```java
public EnumCoordinateSystem getCoordinateSystem();
```

**Return Value**

The coordinate system of the drawing item. It can be the image coordinate or the view coordinate.

**Code Snippet**

```java
EnumCoordinateSystem coordinateSystem = drawingItem.getCoordinateSystem();
```

&nbsp;

## setCoordinateSystem

```java
public void setCoordinateSystem(EnumCoordinateSystem coordinateSystem);
```

**Parameters**

`coordinateSystem`: the coordinate system of the drawing item. It can be the image coordinate or the view coordinate.

**Code Snippet**

```java
drawingItem.setCoordinateSystem(EnumCoordinateSystem.CS_IMAGE);
```

&nbsp;
