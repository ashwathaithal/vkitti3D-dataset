# VKITTI 3D Semantic Segmentation Dataset

This is the outdoor dataset used to evaluate 3D semantic segmentation of point clouds in ([Engelmann et al. ICCV'W17](https://www.vision.rwth-aachen.de/page/3dsemseg)) **Exploring Spatial Context for 3D Semantic Segmentation of Point Clouds** paper.
The dataset is directly derived from the [Virtual KITTI Dataset](http://www.europe.naverlabs.com/Research/Computer-Vision/Proxy-Virtual-Worlds) (v.1.3.1).

All files are provided for convenience only, you can generate the whole dataset yourself form the original Virtual Kitti Dataset.

## Data Format
All files are provided as numpy ```.npy``` files.
Each file fontains a ```N x F``` matrix, where ```N``` is the number of points inside the scene and ```F``` is the number of features per point, in this case ```F=7```.
The features are ```XYZRGBL```, the 3D ```XYZ``` position, the ```RGB``` color and the ground truth semantic label ```L```. 
You can load them as follows:
```python
import numpy as np
point_cloud = np.load('dataset/01/0001_00000.npy')
```

### Tools
[Todo]

### Training and Evaluation
We trained our models using 6-fold cross validation as advertised in [Qi et al.](https://arxiv.org/pdf/1612.00593.pdf) (PointNet). For example, you train your model using sequences 2-5 and evaluate on 1. You then do this for all 6 sequences and average your numbers of the 6 splits.
We report the mean intersection over union (IoU), overall accuracy (over all points) and the average class accuracy.

## Dataset Generation
We split up the original sequences of Virutal KITTI into non-overlapping sub-sequences to perform 6-fold cross validation.
For each sub-sequence, we selected 15 scenes at equidistance timesteps to avoid overlapping data.
