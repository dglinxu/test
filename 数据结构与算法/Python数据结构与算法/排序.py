#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/23 
#开发工具：PyCharm   文件名称：排序.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
'''冒泡法'''
def bubbleSort_old(alist):
    for i in range(1,len(alist)):
        for j in range(len(alist)-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist



'''冒泡排序（改进）'''
def bubbleSort(alist):
    exchange=True
    n=len(alist)-1
    while n>0 and exchange:
        exchange=False
        for i in range(n):
            if alist[i]>alist[i+1]:
               alist[i],alist[i+1]=alist[i+1],alist[i]
               exchange=True
        n-=1
    return alist

def selectionSort(alist):
    for i in range(len(alist)-1):
        t=0
        for j in range(1,len(alist)-i):
            if alist[j]>alist[t]:
                t=j
        alist[t],alist[j]=alist[j],alist[t]
    return alist

'''非标准插入排序'''
def insertSort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist

'''标准插入排序'''
def insertSort_comm(alist):
    for index in range(1,len(alist)):
        cur_value=alist[index]
        pos=index
        while pos>0 and alist[pos-1]>cur_value:
            alist[pos]=alist[pos-1]
            pos-=1
        alist[pos]=cur_value
    return alist


'''希尔排序'''
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount,
                  "The list is", alist)
        sublistcount = sublistcount // 2
    return alist

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentvalue


'''归并排序'''
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return alist


'''快速排序'''
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    return alist

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:

        while leftmark <= rightmark and \
                    alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and \
                    rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark




alist=[8,9,2,3,1,5,8,10,12,1,0,20,6]
# print(bubbleSort(alist))
# print(bubbleSort_old(alist))
# print(selectionSort(alist))
# print(insertSort(alist))
# print(insertSort_comm(alist))
# print(shellSort(alist))
# print(mergeSort(alist))
print(quickSort(alist))
