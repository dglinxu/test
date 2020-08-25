#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/12 
#开发工具：PyCharm   文件名称：反置序列（递归）.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''

def reverse(S,start,stop):
    if start<stop-1:
        S[start],S[stop-1]=S[stop-1],S[start]
        reverse(S,start+1,stop-1)

if __name__ == '__main__':
    s=[1,2,3,4,5,6,7,8,9]
    reverse(s,0,9)
    print(s)
