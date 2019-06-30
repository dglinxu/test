#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 队列的实现.py
@项目名称 : gittest
@修改时间 : 2019/06/30 10:06:43
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
#-------------------------------
#描   述:                       
#-------------------------------
# here put the import lib
class Queue(object):
    def __init__(self):
        self.__list=[]
    
    def enqueue(self,item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list==[]

    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s=Queue()
    print(s.is_empty())
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    print(s.dequeue())
    print(s.size())
    print(s.is_empty())
    

    


