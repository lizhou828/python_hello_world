print("List类型  list是一种有序集合、可扩容（可变长）的数据类型")
# 空的列表：list1=[]; list2=list()
print(" 有序集合，随时增删。包含的数据类型可以不同：整数、浮点数、字符串、list、tuple、dict、set、bool、空值、常量")
print("-"*100)

print("tuple类型的数据结构\n" )
# 空的元祖：tuple1=(); tuple2=tuple()
print("tuple类型的数据结构，有序列表，一旦初始化，无法修改，tuple不可变，所以代码更安全")
print("包含的数据类型可以不同：整数、浮点数、字符串、list、tuple、dict、set、bool、空值、常量")
print("元祖转换为列表：tuple-->list  list(tuple)")
print("虽然tuple不可变，但是它里面的list、dict、set是可以变的")
print("-"*100)

print("dict 词典 类型的数据结构\n" )
d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
print("键值对（key-value）方式存储,类似java的Map，查找速度快；dict的key必须是不可变对象（字符串、数字、元祖）；value包含的数据类型可以不同：整数、浮点数、字符串、list、tuple、dict、set、bool、空值、常量")
# 空的词典：dict1={}; dict2=dict()
# 函数：len()、get()、pop()、del、has_key()、items()、keys()、values()、update()
# 取值：d['Michael']
# 赋值：d['Michael']=100
# 添加：d['Jim']=22
# 删除：pop('Tracy'); del d['Jim']；del d
# 判断key是否存在：'Tracy' in d; d.get('Tracy')如果key不存在，返回None; d.get('Tracy', value) 如果key不存在,返回自己指定的value

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
#
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
print("-"*100)



print("set类型的数据结构\n" )
print(" 无序集合、key不重复")
# 无索引、无切片、作为一个无序的集合，set不记录元素位置或者插入点。因此，set不支持 indexing, slicing, 或其它类序列（sequence-like）的操作
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 要创建一个set，需要提供一个list作为输入集合：
#  s1 = set([1, 2, 3]):set([1,2,3])
#  s2 = set('boy') : set(['b','o','y'])
#  s3 = set(('cmd','pid')) set(['cmd','pid'])
#  s4 = {'txt', 'png', 'jpg', 'xls', 'csv', 'zip', 'xlsx', 'gif', 'GIF'}
# 空的的集合: set1 = set();
#
# 函数：pop()、add()、remove()、update()、len()、clear()、discard()
#
# 添加：add(key)、update();
# 区别
# s.add('boy'): set(['boy', 1, 2, 3]);
# s.update('boy'): set(['boy', 'b', 1, 2, 3, 'o', 'y']);
# s.update([23, 22, 32])
# 添加多项
#
# 删除：remove(key)
# 删除指定位置的元素, 如果不存在，引发KeyError；pop()
# 删除并且返回集合“s”中的一个不确定的元素, 如果为空则引发
# KeyError；clear()
# 删除所有元素；s.discard(x), 如果在
# set “s”中存在元素
# x, 则删除
#
# 交集：set1 & set2(set1.intersection(set2))
# 两个set的共有元素
# 并集： set1 | set2 （set1.union(set2)）两个set的元素相加后去重
# 差集：set1 - set2(set1.difference(set2))
# 集合set1去除和和集合set2相同的部分
#
# 对称差集：set1 ^ set2(set1.symmetric_difference(set2))
# 项在set1或set2中，但不会同时出现在二者中
# 操作：key in set1;
# key not in set1 ；for key in set1;
# 　　　set1.issubset(set2)等价于set1 <= set2: 测试set1中的每一个元素是否都在set2中
# 　　　set1.issuperset(set2)
# 等价于set1 >= set2: 测试set2中的每一个元素是否都在set1中　
# 　　　s.copy()
# 返回
# set “s”的一个浅复制
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错
# 重复元素在set中自动被过滤
# 应用示例：怎么去除海量列表里重复元素：
# a = [11, 22, 33, 44, 11, 22]
# a = list(set(a)):  [33, 11, 44, 22]


# 总结：1、list、tuple是有序列表；dict、set是无序列表
#          Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
# 　　   2、list元素可变、tuple元素不可变
#
# 　　   3、dict和set的key值不可变，唯一性
#
# 　　   4、set只有key没有value
#
# 　　   5、set的用途：去重、并集、交集等
#
# 　　   6、list、tuple：+、*、索引、切片、检查成员等
#
# 　　　7、dict查询效率高，但是消耗内存多；list、tuple查询效率低、但是消耗内存少

