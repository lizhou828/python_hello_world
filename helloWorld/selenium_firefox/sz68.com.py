import random
import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json
from bs4 import BeautifulSoup

host = "https://www.sz68.com"
def get_url_list(html):
	soup = BeautifulSoup(html, features="lxml")

	if not soup.select_one("#land") or soup.select_one("#land").text == "":
		return None

	url_list = []
	for li in soup.select_one("#land").children:
		href = li.a["href"]
		url_list.append(host + href)
	return url_list


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )
url = "https://www.sz68.com/tiaim/web/getLandTarget?code=0015-0001&childCode=0015-0001"
driver.get(url)
# print(driver.page_source)


time.sleep(random.randint(3, 5))  # 随机休眠
# 点击"土地转让"按钮
li = driver.find_element_by_xpath('//*[@id="business"]/li[4]')
li.click()

time.sleep(random.randint(5, 10))  # 随机休眠
# 点击"土地出让"按钮
li = driver.find_element_by_xpath('//*[@id="business"]/li[3]')
li.click()

# print(len(driver.find_elements_by_css_selector(".zhaopaigua_item")))
# print(driver.find_elements_by_css_selector(".zhaopaigua_item"))


page_input = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div[4]/div/div/input")
# 自动填充input框（send_keys方式只对type=text的input框有效，对其他的隐藏域、只读域等无效）
page_input.clear()
page_input.send_keys(2)
next_page_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div[4]/div/div/button")
next_page_button.click()
list = get_url_list(driver.page_source)
print(list)
driver.quit()


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )

for url in list:
	driver.get(url)
	time.sleep(random.randint(3, 5))  # 随机休眠
	print(url + ",len(driver.page_source)=" + str(len(driver.page_source)))
#
# time.sleep(random.randint(5, 10))  # 随机休眠
# page_input.clear()
# page_input.send_keys(4)
# next_page_button.click()
# list = get_url_list(driver.page_source)
# print(list)
#
# time.sleep(random.randint(5, 10))  # 随机休眠
# page_input.clear()
# page_input.send_keys(6)
# next_page_button.click()
# list = get_url_list(driver.page_source)
# print(list)

driver.quit()
