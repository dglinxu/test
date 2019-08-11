# def BinarySearch(alist,target):
#     n=len(alist)
#     if n>0:
#         mid=n//2
#         if alist[mid]==target:
#            return True
#         elif alist[mid]<target:
#            return BinarySearch(alist[mid+1:],target)
#         else:
#             return BinarySearch(alist[:mid],target)
#     return False

def BinarySearch(alist,target):
    l=0 
    h=len(alist)-1
    while l<=h:
        mid=(h+l)//2 
        if alist[mid]==target:
            return True
        elif alist[mid]>target:
            h=mid-1
        else:
            l=mid+1
    return False



if __name__=='__main__':
    alist=[1,2,3,4,5,6,7,8,9,10]
    print(BinarySearch(alist,1))
    print(BinarySearch(alist,10))