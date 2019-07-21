def Bubble_sort(alist,s):
    length=len(alist)
    for i in range(length-1):
        # 增加一个计数器，如果一个冒泡过程不用变换位置，说明序列已经排好序
        count=0
        for j in range(length-1-i):
            if alist[j]>alist[j+1] and s=='a':
                alist[j],alist[j+1]=alist[j+1],alist[j]
                count+=1
            elif alist[j]<alist[j+1] and s=='d':
                alist[j],alist[j+1]=alist[j+1],alist[j]
                count+=1
        if count==0:
            break


if __name__=='__main__':
    alist=[0,5,9,1,2,6,3]
    blist=[0,5,9,1,2,6,3]
    
    print(alist)
    Bubble_sort(alist,'a')
    Bubble_sort(blist,'d')
    print(alist)
    print(blist)
