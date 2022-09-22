# Logo Detection and Classification
Code for the CS 534: Computer Vision project at Rutgers University. Reproduced and extended on the results presented in the paper [Open Set Logo Detection 
and Retrieval](https://arxiv.org/abs/1710.10891)

-----------------------------------------
### Work Done

* Reproduced and improved the mean average precision (mAP) of open set logo detection from the original paper by 24 percentage points using YOLOv5 detector
* Obtained a classification accuracy of 22.56% for 47 classes of the Flickr-47 dataset using a logo classification architecture 
consisting of YOLOv5 and template matching focused on both abstract and textual logos

***

### Tech Stack

* Python 3
* PyTorch
* seaborn

***

### Report and Presentation 

You can access the report [here](https://github.com/kunjmehta/logo-detection-and-classification/blob/main/CV_Report.pdf) and presentation 
[here.](https://github.com/kunjmehta/logo-detection-and-classification/blob/main/CS534%20-%20Final%20Presentation.pdf)

### Structure and Acknowledgements 
* `utils`: Contains code for file handling and bounding box annotation
* `logo_classification.py`: Contains code for the classification of logos in the Flickr-47 dataset
* `YOLOv5_Custom_Training.ipynb`: Contains application of YOLOv5 to the open set dataset and reports the improvement in mAP.

Made as a team with [@animesharma](https://github.com/animesharma)
