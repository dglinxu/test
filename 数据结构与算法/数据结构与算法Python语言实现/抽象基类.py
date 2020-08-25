#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/7 
#开发工具：PyCharm   文件名称：抽象基类.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

from abc import  ABCMeta,abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    #抽象方法，含abstractmethod方法的类不能实例化，
    # 继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，
    # 未被装饰的可以不重写
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence;False otherwise."""
        for j in range(len(self)):
            if self[j]==val:
                return True
        return False

    def index(self,val):
        """Return leftmost index at which val is found(or raise ValueError)."""
        for j in range(len(self)):
            if self[j]==val:
                return j
        raise ValueError('Value not in sequence.')

    def count(self,val):
        """Return the number of elements equal to given value."""
        k=0
        for j in range(len(self)):
            if self[j]==val:
                k+=1
        return k

    if __name__ == '__main__':
        seq=Sequence(20)
        print(seq)