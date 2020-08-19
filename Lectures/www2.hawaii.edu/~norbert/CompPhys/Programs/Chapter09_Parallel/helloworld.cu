#include <stdlib.h>
#include <math.h>

__global__ void VecEval(float *C)
{
  int i = threadIdx.x;
  int j;
  for (j=0; j<=100; j++)
    C[i] = 1./sqrt(1.+i) + j*sin(2.*sin(0.1*i));
}

int main()
{ const int N=1000000;
  float C[N];
  // Kernel invocation with N threads 
  VecEval<<<1, N>>>(C);
}
