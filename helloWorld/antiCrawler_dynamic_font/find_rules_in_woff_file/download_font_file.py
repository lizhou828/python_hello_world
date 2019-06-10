# -*- coding:utf-8 -*-

"""
下载页面上的字体文件，并实时处理
@Function:
@File    :          download_font_file.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-10 14:25     lizhou         1.0         

"""
import re
import urllib
from urllib.request import urlretrieve

if __name__ == "__main__":

    html = ""
    with open("page1.html",'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line :
                line = line.strip()
            if not line :
                continue
            html += line
    print("网页源代码：\n " + html)


    reg = r"\w+\.woff"
    r = re.compile(reg)
    result = re.findall(r,html)
    print(result)

    if result and len(result) == 1:
        font_file_name = result[0]
    url = "http://www.landchina.com/styles/fonts/"
    url += font_file_name
    print("该页面的字体文件链接是：", url)
    urlretrieve(url, font_file_name)

