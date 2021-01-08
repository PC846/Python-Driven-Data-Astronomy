import numpy as np

def angular_dist(ra1, dec1, ra2, dec2):
  rad_ra1, rad_dec1, rad_ra2, rad_dec2 = np.radians(ra1), np.radians(dec1), np.radians(ra2), np.radians(dec2)
  
  b = np.cos(rad_dec1) * np.cos(rad_dec2) * np.sin(np.abs(rad_ra1 - rad_ra2) / 2) ** 2
  
  a = np.sin(abs((rad_dec1 - rad_dec2)/ 2)) ** 2
  
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  angle = np.degrees(d)
  
  return(angle)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))