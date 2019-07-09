#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   2.2计算圆的周长和面积.py
@项目名称 :   Git
@修改时间 :   2019/07/09 14:13:32
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''

# here put the import lib
import math
r=float(input('请输入圆的半径：'))
l=2*math.pi*r
s=math.pi*r**2
print('半径为%.2f厘米圆周的周长是：%.2f厘米' %(r,l))
print('半径为%.2f厘米圆周的面积是：%.2f平方厘米'%(r,s))
