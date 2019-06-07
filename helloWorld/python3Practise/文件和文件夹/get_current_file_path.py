# -*- coding:utf-8 -*-
import sys
import os
print("当前文件目录：",sys.path[0] )
for i in sys.path:
    print(i)

# __file__ 为当前文件
print("当前文件目录：",os.path.dirname(__file__))