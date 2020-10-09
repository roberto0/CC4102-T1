#!/bin/bash

sh run_one_exp.sh 15 14 ../src/binarySearch.py ../data/time_binary.dat
sh run_one_exp.sh 15 14 ../src/indexSearch.py ../data/time_index.dat
sh run_one_exp.sh 15 14 ../src/linearSearch.py ../data/time_linear.dat
