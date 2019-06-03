#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：python实验
# @文  件  名：实验6.py
# @修改时间：2019/4/23 11:00
# @文件说明：求组合Cni的值
""""""""""""""""""""""""""
def cni(n,i):
    miniNI=min(i,n-i)
    # maxNI=max(i,n)
    result=1
    for j in range(0,miniNI):
        result=result*(n-j)/(miniNI-j)
    return result
print(cni(6,2))