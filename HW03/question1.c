
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
//  FILE:		question1.c
//
//  DESCRIPTION:	This contains the program for the question 1
//
//****************************************************************/
//
// To compile it on my PC:
// $ gcc question1.c -o question1.x  -Ofast -mlong-double-64
//
// To run the program:
// $ ./question1.x 
//
// To use Perf command
// $ perf stat -e L1-dcache-load-misses <program/command>
//
//****************************************************************/

// in python >>> print 1.2-1-0.2
// -5.55111512313e-17




# include <stdio.h>


int main(int argc, char *argv[])
{
  
  double x = 1.2;
  
  printf("1.2-1-0.2 = %.30f \n", 1.2-1-0.2);
  
  printf("\nx = 1.2 \n");
  printf("x-1-0.2 = %.30f \n\n", x-1-0.2);
  
} // END

// results:
// 1.2-1-0.2 = -0.000000000000000055511151231258 
//
// x = 1.2 
// x-1-0.2 = 0.000000000000000000000000000000 

















