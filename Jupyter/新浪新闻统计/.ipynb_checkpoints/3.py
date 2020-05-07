#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/3 
#开发工具：PyCharm   文件名称：3.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
from lxml import etree
# import MySQLdb
import requests
# conn = MySQLdb.connect(host='localhost', user='root', password='123456', port=3306, db='pap', charset='utf8')
# cursor = conn.cursor()
headers={
    'cookie': 'SINAGLOBAL=219.143.103.186_1574762579.560816; SUB=_2AkMqu5Muf8NxqwJRmPoWxGPlZYt2zgvEieKc52L1JRMyHRl-yD9jqlI5tRB6ATu9wbi9kLo8OxoHjeZApvuLo5C-313s; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF-3HVKvVX-Q5jxCyV-czu2; UOR=news.hao123.com,news.sina.com.cn,; lxlrttp=1572512346; SGUID=1576150846061_21239829; UM_distinctid=16ef9e965c42b-086800c19d1649-32365f08-100200-16ef9e965c52e6; U_TRS1=000000ba.defc709d.5df245d9.4120fff8; rotatecount=2; Apache=220.202.152.119_1576653423.258154; FEED-MIX-SINA-COM-CN=; ULV=1576653263608:18:18:10:220.202.152.119_1576653423.258154:1576653218143; co=10.13.64.57_1576653.469',
    'referer': 'https://news.sina.com.cn/roll/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

}
#新浪滚动新闻首页获取
def req_url(url):
    res=requests.get(url,headers=headers).json()['result']['data']
    # print(res)
    # print(res[1])
    list1=[]
    for i in res:
        list1.append(i['url'])
        # print(list1)
    return list1
    # '//*[@id="artibody"]/p[4]/text()'
#获取滚动新闻详情页函数
def content_url():
    list2=req_url(url)
    for i in list2:
        headers={
            'cookie': 'SINAGLOBAL=219.143.103.186_1574762579.560816; SUB=_2AkMqu5Muf8NxqwJRmPoWxGPlZYt2zgvEieKc52L1JRMyHRl-yD9jqlI5tRB6ATu9wbi9kLo8OxoHjeZApvuLo5C-313s; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF-3HVKvVX-Q5jxCyV-czu2; UOR=news.hao123.com,news.sina.com.cn,; lxlrttp=1572512346; SGUID=1576150846061_21239829; UM_distinctid=16ef9e965c42b-086800c19d1649-32365f08-100200-16ef9e965c52e6; U_TRS1=000000ba.defc709d.5df245d9.4120fff8; Apache=220.202.152.119_1576653423.258154; ULV=1576653263608:18:18:10:220.202.152.119_1576653423.258154:1576653218143; co=10.13.64.57_1576653.469',
            'Referer': 'https://finance.sina.com.cn/stock/usstock/c/2019-12-18/doc-iihnzahi8408745.shtml',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        res1=requests.get(url=i,headers=headers).content.decode('utf-8')
        # print(res1.decode('utf-8'))
        ele=etree.HTML(res1)
        try:
            title=ele.xpath('//h1/text()')[0].strip()
        except:
            continue
        update_time=ele.xpath('//*[@id="top_bar"]/div/div[2]/span[1]/text()')
        content1=ele.xpath('//*[@id="artibody"]/p/text()')
        content=''
        for i in content1:
            content+=i.strip()
        print('title=',title)
        print('update_time=',update_time)
        print('content=',content)
        # '//*[@id="top_bar"]/div/div[2]/span[1]','update_time'：更新时间的xpath
        # '//*[@id="artibody"]/p[1]'title：标题的xpath
        # '//*[@id="artibody"]/p/text()','content'：内容的xpath
        # save_xinlang(title,update_time,content)
#保存函数
def save_xinlang(title,update_time,content):
    try:
        sql = 'insert into xinlang (title,update_time,content) values ("%s","%s","%s")'
        data = (title,update_time,content)
        cursor.execute(sql,data)
        conn.commit()
    except Exception as e:
        print(e)#打印错误信息
        print("出错了")
if __name__ == '__main__':
    for i in range(1, 2):
        url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=' + str(i) + ''
        req_url(url)
        content_url()
