import re
import urllib.request as request
import os
import time


# 根据url获取网页内容
def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


# 根据网页内容，正则匹配指定格式的图片，并保存
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  # 要加括号，作为元组返回，抓取淘宝的图片png(先看源码中图片的地址路径)reg = r'data-lazy="(.+?\.png)" '
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = 'D:\\test'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'  # 保存在test路径下
    for imgurl in imglist:
        request.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))
        x += 1


# 获取当前时间的毫秒数
def getCurrentMillis():
    current = int(1000 * time.time())
    # print("获取当前时间的毫秒数：" + str(current))
    return current

startTime = getCurrentMillis()
html = getHtml("http://tieba.baidu.com/p/2460150866")  # 淘宝的：html = getHtml(r"http://www.taobao.com/")
endTime = getCurrentMillis()
print("获取网页内容完成，耗时：" + str(int(endTime) - int(startTime)) + "毫秒")

# startTime = time.time()
# timeArray = time.localtime(startTime)
# startTimeStr=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(str(startTimeStr) + " , " + str(startTime))

startTime = getCurrentMillis()
getImg(html)
endTime = getCurrentMillis()

# endTime = time.time()
# timeArray = time.localtime(endTime)
# endTimeStr=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(str(endTimeStr) + " , " + str(endTime))

print("存储所有的图片完成，耗时：" + str(int(endTime) - int(startTime)) + "毫秒")
