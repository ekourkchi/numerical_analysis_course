import numpy as np
from math import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter



def f(x):
  
  y = (3.*pi**4)*(x**2) + log((x-pi)**2)
  
  return y


def bisection(x_min, x_max):
  
  x0 = 0.5*(x_min+x_max)
  y_min = f(x_min)
  y_max = f(x_max)
  
  y0 = f(x0)
  
  if np.sign(y_min) == np.sign(y0):
    x_min = x0
  elif  np.sign(y_max) == np.sign(y0):
    x_max = x0
  
  
  return x_min, x_max, x0, y0
  




if __name__ == '__main__':
  
  
  #x_min = pi-1
  #x_max = pi-1.E-20
  
  #y0 = 1.
  #i = 0
  #while y0 > 0.001 and i<20:
    #x_min, x_max, x0, y0 = bisection(x_min, x_max)
    #print x_min, x_max, x0, y0
    #i+=1
  
  #print x_min, x_max, x0, y0
  
  x = np.arange(0,pi-1,0.01)
  
  x1 = np.arange(pi-1,pi,0.001)
  
  x2 = np.arange(pi+0.001,4.001,0.001)
  
  
  ploting = True
  if ploting:
    fig = plt.figure(figsize=(7.5, 7), dpi=100)
  
    ax = fig.add_axes([0.13, 0.1, 0.85,  0.85]) 
    #ax.xaxis.set_major_locator(MultipleLocator(1))
    #ax.xaxis.set_minor_locator(MultipleLocator(0.2))
  
  
    #plt.minorticks_on()
    plt.tick_params(which='major', length=7, width=1.5)
    plt.tick_params(which='minor', length=4, color='#000033', width=1.0)     
    
    x3 = []
    y3 = []
    y = x + 0.
    for i in range(len(x)):
       y[i] = f(x[i])
       x3.append(x[i])
       y3.append(y[i])
    
    y1 = x1 + 0.
    for i in range(len(x1)):
       y1[i] = f(x1[i])
       x3.append(x1[i])
       y3.append(y1[i])
    
    x3.append(pi)
    y3.append(-100)
       
    y2 = x2 + 0.
    for i in range(len(x2)):
       y2[i] = f(x2[i])
       x3.append(x2[i])
       y3.append(y2[i])


    
    x3 = np.asarray(x3)
    y3 = np.asarray(y3)

       
    ##plt.plot(x, y, '-', markersize = 2, color='black')  # gray    
    ##plt.plot(x1, y1, '-', markersize = 2, color='black')  # gray    
    ##plt.plot(x2, y2, '-', markersize = 2, color='black')  # gray   
    
    
    line, = plt.plot([pi,pi], [3500,4000], '--', markersize = 2, color='green')
    line.set_dashes([1, 2]) 
    plt.xlim(0,4.2)
    plt.ylim(-1,5000)

    plt.plot(x3, y3, '--', markersize = 5, color='black')  # gray   
    
    
    plt.xlabel("x", fontsize=20)
    plt.ylabel("f(x)", fontsize=20)
    ax.annotate('x='+r'$\pi$' , (3, 4100), color='green', size=14)
    print y1[len(y1)-1]
    plt.show()
    

    

    
  
  
  
  

