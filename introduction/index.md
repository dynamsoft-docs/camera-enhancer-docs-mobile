---
layout: default-layout
title: Dynamsoft Camera Enhancer - Introduction
description: This is the documentation - introduction page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, introduction
needAutoGenerateSidebar: true
breadcrumbText: Introduction
---

# Overview of Dynamsoft Camera Enhancer

Dynamsoft Camera Enhancer (DCE) is a software development kit (SDK) that integrates camera control and video frame pretreatment capability. By using DCE camera controlling module, users can acquire higher quality video frames. In the meanwhile, DCE also enables users to make immediate pretreatment on the video frames captured by the camera. Users can embed DCE in all kinds of camera-related applications such as **scanning, barcode decoding and character recognition** to improve their performance.

## Main features

By using DCE, users can embed a multifunctional camera module with a few lines of code in their applications. This camera module can:

- Speed up the video stream processing.
- Enhance the capture and transfer of **high-quality frames**.
- Reduce the misreading rate.
- Intelligently crop the most valuable area from each frame.
- Automatically zoom in to approach the target position.
- Easily control the camera settings.

The following content illustrates the key functions and algorithms. By understanding these functions and algorithms, users can make good use of DCE features on creating their personalized camera module which fulfills the requirements of the applications.

1. **Frame list** - the administrator of video frames

    DCE frame list is the key function that speeds up frame acquisition. It also acts as the administrator that taking over the video frames processed by other DCE functions. The main responsibility of the DCE frame list is to:
    - Take over all the processed video frames.
    - Temporarily store the video frames.
    - Enable the application to fetch frames immediately.
    - Optimize the timing out system.

    DCE frame list reduces the waiting time on fetching frames. For example, in the barcode decoding process, when a decoder finishes decoding on the current frame, it has to acquire a new frame from the camera. Limited by the frame rate of the camera, this process will take a little time. However, If DCE is activated, instead of waiting for the new frames from the camera, decoders can fetch frames from the DCE frame list directly.

    <div align="center">
        <p><img src="overview/assets/DCE-framelist.png" width="70%" alt="DCE frame list"></p>
        <p>DCE frame list</p>
    </div>

    DCE frame list also provides a new solution on timing out. Users can end the current process immediately when the DCE frame list is filled up. This setting can prevent the application from consuming too much time processing the knotty frames.

2. **Fast mode**

    DCE fast mode is processing the frames by cropping them and keep the valuable parts only. It is reducing the size of the frames so that the time consumption on scanning each frame will be reduced. If the fast mode is enabled, frames will be cut into small pieces before transferred to the application. DCE has four different cropping modes and they will be implemented periodically.

    <div align="center">
        <p><img src="overview/assets/Fast-mode.png" width="70%" alt="Fast-mode"></p>
        <p>How fast mode is cropping frames</p>
    </div>

3. **Frame filter**

    Frame filter is designed to filter out high-quality frames and transfer them to the frame list. What DCE frame filter do is to:

    - Discard all the frames if the device is detected to be shaking.
    - Make evaluations on each frame to filter out high-quality frames.

    Sensor filter is available for mobile devices and in the meanwhile, frame sharpness filter can be enabled on all kinds of devices. By making restrictions on video frame sources can prevent the applications from processing the blurry frame and improve the working efficiency and accuracy.

4. **Camera Control**

    DCE camera control module includes:
    - Basic camera settings
    - Camera focus settings
    - Camera zoom settings

    DCE is a highly completed camera module that provides a series of camera control APIs that help users on making personalized settings. The basic camera settings include camera state settings, torch settings, resolution settings, etc. The camera focus settings enable users to enhance the focus capability of the camera to acquire higher-quality frames. Furthermore, once an area is detected to contains target information (e.g., barcode area), the DCE autozoom settings can help the camera approaching the area.

## Programming language

Dynamsoft Camera Enhancer is now available for the following programming languages:

- Java (Android)
- Objective-C & Swift (iOS)

## User Scenarios

- Long-distance decoding

    With the help of DCE, users no longer need to manually approach the barcode area when decoding on the barcode that far from the camera. When a barcode area is found but failed to be decoded, DCE enables the camera to zoom in to the barcode area automatically. Once the barcode is decoded successfully, the zoom factor will be restored to the default value.

- Continuous Scanning

    No matter the users are decoding on the single barcode or trying to decode continuously, DCE can be the best choice to accelerate the barcode decoding process. In continuous barcode decoding works, the DCE frame list is taking over the frame source for the decoder instead of the camera. The decode restart time and timeout mechanism are greatly promoted and the total time consumption on continuous decoding is sharply reduced.

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
