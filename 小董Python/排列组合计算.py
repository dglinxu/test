def c(n,i):
    if not (isinstance(n,int) and isinstance(i,int)):
        print('%s和%s不是整数'%(str(n),str(i)))
        return 
    elif (n<0) and (i<0):
        print('%d和%d没有大于0'%(n,i))
        return 
    elif (n<i):
        print('%d小于%d'%(n,i))
        return 
    sn=1
    si=1
   
    for i in range(i):
        si=si*(i+1)
        sn=sn*(n-i)
    return int(sn/si)

print(c(6.0,2))