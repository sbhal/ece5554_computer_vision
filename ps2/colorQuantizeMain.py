# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:31:02 2015

@author: siddh
"""

from getHueHists import getHueHists
from quantizeHSV import quantizeHSV
from quantizeRGB import quantizeRGB
from computeQuantizationError import computeQuantizationError
import numpy as np
from PIL import Image

im = np.array(Image.open('fish.jpg'))

im_rgb = quantizeRGB(im, 2)
#im_rgb, meanColors = quantizeRGB(im, 5)
im_hsv, meanHues = quantizeHSV(im, 2)

print computeQuantizationError(im, im_rgb)
print computeQuantizationError(im, im_hsv)

getHueHists(im, 5)