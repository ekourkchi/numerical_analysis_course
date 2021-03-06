#*****************************************************************
#
#  NAME:		Ehsan Kourkchi
#
#  HOMEWORK:		6
#
#  CLASS:		Scientific Computation (IfA)
#
#  INSTRUCTOR:		Norbert Schorghofer
#
#  DATE:		October 18, 2015           
#
#  FILE:		ehsan.hw06.py
#
#  DESCRIPTION:	It uses the output of 'ehsan.hw06.py' to make histograms and other analysis.
#  
#  How to run: $ python ehsan.hist.py
#
#****************************************************************

import numpy as np
from math import *
import matplotlib.pyplot as plt
from astropy.table import Table, Column 
import random
import sys
import os


if __name__ == '__main__':
  
  
  inFile = 'energies.v2.txt'
  table = np.genfromtxt(inFile , delimiter=',', filling_values=0, names=True, dtype=None)
  
  E1   = table['E1']
  E2  = table['E2']
  
  E1=E1[0:50000]
  E2=E2[0:50000]
  
  fig = plt.figure(figsize=(6.7, 6), dpi=100)
  ax = fig.add_axes([0.13, 0.1, 0.85,  0.85])
  
  
  Linear_Linear = False
  Log_Linear = False
  Log_Log = False
  Linear_Log = True
  
  
  if Linear_Linear:
    delt = 0.25
    bins = np.arange(0,20,delt)
    bins_center = np.arange(delt,20-0.5*delt,delt)
    n_E1 =  np.histogram(E1/1.E4, bins=bins)
    n_E2 =  np.histogram(E2/1.E4, bins=bins)
    n_E1 = n_E1[0]/1.E4
    n_E2 = n_E2[0]/1.E4
    ax.plot(bins_center, n_E1, label=r'$E_{2000}$')
    ax.plot(bins_center, n_E2, label=r'$E_{1000}$')

    ax.set_ylabel('Number ['+r'$\times 10^4$'+']', fontsize=14)
    ax.set_xlabel('Energy ['+r'$\times 10^4$'+']', fontsize=14)
    #ax.plot(bins_center, np.log10(n_E2), '.-',label=r'$E_{1000}$')
    #ax.plot(bins_center, np.log10(n_E1), '.-',label=r'$E_{1000}$')
  

  
  elif Log_Linear:
    delt = 0.25
    C = 1 + delt
    bins = [1]
    bins_center = [np.sqrt(C)]
    t = 1
    while t < 200.:
      bins.append(t*C)
      bins_center.append(t*C)
      t *= C
    bins_center = bins_center[0:len(bins_center)-1]
    
    
    n_E1 =  np.histogram(E1/1.E3, bins=bins)
    n_E2 =  np.histogram(E2/1.E3, bins=bins)
    n_E1 = n_E1[0]/1.E3
    n_E2 = n_E2[0]/1.E3
    ax.plot(bins_center, n_E1, '.-', label=r'$E_{2000}$')
    ax.plot(bins_center, n_E2, '.-',label=r'$E_{1000}$')

    ax.set_ylabel('Number ['+r'$\times 10^3$'+']', fontsize=14)
    ax.set_xlabel('Energy ['+r'$\times 10^3$'+']', fontsize=14)
    plt.xscale('log')


  elif Log_Log:
    delt = 0.1
    C = 1 + delt
    bins = [1]
    bins_center = [np.sqrt(C)]
    t = 1
    while t < 200.:
      bins.append(t*C)
      bins_center.append(t*C)
      t *= C
    bins_center = bins_center[0:len(bins_center)-1]
    
    
    n_E1 =  np.histogram(E1/1.E3, bins=bins)
    n_E2 =  np.histogram(E2/1.E3, bins=bins)
    n_E1 = n_E1[0]
    n_E2 = n_E2[0]
    ax.plot(bins_center, n_E1, '.-', label=r'$E_{2000}$')
    ax.plot(bins_center, n_E2, '.-',label=r'$E_{1000}$')

    ax.set_ylabel('Number', fontsize=14)
    ax.set_xlabel('Energy ['+r'$\times 10^3$'+']', fontsize=14)
    plt.xscale('log')
    plt.yscale('log')


    

  elif Linear_Log:
    delt = 0.1
    C = 1 + delt
    bins = [1]
    bins_center = [np.sqrt(C)]
    t = 1
    while t < 200.:
      bins.append(t*C)
      bins_center.append(t*C)
      t *= C
    bins_center = bins_center[0:len(bins_center)-1]
    
    
    n_E1 =  np.histogram(E1/1.E3, bins=bins)
    n_E2 =  np.histogram(E2/1.E3, bins=bins)
    n_E1 = n_E1[0]
    n_E2 = n_E2[0]

    ax.set_ylabel('Number', fontsize=14)
    ax.set_xlabel('Energy ['+r'$\times 10^3$'+']', fontsize=14)
    
    #ax.plot(bins_center, n_E2, '.-',label=r'$E_{1000}$')
    ax.plot(bins_center, n_E1, '.-',label=r'$E_{1000}$')
    plt.yscale('log')

   
    x = bins_center[len(bins_center)-20:len(bins_center)-3]
    y = n_E1[len(bins_center)-20:len(bins_center)-3]
    logy = np.log10(y)
    ax.plot(x, y,  '.', color='red')
    z, v = np.polyfit(x, logy, 1, full = False , cov=True)
    p = np.poly1d(z)
    x = np.arange(0,200,5)
    ax.plot(x, 10**(p(x)), '--', color ='black')
    Es = -1.*log10(np.exp(1))/z[0]
    dz =  v[0][0] 
    dEs = dz*log10(np.exp(1))/(z[0]**2)
    print 'Es = ', Es
    print 'dEs = ', dEs  
   

    #x = bins_center[len(bins_center)-20:len(bins_center)-3]
    #y = n_E2[len(bins_center)-20:len(bins_center)-3]
    #logy = np.log10(y)
    #ax.plot(x, y,  '.', color='red')
    #z, v = np.polyfit(x, logy, 1, full = False , cov=True)
    #p = np.poly1d(z)
    #x = np.arange(0,200,5)
    #ax.plot(x, 10**(p(x)), '--', color ='black')
    #Es = -1.*log10(np.exp(1))/z[0]
    #dz =  v[0][0] 
    #dEs = dz*log10(np.exp(1))/(z[0]**2)
    #print 'Es = ', Es
    #print 'dEs = ', dEs
    

   
  
  if Linear_Linear or Log_Linear or Log_Log or Linear_Log:
    ax.legend( loc=1 )
    plt.show()
  
  
  
 
  
  
  
  
  
  
  
