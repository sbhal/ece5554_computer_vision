# -*- coding: utf-8 -*-

from energy_image import energy_image
from reduceHeight import reduceHeight
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave

img = imread('inputSeamCarvingPrague.jpg')
print img.dtype, img.shape
en_im = energy_image(img)

for i in range(100):
    img, en_im = reduceHeight(img, en_im)

plt.imsave("outputReduceHeightPrague", img)

img = imread('inputSeamCarvingMall.jpg')
print img.dtype, img.shape
en_im = energy_image(img)

for i in range(100):
    img, en_im = reduceHeight(img, en_im)

plt.imsave("outputReduceHeightMall", img)