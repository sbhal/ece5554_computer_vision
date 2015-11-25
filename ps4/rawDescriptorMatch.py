# -*- coding: utf-8 -*-

import numpy as np
import scipy.io
import glob
from scipy import misc
import matplotlib.pyplot as plt
from displaySIFTPatches import displaySIFTPatches
from selectRegion import roipoly
from dist2 import dist2
from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from skimage.color import rgb2gray
import matplotlib.cm as cm
import pylab as pl

mat = scipy.io.loadmat('twoFrameData_ol.mat')

print '-->use the mouse to draw a polygon, right click to end it'
pl.imshow(mat['im1'])
MyROI = roipoly(roicolor='r')
print ' the mouse to draw a polygon, right click to end it'
#Ind = MyROI.getIdx(mat['im1'], mat['positions1'])
sift_feature_indices = MyROI.getIdx(mat['im1'], mat['positions1'])
#Ind = [44, 46, 47, 102, 154, 211, 314, 319, 322, 436, 453, 600, 604, 608, 805, 1097, 1110, 1341, 1343]
#sift_feature_indices = [148, 152, 153, 1098]
   # Ind contains the indices of the SIFT features whose centers fall
    # within the selected region of interest.
    # Note that these indices apply to the *rows* of 'descriptors' and
    # 'positions', as well as the entries of 'scales' and 'orients'
    # now display the same image but only in the polygon.
#%%
#col 0 is distance and col 1 is indices
matchFeatures_list = np.empty((0,2))

for sift_descriptor_vector in mat['descriptors1'][sift_feature_indices,:]:
    sift_descriptor_vector = np.array(sift_descriptor_vector, ndmin=2)
    distance_matrix = dist2(sift_descriptor_vector, mat['descriptors2'])
    matchFeatures_list = np.vstack((matchFeatures_list, [np.amin(distance_matrix), np.argmin(distance_matrix)]))

#%%
dist_mean = np.mean(matchFeatures_list[:,0], axis=0)
thresholdFeatureMask = matchFeatures_list[:, 0] < (dist_mean*0.75)
thresholdFeatures_list = matchFeatures_list[thresholdFeatureMask, :]
print thresholdFeatures_list
tlist = np.array(thresholdFeatures_list, dtype=np.uint)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.imshow(mat['im2'])
coners = displaySIFTPatches(mat['positions2'][tlist[:,1], :], mat['scales2'][tlist[:,1], :], mat['orients2'][tlist[:,1], :])
    
for j in range(len(coners)):
    ax.plot([coners[j][0][1], coners[j][1][1]], [coners[j][0][0], coners[j][1][0]], color='g', linestyle='-', linewidth=1)
    ax.plot([coners[j][1][1], coners[j][2][1]], [coners[j][1][0], coners[j][2][0]], color='g', linestyle='-', linewidth=1)
    ax.plot([coners[j][2][1], coners[j][3][1]], [coners[j][2][0], coners[j][3][0]], color='g', linestyle='-', linewidth=1)
    ax.plot([coners[j][3][1], coners[j][0][1]], [coners[j][3][0], coners[j][0][0]], color='g', linestyle='-', linewidth=1)
ax.set_xlim(0, mat['im2'].shape[1])
ax.set_ylim(0, mat['im2'].shape[0])
plt.gca().invert_yaxis()
    
plt.show()

#displaySIFTPatches(mat['positions2'][thresholdFeatures_list[:,1],:], mat['scales2'][thresholdFeatures_list[:,1],:], mat['orients2'][thresholdFeatures_list[:,1],:])

