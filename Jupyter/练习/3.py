#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/4 
#开发工具：PyCharm   文件名称：3.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

stop = False
res = []
while not stop:
    try:
        s = input()
        res.append(s)
    except:
        print(''.join(res[::-1]))
        stop = True
