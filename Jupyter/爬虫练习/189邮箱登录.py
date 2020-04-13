#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/3/21 
#开发工具：PyCharm   文件名称：189邮箱登录.py   
'''说明： 
----------------------------'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url="https://webmail30.189.cn/w2/"
username="humen"
password="A5128900?"

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(url=url)
iframe=driver.find_element_by_xpath("//div[@class='box_right']/iframe")
driver._switch_to.frame(iframe)
account=driver.find_element_by_name('userName')
pwd=driver.find_element_by_name('password')
account.send_keys(username)
pwd.send_keys(password)
time.sleep(5)
driver.find_element_by_id('j-login').click()
time.sleep(30)
driver.close()
