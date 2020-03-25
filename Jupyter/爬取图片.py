#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""""""""""""""""""""""
# @版      本：V1.0
# @作      者：资源
# @联系方式：humen@189.cn
# @创建软件：PyCharm
# @项目名称：Git
# @文  件  名：爬取图片.py
# @修改时间：2020/3/18 10:16
# @文件说明：
""""""""""""""""""""""""""
import  requests
# url='https://goss.veer.com/creative/vcg/veer/1600water/veer-314252786.jpg'
url="https//www.baidu.com"
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
       }
response=requests.get(url=url,headers=header)
# print(response.status_code)
# with open('./图片.jpg','wb') as fp:
#     fp.write(response.content)

