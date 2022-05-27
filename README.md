# Logo Detection and Classification
Code for the CS 534: Computer Vision project at Rutgers University. Reproduced and extended on the results presented in the paper [Open Set Logo Detection 
and Retrieval](https://arxiv.org/abs/1710.10891)

-----------------------------------------
### Work Done

* Reproduced and improved the results of open set and closed set logo detection from the original paper  by a factor of 12% using YOLOv5 detector
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
The file "Step1 + Step2.ipynb" contains code retrieval results using CCA and non-linear neural networks. The file "Step3.ipynb"  contains code for enhancing the explainability
of the model using Vision Transformers and cross-modal learning. The file "Viz.ipynb" contains code and visualizations seen in the report.

Made as a team with [@animesharma](https://github.com/animesharma)
