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

def binaryNearest(p, S):
    first = 0
    last = len(S)-1
    find = False
    index = last
    while first<=last and not find:
        mean = (first + last)//2
        t = S[mean]
        if t == p:
            index = mean
            find = True
        else:
            if p < t:
                last = mean - 1
                if last < 0:
                    return index
                index = last
            else:
                first = mean + 1
    return index


def indexSearch(B,P,T):
    R = []
    S = []
    p = []
    P.seek(0)
    T.seek(0)
    block = lenT//B
    for i in range(block):
        T.seek(i*B)
        S.append(T.read(9))
    for i in range(lenP):
        P.seek(10*i)
        p.append(P.read(9))
    for i in p:
        s = binaryNearest(i,S)
        T.seek(s*B)
        t = T.read(B).split("\n")[:-1]

        #t = []
        #for k in range(B//10):
        #    T.seek(s*B+k*10)
        #    d = T.read(9)
        #    if d != "":
        #        t.append(d)
        #    else:
        #        break

        a = binarySearchMemory(i,t)
        if a != False:
            R.append(str(i).zfill(9)+"\n")
    return R

start = time.time()
pe = open(P, "r")
te = open(T, "r")
lenT = os.path.getsize(T)
lenP = os.path.getsize(P)//10
R = indexSearch(500,pe,te)
end = time.time()
elapsed = end - start
out = open("output_indexSearch.txt","w")
#print(R)
#for i in R:
#    out.write(i)
out.writelines(R)
out.close()
pe.close()
te.close()
print(elapsed)
