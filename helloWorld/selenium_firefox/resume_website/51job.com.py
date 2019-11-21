import random
import time
from selenium import webdriver
from bs4 import BeautifulSoup



# 版权归作者所有，任何形式转载请联系作者。
# 作者：卒离（来自豆瓣）
# 来源：https://www.douban.com/note/707920971/
#
# 作为老牌的招聘网站，51JOB非常好用，也是我认为最好用的一家。大公司、小公司中型公司的各种职位都有，而且虚假招聘信息非常少。
#
# 51JOB的PC端的搜索功能非常好用。只要确定好行业、薪资、工作年限、企业类型等条件，只要替换搜索关键词就可以搜索其他意向工作，非常方便。不像某些招聘平台， 换一个关键词就要重新设定行业等筛选条件，非常耗时。


def get_url_list(html):
	soup = BeautifulSoup(html, features="lxml")
	if not soup.select_one("#resultList") or soup.select_one("#resultList").text == "":
		return None
	obj_list = []
	for div in soup.select_one("#resultList").find_all("div",attrs ={"class":"el"}):
		if "title" in div['class']:
			continue
		a = div.find_all("p",attrs={"class":"t1"})[0].a
		obj = {}
		obj["href"] = a["href"].strip()
		obj["title"]=  a.text.strip()
		obj_list.append(obj)
	return obj_list


options = webdriver.FirefoxProfile()
driver = webdriver.Firefox(options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )

# 查询上海java的职位
url = "https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,231.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
driver.get(url)
# print(driver.page_source)
list = get_url_list(driver.page_source)
print("第一页数据")
print(list)
# time.sleep(random.randint(3, 5))  # 随机休眠
#
# list = get_url_list(driver.page_source)
# print(list)
for i in range(1,3):
	page_input = driver.find_element_by_id("jump_page")
	# 自动填充input框（send_keys方式只对type=text的input框有效，对其他的隐藏域、只读域等无效）
	page_input.clear()
	page_input.send_keys(i+1)
	next_page_button = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[56]/div/div/div/span[3]")
	next_page_button.click()
	time.sleep(random.randint(3, 5))  # 随机休眠
	print("第{}页数据:".format(i+1))
	list = get_url_list(driver.page_source)
	print(list)

driver.quit()
