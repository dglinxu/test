#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版    本：V1.0
# @作    者：林昕明
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：啊哈算法
# @文 件 名：冒泡法.py
# @修改时间：2019/5/9 20:58
# @文件说明：
""""""""""""""""""""""""""
import random
# la=list(map(int,input('请输入排序数组：').split()))
la=[random.randint(10,100) for i in range(10)]
print('原始表是：',la)
l=len(la)
for i in range(l-1):
    for j in range(1,l-i):
        if la[j-1]<la[j]:
            temp=la[j-1]
            la[j-1]=la[j]
            la[j]=temp
        print(la)
print('最后结果是：',la)