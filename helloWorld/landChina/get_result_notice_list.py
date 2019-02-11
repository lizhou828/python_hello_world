# -*- coding:utf-8 -*-

# 测试抓取中国土地市场网的结果公告列表页数据

#1、如出现selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 的提示信息
# 则需安装geckodriver，地址 https://github.com/mozilla/geckodriver/releases

import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# profile = FirefoxProfile()
# 激活手动代理配置（对应着在 profile（配置文件）中设置首选项）
# profile.set_preference("network.proxy.type", 1)
# ip及其端口号配置为 http 协议代理
# profile.set_preference("network.proxy.http", "120.193.241.188")
# profile.set_preference("network.proxy.http_port", 80)

# 所有协议共用一种 ip 及端口，如果单独配置，不必设置该项，因为其默认为 False
# profile.set_preference("network.proxy.share_proxy_settings", True)

# 默认本地地址（localhost）不使用代理，如果有些域名在访问时不想使用代理可以使用类似下面的参数设置
# profile.set_preference("network.proxy.no_proxies_on", "localhost")


# driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()

# driver.implicitly_wait(10) # 隐性等待，最长等10秒
# 隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。注意这里有一个弊端，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步，但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，我仍得等到页面全部完成才能执行下一步，我想等我要的元素出来之后就下一步怎么办？有办法，这就要看selenium提供的另一种等待方式——显性等待wait了
# 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…

driver.maximize_window()#窗口最大化显示
try:
    driver.get('http://www.landchina.com/default.aspx?tabid=263&ComName=default')
    # 强制等待,等待网页加载完成后，才能再去抓取
    time.sleep(10)

    TAB_contentTable = driver.find_element_by_id("TAB_contentTable")
    print(TAB_contentTable.text)
except Exception as e:
    print(e)


# 关闭浏览器
driver.quit()