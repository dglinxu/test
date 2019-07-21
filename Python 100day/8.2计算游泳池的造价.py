#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 8.2计算游泳池的造价.py
@项目名称 : gittest
@修改时间 : 2019/07/14 20:12:26
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
#-------------------------------
#描   述:修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
# 过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
# 输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)                 
#-------------------------------
# here put the import lib
import math
class Swimming(object):
    def __init__(self,r):
        self.__r=r
        # @property
    def radius(self):
        return self._radius

    # @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0
    def circle(self):
        return 2*math.pi*self.__r
    def area(self):
        return math.pi*self.__r**2
# def main():
#     r=int(input('请输入游泳池的半径：'))
#     w=int(input('请输入小路宽度：'))
#     s1=Swimming(r)
#     s2=Swimming(r+w)
#     print('围墙的造价是：%.2f'%(s2.circle*32.5))
#     print('过道的造价是：%.2f'%((s2.arear-s1.arear)*25))

if __name__=='__main__':
    r=float(input('请输入游泳池的半径：'))
    # w=float(input('请输入小路宽度：'))
    small=Swimming(r)
    big=Swimming(r+3)
    # print('围墙的造价是：%.2f'%(big.circle*32.5))
    # print('过道的造价是：%.2f'%((big.arear-small.arear)*25))
    # print('围墙的造价为: ￥%.1f元' % (big.circle * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))