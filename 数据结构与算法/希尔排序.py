def ShellSort(alist):
    length=len(alist)
    gap=length//2 #确定两个元素的距离
    while gap>0: #距离逐渐缩小，最终距离为1
        for i in range(gap,length): #内核为插入排序
            j=i
            while j>0:
                if alist[j]<alist[j-gap]:
                    alist[j],alist[j-gap]=alist[j-gap],alist[j]
                    j-=gap
                else:
                    break
        gap=gap//2 #每次距离对折

if __name__=='__main__':
    alist=[0,5,9,1,2,6,3]
    print(alist)
    ShellSort(alist)
    print(alist)
