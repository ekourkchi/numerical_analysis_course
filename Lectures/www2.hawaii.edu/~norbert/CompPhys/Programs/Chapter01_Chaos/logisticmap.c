#include <math.h>
#include <stdlib.h>
#include <stdio.h>

/* this program is used for numbers in chapter 1 */
int main() {
  double r=1, x;
  int i;
  x=0.8;  // for figures 

  for(i=0;i<10+1000;i++) {
    printf("%d %0.3f\n",i,x);
    //x=sin(r*x);
    x=r*x*(1.-x);
    //x=r*(1.-fabs(2.*x-1.));
    //x=fmod(2.*x,1.);
  }
  return 0;
}

// gcc -frounding-math -fsignaling-nans logisticmap.c -lm

