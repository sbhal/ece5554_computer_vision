from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import scipy.io
import glob
from scipy import misc
import matplotlib.pyplot as plt
from displaySIFTPatches import displaySIFTPatches
from selectRegion import roipoly
from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from skimage.color import rgb2gray
import matplotlib.cm as cm
import pylab as pl

# specific frame dir and siftdir
framesdir = 'frames/'
siftdir = 'sift/'
#siftdir = 'C:/Users/siddh/Desktop/vision-ps4-desk/sift_small/'

# In[2]:

# Get a list of all the .mat file in that directory.
# there is one .mat file per image.

fnames = glob.glob(siftdir + '*.mat')
fnames = [i[-27:] for i in fnames]

print 'reading %d total files...' %(len(fnames))

N = 100 #to visualize a sparser set of the features


# In[3]:

# Loop through all the data files found
for i in range(1):
    print 'reading frame %d of %d' %(i, len(fnames))
    
    # load that file
    fname = siftdir + fnames[i]
    
    mat = scipy.io.loadmat(fname)
    numfeats = mat['descriptors'].shape[0]
    
    #read the associated image
    imname = framesdir + fnames[i][:-4]
    im = misc.imread(imname)

    print 'imname = %s contains %d total features, each of dimension %d' %(imname, numfeats, mat['descriptors'].shape[1]);

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.imshow(im)
    Ind = [750]
    coners = displaySIFTPatches(mat['positions'][Ind,:], mat['scales'][Ind,:], mat['orients'][Ind,:])
    
    print coners
    for j in range(len(coners)):
        ax.plot([coners[j][0][1], coners[j][1][1]], [coners[j][0][0], coners[j][1][0]], color='g', linestyle='-', linewidth=1)
        ax.plot([coners[j][1][1], coners[j][2][1]], [coners[j][1][0], coners[j][2][0]], color='g', linestyle='-', linewidth=1)
        ax.plot([coners[j][2][1], coners[j][3][1]], [coners[j][2][0], coners[j][3][0]], color='g', linestyle='-', linewidth=1)
        ax.plot([coners[j][3][1], coners[j][0][1]], [coners[j][3][0], coners[j][0][0]], color='g', linestyle='-', linewidth=1)
    ax.set_xlim(0, im.shape[1])
    ax.set_ylim(0, im.shape[0])
    plt.gca().invert_yaxis()
    
    plt.show()
    
#%%
patch_num = 750
print imname
im = misc.imread(imname)
img_patch = getPatchFromSIFTParameters(allPos[patch_num,:], allScal[patch_num], allOri[patch_num], rgb2gray(im))
print img_patch
plt.imshow(img_patch,  cmap = cm.Greys_r)
plt.show()
