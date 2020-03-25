#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin       创建时间：2020/3/16 
#开发工具：PyCharm文件名称：1.py   
'''说明： 
----------------------------'''
import requests
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
img=Image.open('./en.png')
gray=img.convert('L')
w,h=gray.size
data=gray.load()
for i in range(w):
    for j in range(h):
        if data[i,j]<130: #解析
            data[i,j]=0
        else:
            data[i,j]=255
gray.show()
text=pytesseract.image_to_string(gray)
print(text)

