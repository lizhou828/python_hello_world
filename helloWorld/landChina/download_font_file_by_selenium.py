from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.command import Command

profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.dir', 'd:\\')

# 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
profile.set_preference('browser.download.folderList', 1)

# profile.set_preference('browser.download.manager.showWhenStarting', False) # 是否显示下载弹出框

# 对于同类型的文件采取相同的操作，不再询问
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'font/x-font-woff')

driver = webdriver.Firefox(firefox_profile=profile)
url = 'http://www.landchina.com/styles/fonts/vcWMpM88o1GOYCKCpDtZpdu9PwXUDNJM.woff'
# driver.get(url)  有问题，不能自动关闭浏览器
# driver.quit()


driver.command_executor._commands["getCurrentUrl"] = Command.GET_CURRENT_URL

# params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': r"C:\Users\lizhou\Downloads"}}
params = {'url': url}
command_result = driver.execute("get", params)  # 有问题，不能自动关闭浏览器
driver.quit()

# ---------------------
# 作者：breakhl
# 来源：CSDN
# 原文：https://blog.csdn.net/weixin_41812940/article/details/82423892
# 版权声明：本文为博主原创文章，转载请附上博文链接！
