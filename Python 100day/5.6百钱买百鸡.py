#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   5.6百钱买百鸡.py
@项目名称 :   Git
@修改时间 :   2019/07/10 11:58:17
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''
# 1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
# 问公鸡 母鸡 小鸡各有多少只
# here put the import lib
for i in range(21):
    for j in range(34):
        sum=i*5+j*3+(100-i-j)/3
        if sum==100:
            print('公鸡：%d 母鸡：%d 小鸡：%d'%(i,j,100-i-j))