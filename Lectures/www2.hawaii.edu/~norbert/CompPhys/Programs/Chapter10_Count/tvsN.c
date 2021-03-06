#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/home/norbert/Research/Nrc/nrutil.h"

void nrerror(char error_text[]);
float *vector(long nl, long nh);
int *ivector(long nl, long nh);
float **matrix(long nrl, long nrh, long ncl, long nch);

void ludcmp(float **a, int n, int *indx, float *d);
void lubksb(float **a, int n, int *indx, float b[]);

//#define MM 512

int main() {
  const int n=MM; 
  float **a,*b,d;
  int i,j,*indx;
  a=matrix(1,n,1,n);
  b=vector(1,n);
  indx=ivector(1,n);
  for(i=1;i<=n;i++) {
    for(j=1;j<=n;j++)
      a[i][j]=1./(i+j);
    b[i]=1.;
  } 
  ludcmp(a,n,indx,&d);
  lubksb(a,n,indx,b);
  //for(i=1;i<=n;i++) printf("%f ",b[i]);
  printf("\n");
  return 0;
}


#define NRANSI
#define TINY 1.0e-20;

void ludcmp(float **a, int n, int *indx, float *d)
{
	int i,imax,j,k;
	float big,dum,sum,temp;
	float *vv;

	vv=vector(1,n);
	*d=1.0;
	for (i=1;i<=n;i++) {
		big=0.0;
		for (j=1;j<=n;j++)
			if ((temp=fabs(a[i][j])) > big) big=temp;
		if (big == 0.0) nrerror("Singular matrix in routine ludcmp");
		vv[i]=1.0/big;
	}
	for (j=1;j<=n;j++) {
		for (i=1;i<j;i++) {
			sum=a[i][j];
			for (k=1;k<i;k++) sum -= a[i][k]*a[k][j];
			a[i][j]=sum;
		}
		big=0.0;
		for (i=j;i<=n;i++) {
			sum=a[i][j];
			for (k=1;k<j;k++)
				sum -= a[i][k]*a[k][j];
			a[i][j]=sum;
			if ( (dum=vv[i]*fabs(sum)) >= big) {
				big=dum;
				imax=i;
			}
		}
		if (j != imax) {
			for (k=1;k<=n;k++) {
				dum=a[imax][k];
				a[imax][k]=a[j][k];
				a[j][k]=dum;
			}
			*d = -(*d);
			vv[imax]=vv[j];
		}
		indx[j]=imax;
		if (a[j][j] == 0.0) a[j][j]=TINY;
		if (j != n) {
			dum=1.0/(a[j][j]);
			for (i=j+1;i<=n;i++) a[i][j] *= dum;
		}
	}
	free_vector(vv,1,n);
}
#undef TINY
#undef NRANSI




void lubksb(float **a, int n, int *indx, float b[])
{
	int i,ii=0,ip,j;
	float sum;

	for (i=1;i<=n;i++) {
		ip=indx[i];
		sum=b[ip];
		b[ip]=b[i];
		if (ii)
			for (j=ii;j<=i-1;j++) sum -= a[i][j]*b[j];
		else if (sum) ii=i;
		b[i]=sum;
	}
	for (i=n;i>=1;i--) {
		sum=b[i];
		for (j=i+1;j<=n;j++) sum -= a[i][j]*b[j];
		b[i]=sum/a[i][i];
	}
}
