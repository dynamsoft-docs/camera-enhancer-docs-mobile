
- Simplified the usage of camera-control APIs. The new APIs are easier to use and cover more scenarios.
- Simplified the usage of camera enhancer features. Users can enable all required features via the method `enableFeatures` by inputting the combined enumeration value.
- Extended the features of `DCECameraView`. Users can add and personalize the overlays and viewfinder on the camera UI.
- Extended the features of `DCEFrame`. `DCEFrame` will store more frame information to cover more scenarios. In addition, the method `toBitmap` is added to enable users to convert `DCEFrame` to a visible image.
- The camera UI will display a fuzzified image instead of the previously captured image when the camera UI is quit and resumed.


