---
layout: default-layout
title: Dynamsoft Camera Enhancer JavaScript API - Main Page
description: This is the main page of Dynamsoft Camera Enhancer JavaScript SDK Auxiliary.
keywords: camera enhancer, auxiliary, javascript, js
needAutoGenerateSidebar: true
needGenerateH3Content: true
noTitleIndex: true
breadcrumbText: Auxiliary
---

# Auxiliary APIs

| API Name | Description |
|---|---|
| [getVersion()](auxiliary.md#getversion) | Returns the version of the library. |
| [detectEnvironment()](auxiliary.md#detectenvironment) | Returns a report on the current running environments. |

## getVersion

Returns the version of the library.

```typescript
getVersion(): string
```

**Parameters**

None.

**Return value**

The version string of the library.

## detectEnvironment

Returns a report (in JSON) on the current running environments.

```typescript
detectEnvironment(): any
```

**Parameters**

None.

**Return value**

A JSON object about the running environment. For example

```js
{
    "wasm": true,
    "worker": true,
    "getUserMedia": true,
    "camera": true,
    "browser": "Chrome",
    "version": 90,
    "OS": "Windows"
}
```
