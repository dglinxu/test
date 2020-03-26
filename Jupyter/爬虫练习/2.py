#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/3/16 
#开发工具：PyCharm   文件名称：2.py
'''说明： 
----------------------------'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        print(driver.title)
        elem = driver.find_element_by_name("q")
        print('++++++++++++++++++++++++++')
        print(elem.text)
        print("++++++++++++++++++++++++++++")
        elem.send_keys("pycon")
        print(elem.text)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()