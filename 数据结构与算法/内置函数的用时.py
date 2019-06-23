#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 内置函数的用时.py
@项目名称 : gittest
@修改时间 : 2019/06/23 10:49:52
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : 测试PYTHON内置函数不同使用时间，比较用时长度。
@存在问题 : 
'''''''''''''''''''''''''''
import timeit
def f1():
    l1=[]
    for i in range(10000):
        l1.append(i)

def f2():
    l1=[]
    for i in range(10000):
        l1+=[i]

def f3():
    l1=[i for i in range(10000)]

def f4():
    l1=[]
    for i in range(10000):
        l1.insert(0,i)

def f5():
    l1=[]
    for i in range(10000):
        l1.extend([i])

def f6():
    l1=list(range(10000))


t1=timeit.Timer('f1()','from __main__ import f1')
print('append 时间：',t1.timeit(100))
t2=timeit.Timer('f2()','from __main__ import f2')
print('+ 时间：',t2.timeit(100))
t3=timeit.Timer('f3()','from __main__ import f3')
print('[i for i in range(10000)] 时间：',t3.timeit(100))
t4=timeit.Timer('f4()','from __main__ import f4')
print('insert  时间：',t4.timeit(100))
t5=timeit.Timer('f5()','from __main__ import f5')
print('extend  时间：',t5.timeit(100))
t6=timeit.Timer('f6()','from __main__ import f6')
print('range  时间：',t6.timeit(100))
