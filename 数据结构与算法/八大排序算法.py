def quicksort(arr, left, right):
    if left >= right:
        return
    num = arr[left]
    low = left
    high = right
    while low < high:
        while arr[high] >= num and low < high:
            high -= 1
        arr[low] = arr[high]
        while arr[low] < num and low < high:
            low += 1
        arr[high] = arr[low]
    arr[high] = num
    quicksort(arr, left, low-1)
    quicksort(arr, low+1, right)


def QuickSort(myList, start, end):
    '''判断low是否小于high,如果为false,直接返回'''
    if start < end:
        i, j = start, end
        '''设置基准数'''
        base = myList[i]

        while i < j:
            '''如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现'''
            while (i < j) and (myList[j] >= base):
                j = j - 1

            '''如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等'''
            myList[i] = myList[j]

            '''同样的方式比较前半区'''
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        '''做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base'''
        myList[i] = base

        '''递归前后半区'''
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList 
    '''避免无返回值'''


def QuickSort(arr):
    if len(arr) < 2:
        return arr
    num = arr[0]
    arr.remove(num)
    left, right = [], []
    for i in arr:
        if i > num:
            right.append(i)
        else:
            left.append(i)
    return QuickSort(left)+[num]+QuickSort(right)

'''这是算法导论中快速排序的算法'''
def quick_sort(myList,start,end):
    if start<end:
        p=pos(myList,start,end)
        quick_sort(myList,start,p-1)
        quick_sort(myList,p+1,end)

def pos(myList,start,end):
    num=myList[end]
    i=start-1
    for j in range(start,end):
        if myList[j]<=num:
            i+=1
            myList[i],myList[j]=myList[j],myList[i] 
    myList[i+1],myList[end]=num,myList[i+1]
    return i+1

'''侏儒排序法'''
def gnomesort(arr): 
    i=0 
    while i<len(arr):
        if i==0 or arr[i-1]<=arr[i]:
            i+=1 
        else:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i-=1



if __name__ == '__main__':
    arr=[0, 5, 9, 1, 2, 6, 3, 3, 2, 5]
    a = [7, 1, 3, 4, 5, 6]
    print(arr)
    gnomesort(arr)
    print(arr)


# 冒泡算法
# 冒泡排序从小到大排序：一开始交换的区间为0~N-1，将第1个数和第2个数进行比较，
# 前面大于后面，交换两个数，否则不交换。再比较第2个数和第三个数，前面大于后面，
# 交换两个数否则不交换。依次进行，最大的数会放在数组最后的位置。
# 然后将范围变为0~N-2，数组第二大的数会放在数组倒数第二的位置。
# 依次进行整个交换过程，最后范围只剩一个数时数组即为有序。
def BubbleSort(list1):
    list_len = len(list1)
    for i in range(list_len-1):  # 排序的次数
        t = 0  # 增加交换标志
        for j in range(1, list_len-i):  # 需要排序的数据
            if list1[j-1] > list1[j]:
                list1[j-1], list1[j] = list1[j], list1[j-1]
                t += 1
        if t == 0:  # 无交换标明所有数据都是已经排好序
            break
