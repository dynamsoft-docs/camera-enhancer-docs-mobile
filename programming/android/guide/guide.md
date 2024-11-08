---
layout: default-layout
title: Guide on Android - Dynamsoft Camera Enhancer
description: This is the documentation - Guide on Android page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Guide on Android
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Guide
permalink: /programming/android/guide/guide.html
ignore: true
---

# Dynamsoft Camera Enhancer User Guide for Android (Java)

The Dynamsoft Camera Enhancer Android SDK enables you to easily control cameras from your Android applications to stream live video and acquire realtime frames.

> **Example Usage**
>
> See how Dynamsoft Camera Enhancer helps in camera control and video recognition:
> - **Barcode scanning from video stream**: check [Dynamsoft Barcode Reader Android User Guide](https://www.dynamsoft.com/barcode-reader/docs/mobile/programming/android/user-guide.html?ver=latest)

Step-by-step guide on how to integrate Dynamsoft Camera Enhancer SDK to your Android app:

## App Prerequisites

- Supported OS: Android 5.0 (API Level 21) or higher.
- Supported ABI: **armeabi-v7a, arm64-v8a, x86 and x86_64**.
- Development Environment: Android Studio 2022.2.1 or higher.

## Build Your First Application

>Note: 
>- The following steps are completed in Android Studio 2022.2.1.

### Create a New Project

1. Open Android Studio and select New Project… in the File > New > New Project… menu to create a new project.

2. Choose the correct template for your project. In this sample, we'll use `Empty Activity`.

3. When prompted, choose your app name (`HelloWorld`) and set the Save location, Language, and Minimum SDK (21)
    >Note: With minSdkVersion set to 21, your app is available on more than 94.1% of devices on the Google Play Store (last update: March 2021).

### Include the library

1. Open the file `HelloWorld\app\build.gradle`, and add the remote repository:

   ```groovy
   repositories {
       maven {
           url "https://download2.dynamsoft.com/maven/aar"
       }
   }
   ```

2. Add reference in the dependencies:

   ```groovy
   dependencies {
       implementation 'com.dynamsoft:dynamsoftcameraenhancer:4.2.10'
       implementation 'com.dynamsoft:dynamsoftcore:3.2.30'
       implementation 'com.dynamsoft:dynamsoftlicense:3.2.20'
   }
   ```

3. Click `Sync Now`. After the synchronization completes, the SDK is added to the project.

4. import the package in the file `MainActivity.java`

    ```java
    import com.dynamsoft.dce.*;
    ```

### License Activation (Optional)

A valid license is required when using the following features:

- Frame Sharpness Filter
- Sensor Filter
- Auto Zoom
- Enhanced Focus
- Fast Mode
- Smart torch

The above features are enabled by triggering method [`enableFeatures`](../primary-api/camera-enhancer.md#enablefeatures). If you are not using these features, you can skip the license activation step.

To activate the license:

1. Include the library

   ```groovy
   dependencies {
       implementation 'com.dynamsoft:dynamsoftlicense:3.2.20'
   }
   ```

2. Initialize the license in your code.

   ```java
   LicenseManager.initLicense("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9", this, (isSuccess, error) -> {
       if (!isSuccess) {
           Log.e(TAG, "InitLicense Error: " + error);
       }
   });
   ```

>Note:
>- Network connection is required for the license to work.
>- "DLS2***" is a time-limited public trial license used in the sample.
>- You can request a 30-day offline trial license via the [Request a Trial License](https://www.dynamsoft.com/customer/license/trialLicense?product=cvs&utm_source=guide&package=android){:target="_blank"} link.

### Create Camera View

1. In the Project window, open app > res > layout > `activity_main.xml`, create a DCE camera view section under the root node.

    ```xml
    <com.dynamsoft.dce.CameraView
        android:id="@+id/cameraView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:layout_editor_absoluteX="25dp"
        tools:layout_editor_absoluteY="0dp" />
    ```

2. Initialize the camera view, and bind to the Camera Enhancer object.

    ```java
    private CameraView cameraView;
    ...
    mCameraView = findViewById(R.id.cameraView);
    ```

### Initialize the CameraEnhancer and Bind the CameraView

Create an instance of Dynamsoft Camera Enhancer

```java
CameraEnhancer mCameraEnhancer;
mCameraEnhancer = new CameraEnhancer(cameraView, this);
```

### Add Code to Open the Camera

Override the MainActivity.onResume and MainActivity.onPause function to open and close camera.

```java
@Override
protected void onResume() {
    super.onResume();
    needCapture = false;
    try {
        // open the default camera.
        mCameraEnhancer.open();
    } catch (CameraEnhancerException e) {
        e.printStackTrace();
    }
}
@Override
protected void onPause() {
    super.onPause();
    try {
        // close the default camera.
        mCameraEnhancer.close();
    } catch (CameraEnhancerException e) {
        e.printStackTrace();
    }
}
```

### Capture Frame

1. In the Project window, open app > res > layout > `activity_main.xml`, and add a `Button` to capture frame.

   ```xml
   <Button
       android:id="@+id/btn_capture"
       android:layout_width="70dp"
       android:layout_height="70dp"
       android:layout_alignParentBottom="true"
       android:layout_centerHorizontal="true"
       android:layout_marginBottom="25dp"
       android:background="@drawable/icon_capture"/>
    ```

2. Add UI variables and event response codes

   ```java
   Button btnCapture;
   ...
   btnCapture = findViewById(R.id.btn_capture);

   btnCapture.setOnClickListener(v -> {
       // Here we just set a flag, the actual capture action will be executed in the `frameOutputCallback`
       needCapture = true;
   });
   ```

3. Add a frame listener to acquire the latest frame from video streaming. Here we capture a frame and show it on the other activity(`ShowPictureActivity`).

   ```java
   static ImageData mFrame;
   ...
   mCameraEnhancer.addListener((frame, nowTime) -> {
       if(needCapture){
           needCapture = false;

           // Capture a frame, display it in the image view of the other activity.
           mFrame = frame;
           Intent intent = new Intent(MainActivity.this,ShowPictureActivity.class);
           startActivity(intent);
       }
   });
   ```

### Additional Steps

1. In the Project window, open app > res > layout > `activity_show_picture.xml`, and add a `ImageView`.

   ```xml
   <ImageView
       android:id="@+id/iv_picture"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
       />
   ```

2. Display the captured frame in ImageView.

   ```java
   public class ShowPictureActivity extends AppCompatActivity {
       private Toolbar toolbar;
       ImageView ivPicture;
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_show_picture);
           ivPicture = findViewById(R.id.iv_picture);
   
           toolbar = findViewById(R.id.toolbar);
           toolbar.setNavigationOnClickListener(new View.OnClickListener() {
               @Override
               public void onClick(View v) {
                   onBackPressed();
               }
           });
           ImageData frame = MainActivity.mFrame;
           // Convert to Bitmap from the captured frame.
           Bitmap bitmap = null;
           try {
               bitmap = frame.toBitmap();
           } catch (CoreException e) {
               e.printStackTrace();
           }
           // Display it in ImageView
           ivPicture.setImageBitmap(bitmap);
       }
   
   }
   ```

### Build and Run the Project

1. Select the device that you want to run your app on from the target device drop-down menu in the toolbar.

2. Click `Run app` button, then Android Studio installs your app on your connected device and starts it.

>Note:
>- For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/android/).
