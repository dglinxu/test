#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/4/5 
#开发工具：PyCharm   文件名称：Range生成器.py   
#E-mail: humen@189.cn
'''说明： 用class生成一个迭代器
----------------------------'''

class Range():
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        else:
            self.start = start
            self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration()

r=Range(10)
for i in r:
    print(i)
