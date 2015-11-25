# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:41:15 2015

@author: sbhal
"""


from energy_image import energy_image
from reduceWidth import reduceWidth
import matplotlib.pyplot as plt
from scipy.misc import imsave


img = imread('inputSeamCarvingPrague.jpg')
print img.dtype, img.shape
en_im = energy_image(img)

for i in range(100):
    img, en_im = reduceWidth(img, en_im)

plt.imsave("outputReduceWidthPrague", img)

img = imread('inputSeamCarvingMall.jpg')
print img.dtype, img.shape
en_im = energy_image(img)

for i in range(100):
    img, en_im = reduceWidth(img, en_im)

plt.imsave("outputReduceWidthMall", img)