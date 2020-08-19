#!/bin/tcsh

cat tvsN.sh | grep MM | awk '{print $4}' >! tmp1
cat tmp | grep u | awk '{print $1}' >! tmp2
pr -mt tmp1 tmp2  | sed 's/u//' >! tmp3
cat tmp3 | sed "s/-D'MM=//" | sed "s/'//" > tmp1
grep -v "|" tmp1 >! tmp2
rm -f a.out tmp1 tmp3
