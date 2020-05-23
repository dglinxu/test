#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/16 
#开发工具：PyCharm   文件名称：奇怪的排序.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
#猴子排序算法
from random import shuffle,randint

def inOrder(li):
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            return False
    return True

def bogo(li):
    while not inOrder(li):
        shuffle(li)
    return li

li=[randint(1,100) for i in range(10)]
t=bogo(li)
print(t)