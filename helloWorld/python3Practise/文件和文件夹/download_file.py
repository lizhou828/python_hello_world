# -*- coding:utf-8 -*-

"""
@Function: 下载文件 并 保存到新文件中
@File    :          download.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-10 14:50     lizhou         1.0         

"""

from urllib.request import urlretrieve
import requests

url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
print("downloading with urllib")
urlretrieve(url, "code.zip")

print("downloading with requests")
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)
