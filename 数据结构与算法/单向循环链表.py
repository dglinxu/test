#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 单向循环链表.py
@项目名称 : gittest
@修改时间 : 2019/07/02 20:12:55
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
# -------------------------------
# 描   述:
# -------------------------------
# here put the import lib


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkCircleList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        if self.is_empty():
            return 0
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def add_front(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            node.next=self.__head
            self.__head = node
            cur.next=node

    def add_rear(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next=node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next=self.__head

    def insert(self, pos, item):
        node = Node(item)
        if pos <= 0:
            self.add_front(item)
        elif pos > self.length()-1:
            self.add_rear(item)
        else:
            cur=self.__head
            count=1
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.elem == item and self.length()==1:
            self.__head = None
            return True
        while cur.next != self.__head:
            if cur.next.elem == item:
                cur.next = cur.next.next
                return True
            else:
                cur = cur.next
        if cur.elem==item:
            
        return False


if __name__ == '__main__':
    sll =SingleLinkCircleList()
    print(sll.is_empty())
    print(sll.length())
    # sll.add_front(10)
    sll.add_rear(20)
    # sll.add_front(50)
    # sll.add_front(40)
    # sll.add_front(30)
    sll.add_rear(30)
    sll.insert(1,"我是插入值")
    print('单向循环链表所有元素是:')
    sll.travel()
    print('单向链表长度是：%d' % (sll.length()))
    print('查找元素20，结果是：',sll.search(20))
    print(sll.remove(20))
    sll.travel()
