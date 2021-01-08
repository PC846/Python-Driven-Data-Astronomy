# Link to catalogues: 
# #http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
# http://ssa.roe.ac.uk/allSky

# Write your import_bss function here.
import numpy as np
import angular_dist

def hms2dec (h,m,s):
  return(15*(h + m / 60 + s / (60 * 60)))

def dms2dec(d,m,s):
  if d < 0:
     sign = -1
  else:
    sign = 1
  return (sign *(abs(d) + m/60 + s / (60 * 60)))


def import_bss():
  bss_arr = []
  cat = np.loadtxt('bss.dat', usecols=range(1,7))
  
  for i, row in enumerate(cat, 1):
    bss_arr.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
    
  return(bss_arr)

def import_super():
  super_arr = []
  cat = np.loadtxt('super.csv', delimiter= ',', skiprows=1, usecols=[0,1])
  
  for i, row in enumerate(cat, 1):
    super_arr.append((i, row[0], row[1]))
    
  return(super_arr)


def find_closest(cat, a, b):
  
  min_dist = np.inf
  min_id = None
  
  for id1, ra1, dec1 in cat:
    dist = angular_dist(ra1, dec1, a, b)
    if dist < min_dist:
      min_id = id1
      min_dist = dist
      
  return(min_id, min_dist) 

   

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
