def maxDiff(alist):
    maxV=-float('inf')
    a=0
    b=0
    l_alist=len(alist)
    for i in range(l_alist-1):
        for j in range(i+1,l_alist):
            t=alist[j]-alist[i]
            if t>maxV:
                maxV=t
                a=i
                b=j
    return maxV,a,b

def max_diff(alist):
    max_d=-float('inf')
    low_head=0
    for i in range(1,len(alist)):
        if alist[i]<alist[low_head]:
            low_head=i
        else:
            v=alist[i]-alist[low_head]
            if v>max_d:
                max_d=v
                high=i
    return max_d,low_head,high

alist=[1,2,3,0,5,6,7]
print(maxDiff(alist))
print(max_diff(alist))
