import numpy as np
import viz

a = np.load('dataset/01/0001_00000.npy')
points = a[:, 0:3]
colors = a[:, 3:6]
#viz.show_pointclouds([points], [colors])
