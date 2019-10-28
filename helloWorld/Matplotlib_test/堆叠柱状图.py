




import matplotlib.pyplot as plt
import numpy as np

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
y1 = [6, 5, 8, 5, 6, 6, 8, 9, 8, 10]
y2 = [5, 3, 6, 4, 3, 4, 7, 4, 4, 6]
y3 = [4, 1, 2, 1, 2, 1, 6, 2, 3, 2]

plt.bar(x, y1, label="label1", color='red')
plt.bar(x, y2, label="label2",color='orange')
plt.bar(x, y3, label="label3", color='lightgreen')
#
# plt.xticks(np.arange(len(x)), x, rotation=0, fontsize=10)  # 数量多可以采用270度，数量少可以采用340度，得到更好的视图
plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.ylabel('数量')
plt.xlabel('name')
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 尺寸
plt.title("title")
# plt.savefig('result.png')
plt.show()
# # matplotlib 的几种柱状图 : https://www.cnblogs.com/BackingStar/p/10986955.html