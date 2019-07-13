#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   2.1判断闰年.py
@项目名称 :   Git
@修改时间 :   2019/07/09 14:01:35
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''

# here put the import lib

while True:
    y=input('请输入要判断的年份：')
    if y=='q':
        break
    else:
        year=int(y)
        is_yeap=(year%4==0 and year%100!=0)or(year%400==0)
        print('是否闰年：',is_yeap)
