import re
import urllib.request
import urllib
import os


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


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
        urllib.request.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))
        x = x + 1


html = getHtml("http://tieba.baidu.com/p/2460150866")  # 淘宝的：html = getHtml(r"http://www.taobao.com/")
getImg(html)