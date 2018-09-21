# -*- coding:utf-8 -*-

import re
import urllib.request as request
import time

# 根据url获取网页内容
def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

# 获取当前时间的毫秒数
def getCurrentMillis():
    current = int(1000 * time.time())
    # print("获取当前时间的毫秒数：" + str(current))
    return current


startTime = getCurrentMillis()
html = getHtml("http://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&recorderguid=JYXT_ZJGG_4465&sitePath&security_verify_data=")
endTime = getCurrentMillis()
print(html)
print("获取网页内容完成，耗时：" + str(int(endTime) - int(startTime)) + "毫秒")