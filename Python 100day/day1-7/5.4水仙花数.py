#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   5.4水仙花数.py
@项目名称 :   Git
@修改时间 :   2019/07/10 11:18:37
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''
# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数
# 如: 153 = 1**3 + 5**3 + 3**3
# here put the import lib
for i in range(1,100000):
    temp=i
    sum=0
    for _ in range(len(str(i))):
        sum=sum+(temp%10)**3
        temp=temp//10
    if sum==i:
        print('%d是水仙花数。'%i)


