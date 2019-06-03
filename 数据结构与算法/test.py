#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""
--------------------------------
   工程名称:数据结构与算法
   文件名称:test.py
   作   者:资源
   邮   箱:humen@189.cn
   创建时间:2018-11-29  11:54
   使用软件:PyCharm
-------------------------------
   描   述:
--------------------------------
"""


def compareStrings(strs):
    dic = {}
    result = []
    for string in strs:
        sortedstr = "".join(sorted(string));
        dic[sortedstr] = [string] if sortedstr not in dic else dic[sortedstr] + [string]
    print(dic)
    for key in dic:
        result += dic[key] if len(dic[key]) >= 2 else []
    return result

strs=["lint","intl","inlt","code"]
b="A"

print(compareStrings(strs))
