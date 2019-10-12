# 参考文档
# python 动态创建变量 获取变量名  https://www.cnblogs.com/Gaoqiking/p/11253001.html
# 使用python创建动态变量名    https://www.jianshu.com/p/1196a51609bf


# exec是python3里的内置函数，支持python代码的动态运行
# 这种方式就相当于是执行了语句“var1=1”
for i in range(5):  # 注意随意指定的5，可看为个数
	exec('var{}={}'.format(i, i))
print(var1, var2, var3)

print("=" * 100)

for i in range(5):
	exec('print(var{}, end=" ")'.format(i))

print("=" * 100)

names = locals()
for i in range(1, 10):
	names['a%i' % i] = input('Abss %d' % i)
for i in range(1, 10):
	print(names['a%i' % i])

print("="*100)
# 利用命名空间动态赋值
# 在Python的命名空间中，将变量名与值存储在字典中，
# 可以通过locals()，globals()函数分别获取局部命名空间和全局命名空间。
createVar = locals()
for i in range(0, 16):
	createVar['r' + str(i)] = i
print(createVar.get("r0"))


print("="*100)

# 动态获取变量名
production1data = (19.2, 21.4, 16.7, 13, 15)
production2data = (9.2, 2.4, 6.7, 12, 13.5)
production3data = (9.2, 2.4, 6.7, 14.1, 5.2)
for i in range(4):
	if i == 0:
		continue
	print(exec("production{i}data".format(i=i)))
