#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/12 
#开发工具：PyCharm   文件名称：文件系统（递归）.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
import os

def disk_usage(path):
    """返回目录当前目录及子目录下的文件总大小"""
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            total+=disk_usage(childpath)
    print('{0:>10}'.format(total),path)
    return total
if __name__ == '__main__':
    path='I:\python\数据结构与算法'
    disk_usage(path)

