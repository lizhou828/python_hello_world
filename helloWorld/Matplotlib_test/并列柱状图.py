import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties




name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width,color='#FFD700', label='boy', tick_label=name_list)
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, num_list1, width=width,color='#32CD32', label='girl')
plt.legend()
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「小黄鸭and小黑鸭」的原创文章，遵循
# CC
# 4.0
# BY - SA
# 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / qq_29721419 / article / details / 71638912