from selenium import webdriver


options = webdriver.FirefoxProfile()
# options.set_preference("general.useragent.override", "Mozilla/5.0()\
#            (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X;\
#            en-us) AppleWebkit/533.17.0 (KHTML, like Gecko)\
#            Version/5.0.2 Mobile/8H7 Safari/6533.18.")

IE_11_USER_AGENT='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
options.set_preference("general.useragent.override", IE_11_USER_AGENT)

# options.update_preferences()
#
# cap = webdriver.DesiredCapabilities.FIREFOX
# cap['firefox_profile'] = options.encoded

driver = webdriver.Firefox(firefox_profile=options)


driver.implicitly_wait(10)#设置超时时间
driver.maximize_window()#窗口最大化显示

#  navigate to the application home page

driver.get("http://www.hngtjy.com/GTJY_HN/")
print(driver.page_source)

#  close the browser window
# driver.quit()