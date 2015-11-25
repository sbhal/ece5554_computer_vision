# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:14:45 2015

@author: siddh
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:08:21 2015

@author: siddh
"""

import glob
import pdb
import os
from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np
import cv2
from common import nothing, clock, draw_str
from predictAction import predictAction
from computeMHI import computeMHI
from huMoments import huMoments

basedir = './'


actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
for actionnum in range(len(actions)):
    subdirname = basedir + actions[actionnum] + '/'
    subdir = os.listdir(subdirname)

    allMHIs = np.empty((480,640,20), dtype=np.float32)
    allMHIs_counter = 0
    for seqnum in range(len(subdir)):
    # cycle through all sequences for this action category
        allMHIs_counter = allMHIs_counter + 1
        allMHIs[:,:,allMHIs_counter] = computeMHI(subdirname + subdir[seqnum])
        cv2.imshow(actions[actionnum]+"- %d"%  seqnum, allMHIs[:,:,allMHIs_counter])
#    cv2.imshow("mask", motion_mask)
        if 0xFF & cv2.waitKey(1) == 27:
            break

#cv2.destroyAllWindows()



#%%

allHuMoments = np.empty((20,7), dtype=np.float32)
for i in range(allMHIs.shape[2]):
    allHuMoments[i,:] = huMoments(allMHIs[:,:,i])
#%%
#testMHI = computeMHI("./leftarmup/leftarm-up-p2-1")
testMHI = computeMHI("./punch/punch-p1-1")
testMoments = huMoments(testMHI)

actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
#actions = ['leftarmup']
trainMHI = np.empty((480,640,20), dtype=np.float32)
trainMHI_counter = 0
for actionnum in range(len(actions)):
    subdirname = basedir + actions[actionnum] + '/'
    subdir = os.listdir(subdirname)
    for seqnum in range(len(subdir)):
    # cycle through all sequences for this action category
        trainMHI[:,:,trainMHI_counter] = computeMHI(subdirname + subdir[seqnum])
        trainMHI_counter = trainMHI_counter + 1

trainMoments = np.empty((trainMHI.shape[2],7), dtype=np.float32)
for i in range(trainMHI.shape[2]):
    trainMoments[i,:] = huMoments(trainMHI[:,:,i])

trainLabels = [i for i in xrange(1,6) for j in xrange(4)]
trainLabels = np.array(trainLabels)

print predictAction(testMoments, trainMoments, trainLabels)