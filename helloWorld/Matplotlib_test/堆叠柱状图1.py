


# https://www.cnblogs.com/HuZihu/p/9390971.html
import pandas as pd
hot_dog=pd.read_csv(r"http://datasets.flowingdata.com/hot-dog-places.csv")
from matplotlib import pyplot as plt
fig,ax=plt.subplots()

year=[int(i) for i in hot_dog.columns]  #年份从header中提取
value=hot_dog.T.values   #将冠亚季军所吃热狗的数量转化成matrix，也就是[[25,24,22],[50.0,31.0,23.5],...]
v1=[i[0]+i[1]+i[2] for i in value]  #第一次画的柱形图y值为冠亚季军所吃热狗数量的总和
v2=[i[1]+i[2] for i in value]  #第二次画的柱形图y值为亚军所吃热狗的数量+季军所吃热狗的数量
v3=[i[2] for i in value]  #第三次画的柱形图y值为季军所吃热狗的数量

ax.bar(year,v1,color="green")
ax.bar(year,v2,color="red")
ax.bar(year,v3,color="blue")
ax.set(xlabel="Year",title="Hotdog game scores 2000-2010")
ax.text(1998,184,"(HDB)")  #设置文字
ax.legend(["first place","second place","third place"])  #设置图例
plt.show()
