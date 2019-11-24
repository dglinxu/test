import random
def getNumber(num,start,end):
    aset=set()
    while len(aset)<num:
        n=random.randint(start,end)
        aset.add(n)
    return aset

print(getNumber(10,10,22))

data={'user'+str(i):{'Move'+str(random.randrange(1,10)):random.randint(1,10) for j in range(random.randrange(15))} for i in range(10)}
for k,v in data.items():
    for k1,v1 in v.items():
        print(k,k1,v1)