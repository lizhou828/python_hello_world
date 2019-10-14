# import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
# num_list = [1.5, 0.6, 7.8, 6]
# num_list1 = [1, 2, 3, 1]
# num_list2 = [2, 1, 2.5, 2.1]
# plt.bar(range(len(num_list)), num_list, label='男孩', fc='y')
# plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='女孩', fc='r')
# plt.bar(range(len(num_list)), num_list2, bottom=num_list+num_list1, label='女孩', tick_label=name_list, fc='g')
# plt.legend()
# plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「小黄鸭and小黑鸭」的原创文章，遵循
# CC
# 4.0
# BY - SA
# 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / qq_29721419 / article / details / 71638912


# # https://www.cnblogs.com/HuZihu/p/9390971.html
# import pandas as pd
# hot_dog=pd.read_csv(r"http://datasets.flowingdata.com/hot-dog-places.csv")
# from matplotlib import pyplot as plt
# fig,ax=plt.subplots()
#
# year=[int(i) for i in hot_dog.columns]  #年份从header中提取
# value=hot_dog.T.values   #将冠亚季军所吃热狗的数量转化成matrix，也就是[[25,24,22],[50.0,31.0,23.5],...]
# v1=[i[0]+i[1]+i[2] for i in value]  #第一次画的柱形图y值为冠亚季军所吃热狗数量的总和
# v2=[i[1]+i[2] for i in value]  #第二次画的柱形图y值为亚军所吃热狗的数量+季军所吃热狗的数量
# v3=[i[2] for i in value]  #第三次画的柱形图y值为季军所吃热狗的数量
#
# ax.bar(year,v1,color="green")
# ax.bar(year,v2,color="red")
# ax.bar(year,v3,color="blue")
# ax.set(xlabel="Year",title="Hotdog game scores 2000-2010")
# ax.text(1998,184,"(HDB)")  #设置文字
# ax.legend(["first place","second place","third place"])  #设置图例
# plt.show()





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