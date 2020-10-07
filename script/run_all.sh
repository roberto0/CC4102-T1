#!/bin/bash

sh benchmark.sh 2 25 1 binarySearch.py time_binary.dat
sh benchmark.sh 2 25 1 indexSearch.py time_index.dat
sh benchmark.sh 2 25 1 linearBinarySearch.py time_linearBinary.dat
sh benchmark.sh 2 25 1 linearSearch.py time_linear.dat
