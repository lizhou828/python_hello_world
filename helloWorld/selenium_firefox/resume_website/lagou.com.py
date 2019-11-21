import random
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def get_url_list(html):
	soup = BeautifulSoup(html, features="lxml")
	li_list = soup.find_all("li", attrs={"class": "con_list_item"})
	if not li_list or len(li_list) == 0:
		return None
	obj_list = []
	for li in li_list:
		a = li.find_all("div",attrs={"class":"p_top"})[0].a
		obj = {}
		href= a["href"].strip()
		if "www.lagou.com" not in href:
			href = "https://www.lagou.com"+href
		obj["href"] = href
		obj["title"]=  a.text.strip()
		obj_list.append(obj)
	return obj_list


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )
driver.maximize_window()

# 查询全国java的职位
url_pattern = "https://www.lagou.com/zhaopin/Java/%d/"
url = url_pattern % (1)
driver.get(url)
# print(driver.page_source)
list = get_url_list(driver.page_source)
print("第一页数据")
print(list)
# time.sleep(random.randint(3, 5))  # 随机休眠
#
# list = get_url_list(driver.page_source)
# print(list)
for i in range(2,4):
	time.sleep(random.randint(3, 5))  # 随机休眠、
	# 下一页
	url = url_pattern % (i)
	driver.get(url)
	time.sleep(random.randint(3, 5))  # 随机休眠

	print("第{}页数据:".format(i))
	list = get_url_list(driver.page_source)
	print(list)

driver.quit()
