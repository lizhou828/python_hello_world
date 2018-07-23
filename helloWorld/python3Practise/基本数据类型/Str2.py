print("#格式化输出 占位符" + "-"*100)

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
print("Suzhou is more than %d years. %s lives in here." % (2500, "qiwsir"));
print("Today's temperature is %.2f" % 12.235)
print( "Today's temperature is %+.2f" % 12.235)

print("I like {0}".format("python")) #这就是python非常提倡的string.format()的格式化方法，其中{索引值}作为占位符，
print("Suzhou is more than {year} years. {name} lives in here.".format(year=2500, name="qiwsir"));
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
