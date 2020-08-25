#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/11 
#开发工具：PyCharm   文件名称：二分查找算法（递归）.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def binary_search(data,target,low,high):
    """找到返回真值"""
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
if __name__ == '__main__':
    data=[1,2,3,4,5,6,7,8,9]
    target=4.5
    print(binary_search(data,target,0,9))

