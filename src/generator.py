#Generador.py

import random
import sys

if len(sys.argv) == 3:
    P = int(sys.argv[1])
    T = int(sys.argv[2])
    if P > T:
        print("El valor de P debe ser mayor que T")
else:
    print("ERROR: P y T")

#B = 5#*(10**6)
random.seed(1)

a=[]
print("Generando P ...")
for i in range(P):
    a.append(int(random.uniform(0,10**9)))
    #print(a[i])

#a.sort()
#a = sorted(a)
#print(a)

p = open("P.txt","w")
for i in a:
    #print(a.zfill(9))
    p.write(str(i).zfill(9)+"\n")

print("Listo P está generado")
p.close()

a=[]
print("Generando T ...")
for i in range(T):
    a.append(int(random.uniform(0,10**9)))
    #print(a[i])

a.sort()
#a = sorted(a)
#print(a)

t = open("T.txt","w")
for i in a:
    #print(a.zfill(9))
    t.write(str(i).zfill(9)+"\n")

print("Listo T está generado")
t.close()
