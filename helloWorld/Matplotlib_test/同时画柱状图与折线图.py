#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a1=[128.3,13.38,63.8,63.07,23.16,6.74,196.18]  #2个分类数据
b=[12.12,2.44,13.82,16.67,26.67,13.52,25.04]

l=[i for i in range(7)] # 7组数据

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[u'粮食',u'棉花',u'油料',u'麻类',u'糖料',u'烤烟',u'蔬菜']

fig = plt.figure()
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

ax2 = ax1.twinx() # this is the important function
plt.bar(l,a1,alpha=0.4,color='#FFD700',label=u'产量')#柱形图的数据、颜色、透明度等
ax2.legend(loc=2)
ax2.set_ylim([0, 200])  #设置y轴取值范围
ax2.set_ylabel(u'产量(吨)')

plt.legend(prop={'family':'SimHei','size':8},loc="upper left") #左上角折线图标注，
plt.xticks(l,lx)
plt.savefig("myplot.png")
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「Leige_Smart」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/leige_smart/article/details/79583470