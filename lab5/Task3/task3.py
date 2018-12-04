import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.cbook import get_sample_data

image = mpimg.imread('C:\\Users\\User\\Desktop\\laba5\\Task3\\pika.png')
img = mpimg.imread('C:\\Users\\User\\Desktop\\laba5\\Task3\\Phot.jpg')   

def rgb_to_gray(img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img

        for i in range(3):
           grayImage[:,:,i] = Avg

        return grayImage       
  
plt.imshow(image)
plt.show()
grayImage = rgb_to_gray(image)  
plt.imshow(grayImage)
plt.savefig('off white pika.png')
plt.show()

titles = ['Original', 'Red channel', 'Green channel', 'Blue channel']
cmaps = [None, plt.cm.Reds_r, plt.cm.Greens_r, plt.cm.Blues_r]

from numpy import array, zeros_like
def channel(img, color):
    if color not in (0, 1, 2): return img
    c = img[..., color]
    z = zeros_like(c)
    return array([(c, z, z), (z, c, z), (z, z, c)][color]).transpose(1,2,0)

colors = range(-1, 3)
fig, axes = plt.subplots(1, 4, figsize=(13,3))
objs = zip(axes, titles, colors)
for ax, title, color in objs:
    ax.imshow(channel(img, color))
    ax.set_title(title)
    ax.set_xticks(())
    ax.set_yticks(())

plt.savefig('LGBT.png')
plt.show()

def contrast():
    img =  Image.open('C:\\Users\\User\\Desktop\\laba5\\Task3\\Phot.jpg')
    img1 = img.copy()
    img = ImageEnhance.Contrast(img).enhance(0.1)
    plt.imshow(img)
    plt.savefig('Baptism_v1.png')
    img.show()
    img1 = ImageEnhance.Contrast(img1).enhance(50.0)
    plt.imshow(img1)
    plt.savefig('Baptism_v2.png')
    img1.show()
    
contrast()