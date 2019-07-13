#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 7.6幸运的基督徒.py
@项目名称 : gittest
@修改时间 : 2019/07/12 20:47:56
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
#-------------------------------
#描   述: 《幸运的基督徒》
# 有15个基督徒和15个非基督徒在海上遇险，
# 为了能让一部分人活下来不得不将其中15个人扔到海里面去，
# 有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，
# 报到9的人就扔到海里面，他后面的人接着从1开始报数，
# 报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
# 15个基督徒都幸免于难，问这些人最开始是怎么站的，
# 哪些位置是基督徒哪些位置是非基督徒。                      
#-------------------------------
# here put the import lib
def luck_man(number=30):
    man_list=['基督']*number
    n=15
    sum=0
    while True:
        for i in range(number):
            if man_list[i]=='基督':
                sum+=1
            if sum==9:
                n-=1
                man_list[i]='异教徒'
                sum=0
            if n<1:
                return man_list

print(luck_man(35))



