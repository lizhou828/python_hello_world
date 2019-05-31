# -*- coding:utf-8 -*-

"""
@Function:
@File    :          readWordsFromFontDic.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-31 8:57     lizhou         1.0         

"""

from aip import AipOcr
import os
import re


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


file_path = r"\landchina_fontDic_2019-05-22.jpg"
image = get_file_content(os.getcwd()+ file_path)

""" 你的 APPID AK SK """
APP_ID = '11460695'
API_KEY = 'uZnBPApbqURDfO8mB1vtGOoX'
SECRET_KEY = 'ksu26AhiugpwOwG5ARVYNHqcRQDP08BT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# """ 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)
# print(result)
text = ""
for li in result['words_result']:

    if not li['words'] or li['words'].startswith("un") or li['words'].startswith("null") or "uni" in li['words']:
        continue

    # if re.match(r'\w',li['words']):
    #     continue
    text += li['words']
print(text)

