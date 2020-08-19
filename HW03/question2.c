﻿
/*****************************************************************
//
//  NAME:		Ehsan Kourkchi
//
//  HOMEWORK:		3
//
//  CLASS:		Scientific Computation (IfA)
//
//  INSTRUCTOR:		Norbert Schorghofer
//
//  DATE:		September 15, 2015           
//
//  FILE:		question2.c
//
//  DESCRIPTION:	This contains the program for the question 2
//
//****************************************************************/
//
// To compile it on my PC:
// $ gcc question2.c -o question2.x  -Ofast -mlong-double-64  -msse2 
// -msse2 flag enables IEEE 754
//
// To run the program:
// $ ./question2.x 
//
// To use Perf command
// $ perf stat -e L1-dcache-load-misses <program/command>
//
//****************************************************************/




# include <stdio.h>


int main(int argc, char *argv[])
{
  
  long double X1 = 0.8;
  long double X2 = 0.8+1.E-15;
  int n=0;
  
  printf("C X%d : %.15lf  %.15lf\n", n, X1, X2);
  for (n=1; n<1010; n++)
  {
    
    // Xn
    X1 = 4.*X1*(1.-X1);
    X2 = 4.*X2*(1.-X2);
    
    if (n == 999)
      printf ("----------------------\n");
    if (n<20 || n>999) 
      printf("C X%d : %.10lf  %.10lf\n", n, X1, X2);
    
  }

// Results: 
// 
// $ ./question2.x 
// C X0 : 0.800000000000000  0.800000000000001
// C X1 : 0.6400000000  0.6400000000
// C X2 : 0.9216000000  0.9216000000
// C X3 : 0.2890137600  0.2890137600
// C X4 : 0.8219392261  0.8219392261
// C X5 : 0.5854205387  0.5854205387
// C X6 : 0.9708133262  0.9708133262
// C X7 : 0.1133392473  0.1133392473
// C X8 : 0.4019738493  0.4019738493
// C X9 : 0.9615634951  0.9615634951
// C X10 : 0.1478365599  0.1478365599
// C X11 : 0.5039236459  0.5039236459
// C X12 : 0.9999384200  0.9999384200
// C X13 : 0.0002463048  0.0002463048
// C X14 : 0.0009849765  0.0009849765
// C X15 : 0.0039360251  0.0039360251
// C X16 : 0.0156821314  0.0156821313
// C X17 : 0.0617448085  0.0617448084
// C X18 : 0.2317295484  0.2317295481
// C X19 : 0.7121238592  0.7121238586
// ----------------------
// C X1000 : 0.4555049566  0.8867826306
// C X1001 : 0.9920807644  0.4015967868
// C X1002 : 0.0314260851  0.9612672305
// C X1003 : 0.1217539451  0.1489301682
// C X1004 : 0.4277196877  0.5069998929
// C X1005 : 0.9791022258  0.9998040060
// C X1006 : 0.0818442289  0.0007838223
// C X1007 : 0.3005830044  0.0031328319
// C X1008 : 0.8409314474  0.0124920689
// C X1009 : 0.5350629926  0.0493440686

  
  
} // END














