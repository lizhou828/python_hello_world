# -*- coding:utf-8 -*-

"""
@Function:          抓取国家药品监督管理局的数据
@File    :          get_sfda_data.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-4-11 13:40     lizhou         1.0         

"""

import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import json
from bs4 import BeautifulSoup

url = "http://app1.sfda.gov.cn/datasearchcnda/face3/base.jsp?tableId=26&tableName=TABLE26&title=%E5%9B%BD%E4%BA%A7%E5%99%A8%E6%A2%B0&bcId=152904417281669781044048234789"

def getListData():
    options = webdriver.FirefoxProfile()
    options.set_preference('permissions.default.image', 2)  # 设置火狐浏览器不加载图片，提高抓取数据的效率
    # 打开浏览器
    driver = webdriver.Firefox(options)
    try:
        driver.get(url)
        time.sleep(2) # 强制等待,等待网页加载完成后，才能再去抓取
        soup = BeautifulSoup(driver.page_source, features="lxml")
        if not soup.select("#content"):
            return None
        alinkList = soup.select("#content")[0].div.contents[2].find_all("a")
        for alink in alinkList:
            print(alink.text + "," + alink["href"])
    except Exception as e:
        print(e)
    driver.quit() # 关闭浏览器


if __name__ == "__main__":
    getListData()