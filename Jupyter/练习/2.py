#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：2.py   
#E-mail:  humen@189.cn
'''说明： 
----------------------------'''

# name='阿土仔'
# alist=[1,2,3]
# def f1():
#     n=100
#     def inner_f():
#         nonlocal n
#         n+=10
#         print(n)
#     inner_f()
#
#     return n
#
#
#
# def f2():
#     print('f2')
#     f1()
# print(f1())
# f2()
import turtle
def fb(n):
    if n<2:
        return n
    return fb(n-1)+fb(n-2)

def goldLine(t,n):
    if n<2:
        return
    else:
        t.circle(fb(n),90)
        goldLine(t,n-1)


t=turtle.Turtle()
t.penup()
t.right(90)
t.forward(500)
t.left(90)
t.pendown()
t.color('green')
goldLine(t,15)
turtle.done()
