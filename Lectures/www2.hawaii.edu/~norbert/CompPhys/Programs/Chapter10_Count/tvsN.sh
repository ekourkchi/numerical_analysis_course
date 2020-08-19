#!/bin/tcsh


gcc -O3 tvsN.c -D'MM=128' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=181' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=255' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=256' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=257' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=362' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=511' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=512' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=513' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=724' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=1023' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=1024' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=1025' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=1448' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=2047' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=2048' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=2049' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=2896' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=4095' ~/Research/Nrc/nrutil.c -lm
time a.out

# will take more than a few minutes

gcc -O3 tvsN.c -D'MM=4096' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=4097' ~/Research/Nrc/nrutil.c -lm
time a.out

gcc -O3 tvsN.c -D'MM=5793' ~/Research/Nrc/nrutil.c -lm
time a.out

