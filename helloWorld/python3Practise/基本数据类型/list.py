# -*- coding:utf-8 -*-
print("List类型 \n" + "-"*100)
a = []  #定义了一个变量a，它是list类型，并且是空的。
print(type(a))
print(bool(a))     #用内置函数bool()看看list类型的变量a的布尔值，因为是空的，所以为False)
print(a)
a = ['2',3,'qiwsir.github.io',[123,"asdf","ad"]] #list类型的元素可以是任意类型
print(a)
print(type(a))
print(bool(a))

a = ['2',3,'qiwsir.github.io']
print(a[0])
print(a[-1])#从最后元素开始算起
print(a[:2])
print(a[1:])
print(a[2][2:13])#可以对列表元素做2次切片
lst = ['python','java','c++']
print(lst.index('java'))
print(lst[-3:-1])
print(lst[-2:-1]) # 同java 一样，也是“左闭右开”
print(lst[-2])
list1 = [1,2,3,4,5,6]
print(list1[::-1])#反转
print(id(list1))
print(id(list1[::-1]))

list2 = reversed(list1)
print(list(list2))

print(len(list1))
print(list1 + a)#list合并
print(list1 * 3 )
print("java" in lst)
print(max(list1))
print(min(list1))
list1.append(7)#追加元素，无返回值，（只把要追加的元素，放到指定的位置上）
list1[len(list1):] = [8]#追加元素
print(list1)





print("\nlist()函数 \n" + "="*100)
print(dir(list))
la = [1,2,3]
print(id(la))
lb = ["abc","def"]
print(id(lb))
la.extend(lb)#extend()方法无返回值，参数必须要是iterable(可迭代的)可迭代的对象，可以是字符串，可以list,但不能数字
la.extend("aad")#la对象扩容了，id值还是不变,（只把要追加的元素，全都扩容过来）
print(la)
print(id(la))
# hasattr()判断一个字符串是否是可迭代的
print(hasattr(la,'__iter__')) #True
print(hasattr(123,'__iter__'))#False

print(la.index(2))#查找指定元素的下标
lc=[1,2,2,1,1,1,3,4,5,6]
print("lc的含有的元素个数是%d : " % len(lc))#长度，即又多少个元素
print("lc中数字1出现的次数是：%d 次"  % lc.count(1))#统计某个元素出现的次数，没有出现则是0




print("\nlist()函数 \n" + "="*100)
ld=['qiwsir', 'github', 'io',"python"]
ld.insert(0,"java")
ld.insert(-2,"php")
ld.insert(9,"C++")
print(ld)
# ld.remove("adsfadf") # 不能删除不存在的元素
ld.remove("php")
print(ld)

ld.remove("python")
print(ld)