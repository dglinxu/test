import random
#列表的方法
alist = []
for i in range(20):
    while True:
        t = random.randint(1, 100)
        if t not in alist:
            alist.append(t)
            break
print(len(alist), alist)

blist = []
while True:
    if len(blist) == 20:
        break
    t = random.randint(1, 100)
    if t not in blist:
        blist.append(t)
print(len(blist), sorted(blist))
#集合方法
aset=set()
while len(aset)<20:
    aset.add(random.randint(1,100))
print(len(aset),aset)

#个函数
clist=random.sample(range(1,101),20) #随机函数取样，取不同的值
print(len(clist),clist)