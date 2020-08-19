
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
  

  limit = 10000
  T = 1
  w = np.zeros(limit, dtype='Float64')
  a = np.zeros(limit, dtype='Float64')  # float64
  n = np.arange(limit, dtype='i')  # (0, 1, 2, ... limit-1)  int32
  
  w[0] = 10        # velocity
  a[0] = 0            # location
  K = 0.1
  
  
  
  n_ensemble = 0
  E = np.zeros(limit, dtype='Float64')
  W = np.zeros(limit, dtype='Float64')
  A = np.zeros(limit, dtype='Float64')
  for a0 in np.arange(0,2*pi,0.01):
    print a0
    a[0] =  a0
    n_ensemble+=1
    for i in n[0:limit-1]:
      a[i+1] = a[i] + T * w[i]
      w[i+1] = w[i] + K * sin(a[i+1])
    E += w**2/2
    W += w
    A += a
  E/=n_ensemble
  W/=n_ensemble
  A/=n_ensemble

  #plt.plot(a/pi, w/pi, 'b-')
  #plt.plot(a[0:10000]/pi, w[0:10000]/pi, 'r-')
  #plt.xlabel(r'$\alpha [\pi]$', fontsize=20)
  #plt.ylabel(r'$\omega [\pi]$', fontsize=20)
 
  
  
  plt.plot(n, E, 'b-')
  plt.xlabel(r'$n$', fontsize=20)
  plt.ylabel(r'$Energy$', fontsize=20)
  
  print "n_ensemble", n_ensemble
  
  
  #E_av = []
  #n_av = []
  #energy = w**2/2
  #for i in np.arange(0,limit-10000, 10000):
    #e_partial = energy[i:i+10000]
    #n_partial = n[i:i+10000]
    #E_av.append(np.average(e_partial))
    #n_av.append(np.average(n_partial))
  
  #plt.plot(n_av, E_av, 'g-')
  #plt.xlabel(r'$n$', fontsize=20)
  #plt.ylabel(r'$Energy$', fontsize=20)
  
  myTable = Table()
  myTable.add_column(Column(data=n, name='n'))
  myTable.add_column(Column(data=A, name='A (Average location)'))
  myTable.add_column(Column(data=W, name='W (Avergae velocity)'))
  myTable.add_column(Column(data=E,  name='Average Energy'))  
  myTable.write('kicke_rotator_2variable', format='ascii.fixed_width',delimiter=',', bookend=False)
  
  plt.show()
    
    
  
  