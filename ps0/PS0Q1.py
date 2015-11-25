import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imsave

#sample = np.random.random((100,100))
#np.save("inputAPS0Q1_1", sample)

#a = np.load("inputAPS0Q1_1.npy")

A = np.load("inputAPS0Q1.npy")
plt.figure()
plt.title("A - orig")
plt.imshow(np.double(A))

#a.reshape(-1).sort(axis=0)
sort = np.sort(A.reshape(-1))
#sort = sort[::-1]
plt.figure()
plt.title("A - sorted")
plt.plot(sort[::-1])


plt.figure()
plt.hist(A, bins=20)
#plt.show()

X = np.empty( (np.shape(A)[0]/2, np.shape(A)[1]/2) )
X = A[(np.shape(A)[0])/2:, (np.shape(A)[1])/2:]
np.save('outputXPS0Q1', X)

plt.figure()
plt.title("X - bottom left quad")
plt.imshow(np.double(X))


Y = np.empty_like(A)
Y = A - np.mean(A)
Y[Y<0] = 0 
np.save('outputYPS0Q1', Y)
plt.figure()
plt.title("Y - Avg inten deducted")
plt.imshow(np.double(Y))

#Z = np.empty((np.shape(a)[0],np.shape(a)[1],3), dtype=np.uint8)
Z = np.empty((np.shape(A)[0],np.shape(A)[1],3), dtype=int)
Z[A >np.mean(A)][0] = 1 
Z[A <=np.mean(A)][2] = 1
"""
for r in range(w):
    for c in range(h):
        if ( Y[r][c] >= avg):
            Z[r][c][0] = 1
        else:
            Z[r][c][2] = 1
"""
plt.figure()
plt.title("red where high intensity")
plt.imshow(np.double(Z))
imsave('outputZPS0Q1.png', Z)

plt.show()