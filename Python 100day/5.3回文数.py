#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 5.3回文数.py
@项目名称 : gittest
@修改时间 : 2019/07/09 21:47:33
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
# -------------------------------
# 描   述:判断输入的正整数是不是回文数
# 回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
# -------------------------------
# here put the import lib
num = int(input('请输入需要判断的数：'))
temp = num
t=0
while temp > 0:
    t=t*10+temp%10
    temp = temp // 10
    
if t==num:
    print('%d是回环数。' % num)
else:
    print('%d不是回环数。' % num)

s=str(num)


if s==s[::-1]:
    print('%d是回环数。' % num)
else:
    print('%d不是回环数。' % num)
