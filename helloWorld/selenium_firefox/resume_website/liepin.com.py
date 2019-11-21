import random
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# 版权归作者所有，任何形式转载请联系作者。
# 作者：卒离（来自豆瓣）
# 来源：https://www.douban.com/note/707920971/
#
# 猎聘网也很好用，不过猎聘网不是很适合应届生（非常优秀的应届生除外），猎聘网主要是猎头职位，当然现在公司直招的也不少。猎聘网的职位一般都是中高端职位，需要条件优秀，三五年工作经验以上，适合应届生的职位比较少。

def get_url_list(html):
	soup = BeautifulSoup(html, features="lxml")
	div_list = soup.find_all("div", attrs={"class": "sojob-item-main"})
	if not div_list or len(div_list) == 0:
		return None
	obj_list = []
	for div in div_list:
		a = div.div.h3.a
		# a = div.find_all("p",attrs={"class":"t1"})[0].a
		obj = {}
		href= a["href"].strip()
		if "www.liepin.com" not in href:
			href = "https://www.liepin.com"+href
		obj["href"] = href
		obj["title"]=  a.text.strip()
		obj_list.append(obj)
	return obj_list


def scroll_to_page_bottom(driver):
	'''
	原因是因为：
		有的网站的弹窗层遮罩、广告遮罩，导致链接无法点击，会报错：a link is not clickable at point (606,858) because another element <div class="wrap"> obscures it
	:param driver:
	:return:
	'''
	# selenium操控浏览器下拉到页面最底端：
	# driver.execute_script("""window.scrollTo(0, document.body.scrollHeight)""")

	# selenium webdriver——JS滚动到指定位置 : https://www.cnblogs.com/hjhsysu/p/5735339.html
    # JS滚动到指定位置(DOM方式)，确保当前元素可见
	# document.getElementsByClassName("pager")[0].scrollIntoView();

	div_list = driver.find_elements_by_css_selector(".sojob-item-main")
	if not div_list or len(div_list) == 0:
		return
	last_index = 0
	if len(div_list) > 2 :
		last_index = len(div_list)-1-1
	driver.execute_script("""
		document.getElementsByClassName("sojob-item-main")[%d].scrollIntoView();
	""" % (last_index))


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )
driver.maximize_window()

# 查询全国java的职位
url = "https://www.liepin.com/zhaopin/?key=java&d_sfrom=search_fp&searchField=1#sfrom=click-pc_homepage-centre_keywordjobs-search_new"
driver.get(url)
# print(driver.page_source)
list = get_url_list(driver.page_source)
print("第一页数据")
print(list)
scroll_to_page_bottom(driver)
# time.sleep(random.randint(3, 5))  # 随机休眠
#
# list = get_url_list(driver.page_source)
# print(list)
for i in range(1,3):
	time.sleep(random.randint(3, 5))  # 随机休眠、
	# 点击下一页
	driver.find_element_by_link_text(u"下一页").click()
	time.sleep(random.randint(3, 5))  # 随机休眠
	scroll_to_page_bottom(driver)
	print("第{}页数据:".format(i+1))
	list = get_url_list(driver.page_source)
	print(list)

driver.quit()
