# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:22:35 2015

@author: siddh
"""
import numpy as np
import cv2
import os
from predictAction import predictAction
from computeMHI import computeMHI
from huMoments import huMoments

basedir = './'
actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
allMHIs_counter = 0
allMHIs = np.empty((480,640,20), dtype=np.float32)
allMoments = np.empty((20,7), dtype=np.float64)
for actionnum in range(len(actions)):
    subdirname = basedir + actions[actionnum] + '/'
    subdir = os.listdir(subdirname)
    for seqnum in range(len(subdir)):
        allMHIs[:,:,allMHIs_counter] = computeMHI(subdirname + subdir[seqnum])
        allMoments[allMHIs_counter,:] = huMoments(allMHIs[:,:,allMHIs_counter])
        allMHIs_counter += 1

allLabels = [i for i in xrange(1,6) for j in xrange(4)]
allLabels = np.array(allLabels)
#%%
actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
#actions = ['leftarmup']
#trainMHI = np.empty((480,640,20), dtype=np.float32)
#trainMHI_counter = 0
np.save("huVectors", allMoments)
np.save("allMHIs", allMHIs)
allMoments = allMoments/np.linalg.norm(allMoments)
confusionMatrix = np.zeros((5,5))
for actionnum in range(len(actions)):
    subdirname = basedir + actions[actionnum] + '/'
    subdir = os.listdir(subdirname)
    for seqnum in range(len(subdir)):
#        testMHI = computeMHI(subdirname + subdir[seqnum])
#        testMoments = huMoments(testMHI)
        testMoments = allMoments[actionnum*4 + seqnum]
        trainMHI = np.delete(allMHIs, (actionnum*4 + seqnum), axis=2)
        trainMoments = np.delete(allMoments, (actionnum*4 + seqnum), axis=0)
        trainLabels = np.delete(allLabels, (actionnum*4 + seqnum), axis=0)
        print actions[actionnum], " and subdir is ", seqnum, " with complete ", subdirname + subdir[seqnum]
#        confusionMatrix[actionnum][predictAction(testMoments, trainMoments, trainLabels)] += 1
        confusionMatrix[actionnum][predictAction(testMoments, allMoments, allLabels)-1] += 1

print confusionMatrix

for i in range(5):
    print "Mean Recognition Rate for "+actions[i] + " class is ", confusionMatrix[i][i] * 25, "%"