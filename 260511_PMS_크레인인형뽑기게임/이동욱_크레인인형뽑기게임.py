import numpy as np
a=[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]

b=np.array(a).T
b

f=[]
move = [1,5,3,5,1,2,1,4]

for l,v in enumerate(move):
    for p,d in enumerate(b[v-1]):

        if d != 0:
            f.append(d)
            b[v-1][p]=0
            break

df = []
for m,s in enumerate(f):
    if f[m]==f[m+1]:
        df.append(s)