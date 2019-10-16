import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="/usr/local/chromedriver_linux64/chromedriver", chrome_options=options)
driver.get("https://map.baidu.com")
print(driver.page_source)
picName="/usr/local/chromedriver_linux64/baidu.png"
time.sleep(3)
driver.save_screenshot(picName)  # 保存截图
driver.quit()
# ————————————————
# 版权声明：本文为CSDN博主「maggie_up」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Maggie_up/article/details/80790344



# 参考文档：
# Centos7安装python3+Selenium+chrome+chromedriver详细 https://blog.csdn.net/Maggie_up/article/details/80790344
# Centos7安装中文字体   https://blog.csdn.net/lizhou828/article/details/102578868