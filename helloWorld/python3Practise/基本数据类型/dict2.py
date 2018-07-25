import copy

print("copy")

x = {"name":"qiwsir", "lang":["python", "java", "c"]}
print(id(x))
z = x #赋值操作，仅仅只是指向同一个dict对象
print(z)  #地址值与x相同
print(id(z))
y = x.copy() #完全拷贝，两个变量的地址值不同

print(id(y))



print("python只存储基本类型的数据，比如int,str，对于不是基础类型的，比如刚才字典的值是列表，python不会在被复制的那个对象中重新存储，而是用引用的方式，指向原来的值")
print(x)
print(id(x))
print(id(x["lang"]))
z = copy.deepcopy(x) # 深度拷贝
print(z)
print(id(z))
print(id(z["lang"]))

print("lang" in x) #是否含有key


print(x.get("langa")) #没有这个key 则返回None
print(type(x.get("langa"))) # class 'NoneType'

x.setdefault("lang")  # 如果有这个key,则啥都不干
print(x)
x.setdefault("web") # 如果没有这个key ，则增加一个key ,value = None
print(x)


x.clear() # 清空字典中所有元素
print(x)
# del x # del是将字典删除，内存中就没有它了，不是为“空”。
# print(x)



print("遍历" + "-" * 100)
dd = {"name":"qiwsir", "lang":"python", "web":"www.itdiffer.com"}
dd_kv = dd.items() # 得到一个关于字典的列表，列表中的元素是由字典中的键和值组成的元组
print(dd_kv)
dd_list =list(dd_kv)
print(dd_list )

