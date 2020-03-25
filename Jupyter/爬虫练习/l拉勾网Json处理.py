#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/3/17 
#开发工具：PyCharm   文件名称：l拉勾网Json处理.py   
'''说明： 
----------------------------'''
import requests
import json
import jsonpath

url='http://www.lagou.com/lbs/getAllCitySearchLables.json'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response=requests.get(url=url,headers=headers)
data=response.text
json_obj=json.loads(data,encoding='gbk')
# with open('./拉钩.json','w',encoding='GBK') as fp:
#     json.dump(response.content,fp)

