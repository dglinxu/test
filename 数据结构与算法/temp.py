#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""
--------------------------------
   工程名称:数据结构与算法
   文件名称:temp.py
   作   者:资源
   邮   箱:humen@189.cn
   创建时间:2018-12-18  11:10
   使用软件:PyCharm
-------------------------------
   描   述:
--------------------------------
"""


def rotateString(s):
    if not s:
        return True

    l, r = 0, len(s) - 1

    while l < r:
        # find left alphanumeric character
        if not s[l].isalnum():
            l += 1
            continue
        # find right alphanumeric character
        if not s[r].isalnum():
            r -= 1
            continue
        # case insensitive compare
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    #
    return True



s='face book is a app'
t=8


print(rotateString(s))
