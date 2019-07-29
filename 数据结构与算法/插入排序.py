def InsertSort(alist):
    # length=len(alist)
    # for i in range(1,length):
    #     for j in range(i):
    #         if alist[i]<alist[j]:
    #             t=alist[i]
    #             for k in range(i,j,-1):
    #                 alist[k]=alist[k-1]
    #             alist[j]=t
    #             break
    # 以上部分自认为的插入排序
    length=len(alist)
    for i in range(1,length):
        for k in range(i,0,-1):
            if alist[k]<alist[k-1]:
                alist[k],alist[k-1]=alist[k-1],alist[k]
            else:
                break


if __name__=='__main__':
    alist=[0,5,9,1,2,6,3]
    print(alist)
    InsertSort(alist)
    print(alist)
    