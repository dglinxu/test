'''第 1 章 课后练习答案
Excercise1.12 练习
R-1.1 编写一个Python函数 is_multiple(n, m)，用来接收两个整数值 n 和 m，
如果 n 是 m 的倍数，即存在整数 i 使得 n = mi，那么函数返回 True，否则返回 False：
'''
def is_multiple(n,m):
    return (n%m==0)

print(is_multiple(4, 2))

