# -*- coding:utf-8 -*-

"""
@Function:
@File    :          test1.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-30 17:48     lizhou         1.0         

"""
from PIL  import Image, ImageDraw, ImageFont

# text = "鑶驋龒龒"
# im = Image.new("RGB", (60, 25), (255, 255, 255))
# dr = ImageDraw.Draw(im)
# font = ImageFont.truetype('icomoon.ttf', 18)
# dr.text((10, 5), text, font=font, fill="#000000")
# im.show()
# im.save("t.png")


s_unicode = u'\u810f\u4e71'
s_str = s_unicode.encode('unicode-escape').decode('unicode-escape')
print(s_str)

unicode_byte="霶鏄朤垘橚和痤旎内偲巊鏾朤".encode("unicode_escape")
unicode_str = str(unicode_byte, encoding = "utf-8")
print(unicode_str)
unicode_strs = unicode_str.split("\\")
for str in unicode_strs:
    if not str or len(str) == 0:
        continue
    # str = eval(r"u'" + '\\u9736' + "'")
    str1 = eval(r"u'" + "\\" + str + "'")
    # str = str.decode('unicode-escape')
    print(str1)

# print('\u548c'.encode('latin-1').decode('unicode_escape'))

