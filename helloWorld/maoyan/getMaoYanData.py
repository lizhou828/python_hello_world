# -*- coding:utf-8 -*-
# pip3 install lxml

# 测试抓取猫眼电影的城市列表数据

from selenium import webdriver
import json

driver = webdriver.Firefox()
driver.get('https://maoyan.com/')
city_list = driver.execute_script('return localStorage.getItem("cities")')
city_json = json.loads(city_list)
print(city_json)