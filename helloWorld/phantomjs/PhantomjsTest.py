# 安装Phantomjs　　
# 按照系统环境下载phantomjs,下载完成之后，将phantomjs.exe解压到python的script文件夹下

# 安装Selenium
# pip3 install selenium
import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
# 设置user-agent请求头
dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片

driver = webdriver.PhantomJS(desired_capabilities=dcap,executable_path = r'D:\ProgramFiles\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.set_page_load_timeout(40)  # 设置页面最长加载时间为40s

# driver.get('https://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-0.dhtml')   #加载网页
# data = driver.page_source   #获取网页文本
# # driver.save_screenshot('1.png')   #截图保存
# print(data)


start = time.time()
url = "http://www.csdn.net"
# url = "file:///"+os.getcwd() + os.sep + "baidu_maps_in_ppt.html"
driver.get(url)
time.sleep(5)
data = driver.title
driver.save_screenshot('csdn.png')
end = time.time()
print("对网页" + url + "进行网页截图，耗时" + "%.2f" % (end-start)+ "秒")


# ---------------------
# 版权声明：本文为CSDN博主「Blackrosetian」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Blackrosetian/article/details/75126904


