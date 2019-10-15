# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5, 0.6, 7.8, 6]
fig = plt.figure(figsize=(6, 6), frameon=False)
subplot1 = fig.add_subplot(111)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.legend(prop={'family': 'SimHei', 'size': 8})  # 右上角折线图标注，设置中文
plt.title("每天降水量")
plt.bar(range(len(num_list)), num_list, fc='red',tick_label=name_list)
subplot1.set_ylim(0, max(num_list)+1)  # 设置y轴取值范围
# subplot1.set_ylabel(u"单位：毫米")
plt.ylabel("单位：毫米")
plt.grid(axis='y', color='gray', linestyle=':', linewidth=1)
plt.show()