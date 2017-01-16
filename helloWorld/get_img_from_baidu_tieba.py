#coding=utf-8
import urllib
import re

# 根据url获取网页内容
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    print html
    return html

# 根据html内容 正则匹配到图片，并保存
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    x = 0
    for imgUrl in imgList:
        urllib.urlretrieve(imgUrl,'%s.jpg' % x)
        x += 1


html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)