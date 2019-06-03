#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：python实验
# @文  件  名：实验4.py
# @修改时间：2019/4/23 11:04
# @文件说明：
""""""""""""""""""""""""""
num=int(input('请输入一个自然数：'))
middle=int(num**0.5)
list1=list(range(2,num))
for i,n in enumerate(list1):
    if i>middle:
        break
    list1[i+1:]=filter(lambda x:x%n!=0,list1[i+1:])
print(list1)