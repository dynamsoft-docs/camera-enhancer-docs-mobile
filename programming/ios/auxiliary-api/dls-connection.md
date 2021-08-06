---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS iDCEDLSConnectionParameters Class
description: This is the documentation - iOS iDCEDLSConnectionParameters Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS iDCEDLSConnectionParameters Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS iDCEDLSConnectionParameters Class
---

# iDCEDLSConnectionParameters

Defines a struct to configure the parameters to connect to the Dynamsoft License Server.

| Attribute Name | Type |
|------|------|
| [`mainServerURL`](#mainserverurl) | NSString* |
| [`standbyServerURL`](#standbyserverurl) | NSString* |
| [`organizationID`](#organizationid) | NSString* |
| [`handshakeCode`](#handshakecode) | NSString* |
| [`sessionPassword`](#sessionpassword) | NSString* |
| [`chargeWay`](#chargeway) | EnumDMChargWay |
| [`UUIDGenerationMethod`](#uuidgenerationmethod) | EnumDMUUIDGenerationMethod |
| [`maxBufferDays`](#maxbufferdays) | NSInteger |
| [`limitedLicenseModules`](#limitedlicensemodules) | NSArray* |
| [`products`](#products) | NSInteger |

## mainServerURL

The URL of the Dynamsoft License Server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```objectivec
NSString* mainServerURL
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

```objectivec
NSString* standbyServerURL
```

## organizationID

Set the organization ID.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```objectivec
NSString* organizationID
```

## handshakeCode

The handshake code.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```objectivec
NSString* handshakeCode
```

## sessionPassword

The session password of the handshake code set in Dynamsoft License Server.

**Value Range**

Any string value

**Default Value**

null

**Code Snippet**

```objectivec
NSString* sessionPassword
```

## chargeWay

Set the charge way.

**Value Range**

Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html) Enumeration items.

**Default Value**

DM_CW_AUTO

**Code Snippet**

```objectivec
EnumDMChargeWay chargeWay
```

**See Also**

[`EnumDMChargeWay`]({{ site.enumerations }}dmchargeway.html)

## UUIDGenerationMethod

Set the method to generate UUID.

**Value Range**

Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html) Enumeration items.

**Default Value**

DM_UUIDGM_RANDOM

**Code Snippet**

```objectivec
EnumDMUUIDGenerationMethod UUIDGenerationMethod
```

**See Also**

[`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}dmuuidgeneration.html)

## maxBufferDays

Set the max days to buffer the license info.

**Value Range**

[7,0x7fffffff]  

**Default Value**

7

**Code Snippet**

```objectivec
NSInteger maxBufferDays
```

## limitedLicenseModules

Set the count of license modules to use.

```objectivec
NSArray* limitedLicenseModules
```

## products

Set the products. This is a combined value of Product Enumration items.

**Value Range**

Any one of the [`EnumProduct`]({{ site.enumerations }}enumproduct.html) Enumeration items.

**Code Snippet**

```objectivec
NSInteger products
```

**See Also**

[`EnumProduct`]({{ site.enumerations }}enumproduct.html)
