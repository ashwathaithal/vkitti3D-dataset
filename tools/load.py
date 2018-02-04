import numpy as np
import viz

g_colors = np.array([[200, 90, 0],  # brown
                     [0, 128, 50],  # dark green
                     [0, 220, 0],  # bright green
                     [255, 0, 0],  # red
                     [100, 100, 100],  # dark gray
                     [200, 200, 200],  # bright gray
                     [255, 0, 255],  # pink
                     [255, 255, 0],  # yellow
                     [128, 0, 255],  # violet
                     [255, 200, 150],  # skin
                     [0, 128, 255],  # dark blue
                     [0, 200, 255],  # bright blue
                     [255, 128, 0]])  # orange

point_cloud = np.load('dataset/01/0001_00000.npy')
points = point_cloud[:, 0:3]
colors_rgb = point_cloud[:, 3:6]
colors_labels = g_colors[point_cloud[:, 6].astype(int)]
viz.show_pointclouds([points, points], [colors_rgb, colors_labels])
