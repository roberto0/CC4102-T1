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

def linearMergeSearch(B,P,T):
    P.seek(0)
    T.seek(0)
    R = []
    p = []
    for i in range(lenP):
        P.seek(10*i)
        p.append(P.read(9))
    p.sort()
    lastT = lenT
    B2 = B//10
    k=0
    for i in range(0,lastT//B):
        t = T.read(B).split("\n")[:-1]
        j = 0
        while j < B2-1 and k<lenP:
            if p[k] == t[j]:
                R.append(str(p[k]).zfill(9)+"\n")
                k=k+1
                j=j+1
            else:
                if p[k] < t[j]:
                    k=k+1
                else:
                    j=j+1

    return R

start = time.time()
pe = open(P, "r")
te = open(T, "r")
lenT = os.path.getsize(T)
lenP = os.path.getsize(P)//10
R = linearMergeSearch(500,pe,te)
end = time.time()
elapsed = end - start
out = open("output_linearMergeSearch.txt","w")
out.writelines(R)
out.close()
pe.close()
te.close()
print(elapsed)
