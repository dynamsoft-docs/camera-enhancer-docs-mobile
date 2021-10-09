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

```Java
class com.dynamsoft.dce.DMLTSConnectionParameters
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

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```java
dceParameters.mainServerURL = "";
```

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

&nbsp;

## standbyServerURL

The URL of the standby license tracking server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```java
dceParameters.standbyServerURL = "";
```

**Remarks**

If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

&nbsp;

## handshakeCode

The handshake code.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```java
dceParameters.handshakeCode = "";
```

&nbsp;

## organizationID

The organization ID

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```java
dceParameters.organizationID = "";
```

&nbsp;

## sessionPassword

The session password of the handshake code set in license tracking server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```java
dceParameters.sessionPassword = "";
```

&nbsp;

## uuidGenerationMethod

Sets the method to generate UUID.

**Value Range**

Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html) Enumeration items.

**Default Value**

DM_UUIDGM_RANDOM

**Code Snippet**

```java
dceParameters.uuidGenerationMethod = EnumCameraDMUUIDGenerationMethod.DM_UUIDGM_RANDOM;
```

**See Also**  

[`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html)

&nbsp;


## maxBufferDays

Sets the max days to buffer the license info.

**Value Range**

[7,0x7fffffff]  

**Default Value**

7

**Code Snippet**


```java
dceParameters.maxBufferDays = 7;
```


&nbsp;

## chargeWay

Sets the charge way.

**Value Range**

Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html) Enumeration items.

**Default Value**

DM_CW_AUTO

**Code Snippet**

```java
dceParameters.chargeWay = EnumDMChargeWay.DM_CW_DEVICE_COUNT;
```

**See Also**  

[`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html)

&nbsp;

## products

Set the products. This is a combined value of Product Enumration items.

**Value Range**

Any one of the [`EnumProduct`]({{ site.enumerations }}enumproduct.html) Enumeration items.

**Code Snippet**

```java
dceParameters.products = EnumProduct.PROD_DBR;
```

**See Also**  

[`EnumProduct`]({{ site.enumerations }}enumproduct.html)
