#Basic data manipulation problem to eventually calcuate the mean tack of a set of FIT images
#and possible find a pulsar!


#Calculating the mean and going through the assignments

import statistics
import numpy as np
from statistics import mean

def calc_mean(data_list):
    mean_of_list = mean(data_list)
    
    return(mean_of_list)


def calc_mean_manual(data_list):
    mean_of_list = sum(data_list) / len (data_list)

    return(mean_of_list)


def calc_stats(csv_file):
  data = np.loadtxt(csv_file, delimiter=',')
  
  c_mean = np.round(np.mean(data), 1)
  c_median = np.round(np.median(data), 1)

  return (c_mean, c_median)

def mean_datasets(csv_files):
  n = len(csv_files)
  
  if n > 0:
    data = np.loadtxt(csv_files[0], delimiter=',')
    for i in range (1, n):
      data += np.loadtxt(csv_files[i], delimiter=',')
      
    data_mean = np.round(data/n, 1)
    
    return(data_mean)


if __name__=='__main__':

    mean_answer = calc_mean([1,2.2,0.3,3.4,7.9])
    print(mean_answer)

    mean_man_answer = calc_mean_manual([1,2.2,0.3,3.4,7.9])
    print(mean_man_answer)

    np_mean = calc_stats('data.csv')