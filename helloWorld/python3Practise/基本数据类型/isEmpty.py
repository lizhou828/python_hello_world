# -*- coding:utf-8 -*-
#False,0,'',[],{},()都可以视为假
m1 = []
m2 = {}
m3 = ()
m4 = {"name":1,"age":2}

#也可用if not m1:print("m1不是列表")

if m1:
    print("m1是列表")
else:
    print("m1不是列表")

if m2:
    print("m2是字典")
else:
    print("m2不是字典")

if m3:
    print("m3是元组")
else:
    print("m3不是元组")


#判断字典是否存在某个key
if('age' in m4.keys()):
    print("m4包含age")
else:
    print("m4不包含age")