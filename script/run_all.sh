#!/bin/bash

sh benchmark.sh 2 25 1 ../src/binarySearch.py ../data/time_binary.dat
sh benchmark.sh 2 25 1 ../src/indexSearch.py ../data/time_index.dat
sh benchmark.sh 2 25 1 ../src/linearBinarySearch.py ../data/time_linearBinary.dat
sh benchmark.sh 2 25 1 ../src/linearSearch.py ../data/time_linear.dat
