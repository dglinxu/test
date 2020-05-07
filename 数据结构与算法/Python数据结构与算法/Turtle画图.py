#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/6 
#开发工具：PyCharm   文件名称：Turtle画图.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

from turtle import *
# myTurtle=Turtle()
# myWin=myTurtle.getscreen()
#
# def drawSpiral(myTurtle,lineLen):
#     if lineLen>0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-3)
#
# drawSpiral(myTurtle,200)
# myWin.exitonclick()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

t = Turtle()
myWin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110, t)
myWin.exitonclick()