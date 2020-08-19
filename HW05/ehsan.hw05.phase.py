
#*****************************************************************
#
#  NAME:		Ehsan Kourkchi
#
#  HOMEWORK:		5
#
#  CLASS:		Scientific Computation (IfA)
#
#  INSTRUCTOR:		Norbert Schorghofer
#
#  DATE:		September 11, 2015           
#
#  FILE:		ehsan.hw05.py
#
#  DESCRIPTION:	This contains the program for the question 2
#  
#  How to run: $ python ehsan.hw05.py
#
#****************************************************************

import numpy as np
from math import *
import matplotlib.pyplot as plt
from astropy.table import Table, Column 
import random

if __name__ == '__main__':
  
  # float64 	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
  

  limit = 1000
  T = 1
  w = np.zeros(limit, dtype='Float64')
  a = np.zeros(limit, dtype='Float64')  # float64
  n = np.arange(limit, dtype='i')  # (0, 1, 2, ... limit-1)  int32
  
  w[0] = 1            # velocity
  a[0] = 0            # location
  K = 5
  
  
  
  n_ensemble = 0

  for w0 in np.arange(1.5,2.5,0.1):
   for a0 in np.arange(1.5,2.5,0.1):
     w[0] =  w0
     a[0] =  a0
     n_ensemble += 1
     for i in n[0:limit-1]:
       a[i+1] = a[i] + T * w[i]
       w[i+1] = w[i] + K * sin(a[i+1])
     
     a -= 2.*pi*(np.floor(a/(2*pi)))
     w -= 2.*pi*(np.floor(w/(2*pi)))
     plt.plot(a, w, '.', color='blue',markersize=1)

  
  plt.xlabel(r'$\alpha$', fontsize=20)
  plt.ylabel(r'$\omega$', fontsize=20)
  plt.xlim(1.5,2.5)
  plt.ylim(1.5,2.5)
  
  plt.show()
    
    
  
  