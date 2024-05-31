---
layout: default-layout
title: Guide on Android - Dynamsoft Camera Enhancer
description: This is the documentation - Guide on Android page of Dynamsoft Camera Enhancer.
keywords:  Camera Enhancer, Guide on Android
needAutoGenerateSidebar: true
noTitleIndex: true
needGenerateH3Content: true
breadcrumbText: Android Guide
permalink: /programming/android/guide/guide-v3.0.3.html
---

# Dynamsoft Camera Enhancer User Guide for Android (Java)

The Dynamsoft Camera Enhancer Android SDK enables you to easily control cameras from your Android applications to stream live video and acquire realtime frames. 

> **Example Usage**
> 
> See how Dynamsoft Camera Enhancer helps in camera control and video recognition:
> - **Barcode scanning from video stream**: check [Dynamsoft Barcode Reader Android User Guide](https://www.dynamsoft.com/barcode-reader/docs/mobile/programming/android/user-guide.html?ver=latest)

Step-by-step guide on how to integrate Dynamsoft Camera Enhancer SDK to your Android app:

## App prerequisites

- System Requirements:
  - Supported OS: Android 5 or higher (Android 7 or higher recommended).
  - Supported ABI: arm64-v8a/armeabi-v7a/x86/x86_64.

- Environment: Android Studio 3.4+.

## Installation

If you don't have SDK yet, please download the Dynamsoft Camera Enhancer(DCE) SDK from the <a href="https://www.dynamsoft.com/camera-enhancer/downloads/1000021-confirmation/?utm_source=docs" target="_blank">Dynamsoft website</a> and unzip the package. After decompression, the root directory of the DCE installation package is `DynamsoftCameraEnhancer`, which is represented by `[INSTALLATION FOLDER]`.

## Build Your First Application

The following sample will demonstrate how to acquire a frame from video streaming by DCE.
>Note: 
>- The following steps are completed in Android Studio 4.2.
>- You can download the similar complete source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/android/HelloWorld).
>- For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/android/).

### Create a New Project 

1. Open Android Studio and select New Project… in the File > New > New Project… menu to create a new project.

2. Choose the correct template for your project. In this sample, we'll use `Empty Activity`.

3. When prompted, choose your app name (`HelloWorld`) and set the Save location, Language, and Minimum SDK (21)
    >Note: With minSdkVersion set to 21, your app is available on more than 94.1% of devices on the Google Play Store (last update: March 2021).

### Include the library

There are two ways to include the Dynamsoft Camera Enhancer SDK into your project:

#### Local Binary Dependency

1. Copy the file `[INSTALLATION FOLDER]\Lib\DynamsoftCameraEnhancerAndroid.aar` to the target directory `HelloWorld\app\libs`

2. Open the file `HelloWorld\app\build.gradle`, and add reference in the dependencies:
    ```
    dependencies {
        implementation fileTree(dir: 'libs', include: ['*.aar'])
    }
    ```

3. Click `Sync Now`. After the synchronization completes, the SDK is added to the project.

4. import the package int the file `MainActivity.java`
    ```java
    import com.dynamsoft.dce.*;
    ```

#### Remote Binary Dependency

1. Open the file `HelloWorld\app\build.gradle`, and add the remote repository:
    ```
    repositories {
        maven {
            url "https://download2.dynamsoft.com/maven/aar"
        }
    }
    ```

2. Add reference in the dependencies:
    ```
    dependencies {
        implementation 'com.dynamsoft:dynamsoftcameraenhancer:2.3.10@aar'
    }
    ```
    >Note:Please replace {version-number} with the correct version number.

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

