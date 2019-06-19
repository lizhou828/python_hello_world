# 字典类型
# 用{} 括起来的，里面的元素是“key”:"value"    多个key value之间用","隔开
from helloWorld import print_info

mydict = {}
print(type(mydict))
person = {"name":"qiwsir","site":"qiwsir.github.io","language":"python"}
print(person["name"])#如果key不存在，这种方式容易报错 KeyError: 'name'
print("person.get(\"name1\") = %s" % person.get("name1"))#如果key不存在，这种方式不会报错
print(id(person))
person["name"] = "liz"
print(id(person))
print("dict的数据类型也是可变长的，与list相似")
print("在字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型。")

# 利用元组在建构字典：
name = (["first","Google"],["second","Yahoo"])
website = dict(name)
print(website)
print(website.keys()) # 所有的key
print(website.values())#所有的value


website = {}.fromkeys(("third", "forth"), "facebook") # 需要提醒的是，这种方法是重新建立一个dict。
print(website)

# dict中的这类以键值对的映射方式存储数据，是一种非常高效的方法，
# 比如要读取值得时候，如果用列表，python需要从头开始读，直到找到指定的那个索引值。
# 但是，在dict中是通过“键”来得到值。要高效得多。 正是这个特点，键值对这样的形式可以用来存储大规模的数据，
# 因为检索快捷。规模越大越明显。所以 ，mongdb这种非关系型数据库在大数据方面比较流行了。

# 它的基本操作：
#
# len(d)，返回字典(d)中的键值对的数量
# d[key]，返回字典(d)中的键(key)的值
# d[key]=value，将值(value)赋给字典(d)中的键(key)
# del d[key]，删除字典(d)的键(key)项（将该键值对删除）
# key in d，检查字典(d)中是否含有键为key的项、

print("格式化输出")
city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"}
print( " Suzhou is a beautiful city, its area code is %(suzhou)s" % city_code)
print("模板输出")
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"qiwsir", "lang":"python"}
print(temp % my)


dd = {'lang': 'python', 'web': 'www.itdiffer.com', 'name': 'qiwsir'}
print(dd)
dd.pop("name") #根据指定的key 来删除
print(dd)


dic = {1:"1",2:"12",3:"123",4:"1234"}

# for k, v in dic.items():
#     if 3 == k:
#         dic.pop(k, "key:"+str(k)+" not exists!")
# 这样删除key会报错：dictionary changed size during iteration

for key in list(dic.keys()):
     if 3 == key:
        del(dic[key])
print_info(dic)


d1 = {"lang":"python"}
d2 = {"song":"I dreamed a dream"}
d1.update(d2)#把字典d2中的内容加到d1中
print(d1)
print(d2)
d2.update([("name","qiwsir"), ("web","itdiffer.com")])
print(d2)
