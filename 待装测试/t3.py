#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""""" """""" """""" """""" ""
# @版    本：V1.0
# @作    者：林昕明
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：待装测试
# @文 件 名：t3.py
# @修改时间：2019/4/21 17:36
# @文件说明：
"""""" """""" """""" """""" ""
# import wx
# class Wxshow(wx.App):
#     def OnInit(self):
#         frame=wx.Frame(None,title='Hello,world！')
#         frame.Show()
#         return True
#
# if __name__ == '__main__':
#     app=Wxshow('hellow,world!')
#     app.MainLoop()






class A:
    z=0
    def __init__(self,x,y):
        loc
        self.x=x
        self.y=y
        self.z+=1
        print('z',self.z)
    def __add__(self, f):
        a=self.x+f.x
        b=self.y+f.y
        print('a+b',a,b)
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return self.y
a=A(1,2)
b=A(5,6)
C=A(1,2)
print(a)

