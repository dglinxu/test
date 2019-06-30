#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 单向链表实现.py
@项目名称 : gittest
@修改时间 : 2019/06/30 15:18:17
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
#-------------------------------
#描   述:   单向链表的实现，生成、增加、删除、插入                    
#-------------------------------
# here put the import lib
class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head==None

    def length(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print()
        
    def add_front(self,item):
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def add_rear(self,item):
        node=Node(item)
        if self.__head==None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,item):
        node=Node(item)
        cur=self.__head
        count=0
        if pos<=0:
           self.add_front(item)
        elif pos>self.length()-1:
             self.add_rear(item)
        else:
            while count<pos-1:
                count+=1
                cur=cur.next
            node.next=cur.next
            cur.next=node

    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False

    def remove(self,item):
        cur=self.__head
        if cur.elem==item:
            self.__head=cur.next
            return True
        while cur.next!=None:
            if cur.next.elem==item:
                cur.next=cur.next.next
                return True
            else:
                cur=cur.next
        return False


if __name__=='__main__':
    sll=SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    # sll.add_front(10)
    # sll.add_rear(20)
    sll.add_front(50)
    # sll.insert(1,"我是插入值")
    print('单向链表所有元素是:')
    sll.travel()   
    print('单向链表长度是：%d'%(sll.length()))
    print(sll.remove(50))
    sll.travel()
