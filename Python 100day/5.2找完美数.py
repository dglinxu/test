#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : 5.2找完美数.py
@项目名称 : gittest
@修改时间 : 2019/07/09 21:02:05
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
# -------------------------------
# 描   述:  找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# -------------------------------
# here put the import lib
import math
for num in range(1, 10000):
    sum = 0
    sum_list=[]
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            sum_list.append(factor)
            if factor > 1 and num / factor != factor:
                sum += num / factor
                sum_list.append(num/factor)
    if sum == num:
        sum_list.sort()
        print('%d='%num,end='')
        # for i in range(len(sum_list)-1):
        #     print('%d+'%sum_list[i],end='')
        # print(int(sum_list[-1]))
        for i in sum_list:
            print('%d'%i,end='')
            if i==sum_list[-1]:
                print()
            else:
                print('+',end='')