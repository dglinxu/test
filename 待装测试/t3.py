#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""""" """""" """""" """""" ""
# @版    本：V1.0
# @作    者：林昕明
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：待装测试
# @文 件 名：t3.py
# @修改时间：2019/4/21 17:36
# @文件说明：
"""""" """""" """""" """""" ""
def fn(n):
    for i in range(n):
        yield i


nums=list(range(10))
# for i in range(31): 
#     print(i+1,fn(i+1)).
for i in range(10):

    print(fn(10))