#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/12 
#开发工具：PyCharm   文件名称：幂函数（递归）.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def pow(x,n):
    if n==0:
        return 1
    else:
        partial=pow(x,n//2)       #当是偶数进行递归，
        result=partial*partial
        if n%2==1:          #这里才判断奇偶
            result*=x       #奇数补乘x
    return result

if __name__ == '__main__':
    print(pow(2,100))
