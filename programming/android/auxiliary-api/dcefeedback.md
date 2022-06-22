---
layout: default-layout
title: DCEFeedback Class - Dynamsoft Camera Enhancer
description: This is the documentation - Android DCEFeedback Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android, DCEFeedback
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DCEFeedback Class
---

# DCEFeedback

| Method | Description |
| ------ | ----------- |
| `vibrate` | Trigger a vibration when the methoded is called. |
| `beep` | Trigger a beep when the methoded is called. |

## vibrate

Trigger a vibration when the methoded is called.

```java
static void vibrate(Context context)
```

**Code Snippet**

```java
DCEFeedback.vibrate(MainActivity.this);
// For example, if `vibrate` is called in the TextResultCallback of DBR, the device will trigger a vibration each time when barcode result is detected.
mReader.setTextResultListener(new TextResultListener() {
    @Override
    public void textResultCallback(int id, ImageData imageData, TextResult[] textResults) {
        ...
        DCEFeedback.vibrate(MainActivity.this);
    }
});
```

## beep

Trigger a beep when the methoded is called.

```java
static void beep(Context context)
```

**Code Snippet**

```java
DCEFeedback.beep(MainActivity.this);
// For example, if `beep` is called in the TextResultCallback of DBR, the device will trigger a beep each time when barcode result is detected.
mReader.setTextResultListener(new TextResultListener() {
    @Override
    public void textResultCallback(int id, ImageData imageData, TextResult[] textResults) {
        ...
        DCEFeedback.beep(MainActivity.this);
    }
});
```
