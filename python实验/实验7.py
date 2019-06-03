#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：python实验
# @文  件  名：实验7.py
# @修改时间：2019/4/23 14:06
# @文件说明：
""""""""""""""""""""""""""
for i in range(100,1000):
    la=list(map(int,str(i)))
    num=sum([i**3 for i in la])
    if num==i:
        print(i)

