from rasterio.plot import show
import rasterio
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from PIL import Image

composite = rasterio.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta\rgb.tif")

width = composite.width
height = composite.height
print("Image Size (Width x Height) is:", width, "x", height,"Pixels")

num_bands = composite.count
print("Total number of bands:", num_bands)
metadata=composite.meta
print("Meta data of tiffile : ",metadata)
des=composite.descriptions
print("Tif Descriptions :",des)
crs=composite.crs
print("CSR :",crs)
rasterio.plot.show_hist(composite, bins=50, histtype='stepfilled', lw=0.0, stacked=False, alpha=0.3)