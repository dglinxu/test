def QuickSort(alist,first,last):
    if first>=last:
        return
    low=first 
    high=last 
    mid=alist[first]
    while low<high:
        while low<high and alist[high]>=mid:
            high-=1 
        alist[low]=alist[high]
        while low<high and alist[low]<mid:
                low+=1
        alist[high]=alist[low]
    alist[low]=mid  
    QuickSort(alist,first,low-1)
    QuickSort(alist,low+1,last)          


if __name__=='__main__':
    alist=[5,0,9,1,2,6,3,5,10,4,8]
    print(alist)
    QuickSort(alist,0,10)
    print(alist)
        

