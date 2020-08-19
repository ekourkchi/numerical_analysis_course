#include <stdlib.h>
#include <math.h>  

void VecEval(float *C)
{
  int i,j;
  for (i=0; i<N; i++)
    for (j=0; j<=100; j++)
      C[i] = 1./sqrt(1.+i) + j*sin(2.*sin(0.1*i));
}

int main()
{ const int N=1000000;
  float C[N];
  VecEval(C);
}
