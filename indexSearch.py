
import sys
import time
import os

lenT = 0

if len(sys.argv) == 3:
    P = sys.argv[1]
    T = sys.argv[2]
else:
    print("ERROR: P y T")

def linearSearchMemory(item,L):
    for l in L:
        if l == item:
            return True
    return False

def binarySearchMemory(p, T):
    first = 0
    last = len(T)-1
    find = False
    while first<=last and not find:
        mean = (first + last)//2
        t = T[mean] 
        if t == p:
            find = True
        else:
            if p < t:
                last = mean-1
            else:
                first = mean+1
    return find

def binaryNearest(p, T):
    first = 0
    last = len(T)-1
    find = False
    index = False
    while first<=last and not find:
        mean = (first + last)//2
        t = T[mean]
        if t == p:
            index = mean
            find = True
        else:
            if p < t:
                last = mean - 1
                index = last
            else:
                index = first
                first = mean + 1
    return last


def indexSearch(B,P,T):
    R = []
    S = []
    P.seek(0)
    T.seek(0)
    block = lenT//B #(10*len(T.readlines()))//B
    for i in range(block):
        T.seek(0)
        T.seek(i*B)
        S.append(T.read(9))
    T.seek(0)
    p = P.readlines()
    for i in p:
        s = binaryNearest(i[:-1],S)
        T.seek(0)
        T.seek(s*B)
        t = T.read(B).split("\n")[:-1]
        a = binarySearchMemory(i[:-1],t)
        if a != False:
            R.append(i)
    return R

start = time.time()
pe = open(P, "r")
te = open(T, "r")
lenT = os.path.getsize(T)
R = indexSearch(500,pe,te)
pe.close()
te.close()
out = open("output_indexSearch.txt","w")
for i in R:
    out.write(i)
out.close()
end = time.time()
elapsed = end - start
print(elapsed)
