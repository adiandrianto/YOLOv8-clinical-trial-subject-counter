To build YOLOv8 model using custom dataset wee need to collect and annotate the data.
Link to video showcase: https://www.linkedin.com/feed/update/urn:li:activity:7146423128448000000/

I used [CVAT](cvat.ai) to annotate my dataset.
Since I want my model to differentiate subject with other personnel (they are all person), I annotate with 2 classes :
1. subject
2. other personnel
   
![image](https://github.com/adiandrianto/YOLOv8-clinical-trial-subject-counter/assets/127647404/2ba0bf0e-19d5-41ad-bf77-5d4dcd0fb88b)

Then I put my finished annotation in [Roboflow](https://app.roboflow.com/) to augment and split dataset to training and validation set (and also test set, if you prefer).
Augmentation used in dataset :
- Rotation: Between -15° and +15°
- Shear: ±20° Horizontal, ±20° Vertical
- Brightness: Between -25% and +25%
- Blur: Up to 2.5px
  
![image](https://github.com/adiandrianto/YOLOv8-clinical-trial-subject-counter/assets/127647404/154c1378-0c62-48c2-b82f-c80062f3b712)

Final dataset is then trained with YOLOv8 small model for 50 epoch.>> see train_yolov8_custom_dataset.ipynb
Then use openCV to make subject counter >>subject_counter.ipynb


