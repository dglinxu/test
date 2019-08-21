def quickSort(arr):
    if len(arr)<2:
        return arr
    mid_num=arr[0]
    arr.remove(mid_num)
    left,right=[],[]
    for i in arr:
        if i>=mid_num:
            right.append(i)
        else:
            left.append(i)
    return quickSort(left)+[mid_num]+quickSort(right)
''''
1、选择一个基准值；2、重新构造左、右两个列表，小数在左，大数在右；3、反复迭代，返回一个新的重构列表。
存在问题：因为新增两个空列表，增加了空间开销。
'''
def quickSort1(arr,left,right):
    if left>right:
        return 
    num=arr[left]
    low=left 
    high=right
    while low<high:
        while arr[high]>=num and low<high: #右边的数与目标数比较，一直找到小于目标数的位置
            high-=1 
        arr[low]=arr[high] #把小于目标数的元素给前面
        while arr[low]<num and low<high:
            low+=1 
        arr[high]=arr[low]
    arr[low]=num
    quickSort1(arr,left,low-1)
    quickSort1(arr,low+1,right)
'''
这种方法不用新增空间，是在列表内部完成
'''


b = [11,99,33,69,77,88,55,11,33,36,39,66,44,22]
print(b)
print(quickSort1(b,0,len(b)-1))
print(b)
