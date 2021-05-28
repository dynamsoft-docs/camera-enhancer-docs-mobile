---
layout: default-layout
title: Dynamsoft Camera Enhancer - Android CameraLTSConnectionParameters Class
description: This is the documentation - Android CameraLTSConnectionParameters Class page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Android CameraLTSConnectionParameters Class
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android CameraLTSConnectionParameters
---

# DMLTSConnectionParameters

`DMLTSConnectionParameters` is the class that defines a struct to configure the parameters to connect to the license tracking server.

## Method

| Name | Type |
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

### mainServerURL

The URL of the license tracking server.

```java
String com.dynamsoft.dce.DMLTSConnectionParameters.mainServerURL
```

- **Value range**
    Any string value

- **Default value**
    null

- **Remarks**
    If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

### standbyServerURL

The URL of the standby license tracking server.

```java
String com.dynamsoft.dce.DMLTSConnectionParameters.standbyServerURL
```

- **Value range**
    Any string value

- **Default value**
    null

- **Remarks**
    If you choose "Dynamsoft-hosting", then no need to change the value of MainServerURL and StandbyServerURL. When both are set to null (default value), it will connect to Dynamsoft's license tracking servers for online verification.

### handshakeCode

The handshake code.

```java
String com.dynamsoft.dce.DMLTSConnectionParameters.handshakeCode
```

- **Value range**
    Any string value

- **Default value**
    null

### organizationID

The organization ID

```java
String com.dynamsoft.dce.DMLTSConnectionParameters.organizationID
```

- **Value range**
    Any string value

- **Default value**
    null

### sessionPassword

The session password of the handshake code set in license tracking server.

```java
String com.dynamsoft.dce.DMLTSConnectionParameters.sessionPassword
```

- **Value range**
    Any string value

- **Default value**
    null

### uuidGenerationMethod

Sets the method to generate UUID.

```java
int com.dynamsoft.dce.DMLTSConnectionParameters.uuidGenerationMethod
```

- **Value range**
    Any one of the [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}other-enums.html#dm_uuidgenerationmethod) Enumeration items.

- **Default value**
    DM_UUIDGM_RANDOM

- **See also**  
    [`EnumDMUUIDGenerationMethod`]({{ site.enumerations }}other-enums.html#dm_uuidgenerationmethod)

### maxBufferDays

Sets the max days to buffer the license info.

```java
int com.dynamsoft.dce.DMLTSConnectionParameters.maxBufferDays
```

- **Value range**
    [7,0x7fffffff]  

- **Default value**
    7

### limitedLicenseModules

Sets the license modules to use.

```java
List<Integer> com.dynamsoft.dce.DMLTSConnectionParameters.limitedLicenseModules
```

- **Value range**
    A list of the [`EnumDMLicenseModule`]({{ site.enumerations }}other-enums.html#dm_licensemodule) Enumeration items.

- **Default value**
    null

- **See also**  
    [`EnumDMLicenseModule`]({{ site.enumerations }}other-enums.html#dm_licensemodule)

### chargeWay

Sets the charge way.

```java
int com.dynamsoft.dce.DMLTSConnectionParameters.chargeWay
```

- **Value range**
    Any one of the [`EnumDMChargeWay`]({{ site.enumerations }}other-enums.html#dm_chargeWay) Enumeration items.

- **Default value**
    DM_CW_AUTO

- **See also**  
    [`EnumDMChargeWay`]({{ site.enumerations }}other-enums.html#dm_chargeWay)
