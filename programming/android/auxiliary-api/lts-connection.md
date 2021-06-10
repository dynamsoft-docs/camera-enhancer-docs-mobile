---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DMLTSConnectionParameters Class
description: This is the documentation - Android DMLTSConnectionParameters Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android DMLTSConnectionParameters Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DMLTSConnectionParameters Class
---

# DMLTSConnectionParameters

`DMLTSConnectionParameters` is the class that defines a struct to configure the parameters to connect to the license tracking server.

Java:

```Java
private com.dynamsoft.dce.DMLTSConnectionParameters dceParameters;
dceParameters = new com.dynamsoft.dce.DMLTSConnectionParameters();
```

Kotlin:

```kotlin
private var dbrParameters: com.dynamsoft.dbr.DMLTSConnectionParameters? = null
dbrParameters = com.dynamsoft.dbr.DMLTSConnectionParameters()
```

| Attribute Name | Type |
|------|------|
| [`mainServerURL`](#mainserverurl) | String |
| [`standbyServerURL`](#standbyserverurl) | String |
| [`handshakeCode`](#handshakecode) | String |
| [`organizationID`](#organizationid) | String |
| [`sessionPassword`](#sessionpassword) | String |
| [`uuidGenerationMethod`](#uuidgenerationmethod) | int |
| [`maxBufferDays`](#maxbufferdays) | int |
| [`limitedLicenseModules`](#limitedlicensemodules) | list |
| [`chargeWay`](#chargeway) | int |
| [`products`](#products) | int |

## mainServerURL

The URL of the license tracking server.

Java:

```java
dbrParameters.mainServerURL = "";
```

Kotlin:

```kotlin
dbrParameters!!.mainServerURL = ""
```

- **Value range**
    Any string value

- **Default value**
    null

- **Remarks**
    If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

## standbyServerURL

The URL of the standby license tracking server.

Java:

```java
dbrParameters.standbyServerURL = "";
```

Kotlin:

```kotlin
dbrParameters!!.standbyServerURL = ""
```

- **Value range**
    Any string value

- **Default value**
    null

- **Remarks**
    If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

## handshakeCode

The handshake code.

Java:

```java
dbrParameters.handshakeCode = "";
```

Kotlin:

```kotlin
dbrParameters!!.handshakeCode = ""
```

- **Value range**
    Any string value

- **Default value**
    null

## organizationID

The organization ID

Java:

```java
dbrParameters.organizationID = "";
```

Kotlin:

```kotlin
dbrParameters!!.organizationID = ""
```

- **Value range**
    Any string value

- **Default value**
    null

## sessionPassword

The session password of the handshake code set in license tracking server.

Java:

```java
dbrParameters.sessionPassword = "";
```

Kotlin:

```kotlin
dbrParameters!!.sessionPassword = ""
```

- **Value range**
    Any string value

- **Default value**
    null

## uuidGenerationMethod

Sets the method to generate UUID.

Java:

```java
dbrParameters.uuidGenerationMethod = int;
```

Kotlin:

```kotlin
dbrParameters!!.uuidGenerationMethod = int
```

- **Value range**
    Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html) Enumeration items.

- **Default value**
    DM_UUIDGM_RANDOM

- **See also**  
    [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html)

## maxBufferDays

Sets the max days to buffer the license info.

Java:

```java
dbrParameters.maxBufferDays = int;
```

Kotlin:

```kotlin
dbrParameters!!.maxBufferDays = int
```

- **Value range**
    [7,0x7fffffff]  

- **Default value**
    7

## chargeWay

Sets the charge way.

Java:

```java
dbrParameters.chargeWay = int;
```

Kotlin:

```kotlin
dceParameters!!.chargeWay = int
```

- **Value range**
    Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html) Enumeration items.

- **Default value**
    DM_CW_AUTO

- **See also**  
    [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html)

## products

Set the products. This is a combined value of Product Enumration items.

Java:

```java
dbrParameters.products = int;
```

Kotlin:

```kotlin
dceParameters!!.products = int
```

- **Value range**
    Any one of the [`EnumProduct`]({{ site.enumerations }}enumproduct.html) Enumeration items.

- **See also**  
    [`EnumProduct`]({{ site.enumerations }}enumproduct.html)
