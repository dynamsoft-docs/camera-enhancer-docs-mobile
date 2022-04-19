

&nbsp;

## drawingStyleId

The property that identifies the ID of the `DrawingStyle`.

```objc
@property (assign, nonatomic) NSInteger drawingStyleId;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

&nbsp;

## state

The property that indicates the state of the `DrawingItem`. View all available `DrawingItem` states in [`EnumDrawingItemState`]({{ site.enumerations }}enum-drawing-item-state.html).

```objc
@property (assign, nonatomic) EnumDrawingItemState state;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

&nbsp;

## coordinateSystem

The property that indicates the coordinate system of the `DrawingItem`. It can be the image coordinate or the view coordinate. View all available `DrawingItem` coordinate systems in [`EnumCoordinateSystem`]({{ site.enumerations }}enum-coordinate-system.html).

```objc
@property (assign, nonatomic) EnumCoordinateSystem coordinateSystem;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

## mediaType

The property that indicates the media type of the `DrawingItem`.

```objc
@property (assign, nonatomic, readonly) EnumDrawingItemMeidaType mediaType;
```

**Code Snippet**

<div class="sample-code-prefix"></div>
>- Objective-C
>- Swift
>
>1. 
```objc

```
2. 
```swift

```

