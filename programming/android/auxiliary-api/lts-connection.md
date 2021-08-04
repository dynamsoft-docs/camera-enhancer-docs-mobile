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

# com.dynamsoft.dce.DMLTSConnectionParameters

`DMLTSConnectionParameters` is the class that defines a struct to configure the parameters to connect to the license tracking server.

Java:

```Java
private com.dynamsoft.dce.DMLTSConnectionParameters dceParameters;
dceParameters = new com.dynamsoft.dce.DMLTSConnectionParameters();
```

Kotlin:

```kotlin
private var dceParameters: com.dynamsoft.dce.DMLTSConnectionParameters? = null
dceParameters = com.dynamsoft.dce.DMLTSConnectionParameters()
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
dceParameters.mainServerURL = "";
```

Kotlin:

```kotlin
dceParameters!!.mainServerURL = ""
```

**Value Range**

Any string value

**Default Value**

null

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

## standbyServerURL

The URL of the standby license tracking server.

Java:

```java
dceParameters.standbyServerURL = "";
```

Kotlin:

```kotlin
dceParameters!!.standbyServerURL = ""
```

**Value Range**

Any string value

**Default Value**

null

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

## handshakeCode

The handshake code.

Java:

```java
dceParameters.handshakeCode = "";
```

Kotlin:

```kotlin
dceParameters!!.handshakeCode = ""
```

**Value Range**

Any string value

**Default Value**

null

## organizationID

The organization ID

Java:

```java
dceParameters.organizationID = "";
```

Kotlin:

```kotlin
dceParameters!!.organizationID = ""
```

**Value Range**

Any string value

**Default Value**

null

## sessionPassword

The session password of the handshake code set in license tracking server.

Java:

```java
dceParameters.sessionPassword = "";
```

Kotlin:

```kotlin
dceParameters!!.sessionPassword = ""
```

**Value Range**

Any string value

**Default Value**

null

## uuidGenerationMethod

Sets the method to generate UUID.

Java:

```java
dceParameters.uuidGenerationMethod = int;
```

Kotlin:

```kotlin
dceParameters!!.uuidGenerationMethod = int
```

**Value Range**

Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html) Enumeration items.

**Default Value**

DM_UUIDGM_RANDOM

**See Also**  

[`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html)

## maxBufferDays

Sets the max days to buffer the license info.

Java:

```java
dceParameters.maxBufferDays = int;
```

Kotlin:

```kotlin
dceParameters!!.maxBufferDays = int
```

**Value Range**

[7,0x7fffffff]  

**Default Value**

7

## chargeWay

Sets the charge way.

Java:

```java
dceParameters.chargeWay = int;
```

Kotlin:

```kotlin
dceParameters!!.chargeWay = int
```

**Value Range**

Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html) Enumeration items.

**Default Value**

DM_CW_AUTO

**See Also**  

[`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html)

## products

Set the products. This is a combined value of Product Enumration items.

Java:

```java
dceParameters.products = int;
```

Kotlin:

```kotlin
dceParameters!!.products = int
```

**Value Range**

Any one of the [`EnumProduct`]({{ site.enumerations }}enumproduct.html) Enumeration items.

**See Also**  

[`EnumProduct`]({{ site.enumerations }}enumproduct.html)
