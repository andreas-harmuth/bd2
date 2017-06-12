
L = [40,10,20,30,50,90,60]
L2 = [45,101,2,300,100,92,61]

sort_i = [i[0] for i in sorted(enumerate(L), key=lambda x:x[1])]

TL = [None]*len(L)
for s_i,i in enumerate(sort_i):
    TL[s_i]  = L2[i]

print(sorted(L))
print(TL)