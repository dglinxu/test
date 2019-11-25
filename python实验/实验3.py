#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""""" """""" """""" """""" ""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：python实验
# @文  件  名：实验3.py
# @修改时间：2019/4/23 11:04
# @文件说明：
"""""" """""" """""" """""" ""

import random, math
num = eval(input('请输入飞镖次数：'))
n = 0
for i in range(num):
    x = random.random()
    y = random.random()
    r = x * x + y * y
    # print(i)
    if r <= 1:
        n = n + 1
print('近似圆周率为：', float((n / num) * 4.0))
