# -*- coding:utf-8 -*-
print("set集合类型，用于去重、交集、并集\n" + "-"*100)
s1 = set("qiwsir") #qiwsir中有两个i，但是在s1中,只有一个i,也就是集合中元素不能重复。
print(s1)
print("利用set()建立起来的集合是可变集合，可变集合都是unhashable类型的。")

s2 = set([123,"google","face","book","facebook","book"])
#在创建集合的时候，如果发现了重复的元素，就会过滤一下，剩下不重复的。
# 而且，从s2的创建可以看出，查看结果是显示的元素顺序排列与开始建立是不同，
# 完全是随意显示的，这说明集合中的元素没有序列。多运行几遍print(s2)  可以看出来
print(s2)
s3 = {} # <class 'dict'>
print(type(s3))
s3 = {"facebook",123}       #通过{}直接创建
print(s3)
print(type(s3))

# 是这种方式不提倡使用，因为在某些情况下，python搞不清楚是字典还是集合
print("list()和set()能够实现两种数据类型之间的转化。")
lst = list(s1)
print(lst)
print("\n看看set数据类型有哪些方法：\n" + "-" * 100)
print(dir(set))
print(help(set.add))
s3.add("lizhou")
print(s3)
a_set = set("python")
print(a_set)
a_set.remove("y") #删除指定元素，如果没有该元素，则报错
print(a_set)
a_set.discard("y") #删除指定元素，如果没有该元素，则报错
print(a_set)#删除指定元素，如果没有该元素，则啥都不干
a_set.clear()
print(a_set)
print(bool(a_set))#空了,bool一下返回False.