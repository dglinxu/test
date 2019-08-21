def quickSort(arr,left,right):
    if left>=right:
        return 
    num=arr[left]
    low=left
    high=right
    while low<high:
        while arr[high]>=num and low<high:
            high-=1 
        arr[low]=arr[high]
        while arr[low]<num and low<high:
            low+=1 
        arr[high]=arr[low]
    arr[high]=num 
    quickSort(arr,left,low-1)
    quickSort(arr,low+1,right)

def QuickSort(arr):
    if len(arr)<2:
        return arr
    num=arr[0]
    arr.remove(num)
    left,right=[],[]
    for i in arr:
        if i>num:
            right.append(i)
        else:
            left.append(i)
    return QuickSort(left)+[num]+QuickSort(right)
    



if __name__=='__main__':
    alist=[0,5,9,1,2,6,3,3,2,5]
    a=[7,1,3,4,5,6]
    print(alist)
    print(QuickSort(alist))
    print(alist)
   
            

# 冒泡算法
# 冒泡排序从小到大排序：一开始交换的区间为0~N-1，将第1个数和第2个数进行比较，
# 前面大于后面，交换两个数，否则不交换。再比较第2个数和第三个数，前面大于后面，
# 交换两个数否则不交换。依次进行，最大的数会放在数组最后的位置。
# 然后将范围变为0~N-2，数组第二大的数会放在数组倒数第二的位置。
# 依次进行整个交换过程，最后范围只剩一个数时数组即为有序。
def BubbleSort(list1):
    list_len=len(list1)
    for i in range(list_len-1): #排序的次数
        t=0 #增加交换标志
        for j in range(1,list_len-i): #需要排序的数据
            if list1[j-1]>list1[j]:
                list1[j-1],list1[j]=list1[j],list1[j-1]
                t+=1
        if t==0: #无交换标明所有数据都是已经排好序
            break