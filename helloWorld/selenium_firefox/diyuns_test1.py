import random
import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )
url = "http://www.diyuns.com/search-list.html?landType=6"
driver.get(url)
# print(driver.page_source)

time.sleep(random.randint(5,10)) # 随机休眠

print(len(driver.find_elements_by_css_selector(".zhaopaigua_item")))
print(driver.find_elements_by_css_selector(".zhaopaigua_item"))
driver.quit()
