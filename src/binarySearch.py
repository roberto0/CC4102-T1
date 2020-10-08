import sys
import time
import os

lenT = 0 
lenP = 0

if len(sys.argv) == 3:
    P = sys.argv[1]
    T = sys.argv[2]
else:
    print("ERROR: P y T")


def binarySearchDisk(p, T):
    first = 0
    T.seek(0)
    last = lenT - 1  #len(T.readlines())-1
    find = False
    while first<=last and not find:
        mean = (first + last)//2
        T.seek(10*mean)
        t = T.read(9)
        if t == p:
            find = t
        else:
            if p < t:
                last = mean-1
            else:
                first = mean+1
    return find

def binarySearch(P,T):
    P.seek(0)
    T.seek(0)
    R = []
    for i in range(lenP):
        P.seek(i*10)
        p = P.read(9)
        a = binarySearchDisk(p,T)
        if a != False:
            R.append(str(p).zfill(9)+"\n")
    return R


start = time.time()
pe = open(P, "r")
te = open(T, "r")
lenT = os.path.getsize(T)//10
lenP = os.path.getsize(P)//10
R = binarySearch(pe,te)
pe.close()
te.close()
out = open("output_binarySearch.txt","w")
#print(R)
#for i in R:
#    out.write(str(i).zfill(9)+"\n")
    #out.write(i)
out.writelines(R)
out.close()
end = time.time()
elapsed = end - start
print(elapsed)