The above features are enabled by triggering method [`enableFeatures`](../primary-api/camera-enhancer.html#enablefeatures). If you are not using these features, you can skip the license activation step.

Use the following code to activate the license:

```java
CameraEnhancer.initLicense("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9", new DCELicenseVerificationListener() {
   @Override
   public void DCELicenseVerificationCallback(boolean isSuccess, Exception error) {
      if(!isSuccess){
         error.printStackTrace();
      }
   }
});
```

>Note:
>- Network connection is required for the license to work.
>- "DLS2***" is a time-limited public trial license used in the sample.
>- You can request a 30-day trial license via the [Request a Trial License](https://www.dynamsoft.com/customer/license/trialLicense?product=cvs&utm_source=guide&package=android){:target="_blank"} link. Offline trial license is also available by [contacting us](https://www.dynamsoft.com/contact/){:target="_blank"}.

### Initialize Dynamsoft Camera Enhancer

Create an instance of Dynamsoft Camera Enhancer

```java
CameraEnhancer mCameraEnhancer;
mCameraEnhancer = new CameraEnhancer(MainActivity.this);
```

### Create Camera View And Control Camera

1. In the Project window, open app > res > layout > `activity_main.xml`, create a DCE camera view section under the root node.

    ```xml
    <com.dynamsoft.dce.DCECameraView
        android:id="@+id/cameraView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:layout_editor_absoluteX="25dp"
        tools:layout_editor_absoluteY="0dp" />
    ```

2. Initialize the camera view, and bind to the Camera Enhancer object.

    ```java
    DCECameraView mCameraView;

    mCameraView = findViewById(R.id.cameraView);
    mCameraEnhancer.setCameraView(mCameraView);
    ```

3. Override the MainActivity.onResume and MainActivity.onPause function to open and close camera.

    ```java
    @Override
    protected void onResume() {
        super.onResume();
        needCapture = false;
        try {
            mCameraEnhancer.open();
        } catch (CameraEnhancerException e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        try {
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
    // Click to capture a frame
    private Button btnCapture;

    btnCapture =(Button)findViewById(R.id.btnCapture);

    btnCapture.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            // Here we just set a flag, the actual capture action will be executed in the `frameOutputCallback`
            needCapture = true;
        }
    });

    ```

3. Add a frame listener to acquire the latest frame from video streaming. Here we capture a frame and show it on the other activity(`ShowPictureActivity`).

    ```java
    static DCEFrame mFrame;

    mCameraEnhancer.addListener(new DCEFrameListener() {
        @Override
        public void frameOutputCallback(DCEFrame frame, long nowTime) {
            if(needCapture){
                needCapture = false;
                mFrame = frame;
                Intent intent = new Intent(MainActivity.this,ShowPictureActivity.class);
                startActivity(intent);
            }
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
        ImageView ivPicture;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_show_picture);
            ivPicture = findViewById(R.id.iv_picture);

            DCEFrame frame = MainActivity.mFrame;

            // Convert to Bitmap from the captured frame.
            Bitmap bitmap = frame.toBitmap();

            // Rotate it to the nature device orientation.
            bitmap = rotateBitmap(bitmap, frame.getOrientation());

            // Display it in ImageView
            ivPicture.setImageBitmap(bitmap);
        }

        private Bitmap rotateBitmap(Bitmap origin, float degree) {
            if (origin == null) {
                return null;
            }
            int width = origin.getWidth();
            int height = origin.getHeight();
            Matrix matrix = new Matrix();
            matrix.setRotate(degree);
            Bitmap newBM = Bitmap.createBitmap(origin, 0, 0, width, height, matrix, false);
            origin.recycle();
            return newBM;
        }
    }
    ```



### Build and Run the Project

1. Select the device that you want to run your app on from the target device drop-down menu in the toolbar.

2. Click `Run app` button, then Android Studio installs your app on your connected device and starts it.

>Note: 
>- You can download the similar complete source code from [Here](https://github.com/Dynamsoft/camera-enhancer-mobile-samples/tree/main/android/HelloWorld).
>- For more samples on using Dynamsoft Camera Enhancer supporting Barcode Reader please [click here](https://github.com/Dynamsoft/barcode-reader-mobile-samples/tree/main/android/).
