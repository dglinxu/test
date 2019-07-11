#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   7.2密码生成器.py
@项目名称 :   Git
@修改时间 :   2019/07/11 17:06:21
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''
# 生成指定长度的随机密码
# here put the import lib
import random

def g_code(c_len=5):
        code='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        code_len=len(code)
        s=''
        for i in range(c_len):
                pos=random.randint(0,code_len-1)
                s=s+code[pos]
        return s

print('密码是：',g_code(8))