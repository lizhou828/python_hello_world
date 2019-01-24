# -*- coding:utf-8 -*-

# 测试抓取中国土地市场网的结果公告列表页数据

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


profile = FirefoxProfile()
# 激活手动代理配置（对应着在 profile（配置文件）中设置首选项）
profile.set_preference("network.proxy.type", 1)
# ip及其端口号配置为 http 协议代理
profile.set_preference("network.proxy.http", "120.193.241.188")
profile.set_preference("network.proxy.http_port", 80)

# 所有协议共用一种 ip 及端口，如果单独配置，不必设置该项，因为其默认为 False
profile.set_preference("network.proxy.share_proxy_settings", True)

# 默认本地地址（localhost）不使用代理，如果有些域名在访问时不想使用代理可以使用类似下面的参数设置
profile.set_preference("network.proxy.no_proxies_on", "localhost")


driver = webdriver.Firefox(profile)
driver.get('http://www.landchina.com/default.aspx?tabid=263')
print(driver.title)

# 关闭浏览器
driver.quit()