# coding:utf-8
# 避免中文乱码

import codecs
import os
import sys

message = "你"
print(message)
print(type(message))
print(len(message))
print(message.encode())
print(message.encode().decode())

print("遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()")

# 经验三：如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
codecs.open(os.getcwd() + r'\字符格式化.png', encoding='utf8')

print(os.getcwd()) #当前文件的目录
print(os.listdir()) #当前目录下的文件

print(sys.argv) # 当前文件的路径

# 经验四：声明字符串直接加u，声明的字符串就是unicode编码的字符串
a = u"中"
print(a)
