#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/5 
#开发工具：PyCharm   文件名称：进制转换.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
def baseConvert(base,decNumber):
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stack=[]
    while decNumber>0:
        n=decNumber%base
        stack.append(digits[n])
        decNumber=decNumber//base
    base_num=''.join(reversed(stack))
    return base_num

if __name__ == '__main__':
    base=16
    num=1036
    print(baseConvert(base,num))
    print('%x'%num)
