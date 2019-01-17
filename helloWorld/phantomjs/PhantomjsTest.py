# 安装Phantomjs　　
# 按照系统环境下载phantomjs,下载完成之后，将phantomjs.exe解压到python的script文件夹下

# 安装Selenium
# pip3 install selenium

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
# 设置user-agent请求头
dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_page_load_timeout(40)  # 设置页面最长加载时间为40s

driver.get('https://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-0.dhtml')   #加载网页
data = driver.page_source   #获取网页文本
# driver.save_screenshot('1.png')   #截图保存
print(data)
driver.quit()