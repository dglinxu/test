#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/6/16
# 开发工具：PyCharm   文件名称：DynamicArray类.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''
import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, item):
        """Return element at index item."""
        if not 0 <= item < self._n:
            raise IndexError('invalid index.')
        return self._A[item]

    def append(self, item):
        """Add item to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = item
        self._n += 1

    def insert(self, k, val):
        """Insert value at index k,shifting  subsequent values rightward."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i - 1]
        self._A[k] = val
        self._n += 1
        

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c


    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()


    def __str__(self):
        return '[' + ','.join(map(str, self._A)) + ']'


if __name__ == '__main__':
    data = DynamicArray()

    for i in range(20):
        n = len(data)
        m = data._capacity
        # print('Length:{0:2d};Size in bytes:{1:4d}'.format(n, m))
        data.append(i)
    data.insert(10,100)
    print(list(data))


