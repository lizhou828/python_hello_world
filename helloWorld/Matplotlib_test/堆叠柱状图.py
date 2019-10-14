import matplotlib.pyplot as plt

name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
plt.bar(range(len(num_list)), num_list, label='boy', fc='y')
plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='girl', tick_label=name_list, fc='r')
plt.legend()
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「小黄鸭and小黑鸭」的原创文章，遵循
# CC
# 4.0
# BY - SA
# 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / qq_29721419 / article / details / 71638912