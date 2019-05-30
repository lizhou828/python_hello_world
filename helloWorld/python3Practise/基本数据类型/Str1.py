import operator
print("中文转unicode,再转回中文【第一种】：" + "="*50)
s_unicode = u'\u810f\u4e71'
s_str = s_unicode.encode('unicode-escape').decode('unicode-escape')
print(s_str)

print("中文转unicode,再转回中文【第二种】：" + "="*50)
unicode_byte="霶鏄朤垘橚和痤旎内偲巊鏾朤".encode("unicode_escape")
unicode_str = str(unicode_byte, encoding = "utf-8")
print(unicode_str)
unicode_strs = unicode_str.split("\\")
for string in unicode_strs:
    if not string or len(string) == 0:
        continue
    string = eval(r"u'" + "\\" + string + "'")
    print(string)

# 特殊字符 、转义符
print("what's your name ")
print('what"s your name ')
print('what\'s your name ')
print("c:\news")
print(r"c:\news")

# 字符串拼接
print("py" + "thon")
print(str(1) + "haha   数字和字符串拼接")
print(1+ int("2"))


# 转义字符	描述
# \	(在行尾时) 续行符
# \	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出

print("hello.I am liz.\
... My website is 'http://.github.io'.")#这里换行，下一行接续
print("you can connect me by qq\\weibo\\gmail")  #\\是为了要后面那个\
# a = input("请输入数字：")
# print(a)
print("取下标、取指定字符串、取子字符串========================================================================================================================")
print("study python"[0])
print("study python"[::-1])#反转
print("study python"[2:8])
print("study python"[1:])
print("study python"[:10])
print("study python"[:20])
lang = "study python"
print(id(lang))
print(id(lang[:]))# 同一个内存地址值，说明是同一个字符串对象

print("字符串是一种序列，所有序列都有如下基本操作：========================================================================================================================")
print(lang.__len__())
print(len(lang))
print("“+”连接字符串")
print(lang + "asdfjadsfa" + ",后面的列表、元组两种序列，都能够如此实现拼接。")
print("a" in lang)
print("py" in lang) #用来判断某个字符串是不是在另外一个字符串内，或者说判断某个字符串内是否包含某个字符串，如果包含，就返回True，否则返回False。
print(type("py" in lang))
print(max(lang))
print(min(lang))
print(ord('a'))
print(ord('A'))
print(ord('0'))#ord()是一个内建函数，能够返回某个字符（注意，是一个字符，不是多个字符组成的串）所对一个的ASCII值（是十进制的），字符a在ASCII中的值是97，空格在ASCII中也有值，是32。顺便说明，反过来，根据整数值得到相应字符，可以使用chr()：
print(chr(97))
print(chr(65))
print(chr(48))
# print(cmp("abc","abd"))# python2.x的写法

print(operator.gt("abc","abd"))      #意思是greater than（大于）
print(operator.ge(1,2))      #意思是greater and equal（大于等于）
print(operator.eq(1,2))      #意思是equal（等于）
print(operator.le(1,2))     #意思是less and equal（小于等于）
print(operator.lt(1,2))      #意思是less than（小于）

print("神奇的乘法-" * 1000)