# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:12:00 2015

@author: sbhal
"""

from energy_image import energy_image
from reduceHeight import reduceHeight
from reduceWidth import reduceWidth
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave

img = imread('ques6_3.jpg')
print img.dtype, img.shape
en_im = energy_image(img)

for i in range(100):
    img, en_im = reduceHeight(img, en_im)
    img, en_im = reduceWidth(img, en_im)

plt.imsave("ques6_1_out_2", img)
