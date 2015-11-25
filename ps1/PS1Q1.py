import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imsave

l1 = [1, 2, 3, 4]
l2 = [0, 1, 5]

convolution = np.convolve(l1, l2, "full")
xcorrelation = np.correlate(l1, l2, "full")

plt.plot(range(len(l1)), l1)

plt.plot(range(len(l2)), l2)

plt.plot(range(len(convolution)), convolution, ':')
plt.plot(range(len(xcorrelation)), xcorrelation, '--')

plt.show()