# -*- coding:utf-8 -*-

print("hello, world");
print("hello", "world");

#print()方法的源码如下
# def print(*args, sep=' ', end='\n', file=None):
# *args 说明 传入的是可变参数 相当于正则表达式中的*，可以类比于java中的 args...

for i in [1,2,3,4,5]:
    print(i)


for i in [1,2,3,4,5]:
    print(i,sep="####",end=" ") # 每打印一次，就已空格结尾（查看源代码发现默认是以"\n"结尾）

