# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:49:08 2015

@author: sbhal
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread, imsave

img = imread('inputPS0Q2.png')
print img.dtype, img.shape
plt.imshow(np.uint8(img))
plt.show()

img_swap = np.empty_like(img) 
img_swap[:,:,1] = img[:,:,0]
img_swap[:,:,0] = img[:,:,1]
img_swap[:,:,2] = img[:,:,2]
imsave('swapImgPS0Q2.png', img_swap)
plt.subplot(321)
plt.title('Image Tone Swapped')
plt.imshow(np.uint8(img_swap))

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img_gray = np.empty((img.shape[0], img.shape[1],3), dtype=int)
img_gray = rgb2gray(img)
imsave('grayImgPS0Q2.png', img_gray)
plt.subplot(322)
plt.title('Gray Image')
plt.imshow(np.uint8(img_gray))

img_neg_gray = np.empty_like(img_gray)
img_neg_gray = 1 - img_gray
imsave('negativeImgPS0Q2.png', img_neg_gray)
plt.subplot(323)
plt.title('Negative of Gray Img')
plt.imshow(np.uint8(img_neg_gray))

img_flip_gray = np.empty_like(img_gray)
img_flip_gray = np.fliplr(img_gray)
imsave('mirrorImgPS0Q2.png', img_flip_gray)
plt.subplot(324)
plt.title('Gray Image Flipped')
plt.imshow(np.uint8(img_flip_gray))

img_flip_gray_avg = np.empty_like(img_gray)
img_flip_gray_avg = (img_gray+img_flip_gray)/2
imsave('avgImgPS0Q2.png', img_flip_gray_avg)
plt.subplot(325)
plt.title('Gray Image Flipped inten red')
plt.imshow(np.uint8(img_flip_gray_avg))

N = np.empty_like(img_gray)
N = np.random.random(img_gray.shape) * 255
np.save('noise', N)

img_gray_with_noise = img_gray + N;
for i in np.nditer(img_gray_with_noise):
    if i>255:
        i = 255
imsave('addNoiseImgPS0Q2.png', img_gray_with_noise)
plt.subplot(326)
plt.title('Gray Image with Noise')
plt.imshow(np.uint8(img_gray_with_noise))

plt.show()