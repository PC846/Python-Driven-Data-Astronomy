#FITS = Flexible Image Transport System. In a FITS file, the image is stored in a numerical array.
#HDU = Header/Data Unit 
#First HDU is called primary HDU
#The files given to me I can't seem to save it onto here...

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

#Opening a FITS file

hdulist = fits.open('image0.fits')
hdulist.info()

#Access individual HDUS

hdulist = fits.open('image0.fits')
data = hdulist[0].data
print(data.shape)

#Visualizing image data

hdulist = fits.open('image0.fits')
data = hdulist[0].data

#plot the 3D array

plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-picels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()