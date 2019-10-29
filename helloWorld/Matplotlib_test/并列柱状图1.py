import matplotlib.pyplot as plt
import numpy as np

# 构建数据
x_data = ['2013', '2014', '2015', '2016', '2017']
y_data = [ 63000, 71000, 84000, 90500, 107000]
y_data2 = [ 51500, 58300, 56800, 59500, 62700]
y_data3 = [ 41500, 48300, 46800, 49500, 42700]
bar_width = 0.3
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 将X轴数据改为使用range(len(x_data), 就是0、1、2...
plt.bar(x=range(len(x_data)), height=y_data, label='C语言基础',
		color='#50E3C2', alpha=0.7, width=bar_width)
# 将X轴数据改为使用np.arange(len(x_data))+bar_width,
# 就是bar_width、1+bar_width、2+bar_width...这样就和第一个柱状图并列了
plt.bar(x=np.arange(len(x_data)) + bar_width, height=y_data2,
		label='Java基础', color='#0080FF', alpha=0.7, width=bar_width,tick_label=x_data)
plt.bar(x=np.arange(len(x_data)) + bar_width+ bar_width, height=y_data3,
		label='Python基础', color='#1F4AC6', alpha=0.7, width=bar_width)

# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
	plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
	plt.text(x + bar_width, y + 100, '%s' % y, ha='center', va='top')
for x, y in enumerate(y_data3):
	plt.text(x + bar_width+bar_width, y + 100, '%s' % y, ha='center', va='top')
# 设置标题
plt.title("编程语言对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("销量")
# 显示图例
plt.legend()
plt.show()