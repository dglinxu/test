#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/5/29 
#开发工具：PyCharm   文件名称：统计文件单词数量.py   
#E-mail: humen@189.cn
'''说明： 
----------------------------'''
import profile
import re

def countWords(text):
    #统计文件中英文每个单词的数量，并返回数量最多的50个单词

    with open(text,'r') as fp:
        all_text=fp.read()

    words=re.split('[^a-zA-Z]+',all_text)

    total={}
    for word in words:
        word=word.lower()
        total[word]=total.get(word,0)+1

    result=sorted(total.items(),key=lambda x:x[1],reverse=True)

    print(result[:50])

if __name__ == '__main__':
    text_name='福尔摩斯.txt'
    profile.run("countWords(text_name)")  #这里的函数是有“”包起来的




