#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 2.py
@项目名称 : gittest
@修改时间 : 2019/06/03 21:22:35
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''

# here put the import lib

a='1010'
b='1110000'
a1=a[::-1]
b1=b[::-1]
if len(a1)<len(b1):
    l=len(b1)
    a1='0'*(len(b1)-len(a1))+a1
else:
    l=len(a1)
    b1='0'*(len(a1)-len(b1))+b1
print(b1[::-1],a1[::-1])
j=0
s=''
for i in range(l):
    t=int(a1[i])+int(b1[i])+j
    if t<2:
        s=str(t)+s
    elif t==2:
        s=str(0)+s
        j=1
    else:
        s=str(1)+s
        j=1
print(str(j)+s)

