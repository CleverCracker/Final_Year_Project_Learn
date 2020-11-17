import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import deltaE_cie76, rgb2lab
from sklearn.cluster import KMeans

# %matplotlib inline

# Working with OpenCv
# Load Image
image = cv2.imread('./images/room.jpg')
plt.imshow(image)

# Convert Image into RED GREEN BLUE
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

# Convert Image into Grey
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap='gray')


# Resized Image
resized_image = cv2.resize(image, (1200, 600))
plt.imshow(resized_image)


def RGB2HEX(color):
    """
    Convert the RGB color into HEX
    """
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    """
    Read image and return RGB Image in return
    """
    return cv2.cvtColor(cv2.imread(iamge_path), cv2.COLOR_BGR2RGB)


def image_scale(image):
    modified_image = []
    for row in image:
        for pixels in row:
            modified_image.append(pixels)
    return modified_image


def get_colors(image, number_of_colors=5, show_chart=False):
    """
    image: The image whose colors we wish to extract.
    number_of_colors: Total colors we want to extract.
    show_chart: A boolean that decides whether we show the pie chart or not.
    """
    modified_image = cv2.resize(
        image, (600, 400), interpolation=cv2.INTER_AREA)

    # modified_image = modified_image.reshape(
    #     modified_image[0]*modified_image[1], 3)
    modified_image = image_scale(modified_image)
    # Clustering Image for Colors
    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    # Calculate Plot
    counts = Counter(labels)
    center_colors = clf.cluster_centers_

    # Order Color by iterative through the key

    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i] for i in counts.keys())]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if show_chart:
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)
    return rgb_colors


get_colors(image)
