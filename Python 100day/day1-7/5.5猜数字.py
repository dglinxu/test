#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 :   5.5猜数字.py
@项目名称 :   Git
@修改时间 :   2019/07/10 11:35:06
@程序作者 :   虎门资源
@编辑软件 :   Visual Studio Code
@程序版本 :   V1.0
@联系方式 :   humen@189.cn
@License :   (C)Copyright 2017-2019, DongGong Humen
@文件说明 :   None
@存在问题 :       
'''''''''''''''''''''''''''
# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
# here put the import lib
from random import randint
target = randint(1, 100)
count = 0
while True:
    guest = int(input('请输入你猜到的数字：'))
    count += 1
    if guest > target:
        print('%d比目标数字大,重新猜' % guest)
    elif guest < target:
        print('%d比目标数字小,重新猜' % guest)
    else:
        print('%d与目标数字一致，你猜对了！你一共猜了%d次' % (guest, count))
        break
if count > 7:
    print('你的智商堪忧')
