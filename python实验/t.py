# -*- coding:utf-8 -*-#
Html_content = """<html><head><title> Python</title></head>
<p class="title"><b>Beautiful Soup的学习</b></p>
<p class="study">学习网址：http://blog.csdn.net/huangzhang_123
 <a href="www.xxx.com" class="abc" id="try1">web开发</a>,
<a href=" www.ccc.com " class="bcd" id="try2">网络爬虫</a> and
<a href=" www.aaa.com " class="efg" id="try3">人工智能</a>;
</p>
<p class="other">...</p>"""

from bs4 import  BeautifulSoup # 引入beautifulsoup
soup = BeautifulSoup(Html_content,'html5lib') #
print(1,soup.head) # 头部原样
print(soup.head.getText()) # 头部数据（即内容）
print(2,soup.title) # 标题原样
print(soup.title.getText()) # 标题数据
print(3,soup.body.b) # 可直接指定标签类别
print(soup.body.b.getText()) # 标签数据
print(4,soup.a)  # 获取指定标签的第一个
print(soup.a.getText()) # 标签内容
print(soup.a['class']) # 标签属性值，若有多个时，同样是返回列表
print(5,soup.find_all('a')) # findall返回的是列表list
for i in soup.find_all('a'): # list的没一个元素是一个标签原样
    print(i)    # 标签原样
    print(i.getText()) # 标签内容
print(7,soup.select('#try3')) # id
print(soup.select('.efg')) # class
print(soup.select('a[class="efg"]')) # 属性

# CSS选择器，可以通过以下3种方式进行查找
# soup.select('#try3') # id
# soup.select('.efg') # class
# soup.select('a[class="efg"]') # 属性
# <a href="www.aaa.com" class="efg" id="try3"> 人工智能</a>

