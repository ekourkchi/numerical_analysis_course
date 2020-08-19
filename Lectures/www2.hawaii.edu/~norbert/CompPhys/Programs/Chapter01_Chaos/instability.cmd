#!/bin/tcsh


# produces table 2-III from two outputs of instability_iter.c

cat tmp1 | awk '{print $1,"&",$2,"&",$3}' > ttt1
cat tmp2 | awk '{print "&",$3,"\\\\"}' > ttt2
paste ttt1 ttt2 | head -15 | tr -s 'e' 'E' 
rm -f ttt1 ttt2


