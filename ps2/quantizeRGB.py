
import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image
import matplotlib.pyplot as plt

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

def quantizeRGB(image, n_colors):
    image = np.array(image, dtype=np.float64) / 255

    w, h, d = tuple(image.shape)
    assert d == 3
    image_array = np.reshape(image, (w * h, d))

    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
    labels = kmeans.predict(image_array)
    im = recreate_image(kmeans.cluster_centers_, labels, w, h)
    plt.imshow(im)
    plt.title('RGB Quantized k = %d' % n_colors)
    return im 

if __name__ == "__main__":
    im = np.array(Image.open('fish.jpg'))
    im2 = quantizeRGB(im, 10)
    plt.imshow(im2)
    plt.title('RGB Quantized k = %d' % k)