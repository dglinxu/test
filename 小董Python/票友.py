#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：小董Python
# @文  件  名：票友.py
# @修改时间：2019/5/14 14:21
# @文件说明：
# 问 题 ： 假 设 己 有 若 干 用 户 名 字 及 其 喜 欢 的 电 影 清 单 ，
# 现 有 某 用 户 ， 己 看 过 并 喜 欢 一 些 电 影 ， 现 在 想 找 个 新 电 影 看 看 ，
# 又 不 知 道 看 什 么 好 。 寻 求 推 荐 ！
# 思 路 ： 根 据 己 有 数 据 ， 查 找 与 该 用 户 爱 好 最 相 似 的 用 户 ，
# 也 就 是 看 过 并 喜 欢 的 电 影 与 该 用 户 最 接 近 ，
# 然 后 从 那 个 用 户 喜 欢 的 电 影 中 选 取 一 个 当 前 用 户 还 没 看 过 的 电 影 ， 进 行 推 荐 。
""""""""""""""""""""""""""
import random
data={'user'+str(i):{'film'+str(random.randrange(1,10)) for j in range(random.randrange(15))} for i in range(10)}
user={'film1','film2','film3','film5'}
similaruser,films=max(data.items(),key=lambda item:len(item[1]&user))#计算电影与样本数据的交集长度，取最长者
print('所有用户数据：')
# for u,f in data.items():
#     print(u,f,sep=':')
for i in data.items():
    print(i[1])
print('相似用户是：',similaruser)
print('TA最喜欢的电影是：',films)
print('没看过的电影是：',films-user)
#print(data)