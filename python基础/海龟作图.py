#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/11 
#开发工具：PyCharm   文件名称：海龟作图.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
import turtle

def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(15)
        tree(branchLen-10,t)
        t.left(30)
        tree(branchLen-10,t)
        t.right(15)
        t.backward(branchLen)
        

def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('green')
    tree(100,t)
    myWin.exitonclick()


main()
