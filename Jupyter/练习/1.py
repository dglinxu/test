#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：1.py   
#Email:humen@189.cn
'''说明： 
----------------------------'''

class People:
    def __init__(self,name,city):
        self.name=name
        self.city=city


    def __str__(self):
        s='{}-{}'.format(self.city,self.name)
        return s

    __repr__ = __str__

    def move_to_city(self,newcity):
        self.city=newcity

    def __lt__(self, other):
        return str(self.city)<str(other.city)

a=People('赵子龙','常山')
b=People('张飞','燕人')
c=People('孙悟空','花果山')
d=People('刘邦','沛县')
e=People(10,12)
a_list=[a,b,c,d,e]
print(a_list)
print(sorted(a_list))