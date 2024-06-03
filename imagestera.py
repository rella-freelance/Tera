#Importing the necessary libraries. Really a number  of them
#repo: https://github.com/PacktPublishing/Hands-On-Image-Processing-with-Python/blob/master/Chapter01/Chapter1.ipynb
#input and output images provided.
# code commented out after it's proven to be working; prevent many displays 
import skimage
print(skimage.__version__)
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, exposure, img_as_float, data #, viewer
#viewer commented out; has problems with skimage version used
from skimage.util import invert, random_noise, montage
import matplotlib.pylab as plt
import matplotlib.image as mpimg
from scipy.ndimage import affine_transform, zoom
from scipy import misc

#reading, saving, displaying images using PIL
im = Image.open("em.png")
print(im.width, im.height, im.mode, im.format, type(im))
#im.show() #works

im_g = im.convert('L') #converting to grayscale, from RGB
#im_g.save('em_gray.png') #saving the converted image to disk


# Image.open("em_gray.png").show() #reading the grayscale image from disk

#reading, saving, displaying images using matplotlib
im = mpimg.imread("em.png") #read image as a numpy array
#print(im.shape, im.dtype, type(im)) #contains an alpha channel; num_channels = 4
plt.figure(figsize=(10,10))
plt.imshow(im)
plt.axis('off')
#plt.show()

im1 = im
im1[im1 < 0.5] = 0
plt.imshow(im1)
plt.axis('off')
plt.tight_layout()
plt.savefig("darkened_em.png")
plt.close()

im = mpimg.imread("darkened_em.png")
plt.figure(figsize=(10,10))
plt,imshow(im)
plt.axis('off')
plt.tight_layout()
#plt.show()

#converting to different color space
im = imread("parrot.png")
im_hsv = color.rgb2hsv(im)
plt.gray()
plt.figure(figsize=(10,8))
plt.subplot(221), plt.imshow(im_hsv[...,0]), plt.title('h', size=20),
plt.axis('off')
plt.subplot(222), plt.imshow(im_hsv[...,1]), plt.title('s', size=20),
plt.axis('off')
plt.subplot(223), plt.imshow(im_hsv[...,2]), plt.title('v', size=20),
plt.axis('off')
plt.subplot(224), plt.axis('off')
plt.show()
