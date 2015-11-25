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
basedir = './'

def computeMHI(directoryName):
    depthfiles = glob.glob(directoryName + '/' + '*.pgm');
    depthfiles = np.sort(depthfiles)
    frame = cv2.imread(depthfiles[0])
    h, w = frame.shape[:2]
    prev_frame = frame.copy()
    motion_history = np.zeros((h, w), np.float32)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[:,:,1] = 255
    for i in range(len(depthfiles)-1):
        frame = cv2.imread(depthfiles[i+1])
        frame_diff = cv2.absdiff(frame, prev_frame)
        gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        ret, motion_mask = cv2.threshold(gray_diff, 70, 1, cv2.THRESH_BINARY)
        timestamp = clock()
        cv2.updateMotionHistory(motion_mask, motion_history, timestamp, duration=0.5)
        prev_frame = frame.copy()
    return motion_history

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
#        cv2.imshow("mhi", allMHIs[:,:,allMHIs_counter])
#    cv2.imshow("mask", motion_mask)
        if 0xFF & cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()



#%%
def huMoments (H):
#    for i in range(allMHIs.shape[2]):
    moments = cv2.moments(H)
    output = cv2.HuMoments(moments)
    return output[:,0]

allHuMoments = np.empty((20,7), dtype=np.float32)
for i in range(allMHIs.shape[2]):
    allHuMoments[i,:] = huMoments(allMHIs[:,:,i])
#%%
testMHI = computeMHI("./leftarmup/leftarm-up-p2-1")
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


#%%

from sklearn.neighbors import KNeighborsClassifier

def predictAction(testMoments, trainMoments, trainLabels):
    neigh = KNeighborsClassifier(n_neighbors=5)
#neigh.fit([trainMHI[:,:,i].flatten() for i in xrange(20)], trainLabels)
#print(neigh.predict([testMHI.flatten()]))
    neigh.fit(trainMoments, trainLabels)
    print(neigh.predict(testMoments))
    print(neigh.predict(trainMoments))
    print(neigh.predict_proba(trainMoments))
    return neigh.predict(testMoments)
