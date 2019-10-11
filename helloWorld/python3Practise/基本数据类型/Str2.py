print("#格式化输出 占位符" + "-"*100)
# 在学习Python中三种很重要的格式化字符串占位符方法，长见识了！ http://blog.az009.com/310.html


# 占位符	说明
# %s	字符串(采用str()的显示)
# %r	字符串(采用repr()的显示)
# %c	单个字符
# %b	二进制整数
# %d	十进制整数
# %i	十进制整数
# %o	八进制整数
# %x	十六进制整数
# %e	指数 (基底写为e)
# %E	指数 (基底写为E)
# %f	浮点数
# %F	浮点数，与上相同
# %g	指数(e)或浮点数 (根据显示长度)
# %G	指数(E)或浮点数 (根据显示长度)

print("I like %s " % "python")
print("%d years" % 15)
print("Suzhou is more than %d years. %s lives in here." % (2500, "qiwsir"))
print("Today's temperature is %.2f" % 12.235)
print( "Today's temperature is %+.2f" % 12.235)

print("I like {0}".format("python")) #这就是python非常提倡的string.format()的格式化方法，其中{索引值}作为占位符，
print("Suzhou is more than {year} years. {name} lives in here.".format(year=2500, name="qiwsir"))
lang = "python   hahaha"
print("I love %(program)s" % {"program":lang})

print("字符串常用的方法:\n " + "-"*100)
print(dir(lang)) # 常用的字符串方法
print(help(str.isalpha))
print("python".isalpha()) #字符串全是字母，应该返回True
print("2python".isalpha() )#字符串含非字母，返回False
a = "I love you"
print(a.split(" "))
print(type(a.split(" ")))
b = "hello  world     "
print(b.strip())
print(len(b.strip()))
print(b.rstrip())
print(b.lstrip())
print(b.upper())#字母大写
print(b.lower()) #字母小写
print(b.capitalize()) #首字母大写
print(b.isupper()) #字母是否全是大写
print(b.islower()) #字母是否全是小写
print(b.istitle()) #符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print(b.title())
print(b.split(" "))
c = "www.baidu.com"
d = c.split(".")
print(d)
print(type(d))
print("#".join(d))



# 函数 str.format()，增强了字符串格式化的功能;不仅可以传入字符、数字,还可以将字典及list作为参数传入。
# 1、传入list
words = [1,2,3,4,5,6,7,8,9]
runDay = '2018-05-06'
insert_sql ='{0},insert_sql("{1}",  "{2}",  "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}")'.format(runDay, *words).replace('"', "'").replace('`', '\`')

print(insert_sql)
print(words)

# list的其他传入样式:
my_list = ['格式化输出', 'www.csdn.net']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))# "0" 是可选的
print('"{0}",  "{1}"'.format(*my_list))
print('{0},"{1}",  "{2}"'.format(runDay, *my_list))

# 2、传入dict
site = {"name": "格式化输出", "url": "www.csdn.net"}
print("网站名：{name}, 地址 {url}".format(**site))

# 3、说明
# 传入list时,是将list名将加"*";而传入字典时是将dict名前加"**"。否则会报错:TypeError: format() argument after ** must be a mapping, not list。
# 格式化参数的顺序是按(0,1,2,3,...)的顺序排下来的;但这个顺序是要传入的各个参数的顺序,而非对应的list或dict里的顺序。
# ————————————————
# 版权声明：本文为CSDN博主「BabyFish13」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/BabyFish13/article/details/80223038