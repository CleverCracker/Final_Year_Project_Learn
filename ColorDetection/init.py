import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import deltaE_cie76, rgb2lab
from sklearn.cluster import KMeans

# %matplotlib inline

# Working with OpenCv
color_detection_path = './ColorDetection/'
load_iamge_path = 'room.jpg'
image = cv2.imread(color_detection_path+load_iamge_path)
