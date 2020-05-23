#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/5/10
# 开发工具：PyCharm   文件名称：List插入与Pop时间.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''
import time
from timeit import Timer

import matplotlib.pyplot as plt


def test1(li):
    return li.insert(0, 0)


def test2(li):
    return li.append(1)


t1, t2, t3, t4 = [], [], [], []
for i in range(100000, 1000001, 100000):
    li = list(range(i))
    t_insert = Timer("test1(li)", "from __main__ import test1,li")
    t_append = Timer("test2(li)", "from __main__ import test2,li")
    t1.append(t_insert.timeit(number=1000))
    t2.append(t_append.timeit(number=1000))
    print(i, t_insert.timeit(number=1000), t_append.timeit(number=1000))
    l1 = list(range(i))
    t_ins = time.time()
    for j in range(1000):
        l1.insert(0, 0)
    t3.append(time.time() - t_ins)
    l2 = list(range(i))
    t_app = time.time()
    for j in range(1000):
        l2.append(0)
    t4.append(time.time() - t_app)
x = list(range(1, 11))
plt.xlabel('X--scale')
plt.ylabel('Y--time')
plt.title('Insert and Append ', fontsize=18)
plt.plot(x, t1, 'g-o', x, t2, 'r-o', x, t3, 'b-o', x, t4, 'y-o')
