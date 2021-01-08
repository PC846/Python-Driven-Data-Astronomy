# Write your mean_fits function here:
from astropy.io import fits
import numpy as np

def mean_fits(FITS_files):
  n = len(FITS_files)
  if n > 0:
    
    hdulist = fits.open(FITS_files[0])
    data = hdulist[0].data
    hdulist.close()
    
    for i in range(1, n):
      hdulist = fits.open(FITS_files[i])
      data += hdulist[0].data
      hdulist.close()
    
    data_mean = data / n
    return data_mean

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()