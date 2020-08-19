#include <math.h>
#include <stdio.h>

/* this program is used for numbers in chapter 1 */
int main() {
  int i;
  double r=1, x=1.; 
  printf("%d %5.3f\n",0,x);
  for(i=1;i<=1020;i++) {
    x=sin(r*x);   /* sine map */
    //x=r*x*(1.-x);   /* logistic map */
    //x=r*(1.-fabs(2.*x-1.));   /* tent map */
    //x=fmod(2.*x,1.);
    printf("%d %5.3f\n",i,x);
  }
  return 0;
}
