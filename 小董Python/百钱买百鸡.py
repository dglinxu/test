
for i in range(21):
    t=int((100-(i*5))/3)
    for j in range(t+1):
        t1=j*3
        t2=100-t-j
        if ((t2/3)+t1+t)==100 and t2%3==0:
            print(i,j,t2)
