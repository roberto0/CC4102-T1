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

def linearSearchMemory(item,L):
    for l in L:
        if l == item:
            return True
    return False

def linearSearch(B,P,T):
    P.seek(0)
    T.seek(0)
    R = []
    p = []
    for i in range(lenP):
        P.seek(10*i)
        p.append(P.read(9))
    lastT = lenT
    #B2 = B//10
    for i in range(0,lastT//B):
        t = T.read(B).split("\n")
        #t = []
        #for k in range(B2):
        #    T.seek(10*k+i*B)
        #    t.append(T.read(9))
        for j in t:
            a = linearSearchMemory(j,p)
            if a != False:
                R.append(str(j).zfill(9)+"\n")
    return R

start = time.time()
pe = open(P, "r")
te = open(T, "r")
lenT = os.path.getsize(T)
lenP = os.path.getsize(P)//10
R = linearSearch(500,pe,te)
pe.close()
te.close()
out = open("output_linearSearch.txt","w")
out.writelines(R)
out.close()
end = time.time()
elapsed = end - start
print(elapsed)
