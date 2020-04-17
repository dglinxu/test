#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：1.py   
#Email:humen@189.cn
'''说明： 
----------------------------'''

name='阿土仔'

def f1():
    global name
    name+='在f1'
    print(name)

f1()