#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo.py.py
# @Time    :2020/7/14 17:24
# @Author  :Harry

from selenium import  webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.title)
