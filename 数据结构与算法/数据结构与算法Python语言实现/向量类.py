#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/7 
#开发工具：PyCharm   文件名称：myVector.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self,d):
        """Create d-dimensional vector of zeros."""
        self._coords=[0]*d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j]=val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self)!=len(other):
            raise ValueError('dimensions must agree.')
        result=Vector(len(self))  #start with vector of zeros,构建新向量，存和
        for j in range(len(self)):
            result[j]=self[j]+other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords==other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self==other

    def __str__(self):
        """Produce string representation of vector."""
        return '<'+str(self._coords)[1:-1]+'>'   #列表表达

if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45  # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])  # print 45 (via __getitem__)
    u = v + v  # <0, 46, 0, 0, 90> (via __add__)
    print(u)  # print <0, 46, 0, 0, 90>
    total = 0
    for entry in v:  # implicit iteration via __len__ and __getitem__
        total += entry
    v2=Vector(5)
    print(v==v)
    print(v._coords)   #私有变量还是能被外部访问



