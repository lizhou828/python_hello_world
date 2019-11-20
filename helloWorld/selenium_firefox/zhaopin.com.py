import random
import time
from selenium import webdriver
from bs4 import BeautifulSoup

host = "https://www.sz68.com"
def get_url_list(html):
	soup = BeautifulSoup(html, features="lxml")
	if not soup.select_one("#listContent") or soup.select_one("#listContent").text == "":
		return None
	obj_list = []
	for div in soup.select_one("#listContent").find_all("div",attrs ={"class":"contentpile__content__wrapper"}):
		a = div.find_all("a",attrs={"class":"contentpile__content__wrapper__item__info"})[0]
		obj = {}
		obj["href"] = a["href"].strip()
		obj["title"]=  a.find_all("span",attrs={"class":"contentpile__content__wrapper__item__info__box__jobname__title"})[0].text.strip()
		obj_list.append(obj)
	return obj_list

def click_warning_button(driver):
	'''
	点击警告弹出框按钮
	:param driver:
	:return:
	'''
	s = driver.find_elements_by_css_selector(".risk-warning__content")
	if len(s) == 1:
		driver.find_elements_by_css_selector(".risk-warning__content")[0].find_element_by_tag_name("button").click()


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )


# 查询上海java的职位
url = "https://sou.zhaopin.com/?jl=538&kw=java&kt=3"
driver.get(url)
time.sleep(random.randint(3, 5))  # 随机休眠
# print(driver.page_source)
click_warning_button(driver)
list = get_url_list(driver.page_source)
print("第一页数据")
print(list)

#
# list = get_url_list(driver.page_source)
# print(list)
for i in range(1,3):
	# pagination_content = driver.find_element_by_id("pagination_content")
	# page_input = pagination_content.find_all("input",attrs={"class":"soupager__pagebox__goinp"})[0]
	# "/html/body/div[1]/div[1]/div[4]/div[3]/div[3]/div/div[91]/div/div[2]/div/div/input"
	page_input = driver.find_element_by_xpath("//*[@id='pagination_content']/div/div/input")

	# 自动填充input框（send_keys方式只对type=text的input框有效，对其他的隐藏域、只读域等无效）
	page_input.clear()
	page_input.send_keys(i+1)
	# next_page_button = driver.find_all("input",attrs={"class":"soupager__pagebox__gobtn"})[0]
	next_page_button = driver.find_element_by_xpath("//*[@id='pagination_content']/div/div/button")
	next_page_button.click()
	time.sleep(random.randint(3, 5))  # 随机休眠
	click_warning_button(driver)
	print("第{}页数据:".format(i+1))
	list = get_url_list(driver.page_source)
	print(list)

driver.quit()


