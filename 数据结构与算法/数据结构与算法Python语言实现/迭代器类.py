#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/6/7
# 开发工具：PyCharm   文件名称：迭代器类.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''

class SequenceIterator:
    """支持任何序列类型的迭代器类"""

    def __init__(self, sequence):
        """Create an iteratior for the given sequence."""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element ,or else raise StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration

    def __iter__(self):
        """By convention,an iterator must return itself as an iterator."""
        return self


if __name__ == '__main__':
    seq = list('abcedifghijk')
    iterator = SequenceIterator(seq)
    for i in iterator:
        print(i, end=' ')
    print(iterator.__next__())
