import random
alist=[random.randint(1,9) for i in range(3)]
blist=[]
for i in alist:
    for j in alist:
        for k in alist:
            t=int(str(i)+str(j)+str(k))
            if t not in blist:
                blist.append(t)
print(alist)
print(sorted(blist))