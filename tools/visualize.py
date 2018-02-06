import numpy as np
import argparse
import viz

class2color = np.array([[200, 90, 0], # brown
                     [0, 128, 50],    # dark green
                     [0, 220, 0],     # bright green
                     [255, 0, 0],     # red
                     [100, 100, 100], # dark gray
                     [200, 200, 200], # bright gray
                     [255, 0, 255],   # pink
                     [255, 255, 0],   # yellow
                     [128, 0, 255],   # violet
                     [255, 200, 150], # skin
                     [0, 128, 255],   # dark blue
                     [0, 200, 255],   # bright blue
                     [255, 128, 0],   # orange
                     [0,0,0]])        # black


def main(pc_path):
    point_cloud = np.load(pc_path)
    points = point_cloud[:, 0:3]
    colors_rgb = point_cloud[:, 3:6]
    colors_labels = class2color[point_cloud[:, 6].astype(int)]
    viz.show_pointclouds([points, points], [colors_rgb, colors_labels])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualizer of point clouds")

    parser.add_argument('--pc_path', nargs='?', const='../dataset/01/0001_00000.npy',
                        type=str, default='../dataset/01/0001_00000.npy',
                        help='path to numpy pointcloud for visualization')

    args = parser.parse_args()

    main(pc_path=args.pc_path)
