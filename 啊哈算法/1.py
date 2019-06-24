import time
star=time.time()
for a in range(1,1001):
    # print(a)
    for b in range(1,1001):
        # print(b)
        for c in range(max(a,b)+1,1001):
            if ((a**2)+(b**2))==(c**2):
                print(a,b,c)
                
endt=time.time()
print('程序运行时间：',endt-star)
        