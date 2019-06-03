#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""
--------------------------------
   工程名称:数据结构与算法
   文件名称:排序.py
   作   者:资源
   邮   箱:humen@189.cn
   创建时间:2018-11-28  14:34
   使用软件:PyCharm
-------------------------------
   描   述:
--------------------------------
"""
# 冒泡排序法，从小到大排序。
def bubbleSort(alist):
    print('冒泡排序法：')
    listLengh=len(alist)
    for i in range(listLengh):
        for j in range(1,listLengh-i):
            if alist[j]<alist[j-1]:
                alist[j-1],alist[j]=alist[j],alist[j-1]

    return alist

# 选择排序
def selectionSort(alist):
    print('选择排序法：')
    listLengh=len(alist)

    for i in range(listLengh):
        minIndex=i
        for j in range(i+1,listLengh):
            if alist[j]<alist[minIndex]:
                minIndex=j
        alist[minIndex],alist[i]=alist[i],alist[minIndex]

    return alist


# 插入排序法
def insertSort(alist):
    print('插入排序法：')
    listLength=len(alist)
    for i in range(1,listLength):
        temp=alist[i]
        j=i
        while j>=0:
            if j==0:
                alist[j]=temp
                break
            elif alist[j-1]>temp:
                alist[j]=alist[j-1]
            else:
                alist[j]=temp
                break
            j-=1

    return alist

def insertionSort(alist):
    for i, item_i in enumerate(alist):

        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i

    return alist

unsorted_list = [10,6, 5, 3, 1, 6, 9, 2, 4,0]
print(insertSort(unsorted_list))