#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 第一次尝试.py
@项目名称 : gittest
@修改时间 : 2019/06/23 09:39:29
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : a+b+c=1000,求满足a^2+b^2=c^2的自然数组合。
@存在问题 : 
'''''''''''''''''''''''''''
import time
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print('a,b,c:%d,%d,%d' % (a, b, c))
end_time = time.time()
print('程序运行时间是：%d秒' % (end_time-start_time))
