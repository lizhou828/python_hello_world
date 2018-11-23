#!/usr/bin/env python

# -*- coding:utf-8 -*-

import requests

import random



if __name__ == "__main__":

    # 不同浏览器的UA
    # header_list是个list类型，里面每个元素dict类型的
    header_list = [

        # 遨游
        {"user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},

        # 火狐
        {"user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},

        # 谷歌
        {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    ]

    # 不同的代理IP(该代理ip可能已经失效，请自行去站大爷网站上购买开通)

    proxy_list = [
        {"http": "119.27.177.169:8080"},
        {"http": "188.17.155.20:5652"}
    ]

    # 随机获取UA和代理IP
    header = random.choice(header_list)
    proxy = random.choice(proxy_list)

    url = "https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xd74f851b000093ca&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=599&rsv_sug4=1435"

    # 参数3：设置代理


    response = requests.get(url=url, headers=header, proxies=proxy)

    response.encoding = "utf - 8"

#   with open("","") as 是个完整的语句
#   查看open方法的源码可知：
#     此处wb读写文件的的模式,
#      'w'       open for writing, truncating the file first（以写文件的形式打开文件，并首先清楚文件中的数据）
#      'b'       binary mode
    with open("daili.html", "wb") as fp:
        fp.write(response.content)

# 正常的读写文件如下所示：
#     try:
#         f = open('/Users/michael/notfound.txt', 'r')
#         content = f.read()
#         print(content)
#     finally:
#         if f:
#             f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()
# 方法：
#     with open('/path/to/file', 'r',encoding='gbk',errors='ignore') as f:
#         for line in f.readlines():       #调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
#             print(line.strip())          # 把末尾的'\n'删掉
#         print(f.read())                  #调用read()会一次性读取文件的全部内
#        f.write('Hello, world!')

    # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()
    # 函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：即在open方法的参数中加上 errors='ignore'

    # 总结：以后读写文件都使用with open() 语句，不要再像以前那样用f = open() 这种语句了

    # 切换成原来的IP
    requests.get(url, proxies={"http": ""})
