---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android DMDLSConnectionParameters Class
description: This is the documentation - Android DMDLSConnectionParameters Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android DMDLSConnectionParameters Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android DMDLSConnectionParameters Class
---

# com.dynamsoft.dce.DMDLSConnectionParameters

`DMDLSConnectionParameters` is the class that defines a struct to configure the parameters to connect to the Dynamsoft License Server.

Java:

```Java
private com.dynamsoft.dce.DMDLSConnectionParameters dceParameters;
dceParameters = new com.dynamsoft.dce.DMDLSConnectionParameters();
```

Kotlin:

```kotlin
private var dceParameters: com.dynamsoft.dce.DMDLSConnectionParameters? = null
dceParameters = com.dynamsoft.dce.DMDLSConnectionParameters()
```

| Attribute Name | Type |
| -------------- | ---- |
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

The URL of the Dynamsoft License Server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

Java:

```java
dceParameters.mainServerURL = "";
```

Kotlin:

```kotlin
dceParameters!!.mainServerURL = ""
```

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft License Servers for online verification.

## standbyServerURL

The URL of the standby Dynamsoft License Server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

Java:

```java
dceParameters.standbyServerURL = "";
```

Kotlin:

```kotlin
dceParameters!!.standbyServerURL = ""
```

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft License Servers for online verification.

## handshakeCode

The handshake code.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

Java:

```java
dceParameters.handshakeCode = "";
```

Kotlin:

```kotlin
dceParameters!!.handshakeCode = ""
```

## organizationID

The organization ID

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

Java:

```java
dceParameters.organizationID = "";
```

Kotlin:

```kotlin
dceParameters!!.organizationID = ""
```

## sessionPassword

The session password of the handshake code set in Dynamsoft License Server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

Java:

```java
dceParameters.sessionPassword = "";
```

Kotlin:

```kotlin
dceParameters!!.sessionPassword = ""
```

## uuidGenerationMethod

Sets the method to generate UUID.

**Value Range**

Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html) Enumeration items.

**Default Value**

DM_UUIDGM_RANDOM

**Code Snippet**

Java:

```java
dceParameters.uuidGenerationMethod = int;
```

Kotlin:

```kotlin
dceParameters!!.uuidGenerationMethod = int
```

**See Also**

[`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html)

## maxBufferDays

Sets the max days to buffer the license info.

**Value Range**

[7,0x7fffffff]  

**Default Value**

7

**Code Snippet**

Java:

```java
dceParameters.maxBufferDays = int;
```

Kotlin:

```kotlin
dceParameters!!.maxBufferDays = int
```

## chargeWay

Sets the charge way.

**Value Range**

Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html) Enumeration items.

**Default Value**

DM_CW_AUTO

**Code Snippet**

Java:

```java
dceParameters.chargeWay = int;
```

Kotlin:

```kotlin
dceParameters!!.chargeWay = int
```

**See Also**

[`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html)

## products

Set the products. This is a combined value of Product Enumration items.

**Value Range**

Any one of the [`EnumProduct`]({{ site.enumerations }}enumproduct.html) Enumeration items.

**Code Snippet**

Java:

```java
dceParameters.products = int;
```

Kotlin:

```kotlin
dceParameters!!.products = int
```

**See Also**

[`EnumProduct`]({{ site.enumerations }}enumproduct.html)
