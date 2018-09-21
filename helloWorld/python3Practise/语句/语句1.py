# -*- coding:utf-8 -*-

print("hello, world");
print("hello", "world");

#print()方法的源码如下
# def print(*args, sep=' ', end='\n', file=None):
# *args 说明 传入的是可变参数 相当于正则表达式中的*，可以类比于java中的 args...
# *args接收的是一个tuple类型（定长的数组）的数据；

for i in [1,2,3,4,5]:
    print(i)


for i in [1,2,3,4,5]:
    print(i,sep="####",end=" ") # 每打印一次，就已空格结尾（查看源代码发现默认是以"\n"结尾）



print()
print("模块导入" + "="*100)

# 非常明确、可读性好
# >>> import math
# >>> math.pow(3,2)


# 如果引入模块多了，可读性就下降了
# >>> from math import pow
# >>> pow(3,2)


# 这是在前面那种方式基础上的发展，将从某个模块引入的函数重命名，比如讲pow充命名为pingfang，然后使用pingfang()就相当于在使用pow()了。
# >>> from math import pow as pingfang
# >>> pingfang(3,2)


# 引入多个函数

# >>> from math import pow, e, pi
# >>> pow(e,pi)
# 23.140692632779263
#
#
# >>> from math import *
# >>> pow(3,2)
# 9.0
# >>> sqrt(9)
# 3.0


print("赋值语句" + "="*100)
# 单个变量赋值
a=1
print(a)

#多个变量赋值
x, y, z = 1, "python", ["hello", "world"]
print(x,y,z)

#两个变量的值对调
print("两个变量的值对调,相当于swap ，真是亮瞎眼!!!!!!!!!")
a = 2
b = 9
print(a,b)
a, b = b, a
print(a,b)

#链式赋值
m = n = "I use python"
print(m,n)
print(id(m))
print(id(n))
#id值相同，说明m , n 指向的是同一个对象
# 还可以用is来判断是不是同一个对象
print(m is n)

print("is关键字=======")
a = "I use python"
b = a
print(a is b)
b = "I use python"
print(a is b) #特别注意在python2.x的版本中，这个地方是false


print("增量赋值 += ")
x = 9
x += 1
print(x)
