import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def load_fits(FITS_image):

  #opening FITS image
  hdulist = fits.open(FITS_image)
  data = hdulist[0].data
  
  #Finding position of the maximum number
  arg_max = np.argmax(data)
  
  #Convert flat index into index tuple
  max_pos = np.unravel_index(arg_max, data.shape)
  
  return(max_pos)



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 
