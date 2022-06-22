---
layout: default-layout
title: Dynamsoft Camera Enhancer - iOS iDMLTSConnectionParameters Class
description: This is the documentation - iOS iDMLTSConnectionParameters Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, iOS iDMLTSConnectionParameters Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: iOS iDMLTSConnectionParameters Class - v1.0
---

# iDMLTSConnectionParameters

Defines a struct to configure the parameters to connect to the license tracking server.

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

The URL of the license tracking server.

```objc
NSString* mainServerURL
```

## standbyServerURL

The URL of the standby license tracking server.

```objc
NSString* standbyServerURL
```

## organizationID

Set the organization ID.

```objc
NSString* organizationID
```

## handshakeCode

The handshake code.

```objc
NSString* handshakeCode
```

## sessionPassword

The session password of the handshake code set in license tracking server.

```objc
NSString* sessionPassword
```

## chargeWay

Set the charge way.

```objc
EnumDMChargeWay chargeWay
```

## UUIDGenerationMethod

Set the method to generate UUID.

```objc
EnumDMUUIDGenerationMethod UUIDGenerationMethod
```

## maxBufferDays

Set the max days to buffer the license info.

```objc
NSInteger maxBufferDays
```

## limitedLicenseModules

Set the count of license modules to use.

```objc
NSArray* limitedLicenseModules
```

## products

Set the products. This is a combined value of Product Enumration items.

```objc
NSInteger products
```
