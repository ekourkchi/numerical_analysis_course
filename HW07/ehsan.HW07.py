#*****************************************************************
#
#  NAME:		Ehsan Kourkchi
#
#  HOMEWORK:		7
#
#  CLASS:		Scientific Computation (IfA)
#
#  INSTRUCTOR:		Norbert Schorghofer
#
#  DATE:		October 28, 2015           
#
#  FILE:		ehsan.HW07.py
#
#  DESCRIPTION:	
#  
#  How to run: $ python ehsan.HW07.py
#
#****************************************************************

import numpy as np
from math import *
import matplotlib.pyplot as plt
from astropy.table import Table, Column 
import random
import sys
import os

# eccentricity
# e = 0
e = 0.9671   # for Halley's commet

###############################################
# f(E,M) = E-e*sin(E)-M
# E is the eccentric anomaly
# e is the eccentricity
# M is the mean anomaly
def f(E, M):
  
  return E-e*sin(E)-M

###############################################
# This is the derivative of the function "f(E,M)" 
# that is defined above, with respect to E
def df(E):
  
  return 1-e*cos(E)

###############################################
# Newtons mthod to find the roots of the function "f"
# given its derivative "df". THreshold is the required accuracy 
# of the root, i.e. how accurate we want to reach to zero
# E0 is the first guwss
def newton_solver(f, df, threshold, M, E0):
  
  M = M - 2.*pi*floor(M/2./pi)
  M0 = f(E0, M)
  n_iter = 0 
  
  # setting an upper limit for the number of iterations, i.e. 2000 here
  # Throw an exception if it does not find the root within the define threshold
  while n_iter<2000 and abs(M0) > threshold:
    
    n_iter += 1
    E0 = E0 - f(E0, M)/df(E0)
    M0 = f(E0, M)
    #print M0
  
  if n_iter==2000:
    print "\n# of iteration:" , n_iter
    print "Threshold: ", threshold
    print "M=" , M
    print "\n"
    raise ValueError('Could not find the root after 2000 iteration.') 
    return None
  
  return E0
    
    
  
  
###############################################

if __name__ == '__main__':
  
  
  #E = np.arange(0., 2*pi, 0.0001)
  
  #M = E - e * np.sin(E)
  
  #fig = plt.figure(figsize=(6.7, 6), dpi=100)
  #ax = fig.add_axes([0.13, 0.1, 0.85,  0.85])
    
  #ax.plot(E/2./pi, M/2/pi)

  #ax.set_ylabel(r'$M \sim[2\pi]$', fontsize=14)
  #ax.set_xlabel(r'$E \sim[2\pi]$', fontsize=14)

  
  
  # sampling the time domain
  #dt = 1.E-6
  #t_T = np.arange(0., 1.+dt, dt)
  #M = 2.*pi*t_T
  #E = M*1.0
  
  #for i in range(len(M)):
    #E[i] = newton_solver(f, df, 1.E-15, M[i], 1.)
  
  #a_r = E * 1.0
  #for i in range(len(E)):
    #a_r[i] = (1/(1-e*cos(E[i])))
  
  #ax.plot(t_T, a_r)
  #ax.set_ylabel(r'$a/r$', fontsize=14)
  #ax.set_xlabel(r'$t/T$', fontsize=14)
  #ax.set_ylim([0, 5])
  #print 'first method, <(a/r)^2>_t = ', np.average(a_r**2)
  
  
  
  ### NOTE  #####
  # This is more efficient, since a/r is symetric relative to time (the orbit is symetric anyway),
  # we ca ndo the calculations for half of the time domain only. + using dfferent resolutions for critical parts.
  t_T1 = np.arange(0., 0.1, 1.E-7)
  t_T2 = np.arange(0.1,0.2,1.E-7)
  t_T3 = np.arange(0.2,0.3,1.E-6)
  t_T4 = np.arange(0.3,0.5,1.E-6)
  t_T = np.concatenate((t_T1, t_T2, t_T3, t_T4))
  M = 2.*pi*t_T
  E = M*1.0
  
  for i in range(len(M)):
    E[i] = newton_solver(f, df, 1.E-15, M[i], 1.)
  
  
 
  sum_ar2 = 0
  for i in range(1,len(t_T)):
     sum_ar2 += ((1/(1-e*cos(E[i-1])))**2)*(t_T[i]-t_T[i-1])
  print '2nd method, <(a/r)^2>_t = ', sum_ar2/0.5
  
  plt.show()
  
  
  
