#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/4/5
# 开发工具：PyCharm   文件名称：斐波那契迭代器及生成器.py
# E-mail: humen@189.cn
'''说明： f(n)=f(n-1)+f(n-2)-->curr=prev+curr
----------------------------'''


class Fib():
    def __init__(self, n):
        self.prev = 0
        self.curr = 1
        self.count = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            result = self.prev
            self.prev, self.curr = self.curr, self.prev + self.curr
            return result
        else:
            raise StopIteration()


def fib(n):
    prev = 0
    curr = 1
    for i in range(n):
        yield prev
        prev, curr = curr, prev + curr


# for i in Fib(10):
#     print(i)
# print(Fib(10).__sizeof__())

for i in fib(10):
    print(i)
