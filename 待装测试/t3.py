#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版    本：V1.0
# @作    者：林昕明
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：待装测试
# @文 件 名：t3.py
# @修改时间：2019/4/21 17:36
# @文件说明：
""""""""""""""""""""""""""
num=int(input('请一个输入自然数：'))
list1=list(range(2,num+1))
print(list1)
middle=int(num**0.5)
print(middle)
for i,n in enumerate(list1):
    if i>middle:
        break
    list1[i+1:]=filter(lambda x:x%n!=0,list1[i+1:])
print(list1)