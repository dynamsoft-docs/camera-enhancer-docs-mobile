---
layout: default-layout
title: Dynamsoft Camera Enhancer - Introduction
description: This is the documentation - introduction page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, introduction
needAutoGenerateSidebar: true
breadcrumbText: Introduction
---

# Overview of Dynamsoft Camera Enhancer

Dynamsoft Camera Enhancer (DCE) is a multifunctional SDK specially designed for improving camera performance on video stream decoding. Users can deploy a camera module with just a few lines of code with the help of DCE. In this camera module, users can easily apply frame processing algorithms that improve barcode decode efficiency. Further, flexible camera controlling APIs are available as well, which promotes user experience.

## Advantages

- Accelerate on barcode reading.
  - DCE frame list improves decoding speed.
  - DCE fast mode accelerate on single barcode decoding.
- Reduce misreading rate.
  - DCE frame filter makes sure the decode accuracy and efficiency.
- Flexible camera controlling APIs.
  - All basic camera settings available.
  - Zoom and focus settings available.

## Main features

1. Frame list

    DCE frame list is able to:
    - Temporarily store video frames.
    - Reduce waiting time on restarting decode works.
    - help decoders on timing out mechanism.
    
    DCE frame list reduces waiting time on decoding. Normally, when a decoder finishes decoding on the current frame, it has to acquire a new frame from the camera. Limited by the frame rate of the camera, this process will take a little time. However, If DCE is activated, instead of waiting for the new frames from the camera, decoders can fetch frames from the DCE frame list directly. Further, the DCE frame list also helps when the decoder is blocked on decoding a certain frame. The decoder will restart the decoding process and fetch a new frame from the frame list immediately when the frame list is filled up.

    <div align="center">
        <p><img src="overview/assets/DCE-framelist.png" width="70%" alt="DCE frame list"></p>
        <p>DCE frame list</p>
    </div>

2. Fast mode

    DCE fast mode is able to:
    - Speed up single barcode decoding process
    - Improve single barcode decoding accuracy

    DCE fast mode is specially designed for single barcode decoding. If the fast mode is enabled, frames will be cut into small pieces before transferred to the decoder. DCE has four different clipping modes and they will be implemented periodically. This process sharply reduces the scan area size for decoders, which decreases the decoding time consumption.

    <div align="center">
        <p><img src="overview/assets/Fast-mode.png" width="70%" alt="Fast-mode"></p>
        <p>Fast mode clip area</p>
    </div>

3. Frame filter

    DCE frame filter is able to:
    - Skip blurry frames.
    - Improve the decoding success rate
    - Reduce misreading rate

    DCE frame filter will discard the blurry frames before decoders start decoding on the video stream. If frame filter is enabled, the filtered frames will be stored in the DCE frame list for further decode process. The DCE frame filter makes sure that the decoder works on high-quality frames. Under the frame filter mode, the decode success rate will be improved and misreading will be declined.

4. Camera Control

    DCE camera control module:
    - Enables user to make various focus settings
    - Enables camera autozoom to approach the barcode area
    - Enables user to make flexible settings on the camera

    DCE is a highly completed camera module that provides a series of camera control APIs that help users on making personalized settings. The camera control APIs include focus control, zoom control, and other basic camera control.

## Programming language

Dynamsoft Camera Enhancer is now available for the following programming languages:

- Java (Android)
- Objective-C & Swift (iOS)

## User Scenarios

- Long-distance decoding

    With the help of DCE, users no longer need to manually approach the barcode area when decoding on the barcode that far from the camera. When a barcode area is found but failed to be decoded, DCE enables the camera to zoom in to the barcode area automatically. Once the barcode is decoded successfully, the zoom factor will be restored to the default value.

- Continuous decoding

    No matter the users are decoding on the single barcode or trying to decode continuously, DCE can be the best choice to accelerate the barcode decoding process. In continuous barcode decoding works, DCE frame list is taking over the frame source for the decoder instead of the camera. The decode restart time and timeout mechanism are greatly promoted and the total time consumption on continuous decoding is sharply reduced.

- Old devices

    Bounded up with camera performance, it is always a huge challenge for barcode decoders to perform well on old devices. DCE is breaking through these hardware issues by enabling high-standard autofocus and frame filter functions. With the help of DCE, devices can immediately extract high-quality frames from the video stream and efficiently complete the barcode decoding works.

## About this documentation

This documentation aims at helping you on learning, understanding, and using Dynamsoft Camera Enhancer. In this documentation, you can find useful information that guides you step by step from installation to further development.

## Quick links

- [Programming guides]({{site.programming}})
- View APIs
  - [Android]({{site.android-api}})
  - [iOS]({{site.ios-api}})
- [Contact us]({{site.contact-us}})
