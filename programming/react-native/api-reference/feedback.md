---
layout: default-layout
title: FeedBack Class - Dynamsoft Capture Vision React Native
description: FeedBack class of Dynamsoft Capture Vision React Native provides API to control the haptic feedback features of a phone.
keywords: haptic, feedback, barcode reader, React Native, capture vision
needGenerateH3Content: true
needAutoGenerateSidebar: true
noTitleIndex: true
---

# FeedBack

The `FeedBack` class allows you to control the haptic feedback features so that the phone can either beep or vibrate when a result is found.

## Definition

*Assembly:* dynamsoft-capture-vision-react-native

```js
class FeedBack
```

## Methods

### beep

Plays a beep sound when a captured result is found.

```js
static beep(): void
```

### vibrate

Triggers a vibration when a captured result is found.

```js
static vibrate(): void
```
