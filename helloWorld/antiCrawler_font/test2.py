# -*- coding:utf-8 -*-

"""
@Function:
@File    :          test2.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-30 17:52     lizhou         1.0         

"""

from fontTools.ttLib import TTFont

#打开本地字体文件
font = TTFont('icomoon.ttf')

# 读取字体的映射关系
uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder() # 参数'cmap' 表示汉字对应的映射 为unicode编码
print(uni_list)