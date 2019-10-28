import matplotlib.pyplot as plt
import numpy as np

# 构建数据
x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
y_data3 = [42000, 34200, 21500, 18300, 16800, 19500, 42700]

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.bar(x=x_data, height=y_data, label='C语言基础', color='steelblue', alpha=0.8)
plt.bar(x=x_data, height=y_data2, label='Java基础', color='indianred', alpha=0.8)
plt.bar(x=x_data, height=y_data3, label='python基础', color='green', alpha=0.8)

# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
	plt.text(x, y, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
	plt.text(x, y, '%s' % y, ha='center', va='top')

for x, y in enumerate(y_data3):
	plt.text(x, y, '%s' % y, ha='center', va='top')
# 设置标题
plt.title("Java与Android图书对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("销量")
# 显示图例
plt.legend()
plt.show()