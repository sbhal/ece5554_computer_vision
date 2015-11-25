# -*- coding: utf-8 -*-

from energy_image import energy_image, energy_image_2
from reduceHeight import reduceHeight
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from displaySeam import displaySeam
from reduceWidth import reduceWidth

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import imread, imsave
from scipy import ndimage
#from skimage import img_as_float

x1 = np.array([0, -(0.5), 0.5, 0])
x2 = np.array([0, 0.5, -0.5, 0])
xconvolution = ndimage.convolve(x1, x2, mode='constant', cval=0.0)
img = imread('inputSeamCarvingPrague.jpg')
#print img.dtype, img.shape
#plt.imshow(img)
#plt.imshow(img[: : ], cmap = plt.get_cmap('gray'))
#plt.imshow(energy_image(img), cmap = plt.get_cmap('gray'))

en_image = energy_image(img)
plt.figure()
plt.title('Gradient Energy Intensity')
plt.imshow(en_image)
plt.show()
v_cum_min_energy = cumulative_minimum_energy_map(en_image, 'VERTICAL')
plt.figure()
plt.title('Cumulative Vertical Intensity')
plt.imshow(v_cum_min_energy)
plt.show()
h_cum_min_energy = cumulative_minimum_energy_map(en_image, 'HORIZONTAL')
plt.figure()
plt.title('Cumulative Horizontal Intensity')
plt.imshow(h_cum_min_energy)
plt.show()

plt.figure()
plt.title('Original Image')
plt.imshow(img)
plt.show()

displaySeam(img, find_optimal_vertical_seam(v_cum_min_energy), 'VERTICAL')


displaySeam(img, find_optimal_horizontal_seam(h_cum_min_energy), 'HORIZONTAL')
"""

#vSeam = find_optimal_horizontal_seam(cum_min_energy)
vSeam = find_optimal_vertical_seam(cum_min_energy)
#print find_optimal_horizontal_seam(w)
displaySeam(img, vSeam, 'VERTICAL')
plt.figure(2)
plt.hold(False)
plt.subplot(121)
plt.title('Display after seam')
plt.imshow(img)

for i in range(1):
    img, en_image = reduceWidth(img, en_image)
plt.subplot(122)
plt.imshow(img)
imsave("crop_output.jpg", img)

"""
plt.show()
print "-------------FINISH-----------------"

