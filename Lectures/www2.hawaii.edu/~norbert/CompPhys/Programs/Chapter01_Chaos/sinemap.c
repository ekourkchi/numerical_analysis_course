#include <math.h>
#include <stdlib.h>
#include <stdio.h>

/* this program is used for figures in chapter 1 */
int main() {
  double r, x, xold;
  int i;
  for(r=0.;r<=3.1415927;r+=0.0025) {
    //for(r=0.;r<=4.;r+=0.01/2) {
    x=0.4;  // for figures 
    xold=-9.;
    for(i=1;i<=630;i++) {  // for map_sin figure
      //for(i=1;i<=700-60;i++) {  // for map_log figure
      x=sin(r*x);
      //x=r*x*(1.-x);
      //x=r*(1.-fabs(2.*x-1.));
      //x=fmod(2.*x,1.);
      if (i>=600 && fabs(x-xold)>1.e-5) {
	printf("%f %f\n",r,x);
	xold=x;
      }
    }
    printf("\n");
  }
  return 0;
}
