#
# tuple 英 [tʌpl]   美 [tʌpl]
# n. 元组，数组
# 元组里面的数据特性：定长、有序、只读、
#可用于数据库查询出来的、结构化的数据



print("tuple类型的数据结构，有序列表，一旦初始化，无法修改，tuple不可变，所以代码更安全")
s = "abc"
print(s)
print(type(s))
t = 1,False,123,'abc',["come","here"]
print(t) #  元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
print(type(t)) # 所谓“元”组，就是用“圆”括号啦。
print("I love %s, and I am a %s" % ('python', 'programmer'))# 这里的圆括号，就是一个元组。
# 显然，tuple是一种序列类型的数据，这点上跟list/str类似。
# 它的特点就是其中的元素不能更改，这点上跟list不同，倒是跟str类似；
# 它的元素又可以是任何类型的数据，这点上跟list相同，但不同于str

# t[0] = 8   #编译期提示：tuple类型不支持元素赋值
print("t[0] = 8   #编译期提示：tuple类型不支持元素赋值")
print("所有在list中可以修改list的方法，在tuple中，都失效。")
print(t)
# tuple就是有点像一个融合了部分list和部分str属性的杂交产物。此言有理。
print(t[2])
print(t[1:])#用法有点像取字符串
print(t[4][1])#用法有点像二维数组
a = (3)
print(type(a)) # int类型
aa = (3,) # 特别提醒，如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。
print(type(aa))# tuple类型
print("分别用list()和tuple()能够实现两者的转化")
print("-" * 100)
print("tuple类型存在的意义：")
print("1、Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。")

print("2、如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，"
      "说明这一数据是常量。\n如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。")

print("3、Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。\n"
      " Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。"
      "只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。")

print("4、Tuples 可以用在字符串格式化输出中")