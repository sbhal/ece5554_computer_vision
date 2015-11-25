#!/usr/bin/python
#from cv2 import *
#from cv2.cv import *
#from opencv.highgui import *
import sys
import time
import cv2
import numpy as np
from math import cos,sin
#%%
CLOCKS_PER_SEC = 1.0
MHI_DURATION = 1;
MAX_TIME_DELTA = 0.5;
MIN_TIME_DELTA = 0.05;
N = 4;
buf = range(10) 
last = 0;
mhi = None; # MHI
orient = None; # orientation
mask = None; # valid orientation mask
segmask = None; # motion segmentation map
storage = None; # temporary storage

def update_mhi( img, dst, diff_threshold ):
    global last
    global mhi
    global storage
    global mask
    global orient
    global segmask
    timestamp = time.clock()/CLOCKS_PER_SEC # get current time in seconds
#    size = cvSize(img.width,img.height) # get current frame size
    idx1 = last
    if not mhi or mhi.width != img.shape[1] or mhi.height != img.shape[1]: 
        for i in range( N ):
            buf[i] = np.zeros((img[1].shape[1], img[1].shape[0]), dtype=np.uint8)
        mhi = np.zeros((img[1].shape[1], img[1].shape[0]), dtype=np.float32) # clear MHI at the beginning
        orient = np.empty_like(mhi)
        segmask = np.empty_like(mhi)
        mask = np.empty((img[1].shape[1], img[1].shape[0]), dtype=np.uint8)

#    cv2.cvtColor( img, buf[last], cv2.CV_BGR2GRAY) # convert frame to grayscale
    idx2 = (last + 1) % N # index of (last - (N-1))th frame
    last = idx2
    silh = buf[idx2]
    cv2.cvAbsDiff( buf[idx1], buf[idx2], silh ) # get difference between frames
    cv2.cvThreshold( silh, silh, diff_threshold, 1, cv2.CV_THRESH_BINARY ) # and threshold it
    cv2.cvUpdateMotionHistory( silh, mhi, timestamp, MHI_DURATION ) # update MHI
    cv2.cvCvtScale( mhi, mask, 255./MHI_DURATION, (MHI_DURATION - timestamp)*255./MHI_DURATION )
    dst[:] = 0
    cv2.cvMerge( mask, None, None, None, dst )
    cv2.cvCalcMotionGradient( mhi, mask, orient, MAX_TIME_DELTA, MIN_TIME_DELTA, 3 )
    if( not storage ):
        storage = cvCreateMemStorage(0);
    else:
        cvClearMemStorage(storage);
    seq = cv2.cvSegmentMotion( mhi, segmask, storage, timestamp, MAX_TIME_DELTA );
    for i in range(-1, seq.total):
        if( i < 0 ):  # case of the whole image
            comp_rect = cvRect( 0, 0, size.width, size.height );
            color = CV_RGB(255,255,255);
            magnitude = 100.;
        else:  # i-th motion component
            comp_rect = seq[i].rect 
            if( comp_rect.width + comp_rect.height < 100 ): # reject very small components
                continue;
            color = CV_RGB(255,0,0);
            magnitude = 30.;
        silh_roi = cvGetSubRect(silh, comp_rect);
        mhi_roi = cvGetSubRect( mhi, comp_rect );
        orient_roi = cvGetSubRect( orient, comp_rect );
        mask_roi = cvGetSubRect( mask, comp_rect );
        angle = cvCalcGlobalOrientation( orient_roi, mask_roi, mhi_roi, timestamp, MHI_DURATION);
        angle = 360.0 - angle;  # adjust for images with top-left origin
        count = cvNorm( silh_roi, None, CV_L1, None ); # calculate number of points within silhouette ROI
        if( count < comp_rect.width * comp_rect.height * 0.05 ):
            continue;
        center = cvPoint( (comp_rect.x + comp_rect.width/2),
                          (comp_rect.y + comp_rect.height/2) );
        cvCircle( dst, center, cvRound(magnitude*1.2), color, 3, CV_AA, 0 );
        cvLine( dst, center, cvPoint( cvRound( center.x + magnitude*cos(angle*CV_PI/180)),
                cvRound( center.y - magnitude*sin(angle*CV_PI/180))), color, 3, CV_AA, 0 );

if __name__ == "__main__":
    motion = 0;
    capture = 0;

    if len(sys.argv)==1:
        capture = cv2.VideoCapture( 0 )
    elif len(sys.argv)==2 and sys.argv[1].isdigit():
        capture = cv2.VideoCapture( int(sys.argv[1]) )
    elif len(sys.argv)==2:
        capture = cv2.VideoCapture( sys.argv[1] ); 

    if not capture:
        print "Could not initialize capturing..."
        sys.exit(-1)
        
#    cvNamedWindow( "Motion", 1 );
    while True:
        image = capture.read();
        if( image ):
            if( not motion ):
                    motion = image[1].copy()
#                    cvCreateImage( cvSize(image.width,image.height), 8, 3 );
#                    cvZero( motion );
#                    motion.origin = image.origin;
            update_mhi( image, motion, 30 );
            cvShowImage( "Motion", motion );
            if( cvWaitKey(10) != -1 ):
                break;
        else:
            break
    cvDestroyWindow( "Motion" );
