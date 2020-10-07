#!/bin/bash
STARTN=$1
ENDN=$2
DN=$3
BINARY=$4
OUTPATH=$5
for N in `seq ${STARTN} ${DN} ${ENDN}`;
do
    echo  "python3 ${BINARY} ../data/P.txt ../data/T.txt"
    value=`python3 ${BINARY} ../data/P.txt ../data/T.txt`
    echo "$value"
    echo -n "${value}"        >> ${OUTPATH}
    echo " " >> ${OUTPATH}
done

