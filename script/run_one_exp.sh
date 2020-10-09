#!/bin/bash
if [ "$#" -ne 4 ]; then
    echo "run as ${0} STEP-ITERATOR K BINARY OUTPUT"
    echo "for example: sh ${0} 10 6 binarySearch.py time_binary.dat"
    exit;
fi
ENDN=$1
K=$2
BINARY=$3
OUTPATH=$4
for N in `seq 0 1 ${ENDN}`;
do
	acc=0;	
	cd ../data
    echo  "python3 generator.py $((10**4)) $(((10**6)/(2**N)))"	
    value=`python3 generator.py $((10**4)) $(((10**6)/(2**N)))`
	cd ../output
	for q in `seq 1 1 $K`
	do
		echo  "python3 ${BINARY} ../data/P.txt ../data/T.txt"
		value=`python3 ${BINARY} ../data/P.txt ../data/T.txt`
		echo "$value"
		acc=$(echo "scale=10; $value+$acc" | bc)
	done
	mean=$(echo "scale=10; $acc/$K" | bc)
    ro=$((((10**6)/(2**N))/(10**4)))
	#echo "---> $ro	$mean"
	echo " "
	echo " "
	echo -n "$ro ${mean}"        >> ${OUTPATH}
	echo " " >> ${OUTPATH}
done
 
