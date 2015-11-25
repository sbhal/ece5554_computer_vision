# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:11:42 2015

@author: siddh
"""
import cv2
from common import nothing, clock, draw_str

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
