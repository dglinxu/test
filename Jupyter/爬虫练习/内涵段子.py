#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin      创建时间：2020/3/16 
#文件名称：内涵段子.py   开发工具：PyCharm
'''文件说明： 
----------------------------'''
import requests
from lxml import etree

url_first='https://www.neihanba.com/dz/'
url_list="https://www.neihanba.com/dz/list_%d.html"
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
if __name__ == '__main__':
    fp=open('./内涵段子.txt','a',encoding='utf-8')
    for i in range(1,101):
        if i==1:
            url=url_first
        else:
            url=url_list%(i)
        response=requests.get(url,headers=headers)
        response.encoding='GBK'
        # with open('内含段子.html','w',encoding='utf-8') as fp:
        #     fp.write(response.text)
        html=etree.HTML(response.text)
        result=html.xpath('//ul[contains(@class,"piclist")]/li')
        for r in result:
            title=r.xpath('.//h4//a/b/text()')[0].strip()
            content=r.xpath('.//div[@class="f18 mb20"]/text()')[0].strip().strip('\n')
            info=''.join(r.xpath('.//div[@class="ft"]/span//text()')[1:])
            fp.write('%s\t%s\n%s\n'%(title,info,content))
    fp.close()
