#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''''''''''''''''''''''''''
@文件名称 : temp.py
@项目名称 : gittest
@修改时间 : 2019/06/23 16:29:47
@程序作者 : 虎门资源
@编辑软件 : Visual Studio Code
@程序版本 : V1.0
@联系方式 : humen@189.cn
@License : (C)Copyright 2017-2019, DongGong Humen
@文件说明 : None
@存在问题 : 
'''''''''''''''''''''''''''
#-------------------------------
#描   述:                       
#-------------------------------
# here put the import lib
strs=["flower","flow","flight"]
for tmp in zip(*strs):
    tmp_set=set(tmp)
    print(tmp_set)

print(list(zip(*strs)))        
       res = ""
        # for tmp in zip(*strs):
        #     tmp_set = set(tmp)
        #     if len(tmp_set) == 1:
        #         res += tmp[0]
        #     else:
        #         break
