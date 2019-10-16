import time

from selenium import webdriver


#谷歌浏览器 与 selenium集成
# 谷歌浏览器下载地址
# chromedriver下载地址 https://npm.taobao.org/mirrors/chromedriver/
# https://npm.taobao.org/mirrors/chromedriver/2.40/chromedriver_linux64.zip
# https://npm.taobao.org/mirrors/chromedriver/2.40/chromedriver_win32.zip
# chromedriver.exe文件下载完成后，放到${PYTHON_HOME}目录下

#
# Google Chrome v67.0.3396.79 无更新功能版 64位
# https://redirector.gvt1.com/edgedl/release2/chrome/JVpmpNux-Eo_67.0.3396.79/67.0.3396.79_chrome_installer.exe
# https://dl.google.com/release2/chrome/JVpmpNux-Eo_67.0.3396.79/67.0.3396.79_chrome_installer.exe

# ChromeDriver与Chrome版本对应参照表及ChromeDriver下载链接
# ChromeDriver Version                 Chrome Version
# 78.0.3904.11               78
# 77.0.3865.40                 77
# 77.0.3865.10                 77
# 76.0.3809.126                 76
# 76.0.3809.68                 76
# 76.0.3809.25                 76
# 76.0.3809.12                 76
# 75.0.3770.90                 75
# 75.0.3770.8                 75
# 74.0.3729.6                 74
# 73.0.3683.68                 73
# 72.0.3626.69                 72
# 2.46                 71-73
# 2.46                 71-73
# 2.45                 70-72
# 2.44                 69-71
# 2.43                 69-71
# 2.42                 68-70
# 2.41                 67-69
# 2.40                 66-68
# 2.39                 66-68
# 2.38                 65-67
# 2.37                 64-66
# 2.36                 63-65
# 2.35                 62-64
# …                 …
# ————————————————
# 版权声明：本文为CSDN博主「Peter.Pan」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/BinGISer/article/details/88559532

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome( chrome_options=options)
driver.get("https://map.baidu.com")
print(driver.page_source)
picName="map_baidu.png"
time.sleep(3)
driver.save_screenshot(picName)  # 保存截图
driver.quit()
# ————————————————
# 版权声明：本文为CSDN博主「maggie_up」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Maggie_up/article/details/80790344