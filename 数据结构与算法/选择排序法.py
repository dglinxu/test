def Seletionsort(alist):
    length = len(alist)
    if length == 1:
        return
    for j in range(length-1):
        min = alist[j]
        t = j
        for i in range(j+1, length):
           if min > alist[i]:
              min = alist[i]
              t = i
        alist[t] = alist[j]
        alist[j] = min

if __name__=='__main__':
    alist=[0,5,9,1,2,6,3]
    print(alist)
    Seletionsort(alist)
    print(alist)
