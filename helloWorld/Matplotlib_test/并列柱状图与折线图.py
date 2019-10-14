#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
# 产量数据（共2组）
a1=[128.3,13.38,63.8,63.07,23.16,6.74,176.18]
a2=[118.3,12.38,62.8,61.07,21.16,5.74,171.18]

#增长率数据
b=[12.12,2.44,13.82,16.67,26.67,13.52,25.04]

l=[i for i in range(7)] # 7组数据

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[u'粮食',u'棉花',u'油料',u'麻类',u'糖料',u'烤烟',u'蔬菜']

fig = plt.figure(figsize=(6, 4)) #  width, height in inches  ， If not provided, defaults to:rc:`figure.figsize` = ``[6.4, 4.8]``.
ax1 = fig.add_subplot(111)
plt.title("粮食产量与增长率")
plt.xlabel("粮食种类")
ax1.plot(l, b,'og-',label=u'增长率')
ax1.yaxis.set_major_formatter(yticks)
for i,(_x,_y) in enumerate(zip(l,b)):
    plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
ax1.set_ylim([0, 30])#设置y轴取值范围
ax1.set_ylabel(u'增长率(百分比)')
plt.legend(prop={'family':'SimHei','size':8})  #右上角折线图标注，设置中文

# 柱状图，设置两组数与总宽度
total_width, n = 0.8, 2
width = total_width / n # 每条柱状图的宽度

ax2 = ax1.twinx() # this is the important function
plt.bar(l,a1,alpha=0.4, width=width,color='#FFD700',label=u'2017产量')#柱形图的数据、颜色、透明度等
ax2.legend(loc=2)
ax2.set_ylim([0, 200])  #设置y轴取值范围
ax2.set_ylabel(u'产量(吨)')
for i in range(len(l)):
	l[i] = l[i] + width
plt.bar(l, a2, width=width,alpha=0.4,color='#32CD32',label=u'2018产量')

plt.legend(prop={'family':'SimHei','size':8},loc="upper left") #左上角折线图标注，
plt.xticks(l,lx)
plt.savefig("myplot.png")
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「Leige_Smart」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/leige_smart/article/details/79583470