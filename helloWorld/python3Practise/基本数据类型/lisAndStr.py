print("list类型与str类型的比较\n" + "-"*1000)
# 相同点
# 都属于序列类型的数据
# 所谓序列类型的数据，就是说它的每一个元素都可以通过指定一个编号，行话叫做“偏移量”的方式得到，而要想一次得到多个元素，可以使用切片。偏移量从0开始，总元素数减1结束。

# 区别
# list和str的最大区别是：list是可以改变的，str不可变。这个怎么理解呢？
# 首先看对list的这些操作，其特点是在原处将list进行了修改：
lst = ['qiwsir', 'github', 'io']
# lst.append()
# lst.insert()
# lst.pop()
# lst[1] = "21312"

# 以上这些操作，如果用在str上，都会报错，
str = "Welcome"
# str[1] = "1"
# print(str)

# 如果要修改一个str，不得不这样：
print(str[0] + "E" + str[2:])  #其实，在这种做法中，相当于重新生成了一个str

print("list类型与str类型的转化\n" + "-"*1000)
line = "Hello.I am qiwsir.Welcome you."
print(line.split("."))
print(line.split(".",1)) #后面的参数1 表示最多切多少个，详情可以阅读源码介绍
print(help(str.split)) #如果split()不输入任何参数，显示就是见到任何分割符号，就用其分割了。

s = "I am, writing\npython\tbook on line"
print(s.split())