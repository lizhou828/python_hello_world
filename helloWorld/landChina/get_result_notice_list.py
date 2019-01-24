# -*- coding:utf-8 -*-

# 测试抓取中国土地市场网的结果公告列表页数据

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.landchina.com/default.aspx?tabid=263')
print(driver.title)
