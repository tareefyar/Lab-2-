import matplotlib.pyplot as plt
from rasterio.plot import show
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image

#Opening RGB  bands separatly
r_band = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta\B4.tif")
g_band = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta\B3.tif")
b_band = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta\B2.tif")

#RED Band
fig1 = plt.figure(figsize=(5, 5))
ax1 = fig1.add_subplot(2, 2, 1)
ax1.imshow(r_band,cmap= "Reds")
plt.title("RED Band")

#Greeen Band
fig2 = plt.figure(figsize=(5, 10))
ax2 = fig2.add_subplot(2, 2, 2)
ax2.imshow(g_band,cmap= "Greens")
plt.title("Green Band")

#Blue Band
fig3 = plt.figure(figsize=(10, 10))
ax3 = fig3.add_subplot(2, 2, 3)
ax3.imshow(r_band,cmap= "Blues")
plt.title("Blue Band")
plt.show()