def Seletionsort(alist):
    length = len(alist)
    for j in range(length-1):
        min = j
        for i in range(j+1, length):
           if alist[min] > alist[i]:
              min = i
        alist[j],alist[min] = alist[min],alist[j]
        
        

if __name__=='__main__':
    alist=[0,5,9,1,2,6,3]
    print(alist)
    Seletionsort(alist)
    print(alist)
