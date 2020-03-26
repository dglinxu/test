#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/3/23 
#开发工具：PyCharm   文件名称：攀登者评论.py   
'''说明： 
----------------------------'''
import requests
from lxml import etree

url='https://movie.douban.com/subject/30413052/comments?start=0&limit=%d&sort=new_score&status=P'
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'ll="118297"; bid=7HIeKW5RDAA; trc_cookie_storage=taboola%2520global%253Auser-id%3D0880785c-74f8-48fe-85f9-c3eda50fedc4-tuct4ac6edb; _vwo_uuid_v2=D3CFB7E4FFBFE17E2C7741AC087A03FE0|af7c9dc43a90230876cb1f02f092747d; __utmv=30149280.12238; __utmz=30149280.1580286540.4.4.utmcsr=bd-film.cc|utmccn=(referral)|utmcmd=referral|utmcct=/gq/27146.htm; __gads=ID=399242129e00fcf9:T=1580286556:S=ALNI_Mbhfyo6R61ZBe2dnNNwcpPS6ahP1A; gr_user_id=167e4ee4-74aa-4443-8217-0db7496f5147; __utma=30149280.732919656.1572075041.1584366723.1584972662.6; __utmc=30149280; __utmt=1; __utmb=30149280.2.10.1584972662; __utma=223695111.1800555344.1572075044.1580286540.1584972683.5; __utmb=223695111.0.10.1584972683; __utmc=223695111; __utmz=223695111.1584972683.5.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1584972683%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E6%2594%2580%25E7%2599%25BB%25E8%2580%2585%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=8aac6956f65df3a7.1572075044.5.1584972887.1580286552.',
'Host':'movie.douban.com',
'Referer':'https://movie.douban.com/subject/30413052/',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',}
if __name__ == '__main__':
    for i in range(1):
        if i==25:
            url_climb=url%(490)
        else:
            url_climb=url%(i*20)
        response=requests.get(url=url,headers=headers)
        print(response.text)